# Body-first normalization and stale-review guard

## Why this exists

For long Korean TTimes dialogue, timestamps and SRT indices distract editors from broken Korean. The cue-body TXT must be the sole editorial authority. However, body-first editing introduces a second risk: “normalization” can drift into broad compression, and reviews dispatched before a large Main rewrite can become stale.

## Required order

```text
immutable transcript-close body baseline
→ mechanical body audit
→ local high-confidence correction
→ Main whole-body sentence/segmentation pass
→ reviewers inspect the current candidate body
→ Main integrates only source-backed findings
→ freeze final body + manifest/hash
→ align frozen lines to ASR words
→ prove SRT bodies equal frozen body exactly
```

Never repair prose directly inside timestamped SRT blocks. If text changes after alignment, edit the body TXT and regenerate the SRT.

## Immutable baseline

Before editing, preserve a transcript-close body baseline and record:

- path and SHA-256
- non-empty line count
- character count
- question-mark count
- numbers/ranges/units inventory
- English/product/company token inventory

The baseline is for omission and drift checks, not for delivery.

## Local normalization rule

“정상화” means:

- correct obvious ASR errors, particles, spacing, names, numbers, and units
- repair a broken sentence locally
- rebalance adjacent cues so each visual beat reads naturally
- remove repeated fillers only when no meaning, stance, emphasis, or turn-taking is lost

It does **not** mean summarizing several spoken clauses into polished prose. Prefer exact old-block → new-block replacements with expected occurrence counts. Avoid broad global phrase replacement unless it is a safe spelling normalization.

## Drift gate

After each major pass, compare candidate vs baseline:

- line-count delta
- character-count delta
- question-mark delta
- missing numbers/ranges/units
- missing company/product/person names
- missing negation or uncertainty markers

A large drop is a review trigger, not automatic proof of failure. As a practical warning, investigate reductions around 5%+ in characters or 8%+ in cue count. Read the changed blocks and run omission/distortion review against the **current** candidate. Do not explain a large reduction away as “just filler” without evidence.

When a precise number was simplified during normalization (`69% 이상` → `약 70%`), restore the source detail unless audio disproves it.

## Reviewer freshness rule

Reviewer findings are valid only for the body revision they inspected.

- Dispatch reviewers after the candidate body is stable enough to review.
- Record the reviewed body hash or character/line counts in the brief.
- If Main substantially rewrites the body after dispatch, treat line numbers and “no omissions” conclusions as stale.
- Re-run at least omission/distortion review on the current candidate, or perform an explicit baseline-vs-current content inventory before freeze.
- Search findings by quoted phrase when line numbers drift.

Recommended roles:

1. terms/numbers/ASR reviewer
2. sentence/segmentation reviewer
3. omission/distortion/over-polish reviewer

## Body quality gate

Before freeze:

- 27 visible characters max unless explicitly approved otherwise
- no mechanical final periods
- no number+unit splits
- no sentence-ending + new-sentence packing
- no stranded predicate/object/dependent noun
- all ≤7-character cues manually classified as real reactions, greetings, questions, or intentional emphasis
- all known-bad ASR spellings absent
- every ambiguous high-risk number/name/contract direction checked against source audio or authoritative evidence
- question-mark changes explained; punctuation count alone is never semantic proof

## Alignment gate

Only after body freeze:

1. align each frozen line to ASR word timestamps
2. inspect low-match cues manually with previous/next cues and the matching word-timestamp window visible
3. treat low fuzzy-match cues as a **wording-drift diagnostic before a timing defect**:
   - if Main reordered or paraphrased spoken phrases, restore source-close readable word order in the body;
   - freeze/copy the body again and rerun alignment;
   - manually force cue boundaries only after the body wording is stable.
4. enforce sequential, positive, non-overlapping times
5. inspect long holds, flashes, and reading speed; aim for no cue above about 18 CPS when nearby silence can safely extend display time
6. when correcting fast cues, consume only real adjacent silent gaps without overlap or unrelated-speech drift; do not move a caption into another sentence merely to improve CPS
7. assert `SRT cue bodies == frozen body lines` exactly after every regeneration and timing refinement
8. spot-check first, middle, last, all targeted-audio corrections, every low-match cue, and every manually adjusted cue
9. deliver only the clean `*_srt.txt` unless the user asks for reports

### Important pitfall

Broad readability rewriting can lower fuzzy alignment quality by changing phrase order even when the new Korean sounds better. For this workflow, the preferred recovery is source-close readable wording, not plausible-looking timestamps attached to a paraphrase. This improves both original-speech fidelity and timing reliability.
