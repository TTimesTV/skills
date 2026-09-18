# Front-half “0건 수렴검수” residual question→answer scan

Use after a prior generation’s many segmentation findings have already been applied to an immutable long-form candidate and the next assignment asks whether a bounded half has converged to zero.

## Durable lesson

A convergence label such as `0건 수렴검수` is an acceptance target, not a required verdict. Even when all prior proposed strings remain present, run a fresh intra-cue scan for `?` followed by additional text. One residual packed question→answer beat is enough to keep the result at FAIL.

## Required classification

For every cue containing text after `?`, classify it manually:

1. **Non-finding:** quoted or reported question whose suffix is an attribution/continuation, e.g. `...?라고`, `...?"라고 나오게 되고`.
2. **Finding:** a completed direct/rhetorical question followed in the same cue by the start of its answer, especially when the following cue continues that answer.

Do not flag punctuation mechanically. Read the previous and next cue and decide by speech function.

## Token-preserving repair pattern

Current:

```text
중국 건 뭐냐? 단순 업무로, 비용
이게 뭐냐면 효율화예요
```

Better boundary-only redistribution:

```text
중국 건 뭐냐?
단순 업무로, 비용 이게 뭐냐면 효율화예요
```

The repair separates the completed question from the answer, preserves token order/content, and keeps both cues within the 27-character box.

## Convergence report gate

- Freeze and hash the candidate; never edit it during review.
- Inspect every assigned cue and boundary plus the requested outer seam.
- Verify prior in-scope proposals by exact current-string occurrence, but do not treat that as proof of zero new findings.
- Enumerate adjacent pairs that fit under 27 only as candidates; do not fail optional merges.
- Separately scan `?` followed by text, direct quotations, and changed windows.
- State PASS only when confirmed blocking findings are exactly zero; otherwise report the residual finding even if the assignment title says `0건`.
- Recheck the closing candidate hash and state `no_candidate_edits: true`.
