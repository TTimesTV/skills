#!/usr/bin/env python3
"""Shift precomputed first-cut YouTube chapters by a final-upload body offset.

Example:
  python shift_first_cut_timestamps.py first_cut_timestamps.txt \
    --body-offset 01:42 \
    --prefix '00:00|2027 AX 전략 컨퍼런스' \
    --prefix '00:24|하이라이트' \
    --output final_timestamps.txt
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


LINE_RE = re.compile(r"^(?P<time>\d{1,2}:\d{2}(?::\d{2})?)\s+(?P<title>\S.*)$")
TIME_RE = re.compile(r"^(?:(?P<hours>\d{1,2}):)?(?P<minutes>[0-5]?\d):(?P<seconds>[0-5]\d)$")


def parse_time(value: str) -> int:
    match = TIME_RE.fullmatch(value)
    if not match:
        raise ValueError(f"invalid timestamp: {value}")
    hours = int(match.group("hours") or 0)
    minutes = int(match.group("minutes"))
    seconds = int(match.group("seconds"))
    return hours * 3600 + minutes * 60 + seconds


def format_time(total: int) -> str:
    if total < 0:
        raise ValueError("negative timestamp")
    hours, rem = divmod(total, 3600)
    minutes, seconds = divmod(rem, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def parse_chapter_line(line: str) -> tuple[int, str]:
    match = LINE_RE.match(line.strip())
    if not match:
        raise ValueError(f"invalid chapter line: {line!r}")
    return parse_time(match.group("time")), match.group("title").strip()


def parse_prefix(value: str) -> tuple[int, str]:
    if "|" not in value:
        raise ValueError("--prefix must be TIME|TITLE")
    time_text, title = value.split("|", 1)
    title = title.strip()
    if not title:
        raise ValueError("empty prefix title")
    return parse_time(time_text.strip()), title


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("first_cut", type=Path)
    parser.add_argument("--body-offset", required=True, help="final-upload start of unchanged first-cut body")
    parser.add_argument("--prefix", action="append", default=[], help="repeatable TIME|TITLE prefix chapter")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--min-seconds", type=int, default=10)
    args = parser.parse_args()

    try:
        offset = parse_time(args.body_offset)
        body = [
            parse_chapter_line(line)
            for line in args.first_cut.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        entries = [parse_prefix(value) for value in args.prefix]
    except ValueError as error:
        parser.error(str(error))

    if not body:
        raise SystemExit("first-cut chapter list is empty")
    if body[0][0] != 0:
        raise SystemExit("first-cut chapter list must begin at 00:00")

    entries.extend((seconds + offset, title) for seconds, title in body)
    entries.sort(key=lambda item: item[0])

    if not entries or entries[0][0] != 0:
        raise SystemExit("final chapter list must begin at 00:00; add a 00:00 prefix")

    if entries[-1][0] >= 100 * 3600:
        raise SystemExit("timestamp exceeds verifier-supported 99:59:59 range")

    seen_times: set[int] = set()
    for index, (seconds, title) in enumerate(entries):
        if seconds in seen_times:
            raise SystemExit(f"duplicate chapter time: {format_time(seconds)}")
        seen_times.add(seconds)
        if index and seconds - entries[index - 1][0] < args.min_seconds:
            raise SystemExit(
                f"chapters too close: {format_time(entries[index - 1][0])} and {format_time(seconds)}"
            )
        if not title:
            raise SystemExit("empty chapter title")

    output = "\n".join(f"{format_time(seconds)} {title}" for seconds, title in entries) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(f"chapters={len(entries)} body_offset={format_time(offset)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
