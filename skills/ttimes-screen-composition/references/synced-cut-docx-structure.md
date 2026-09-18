# Synced cut DOCX structure

## Class definition

In this TTimes workflow, `싱크` is an upstream document operation:

```text
approved cut transcript + cut MP3
→ speaker/chunk start anchors on the cut-audio timeline
→ synced cut DOCX
→ later material/screen-composition instructions
```

It is not spoken-caption SRT, source-text correction, diarization alone, or screen composition itself. The output is a paragraph-level timeline map used before `자료-완료` work.

## Observed corpus

Source: user-provided `(자료) 이주환 2편 컷편.docx` (2026-07-21).

- 215 paragraphs: 72 speaker/time labels + 72 body paragraphs + 71 blank separators
- 72 sync blocks: 이주환 45, 홍재의 27
- exact repeating grammar: `[speaker MM:SS]` → `[one body paragraph]` → `[blank paragraph]`
- first anchor `00:00`, last anchor `38:34`; start-only, whole-second precision
- no tables, images, comments, text boxes, highlights, colored runs, Track Changes, `//NN`, `//자막`, or `@@`
- plain A4/Normal DOCX; its authority comes from structure and timing, not visual formatting

Timing/chunk evidence:

- median block duration: 32.5 s
- speaker-change edges: 53, median 19 s
- same-speaker continuation splits: 18, median 61 s, range 47–73 s
- short speaker-turn reactions remain independent, including 1-second blocks
- body median 244 chars; guest blocks average longer than host blocks

This supports a hybrid split rule: **speaker turn first; long same-speaker turns split near a semantic boundary around one minute**.

## Canonical block contract

```text
SYNC_BLOCK
- speaker: exact speaker identity
- start: MM:SS on the cut MP3
- text: the approved cut transcript span, unchanged
- end: implicit next block start
- split_reason: SPEAKER_CHANGE | SAME_SPEAKER_LONG_TURN
```

Render as:

```text
홍재의 00:00
[approved spoken text for this interval]

이주환 00:43
[approved spoken text for this interval]
```

Rules:

1. Cut MP3 is the timing authority; approved cut transcript is the text authority.
2. Create a new block at every speaker change, however short.
3. If one speaker continues for roughly a minute, split at the nearest defensible sentence/thought boundary rather than mechanically at exactly 60 seconds.
4. Record only the block start as `MM:SS`; the next block start is the implicit end.
5. Keep each block's text as one paragraph and insert exactly one blank paragraph between blocks.
6. Preserve repetitions, reactions, rough fragments, punctuation, and existing transcript wording. Correction, subtitle segmentation, and material placement are separate downstream jobs.
7. Do not reuse SRT cue boundaries as sync blocks; sync granularity is much coarser.
8. If the cut audio or approved cut changes, downstream sync anchors are stale and must be regenerated.

## Package-topology interpretation

A filename such as `(자료) ... 컷편.docx` can still be only a synced base. If OOXML has no formatting-bearing production objects, classify it as:

```text
SYNCED_BASE / SPLIT_WORKING_PACKAGE
```

Do not infer missing screen placements. A later `자료-완료` artifact adds numbered assets, editorial captions, highlights, blue speech sync, and internal corrections on top of this base.

## Verification

- paragraph count follows `3N-1`
- exactly N speaker/time labels and N nonempty body paragraphs
- labels match `^speaker MM:SS$`
- times are monotonic and first anchor normally starts at `00:00`
- each label is followed by one nonempty body paragraph
- one blank paragraph separates records
- speaker identity and transcript order match the approved source
- same-speaker long-turn splits are near meaningful boundaries
- no text was silently corrected, summarized, or rewritten during sync
