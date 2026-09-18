# First-cut CC → final-upload prefix shift

**Status:** operational. **Scope:** a validated first-cut chapter list and a final assembly that adds a prefix before an unchanged or verified-compatible body.

## Choose the contract before inspecting the final body

| Evidence | Required checking |
| --- | --- |
| Producer/editor explicitly states that only front ad/highlight were added and the body is identical | Treat that statement as current production information. Inspect only the prefix, calculate `BODY_OFFSET`, shift deterministically, validate once, and return. Do not add late-body checks or full-final ASR. |
| No explicit same-body statement | Check duration delta, a long opening anchor, and one later anchor. A mid-roll, replacement intro, reorder, or failed anchor means that one global offset is unsafe. |

The explicit same-body contract wins over historical calibration procedures. It does not authorize inventing a body relationship when the producer has not stated one.

## Operational flow

1. On the first-cut URL, extract manual `ko` CC or automatic `ko-orig` CC and validate semantic body chapters.
2. Save the first-cut video ID, duration, validated list, and opening audio/text anchor.
3. On the final upload, identify the actual front-ad, highlight, and main-body transition. Do not treat a reused highlight excerpt as the body start.
4. Set the exact main-body start as `BODY_OFFSET`.
5. For the applicable contract above, shift every first-cut body chapter by that offset and add prefix chapters separately.
6. Validate the final text once. If normal-path evidence shows an internal body edit, preserve reusable titles but use final CC or a disclosed, authorized fallback for affected boundaries.

## Deterministic helper

```bash
python3 scripts/shift_first_cut_timestamps.py first_cut_timestamps.txt \
  --body-offset 01:42 \
  --prefix '00:00|2027 AX 전략 컨퍼런스' \
  --prefix '00:24|하이라이트' \
  --output final_timestamps.txt
python3 scripts/verify_timestamps.py final_timestamps.txt
```

The helper requires a first-cut list beginning at `00:00`, rejects invalid time grammar and duplicate/too-close times, and emits a list compatible with the structural verifier. See [script contracts](../scripts/README.md).

## Guardrails

- Do not hard-code the duration or title of any prefix from another upload.
- Do not use a simple global shift when the normal-path checks find an internal edit.
- Do not restart semantic chapter research for an explicitly unchanged body.
- Do not claim an ASR fallback is YouTube CC.

The prior Park Young-sun–Park Nam-gyu run is an [historical calibration case](calibration-case.md), not a default timing template.
