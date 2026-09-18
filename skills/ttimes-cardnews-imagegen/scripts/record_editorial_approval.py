#!/usr/bin/env python3
"""Append explicit editorial approvals and build a compact preference snapshot."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import tempfile

VALID_STATUS = {"proposed", "approved", "rejected", "revised"}
REQUIRED = {"date", "format", "episode", "artifact", "field", "status", "candidate", "final", "reason", "signals", "source"}
DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = DEFAULT_ROOT / "references" / "editorial-approval-ledger.jsonl"
DEFAULT_SNAPSHOT = DEFAULT_ROOT / "references" / "editorial-preference-snapshot.json"


def read_events(path: Path) -> list[dict]:
    events: list[dict] = []
    if not path.exists():
        return events
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        event = json.loads(raw)
        missing = REQUIRED - event.keys()
        if missing:
            raise ValueError(f"{path}:{line_no}: missing {sorted(missing)}")
        if event["status"] not in VALID_STATUS:
            raise ValueError(f"{path}:{line_no}: invalid status {event['status']}")
        if not isinstance(event["signals"], list):
            raise ValueError(f"{path}:{line_no}: signals must be a list")
        events.append(event)
    return events


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as fh:
        fh.write(text)
        temp = Path(fh.name)
    temp.replace(path)


def append_event(args: argparse.Namespace) -> None:
    ledger = Path(args.ledger)
    event = {
        "date": args.date,
        "format": args.format,
        "episode": args.episode,
        "artifact": args.artifact,
        "field": args.field,
        "status": args.status,
        "candidate": args.candidate,
        "final": args.final,
        "reason": args.reason,
        "signals": args.signals,
        "source": args.source,
    }
    # Validate the existing ledger and prevent accidental duplicate writes.
    events = read_events(ledger)
    identity = (event["date"], event["format"], event["episode"], event["artifact"], event["field"], event["status"], event["candidate"], event["final"])
    for old in events:
        old_identity = (old["date"], old["format"], old["episode"], old["artifact"], old["field"], old["status"], old["candidate"], old["final"])
        if old_identity == identity:
            raise SystemExit("duplicate event; ledger unchanged")
    line = json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n"
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with ledger.open("a", encoding="utf-8") as fh:
        fh.write(line)
    print(f"appended=1 ledger={ledger}")


def summarize(args: argparse.Namespace) -> None:
    ledger = Path(args.ledger)
    output = Path(args.output)
    events = read_events(ledger)
    formats: dict[str, list[dict]] = defaultdict(list)
    for event in events:
        formats[event["format"]].append(event)

    snapshot: dict = {
        "schema_version": "1.0.0",
        "generated_from": str(ledger),
        "event_count": len(events),
        "formats": {},
        "promotion_policy": {
            "hard_rule": "explicit user instruction applies immediately",
            "default_pattern": "promote after the same signal appears in at least 3 independent episodes",
            "latest_instruction_wins": True,
        },
    }

    for fmt, fmt_events in sorted(formats.items()):
        status_counts = Counter(e["status"] for e in fmt_events)
        positive_signals = Counter()
        rejected_signals = Counter()
        episode_sets: dict[str, set[str]] = defaultdict(set)
        examples: dict[str, list[dict]] = defaultdict(list)
        for event in fmt_events:
            target = rejected_signals if event["status"] == "rejected" else positive_signals
            for signal in event["signals"]:
                target[signal] += 1
                episode_sets[signal].add(event["episode"])
            if event["status"] in {"approved", "revised"} and event["final"]:
                examples[event["artifact"]].append({
                    "field": event["field"],
                    "final": event["final"],
                    "episode": event["episode"],
                    "signals": event["signals"],
                })

        snapshot["formats"][fmt] = {
            "event_count": len(fmt_events),
            "episode_count": len({e["episode"] for e in fmt_events}),
            "status_counts": dict(sorted(status_counts.items())),
            "positive_signals": [
                {"signal": signal, "events": count, "episodes": len(episode_sets[signal]), "promoted_default": len(episode_sets[signal]) >= 3}
                for signal, count in positive_signals.most_common()
            ],
            "rejected_signals": [
                {"signal": signal, "events": count, "episodes": len(episode_sets[signal])}
                for signal, count in rejected_signals.most_common()
            ],
            "approved_examples": dict(sorted(examples.items())),
        }

    atomic_write(output, json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n")
    print(f"events={len(events)} formats={len(formats)} output={output}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p_append = sub.add_parser("append")
    p_append.add_argument("--ledger", default=str(DEFAULT_LEDGER))
    p_append.add_argument("--date", default=date.today().isoformat())
    p_append.add_argument("--format", required=True)
    p_append.add_argument("--episode", required=True)
    p_append.add_argument("--artifact", required=True)
    p_append.add_argument("--field", required=True)
    p_append.add_argument("--status", required=True, choices=sorted(VALID_STATUS))
    p_append.add_argument("--candidate", default="")
    p_append.add_argument("--final", default="")
    p_append.add_argument("--reason", required=True)
    p_append.add_argument("--signals", nargs="+", required=True)
    p_append.add_argument("--source", choices=["explicit_user", "user_edit", "observed_choice"], required=True)
    p_append.set_defaults(func=append_event)

    p_summary = sub.add_parser("summarize")
    p_summary.add_argument("--ledger", default=str(DEFAULT_LEDGER))
    p_summary.add_argument("--output", default=str(DEFAULT_SNAPSHOT))
    p_summary.set_defaults(func=summarize)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
