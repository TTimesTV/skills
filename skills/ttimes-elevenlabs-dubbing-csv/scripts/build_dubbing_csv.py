#!/usr/bin/env python3
"""Build an import-ready Dubbing Studio CSV from a complete edits ledger."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from validate_dubbing_csv import HEADERS, read_csv, validate


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--edits", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    edits_path = Path(args.edits).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    report_path = Path(args.report).expanduser().resolve()

    headers, source_rows = read_csv(source)
    if headers != HEADERS:
        raise SystemExit(f"source headers must be exactly {HEADERS}; got {headers}")

    payload = json.loads(edits_path.read_text(encoding="utf-8"))
    edit_rows = payload.get("rows") if isinstance(payload, dict) else None
    if not isinstance(edit_rows, list):
        raise SystemExit("edits JSON must be an object containing a rows list")

    by_index: dict[int, dict] = {}
    for item in edit_rows:
        if not isinstance(item, dict) or not isinstance(item.get("row"), int):
            raise SystemExit("every edit must contain an integer row")
        index = item["row"]
        if index in by_index:
            raise SystemExit(f"duplicate edit row: {index}")
        by_index[index] = item

    expected = set(range(1, len(source_rows) + 1))
    actual = set(by_index)
    if expected != actual:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise SystemExit(f"edit coverage mismatch missing={missing} extra={extra}")

    final_rows: list[dict[str, str]] = []
    changes: list[dict] = []
    for index, source_row in enumerate(source_rows, 1):
        edit = by_index[index]
        transcription = edit.get("transcription")
        translation = edit.get("translation")
        if not isinstance(transcription, str) or not transcription.strip():
            raise SystemExit(f"row {index}: non-empty transcription required")
        if not isinstance(translation, str) or not translation.strip():
            raise SystemExit(f"row {index}: non-empty translation required")
        if "\n" in transcription or "\r" in transcription or "\n" in translation or "\r" in translation:
            raise SystemExit(f"row {index}: embedded newline is not allowed")

        final = {
            "speaker": source_row["speaker"],
            "start_time": source_row["start_time"],
            "end_time": source_row["end_time"],
            "transcription": transcription.strip(),
            "translation": translation.strip(),
        }
        final_rows.append(final)
        changes.append({
            "row": index,
            "speaker": source_row["speaker"],
            "start_time": source_row["start_time"],
            "end_time": source_row["end_time"],
            "source_transcription": source_row["transcription"],
            "final_transcription": final["transcription"],
            "translation": final["translation"],
            "transcription_changed": source_row["transcription"] != final["transcription"],
        })

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADERS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(final_rows)

    validation = validate(output, source, allow_empty_translation=False)
    report = {
        "source": str(source),
        "source_sha256": sha256(source),
        "edits": str(edits_path),
        "edits_sha256": sha256(edits_path),
        "output": str(output),
        "output_sha256": sha256(output),
        "row_count": len(final_rows),
        "changed_transcriptions": sum(item["transcription_changed"] for item in changes),
        "validation": validation,
        "changes": changes,
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "pass": validation["pass"],
        "rows": len(final_rows),
        "changed_transcriptions": report["changed_transcriptions"],
        "fit_counts": validation["fit_counts"],
        "errors": len(validation["errors"]),
        "warnings": len(validation["warnings"]),
        "output": str(output),
        "report": str(report_path),
    }, ensure_ascii=False))
    return 0 if validation["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
