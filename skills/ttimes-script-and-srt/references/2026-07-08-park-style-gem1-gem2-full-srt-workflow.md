# 2026-07-08 Park-style Gem1/Gem2 full SRT workflow

## Context

User explicitly rejected the heavy “95점 gate / repeated global patch / audit loop” approach for a 75-minute AI-chip MP3 because it became slow and still visibly broken. They asked to revive the earlier Park Jongcheon-style workflow:

1. MP3 download and MLX Whisper transcription.
2. Gem1-style minimal transcript correction.
3. Gem2-style readable spoken-caption segmentation.
4. Align the resulting caption-body lines to MLX Whisper word timestamps and deliver an `srt.txt` file.

The user said to deliver the result even if not claiming 95점. In this mode, avoid over-explaining and produce the file.

## Durable workflow lesson

When the user says “박종천 때 하던 방식”, “Gem1/Gem2”, or “그냥 srt.txt 줘”, run a production path rather than an endless review path:

```text
source MP3 / existing ASR
→ ASR chunk files
→ subagents convert chunks with Gem1 minimal correction + Gem2 segmentation
→ Main Hermes concatenates chunk outputs
→ light mechanical validation
→ align to MLX word timestamps
→ deliver SRT-as-.txt + optional script txt
```

## Gem1 interpretation

Gem1 is **transcript-close correction**, not rewriting:

- Preserve speaker wording, order, colloquial structure, and meaningful repetition.
- Correct only clear ASR errors, particles, spacing, acronyms, proper nouns, numbers, and units.
- Do not summarize, delete, broadly paraphrase, or create polished prose.
- If a term/number is uncertain, prefer the nearest ASR/contextual reading and optionally note it in a report; do not invent.

## Gem2 interpretation

Gem2 is the critical caption segmentation pass:

- Output cue bodies only: one line per cue, no indices/timestamps/markdown.
- Target ≤25 visible Korean chars where possible; max should normally be ≤25 for this user.
- Prefer average around 14–18 visible chars, but preserve meaning closure over mechanical packing.
- Avoid ugly splits of:
  - `할 수 있다`, `되는 거죠`, `것 같습니다`
  - number+unit/range
  - company/product names
  - list clusters such as `구글, AWS, 마이크로소프트`
- Avoid over-fragmenting into tiny cue clusters; after automated merge/split, inspect representative ranges.

## Subagent use pattern

For long files, split into large time chunks (e.g. 00–25, 25–50, 50–76 minutes) and ask subagents to write chunk-level caption-body files directly, not just critique. Require each subagent to save:

```text
park_style/agents/partN_captions.txt
park_style/agents/partN_report.md
```

Main Hermes then owns concatenation, validation, alignment, and delivery.

## Alignment/delivery pattern

1. Concatenate non-empty lines from the chunk caption files.
2. Build a merged `words` JSON from `asr/source_large_v3_turbo.json` if only full MLX JSON exists:
   ```json
   {"duration": <last_word_end>, "words": [{"word": ..., "start": ..., "end": ...}, ...]}
   ```
3. Use `media-localization-workflows/scripts/align_lines_to_chunked_words.py` to preserve each caption line exactly while assigning timings.
4. Validate:
   - `script_lines == srt_cues`
   - `exact_body_match == true`
   - no malformed cues, overlaps, or non-positive durations
   - max visible length and duration sanity
5. On Telegram, deliver the SRT contents as `.txt` first:
   ```text
   MEDIA:/.../YYMMDD_topic_Gem1Gem2_srt.txt
   ```
   Optionally also deliver the plain script `.txt`.

## Important pitfall

If the user asks for this fast Park-style workflow, do not keep debating score, accountability, or subagent failures. The requested output is a usable `srt.txt` draft. Report validation briefly and attach the file.
