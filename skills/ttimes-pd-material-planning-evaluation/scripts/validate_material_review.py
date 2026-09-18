#!/usr/bin/env python3
"""Deterministically validate a TTimes material-planning review.

Usage:
  python validate_material_review.py REVIEW.md \
    --credit '글·자료: 박성수 PD' \
    --selection 84 --sync 88 --function-score 80 --total 84 \
    --duration-label 26:33 --regular-frames 531 --scene-frames 247 --sheets 27
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("review", type=Path)
    ap.add_argument("--credit", required=True)
    ap.add_argument("--selection", type=int, required=True)
    ap.add_argument("--sync", type=int, required=True)
    ap.add_argument("--function-score", type=int, required=True)
    ap.add_argument("--total", type=int, required=True)
    ap.add_argument("--duration-label")
    ap.add_argument("--regular-frames", type=int)
    ap.add_argument("--scene-frames", type=int)
    ap.add_argument("--sheets", type=int)
    args = ap.parse_args()

    failures: list[str] = []
    try:
        raw = args.review.read_bytes()
        text = raw.decode("utf-8")
    except Exception as exc:
        print(json.dumps({"pass": False, "failures": [f"UTF-8 read failed: {exc}"]}, ensure_ascii=False, indent=2))
        return 1

    def require(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    require(args.credit in text, "exact credit string missing")
    require("자료 전용 범위 확인" in text, "material-only scope phrase missing")

    # Verify the two caption dimensions independently; a raw phrase count can pass
    # accidentally when the same phrase is repeated elsewhere in prose.
    for label in ("강조자막 선택", "강조자막 문구"):
        pattern = rf"\|\s*{re.escape(label)}\s*\|[^\n]*확인 불가·총점 제외"
        require(bool(re.search(pattern, text)), f"excluded score-table row missing: {label}")

    exact = (args.selection * 25 + args.sync * 20 + args.function_score * 20) / 65
    rounded = round(exact)
    require(rounded == args.total, f"supplied total {args.total} disagrees with formula ({exact})")
    require(f"총점: {args.total}/100" in text, "displayed total missing or inconsistent")
    require(
        all(str(x) in text for x in (args.selection, args.sync, args.function_score)),
        "one or more component scores absent",
    )

    # Accept all standard circled finding numbers, not only ①–⑩. Long-form
    # reviews can legitimately contain 11+ findings; silently dropping ⑪+
    # makes strength/weakness counts and schema checks falsely pass.
    headings = list(re.finditer(r"^###\s+[①-⑳]", text, re.M))
    blocks: list[str] = []
    for i, match in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        blocks.append(text[match.start():end])
    common_fields = ("**화면 객체:**", "**동시 발화 기능:**", "**판정:**")
    improvement_fields = ("**PD 개선점:**", "**공동 기획 개선점:**")
    complete = sum(
        all(field in block for field in common_fields)
        and any(field in block for field in improvement_fields)
        for block in blocks
    )
    strengths = sum("**강점.**" in block for block in blocks)
    weaknesses = sum("**약점.**" in block for block in blocks)
    require(len(blocks) >= 5, "fewer than five findings")
    require(complete == len(blocks), "one or more findings lack required fields")
    require(strengths >= 3, "fewer than three strengths")
    require(weaknesses >= 2, "fewer than two weaknesses")

    if args.duration_label:
        require(args.duration_label in text, "duration label missing")
    for value, label in (
        (args.regular_frames, "regular-frame count"),
        (args.scene_frames, "scene-frame count"),
        (args.sheets, "sheet count"),
    ):
        if value is not None:
            require(str(value) in text, f"{label} missing")

    result = {
        "pass": not failures,
        "utf8": True,
        "bytes": len(raw),
        "computed_exact": exact,
        "computed_rounded": rounded,
        "findings": len(blocks),
        "complete_findings": complete,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
