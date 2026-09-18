# Long-form SRT review convergence and freeze discipline (2026-07-21)

## Why this exists

A long approved-cut interview entered an expensive review loop:

1. Main froze candidate A and dispatched source/segmentation/term reviewers.
2. Main kept editing the live body while reviewers ran.
3. Returned line numbers and conclusions belonged to stale candidate A.
4. Main applied findings, froze B, then edited B again while fresh reviewers ran.
5. Source-fidelity fixes restored spoken tokens while segmentation fixes removed or paraphrased them, producing oscillation.
6. Repeated full alignment/coverage runs consumed the tool budget before final delivery.

The durable lesson is not “review more.” It is to make review generations finite, immutable, role-bounded, and convergent.

## Convergent review protocol

### 1. Finish Main body work before the review generation

Before freezing:

- run source-diff and correction-ledger checks;
- run whole-body intra-cue grammar and every-boundary protected-phrase checks;
- run one diagnostic alignment only if timing can expose body omissions;
- integrate all Main-known fixes in one batch.

Do not dispatch final reviewers while Main still has a queue of planned body edits.

### 2. Freeze one immutable candidate

Copy the body to `review/candidate_<sha256>.txt`; record hash, line count, char count, question count, max length, and source-diff metrics. Reviewers receive only this path.

While final reviewers run, **do not edit the working body**. Work only on non-text preparation such as delivery naming or validation scripts. Any text edit invalidates the review generation.

### 3. Bound reviewer authority

- Source reviewer: may demand restoration/removal of lexical tokens only with approved transcript plus audio/ASR evidence.
- Segmentation reviewer: token-preserving boundary and punctuation changes only. It may flag an intra-cue lexical problem but must not silently rewrite it.
- Term reviewer: canonical spelling/case/number. Do not force unspoken English parentheticals or glossary expansions when they break the 27-char box or protected phrases.

When roles conflict, use this hierarchy:

1. actual cut audio;
2. approved cut transcript;
3. correction ledger / verified official term;
4. readable Korean minimal correction;
5. reviewer preference.

A cleaner paraphrase is not automatically a correction.

### 4. Integrate once, by exact string

After all reviewers in the generation return:

- apply only exact strings still present;
- classify each finding as source restoration, grammar correction, boundary move, punctuation, or terminology;
- resolve conflicting findings before editing;
- apply the accepted set in one Main batch;
- generalize confirmed error classes across the whole body;
- run mechanical audits once.

Do not alternate source and segmentation patches line by line; this recreates the same conflict repeatedly.

### 5. One fresh verification generation

If integration changed the body materially, freeze candidate B and run one final combined fresh verifier. During this verifier, do not edit. Candidate B is the intended delivery revision.

If candidate B returns a small number of exact confirmed errors, patch them and run Main's deterministic full audits; request another reviewer generation only when the fixes alter meaning, source coverage, or many boundaries. Avoid infinite “one more fresh reviewer” loops.

## Alignment budget

- Mutable-body stage: at most one diagnostic alignment to expose missing spoken words or sub-0.7-second segmentation failures.
- Frozen final stage: one full alignment, gap classification, timing repair, and final regeneration.
- Do not repeatedly align every intermediate patch generation.

For ASR gaps, distinguish:

- **word absent from body** → source/grammar decision; timing cannot fix it;
- **word present in body but outside cue interval** → timing-only extension;
- **filler/false start intentionally omitted** → document intentional omission if allowed by the task;
- **approved-cut strict mode** → preserve clearly audible short responses and meaningful false starts unless explicitly authorized to clean them.

## Punctuation and lint cautions

A cue ending in a comma is not automatically structurally wrong when it is an intentional list, quote continuation, or audible false start. Mechanical `final comma` warnings require manual adjudication. Do not remove living punctuation merely to make a structural counter zero.

## Patch-scope safety during integration

A review finding may require deleting or replacing one cue, but broad block replacement can silently remove valid neighboring cues. This is especially dangerous with a three-line `old_string` replaced by an empty string.

- Delete only the exact cue plus the minimum newline needed; never use surrounding meaningful cues merely to make the match unique and then replace the whole block with empty text.
- After every deletion, quote-boundary edit, or multi-cue repartition, re-read at least 2–3 cues on both sides and compare the local normalized source sequence.
- After each integration batch, run the whole-body source/body diff again. A passing length/SRT validator cannot detect a valid sentence that was accidentally deleted.
- If a broad patch applies more text than intended, restore the neighboring source lines immediately before doing any further review or alignment.

## Async-review completion gate

A dispatched background reviewer is incomplete until its actual report/summarized result returns and Main has adjudicated it.

- Do not mark the review todo complete, copy the candidate to the final delivery name, or call the artifact `final` while the required latest-hash reviewer is still running.
- Tool-call or context pressure is not a reason to silently promote a provisional candidate. If necessary, stop editing and wait; if the user explicitly needs an early artifact, label it `Main 검증 선납품본` and state that a reviewed replacement may follow.
- Reviewer self-reports for older hashes remain useful only through exact-current-string matching. They do not certify the current candidate.
- The delivery hash must be recorded after the last body edit and must match the body used for the final SRT generation.

## Final gate

Before delivery, the exact delivered body hash must be the hash reviewed or the result of only explicitly enumerated tiny fixes followed by complete deterministic audits. Report neither “review integrated” nor “final” while a required reviewer is still running. Also verify that the final reviewer report file/result actually exists and has been read; dispatch success alone is not review completion.
