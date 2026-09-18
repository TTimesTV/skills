#!/usr/bin/env python3
"""Read-only helpers for existing ElevenLabs Legacy Dubbing Studio projects."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlencode
import urllib.request

from elevenlabs.client import ElevenLabs


def api_key() -> str:
    key = os.getenv("ELEVENLABS_API_KEY", "").strip()
    if key:
        return key
    env_file = Path.home() / ".hermes" / ".env"
    if env_file.exists():
        for raw in env_file.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if line.startswith("ELEVENLABS_API_KEY="):
                return line.split("=", 1)[1].strip().strip("\"'")
    raise SystemExit("ELEVENLABS_API_KEY is not configured")


def list_dubs(query: str, limit: int) -> list[dict]:
    key = api_key()
    cursor = None
    results: list[dict] = []
    while len(results) < limit:
        params = {
            "page_size": min(200, max(1, limit)),
            "filter_by_creator": "all",
            "order_by": "created_at",
            "order_direction": "DESCENDING",
        }
        if cursor:
            params["cursor"] = cursor
        req = urllib.request.Request(
            "https://api.elevenlabs.io/v1/dubbing?" + urlencode(params),
            headers={"xi-api-key": key},
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            payload = json.load(response)
        for item in payload.get("dubs", []):
            if not query or query.casefold() in item.get("name", "").casefold():
                results.append({
                    field: item.get(field)
                    for field in [
                        "dubbing_id", "name", "status", "editable", "source_language",
                        "target_languages", "created_at", "media_metadata",
                    ]
                })
                if len(results) >= limit:
                    break
        if not payload.get("has_more") or not payload.get("next_cursor"):
            break
        cursor = payload["next_cursor"]
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list")
    p_list.add_argument("--query", default="")
    p_list.add_argument("--limit", type=int, default=20)

    p_srt = sub.add_parser("export-srt")
    p_srt.add_argument("dubbing_id")
    p_srt.add_argument("--lang", default="en")
    p_srt.add_argument("--output", required=True)

    p_probe = sub.add_parser("probe")
    p_probe.add_argument("dubbing_id")
    p_probe.add_argument("--lang", default="en")

    args = parser.parse_args()
    if args.command == "list":
        items = list_dubs(args.query, args.limit)
        print(json.dumps({"count": len(items), "dubs": items}, ensure_ascii=False, indent=2))
        return 0

    client = ElevenLabs(api_key=api_key())
    if args.command == "export-srt":
        text = client.dubbing.get_transcript_for_dub(args.dubbing_id, args.lang, format_type="srt")
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(json.dumps({"output": str(output), "characters": len(text)}, ensure_ascii=False))
        return 0

    if args.command == "probe":
        metadata = client.dubbing.get_dubbing_project_metadata(args.dubbing_id)
        md = metadata.dict() if hasattr(metadata, "dict") else vars(metadata)
        result = {
            "metadata": md,
            "target_transcript_read": False,
            "segment_resource_write_access": False,
        }
        try:
            text = client.dubbing.get_transcript_for_dub(args.dubbing_id, args.lang, format_type="srt")
            result["target_transcript_read"] = True
            result["target_srt_characters"] = len(text)
        except Exception as exc:
            result["target_transcript_error"] = type(exc).__name__
        try:
            client.dubbing.get_dubbing_resource(args.dubbing_id)
            result["segment_resource_write_access"] = True
        except Exception as exc:
            result["segment_resource_error"] = type(exc).__name__
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
