#!/usr/bin/env python3
"""Validate ElevenLabs Dubbing Studio CSV structure and English timing fit."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

HEADERS = ["speaker", "start_time", "end_time", "transcription", "translation"]
IMMUTABLE = ["speaker", "start_time", "end_time"]
TIME_RE = re.compile(r"^(\d{2}):(\d{2}):(\d{2}),(\d{3})$")
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[’'\-][A-Za-z0-9]+)*")
HANGUL_RE = re.compile(r"[가-힣]")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_time(value: str) -> float:
    match = TIME_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"invalid timecode: {value!r}")
    hh, mm, ss, ms = map(int, match.groups())
    if mm >= 60 or ss >= 60:
        raise ValueError(f"invalid timecode: {value!r}")
    return hh * 3600 + mm * 60 + ss + ms / 1000


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        rows = [dict(row) for row in reader]
    return headers, rows


def estimate_fit(text: str, duration: float) -> dict[str, Any]:
    words = WORD_RE.findall(text)
    word_count = len(words)
    wps = word_count / duration if duration > 0 else 999.0
    # 156 wpm baseline plus restrained pause/acronym penalties.
    estimated = word_count / 2.6
    estimated += 0.10 * len(re.findall(r"[,;:]", text))
    estimated += 0.15 * len(re.findall(r"[.!?](?=\s|$)", text))
    acronym_extra = sum(max(0, len(token) - 1) * 0.08 for token in words if token.isupper() and len(token) >= 2)
    estimated += acronym_extra
    ratio = estimated / duration if duration > 0 else 999.0

    if wps > 3.2 or ratio > 1.15:
        fit_class = "hard_overfit"
    elif wps > 2.9 or ratio > 1.0:
        fit_class = "overfit"
    elif ratio > 0.92:
        fit_class = "acceptable"
    else:
        fit_class = "preferred"
    return {
        "words": word_count,
        "words_per_second": round(wps, 3),
        "estimated_speech_seconds": round(estimated, 3),
        "window_ratio": round(ratio, 3),
        "fit_class": fit_class,
    }


def validate(candidate: Path, source: Path | None, allow_empty_translation: bool) -> dict[str, Any]:
    headers, rows = read_csv(candidate)
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    row_metrics: list[dict[str, Any]] = []

    if headers != HEADERS:
        errors.append({"type": "headers", "expected": HEADERS, "actual": headers})

    source_rows: list[dict[str, str]] | None = None
    if source:
        source_headers, source_rows = read_csv(source)
        if source_headers != HEADERS:
            errors.append({"type": "source_headers", "expected": HEADERS, "actual": source_headers})
        if len(rows) != len(source_rows):
            errors.append({"type": "row_count", "source": len(source_rows), "candidate": len(rows)})

    previous_start = -1.0
    fit_counts: Counter[str] = Counter()
    missing_korean = 0
    missing_translation = 0

    for index, row in enumerate(rows, 1):
        for field in HEADERS:
            if row.get(field) is None:
                errors.append({"type": "missing_column_value", "row": index, "field": field})

        try:
            start = parse_time(row.get("start_time", ""))
            end = parse_time(row.get("end_time", ""))
        except ValueError as exc:
            errors.append({"type": "timecode", "row": index, "message": str(exc)})
            continue

        if end <= start:
            errors.append({"type": "nonpositive_duration", "row": index, "start": start, "end": end})
        if start < previous_start:
            errors.append({"type": "nonmonotonic_start", "row": index, "previous": previous_start, "actual": start})
        previous_start = start

        if source_rows and index <= len(source_rows):
            src = source_rows[index - 1]
            for field in IMMUTABLE:
                if row.get(field, "") != src.get(field, ""):
                    errors.append({
                        "type": "immutable_changed",
                        "row": index,
                        "field": field,
                        "source": src.get(field, ""),
                        "candidate": row.get(field, ""),
                    })

        transcription = row.get("transcription", "")
        translation = row.get("translation", "")
        if not transcription.strip():
            missing_korean += 1
            errors.append({"type": "empty_transcription", "row": index})
        if "\n" in transcription or "\r" in transcription:
            errors.append({"type": "embedded_newline", "row": index, "field": "transcription"})

        if not translation.strip():
            missing_translation += 1
            if not allow_empty_translation:
                errors.append({"type": "empty_translation", "row": index})
            continue
        if "\n" in translation or "\r" in translation:
            errors.append({"type": "embedded_newline", "row": index, "field": "translation"})
        if HANGUL_RE.search(translation):
            warnings.append({"type": "hangul_in_translation", "row": index})

        duration = end - start
        fit = estimate_fit(translation, duration)
        fit_counts[fit["fit_class"]] += 1
        metric = {"row": index, "duration_seconds": round(duration, 3), **fit}
        row_metrics.append(metric)
        if fit["fit_class"] == "hard_overfit":
            errors.append({"type": "hard_overfit", **metric})
        elif fit["fit_class"] == "overfit":
            warnings.append({"type": "overfit", **metric})
        elif fit["fit_class"] == "acceptable":
            warnings.append({"type": "tight_fit", **metric})

    report: dict[str, Any] = {
        "candidate": str(candidate),
        "candidate_sha256": sha256(candidate),
        "source": str(source) if source else None,
        "source_sha256": sha256(source) if source else None,
        "headers": headers,
        "row_count": len(rows),
        "speakers": sorted({row.get("speaker", "") for row in rows}),
        "first_start": rows[0].get("start_time") if rows else None,
        "last_end": rows[-1].get("end_time") if rows else None,
        "missing_transcription": missing_korean,
        "missing_translation": missing_translation,
        "fit_counts": {key: fit_counts.get(key, 0) for key in ["preferred", "acceptable", "overfit", "hard_overfit"]},
        "errors": errors,
        "warnings": warnings,
        "row_metrics": row_metrics,
        "pass": not errors,
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate")
    parser.add_argument("--source")
    parser.add_argument("--allow-empty-translation", action="store_true")
    parser.add_argument("--report")
    args = parser.parse_args()

    candidate = Path(args.candidate).expanduser().resolve()
    source = Path(args.source).expanduser().resolve() if args.source else None
    report = validate(candidate, source, args.allow_empty_translation)
    if args.report:
        output = Path(args.report).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "pass": report["pass"],
        "rows": report["row_count"],
        "missing_translation": report["missing_translation"],
        "fit_counts": report["fit_counts"],
        "errors": len(report["errors"]),
        "warnings": len(report["warnings"]),
        "sha256": report["candidate_sha256"],
    }, ensure_ascii=False))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
