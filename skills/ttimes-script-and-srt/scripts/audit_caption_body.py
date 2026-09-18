#!/usr/bin/env python3
"""Dependency-free lint for timecode-free Korean caption-body TXT."""

import argparse
import json
import re
from pathlib import Path

DEFAULT_ALLOWED_SHORT = {
    "네", "아니요", "그렇죠", "맞아요", "안녕하세요", "안녕하십니까?",
    "감사합니다", "왜요?", "정말요?", "그런가요?", "GPU가요?", "10배네요?",
}
UNIT_PREFIXES = ("개", "명", "원", "년", "개월", "배", "장", "대", "곳", "%")
ATTACHMENT_RE = re.compile(
    r"(?:[가-힣]+(?:았|었|였|했|켰)죠|합니다|됩니다|있습니다|거든요|잖아요|말이죠|좋아요|맞아요)\s+\S+"
)


def audit_lines(lines, max_chars=27, allowed_short=None):
    allowed = DEFAULT_ALLOWED_SHORT | set(allowed_short or [])
    findings = []
    for i, raw in enumerate(lines):
        line = raw.strip()
        prev = lines[i - 1].strip() if i else ""
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        n = i + 1

        if len(line) <= 7 and line not in allowed:
            findings.append({"type": "short_manual_review", "line": n, "text": line, "prev": prev, "next": nxt})

        # Require an actual digit before Korean large-number suffixes; avoids matching 어렵겠지만.
        if re.search(r"\d(?:만|억|조)?$", line) and nxt.startswith(UNIT_PREFIXES):
            findings.append({"type": "number_unit_split", "line": n, "text": line, "next": nxt})

        match = ATTACHMENT_RE.search(line)
        if match:
            findings.append({"type": "sentence_attachment", "line": n, "text": line, "marker": match.group(0).split()[0]})

        if len(line) > max_chars:
            findings.append({"type": "over_max", "line": n, "text": line, "length": len(line)})
        elif len(line) > 25:
            findings.append({"type": "over25_warning", "line": n, "text": line, "length": len(line)})

        if line.endswith("."):
            findings.append({"type": "mechanical_final_period", "line": n, "text": line})

    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("body", type=Path)
    ap.add_argument("--max-chars", type=int, default=27)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()

    lines = [x for x in args.body.read_text().splitlines() if x.strip()]
    findings = audit_lines(lines, max_chars=args.max_chars)
    counts = {}
    for item in findings:
        counts[item["type"]] = counts.get(item["type"], 0) + 1
    report = {
        "path": str(args.body),
        "lines": len(lines),
        "max_length": max(map(len, lines), default=0),
        "question_marks": sum(x.count("?") for x in lines),
        "counts": counts,
        "findings": findings,
    }
    if args.json_out:
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps({k: report[k] for k in ("lines", "max_length", "question_marks", "counts")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
