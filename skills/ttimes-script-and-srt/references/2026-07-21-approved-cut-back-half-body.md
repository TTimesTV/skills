# Approved-cut transcript back-half → TTimes cue-body first draft

## Use case

Use when the user asks for a named episode's **approved cut transcript** (`승인 컷 원고`) and a specific section such as the back half to be converted directly into a first-pass TTimes spoken-caption body.

This is a lightweight body-generation route, not a full ASR/SRT workflow:

```text
accepted transcript range + prior-episode style reference
→ source-close correction
→ TTimes cue-body segmentation
→ mechanical validation
→ save one plain TXT body
```

## Procedure

1. Read only the requested accepted-transcript range, including enough boundary context to identify the true start and end.
2. Read a representative prior approved/final episode body or SRT from the same series. Use its cue rhythm as style evidence, but never copy its wording or timing.
3. Start from the requested range exactly; do not leak preceding material into the deliverable merely because it appears in the same read window.
4. Preserve every meaningful spoken detail, speaker turn, question, reaction, repetition, and unfinished lead-in that survives the approved cut. Remove speaker names and timestamps only.
5. Apply minimal correction: spacing, punctuation useful for subtitles, proper nouns, and obvious ASR corruption. Do not summarize or broadly rewrite.
6. Segment as one non-empty cue body per line. Prefer small-sentence readability and keep predicates, dependent nouns, quoted titles, and technical names attached where practical.
7. Validate before delivery:
   - no blank lines
   - no speaker labels or timestamps
   - no sentence-final prose periods
   - maximum visible length at or below the project limit (27 including spaces in this run)
   - inspect every over-25 line manually
   - run the protected-phrase adjacency audit and adjudicate hits rather than requiring regex zero
8. Deliver only the saved path plus terse metrics unless the user asks for the body in chat.

## Practical segmentation lessons

- Parenthetical bilingual terms can exceed the box even when the Korean phrase itself is short. Preserve both forms but split deliberately, e.g. Korean title on one cue and the English equivalent plus predicate on the next.
- A technical phrase may create an unavoidable lint candidate. Lint candidates are review prompts, not automatic failures; choose the least damaging boundary while preserving source order and wording.
- Spacing corrections such as `한 번` can add one visible character and push a previously valid line over 27. Re-run length validation after every lexical or spacing patch.
- A final assertion script should check line count, max length, blank lines, speaker/timestamp patterns, and sentence-final periods. Do not report `이슈 없음` before those assertions pass.

## Session result pattern

The 2026-07-21 back-half run produced a 154-line body with maximum length 27, zero blank lines, zero speaker/timestamp hits, zero over-27 lines, and zero sentence-final periods. The useful learning is the route and validation sequence, not those exact counts.
