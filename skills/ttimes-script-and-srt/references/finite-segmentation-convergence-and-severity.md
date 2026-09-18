# Finite segmentation convergence and severity gate

## Problem

Long-form all-boundary review can become non-terminating even when source fidelity is already PASS. Each fresh reviewer may discover more adjacent cues that *could* be merged under 27 characters, then a later review proposes another equally valid packing. This confuses optional density/style improvements with delivery-blocking segmentation defects.

## Severity classes

### Blocking — must reach zero

Count as a blocking segmentation finding when the current cue architecture causes at least one of these:

- a protected grammatical chunk is split: adnominal+noun, dependent noun+predicate, object/adverbial+predicate, auxiliary verb, number+unit, fixed technical name;
- a cue is an orphan fragment that cannot be understood as an intentional topic-setting beat, transition, reaction, or emphasis;
- two completed question/answer or separate thought beats are packed into one cue;
- direct quotation, particle, negation, hedge, scope, or predicate attachment is misleading;
- cue exceeds the approved visual maximum;
- source/timing evidence shows omitted or reordered meaning.

### Optional — do not block delivery

Do not count as a failure merely because:

- two adjacent, independently readable cues would also fit when merged;
- a subject cue and predicate cue form a natural two-beat reveal and neither is orphaned;
- a 26–27 character merge is denser but not materially easier to read;
- another reviewer prefers a different valid rhythm without fixing grammar, meaning, or visual-box risk.

Adjacent-fit enumeration is a candidate generator, not a zero-tolerance lint rule.

## Finite convergence protocol

1. Generation A: full independent source/term and all-boundary segmentation reviews on one immutable hash.
2. Integrate accepted blocking findings once.
3. Generation B: full role-bounded regression review on the new immutable hash.
4. If B changes only token-preserving boundaries, the next verification is limited to:
   - every changed window plus one outer seam;
   - deterministic whole-body audits;
   - any previously unreviewed partition.
   Do not reopen untouched, already-all-boundary-reviewed regions as a fresh aesthetic optimization search.
5. A third full generation is justified only by material lexical/source changes, a missing partition, or evidence that prior review was not actually exhaustive.
6. Freeze when source/term findings are zero and blocking segmentation findings are zero. Record optional style alternatives as non-findings/caveats, not FAIL items.

## Main adjudication questions

For every proposed merge, ask:

1. Does the viewer currently have to wait for the next cue to understand grammar?
2. Is the first cue truly orphaned, or is it a valid topic/rhythm beat?
3. Does the proposal fix a protected relation, or merely pack more text?
4. Does merging to 26–27 characters reduce readability despite grammatical completion?
5. Would another reviewer reasonably split it back without changing meaning?

If only questions 3–5 indicate stylistic preference, treat the proposal as optional.
