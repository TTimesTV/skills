#!/usr/bin/env python3
"""Validate a YouTube chapter timestamp list."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

RX = re.compile(r"^\s*((?:\d{1,2}:)?\d{1,2}:\d{2})\s+(.+?)\s*$")

def to_seconds(ts: str) -> int:
    p = [int(x) for x in ts.split(":")]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("file"); args = ap.parse_args()
    lines = [x for x in Path(args.file).read_text(encoding="utf-8").splitlines() if x.strip()]
    errors, warnings, chapters = [], [], []
    for n, line in enumerate(lines, 1):
        m = RX.match(line)
        if not m:
            errors.append(f"line {n}: invalid format: {line}"); continue
        ts, title = m.groups(); sec = to_seconds(ts)
        if int(ts.split(":")[-1]) >= 60 or int(ts.split(":")[-2]) >= 60:
            errors.append(f"line {n}: invalid time value: {ts}")
        chapters.append((sec, ts, title, n))
    if len(chapters) < 3: errors.append("YouTube manual chapters require at least 3 timestamps")
    if chapters and chapters[0][0] != 0: errors.append("first timestamp must start at 00:00")
    seen = set()
    for i, (sec, ts, title, n) in enumerate(chapters):
        if i and sec <= chapters[i-1][0]: errors.append(f"line {n}: timestamps not strictly ascending")
        if i and sec - chapters[i-1][0] < 10: errors.append(f"line {n}: chapter shorter than 10 seconds")
        key = re.sub(r"\s+", "", title).lower()
        if key in seen: warnings.append(f"line {n}: duplicate title: {title}")
        seen.add(key)
        if title.endswith((".", "。")): warnings.append(f"line {n}: TTimes title should normally omit a final period")
        if len(title) > 40: warnings.append(f"line {n}: long title ({len(title)} chars): {title}")
        if len(title) < 3: warnings.append(f"line {n}: vague/short title: {title}")
    for x in errors: print("ERROR", x)
    for x in warnings: print("WARN", x)
    print(f"chapters={len(chapters)} errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
