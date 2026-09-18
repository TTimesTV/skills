# Final-upload CC workflow

**Status:** operational. **Applies when:** the requested final YouTube upload has usable Korean manual `ko` or automatic `ko-orig` captions.

## Collect only the needed evidence

```bash
python3 scripts/extract_youtube_cc.py "YOUTUBE_URL" --out-dir "WORK_DIR"
```

The helper records metadata, `transcript.tsv`, `chapter_source_pack.md`, candidate boundaries, and any existing description chapters. Prefer manual `ko`; fall back to automatic `ko-orig` only when it is the available Korean caption source.

If the user asks only to extract coherent chapters already published in the description, return those exact lines. If no usable CC is available, state that fact. A fallback ASR needs explicit disclosure and must not be represented as YouTube CC.

## Make editorial decisions on the final timeline

1. Read the first-90-seconds material and classify the actual promo, highlight, intro, and body. A common `00:16` highlight is not a template rule.
2. Read candidate boundaries as recall hints. Select only genuine question/topic setup, new thesis, named-case, transition, or field-location pivots.
3. Snap each selected pivot to the exact CC cue. For a question title, use the setup when it establishes the promise; for a thesis title, use the first explicit thesis cue.
4. Write specific, supportable titles. Preserve useful named entities and punctuation; avoid generic labels and final periods.
5. Use chapter count and spacing as a consequence of structure, not a quota. Historical observed ranges are in [house-style observation](../references/recent-sample-analysis.md).

## Validate and deliver

Save a single plain-text chapter list, run `python3 scripts/verify_timestamps.py final_timestamps.txt`, and deliver the list in one copy-ready code block. The verifier establishes structural validity only; it does not prove semantic quality or player sync.
