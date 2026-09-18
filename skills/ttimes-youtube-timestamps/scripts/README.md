# Timestamp helper contracts

**Status:** operational. Helpers validate or transform text contracts; they do not prove actual video/audio synchronization.

| Script | Input | Output / result |
| --- | --- | --- |
| `extract_youtube_cc.py` | YouTube URL and output directory | metadata, Korean CC-derived source files, and candidate-boundary material; requires network access and available YouTube captions |
| `shift_first_cut_timestamps.py` | validated first-cut list, body offset, prefix chapters | deterministic final chapter text; exits nonzero for invalid grammar, duplicate times, missing `00:00`, or chapters closer than the configured minimum |
| `verify_timestamps.py` | final chapter text | exit `0` only when structural errors are zero; warnings are editorial review items, not an approval signal |

## Shared time grammar

All chapter input accepted by the shift helper uses `MM:SS` or `HH:MM:SS`: hours are one or two digits; minutes and seconds must be `00`–`59` (a one-digit minute is accepted in input). The shift helper rejects malformed source and offset values rather than silently normalizing them. Its emitted timestamps are accepted by `verify_timestamps.py`.

## Minimal validation chain

```bash
python3 scripts/shift_first_cut_timestamps.py first_cut.txt --body-offset 01:42 --prefix '00:00|인트로' --output final_timestamps.txt
python3 scripts/verify_timestamps.py final_timestamps.txt
```

Passing this chain proves text-structure compatibility only. Real CC selection, prefix/body matching, semantic chapter choices, and user approval remain separate evidence.
