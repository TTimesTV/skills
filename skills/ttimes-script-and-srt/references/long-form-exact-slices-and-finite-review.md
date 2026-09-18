# Long-form no-caption captioning: exact slices and finite review

Use this note for 40–60+ minute technical interviews where Main builds a full spoken-caption body from chunked ASR.

## 1. Exact bounded drafting

- Extract timestamped source slices physically before dispatch. For long programs, 10-minute slices are a safe default; do not hand a drafter both a bounded source and an unbounded timecode-free baseline.
- Save slice manifest fields: first/last timestamp, segment count, character count, SHA-256.
- Require the drafter to report the exact source hash and boundary timestamps, then Main must inspect actual first/last output text.
- A draft that crosses its assigned range is scope-invalid even if its line counts and self-report look plausible. Quarantine it under `obsolete/`; do not splice it.

## 2. Long-review partitioning

- Source/term/number review: split into contiguous windows no longer than about 30 minutes.
- Segmentation review: split a 1,500–2,000 cue candidate into contiguous 900–1,000 cue responsibilities.
- Every partition must inspect the same immutable candidate hash. Assign each seam explicitly or include it in both neighboring briefs.
- Keep web research out of timed review. Supply local auto captions, glossary, correction ledger, targeted ASR clips, and audio. Main resolves unresolved external facts.
- Read the saved report, not only the async headline. A summary can reverse a from/to correction or omit an audio-required caveat.

## 3. Targeted audio adjudication

For damaged names, numeric examples, contract amounts, years, or causal wording:

1. Cut a narrow 12–30 second clip around the phrase.
2. Re-run a second MLX model with word timestamps and previous-text conditioning off.
3. Compare primary ASR, auto captions, targeted ASR, sentence syntax, and verified canonical spelling.
4. Preserve a clip-confirmed spoken slip when the task is source-faithful; correct a proper-name spelling only when the intended canonical entity is clear.
5. Record the chosen form and evidence in the correction ledger.

Do not let a reviewer replace an ambiguous phrase with a familiar product/company name without this gate.

## 4. Finite segmentation convergence

The acceptance target is **zero blocking defects**, not zero possible merges.

Blocking:
- protected phrase split
- orphan fragment with no small-sentence readability
- packed question/answer beats
- misleading quote/predicate attachment
- overlength cue
- token/source-order loss

Optional, not blocking:
- two independently readable cues that could also fit together under 27 characters
- an equally valid rhythm alternative
- a topic-setting fragment or short reaction that works on screen

Finite protocol:

1. Run one exhaustive every-cue/every-boundary review on an immutable hash.
2. Integrate all adjudicated findings once.
3. Recheck changed windows and both outer seams, plus deterministic whole-body lint.
4. Do **not** reopen untouched ranges as a new aesthetic search. Repeated full-range reviews can endlessly discover increasingly optional 27-character packing.
5. Run another full review only if lexical/source edits changed meaning, a partition was never reviewed, or the previous pass was not exhaustive.

## 5. Final body gates

- Source/term review PASS on the delivery hash or on an earlier hash followed only by proven token-preserving boundary moves.
- No blanks, sentence-final periods, rejected terms, or cues over the project maximum.
- Baseline drift remains below the omission trigger or receives an explicit omission review.
- Freeze body/hash before final alignment; do not spend the alignment budget on every intermediate revision.
