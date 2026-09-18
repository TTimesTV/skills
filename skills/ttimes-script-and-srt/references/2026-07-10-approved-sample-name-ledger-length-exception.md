# Approved sample freeze, name ledger, and protected length exception

## Reusable lesson

For long TTimes SRT rebuilds, the approved 0–3 minute sample is a style contract, not disposable scaffolding.

1. Freeze the approved sample text and hash it.
2. Build the full body by preserving the sample as an exact prefix.
3. Before every final alignment, assert `full_body[:sample_line_count] == approved_sample`.
4. Do not let later global cleanup, old-body reuse, or automated merging rewrite approved sample cues.

## User-corrected proper names

A direct user correction such as a reporter/person spelling is authoritative for caption text.

- Add it to the project glossary/correction ledger immediately.
- Patch every derived editable artifact: approved sample, transcript-close baseline, working/final body, glossary, manifests when applicable, and deterministic builder scripts that could regenerate the old form.
- Keep raw ASR JSON immutable as source evidence unless the workflow explicitly defines a corrected-ASR derivative.
- Re-scan the workspace for the rejected spelling before final delivery.

Session example: `홍재희` was corrected by the user to `홍재의 기자`. The corrected form had to propagate to sample, baseline, glossary, builder, full body, and final SRT, while raw MLX output remained unchanged.

## Protected overlength exception

Character limits must not cause meaning deletion.

Session example:

```text
업무의 임팩트를 높이는 AI 레버리지 전략 실습 강좌
```

This source-faithful title is 29 visible characters. Removing `업무의` changed the scope of meaning, and an independent reviewer caught the omission. The user approved the restored 29-character cue.

Rule:

- First try a meaning-complete, source-faithful rewrite within the normal 25 target / 27 max.
- Never delete a meaningful source word solely to satisfy the limit.
- If the phrase is a title, quote, proper noun cluster, or other indivisible unit and no faithful ≤27 form exists, keep it whole only with explicit user approval (including approval of a sample containing it).
- Record the cue, length, and reason in the validation manifest.
- Preserve approved exceptions exactly in the full body and final SRT.

## Review-order pitfall

A broad protected-phrase linter is a candidate generator, not an editor. It may flag natural topic→answer and cause→result boundaries. Conversely, zero regex hits can still miss subject/predicate or omission errors. Main must adjudicate every candidate, manually read every adjacent cue pair, and compare reviewer findings against the current body hash.
