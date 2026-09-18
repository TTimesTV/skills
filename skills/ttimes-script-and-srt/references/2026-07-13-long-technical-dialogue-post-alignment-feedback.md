# Long technical dialogue: post-alignment feedback and factual-slip handling

## Trigger

Use this pattern for a 30–50 minute Korean technical dialogue with no YouTube captions, especially when MLX ASR contains scientific terms, proper nouns, numbers, and malformed spoken clauses.

## Proven workflow

1. Download and verify source duration and tail audio.
2. Run chunked MLX Whisper with word timestamps and no previous-text conditioning.
3. Build and triple-review a 0–3 minute sample before full segmentation.
4. Freeze the approved sample as an exact prefix with line count, SHA256, and any approved 28-character exception.
5. Keep raw ASR immutable; maintain a correction ledger with `from`, `to`, and `basis`.
6. Build a transcript-close full-body baseline, record cue/character/number inventories, then use chunk reviewers for all-boundary plus all-cue/source checks.
7. After Main substantially rewrites the body, run a freshness review against the actual delivery candidate. Old line numbers are hints only; apply findings by exact current string.
8. Fuzzy-align the frozen body character stream to MLX word characters, map each cue to matched word ranges, and generate initial timings.
9. Audit ASR word-midpoint coverage and every speech-containing gap. Classify each unmatched span as previous-thought residue, next-thought connector/correction, meaningful omitted text, or true silence. Never fill by blind midpoint.
10. Run a post-alignment short-duration audit. Cues under about 0.7 seconds often reveal body problems, not merely timing problems. Merge or rewrite protected chunks in the body, then regenerate all timing from the beginning.
11. Re-run body/SRT exact-match, monotonicity, overlaps, duration, coverage, terminology, and approved-prefix checks after every body change.

## Factual slips versus ASR errors

Targeted clip re-ASR can confirm that a speaker actually said a factually suspect term. In that case preserve the spoken wording in subtitles unless the user explicitly wants factual correction. Examples from this class of task include a speaker saying an institution, elapsed year count, or place name that conflicts with outside facts. Record the decision in the correction ledger as `preserve actual speech`.

Correct only when evidence supports recognition/terminology error, such as a malformed scientific term or impossible grammar whose intended technical phrase is clear from audio and context.

## Post-alignment feedback examples

Bad body boundaries exposed by sub-0.7-second cues:

```text
응용된 상용화, 이렇게
생각할 수 있는데
```

Better:

```text
응용된 상용화, 이렇게 생각할 수 있는데
```

Bad:

```text
1일이나 2일 정도
저장한다면
```

Better:

```text
1일이나 2일 정도 저장한다면
```

A very short reaction or intentional emphasis may remain short. Do not lengthen it by showing the next idea before it is spoken. If a short cue is a broken predicate/dependent-noun chunk, fix the body rather than stretching timestamps.

## Coverage classification

For a gap between cue A and cue B containing ASR words:

- Words complete or repeat A: extend A only to their actual final word.
- Words begin B or are B's connector: move B's start to their actual first word.
- Meaningful content absent from both bodies: restore source-close text as a cue, then realign.
- Disfluency already represented by a corrected sentence: assign timing to the semantically matching side without inventing text.
- True silence: keep the visual gap.

Acceptance gate: zero unreviewed speech-containing gaps above the visible-gap threshold (about 0.25 seconds), even if total word-midpoint coverage is below 100% because tiny boundary safety margins remain.
