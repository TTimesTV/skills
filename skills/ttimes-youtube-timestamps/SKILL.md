---
name: ttimes-youtube-timestamps
description: "Create TTimes-style YouTube description timestamps/chapters from YouTube-provided CC. Use for 티타임즈 타임스탬프, 유튜브 챕터, 설명란 타임라인 — not SRT subtitles. Learned from 10 recent TTimesTV videos and 85 published chapters."
metadata:
  version: 1.4.0
---

# TTimes YouTube Timestamps

## Trigger and boundary

Use for `티타임즈 타임스탬프`, `유튜브 타임스탬프`, `설명란 챕터`, or a `00:00 제목` chapter list.

This delivers a short YouTube-description chapter list. It is not an SRT, subtitle timing, or a timestamped full transcript.

| Requested result | Primary route |
| --- | --- |
| Spoken-caption body or SRT | `ttimes-script-and-srt` |
| Description chapters only | this skill |
| Hashtags, chapters, and a pinned comment package | `ttimes-youtube-upload-package` with this skill for chapters |
| An ambiguous URL or `/plan` | Ask which deliverable is wanted; do not guess |

## Current contract

1. Use the final-upload CC path when usable Korean YouTube CC is available. Follow [final CC workflow](workflows/final-cc.md).
2. Use the first-cut prefix path only when the body chapter list was already validated. Follow [first-cut prefix workflow](references/first-cut-prefix-shift-workflow.md).
3. If a producer explicitly declares that the body is unchanged except for the front prefix, that production statement authorizes the prefix-only path. Otherwise use the ordinary duration, opening-anchor, and later-anchor gates.
4. If the final description already has the requested coherent chapters and the user asks to extract them, return those exact chapter lines unless editorial retiming is explicitly requested.
5. Do not claim that a fallback ASR result is YouTube CC. If no usable CC exists, disclose the missing input and only use an available, user-authorized fallback.

## Editorial rules that always apply

- Do not hard-code `00:16 하이라이트`; classify the actual first-minute promo, highlight, intro, and body structure.
- Candidate detection is recall-oriented, not a final boundary. Select semantic pivots and snap each selected boundary to an exact CC cue.
- A chapter title is concise editorial compression. Keep the central entity or claim, avoid generic labels and final periods, and do not overclaim the adjacent CC.
- Historical style statistics and calibration examples are evidence, not quotas. See [house-style observation](references/recent-sample-analysis.md) and [calibration case](references/calibration-case.md).

## Delivery and validation

Return the chapter list as one copy-ready fenced plain-text block unless the user asks for explanation or a file:

```text
00:00 제목
00:16 하이라이트
02:06 AI칩이란?
```

Before delivery, save the list as `final_timestamps.txt` and run:

```bash
python3 scripts/verify_timestamps.py final_timestamps.txt
```

The list must start at `00:00`, contain at least three ascending timestamps, and keep at least 10 seconds between chapters. Exit code `0` means no structural errors; warnings still require editorial judgment. See [script contracts](scripts/README.md).

## Reference selection

| Need | Read | Status and scope |
| --- | --- | --- |
| Extract and edit chapters from final YouTube CC | [final CC workflow](workflows/final-cc.md) | operational; usable CC required |
| Shift a validated first-cut list after a prefix | [first-cut prefix workflow](references/first-cut-prefix-shift-workflow.md) | operational; explicit same-body statement or ordinary match gates required |
| Understand observed 2026-07 style | [house-style observation](references/recent-sample-analysis.md) | historical; not a quota |
| Inspect one prior prefix-shift calibration | [calibration case](references/calibration-case.md) | calibration; not a template duration |
| Run or interpret helpers | [script contracts](scripts/README.md) | operational |

If a reference conflicts with this root current contract, this root contract wins. The former producer-handoff filename remains a [compatibility pointer](references/producer-declared-cut-cc-prefix-only-handoff.md), not an independent rule source.
