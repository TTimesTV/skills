# Quantitative runtime-discrepancy attribution

Use this when a DOCX-guided rough cut is materially longer or shorter than a human editor’s claimed result and the task is to identify the missing time without changing source files.

## 1. Freeze the duration ledger

Record independently:

- source duration
- generated rough-cut duration
- claimed editor duration, explicitly preserving qualifiers such as “about”
- generated union-cut duration
- crossfade contribution

Compute the unexplained delta from probed media durations, not rounded display labels. Do not treat an approximate claimed runtime as frame-accurate ground truth.

## 2. Search for alternate edit-document semantics

Before blaming alignment, inspect all matching source/original/cut-edit DOCX variants already available for the same recording. Hash them and parse `word/document.xml` directly. Compare:

- active strike/double-strike characters and semantic groups
- `w:del`/`w:moveFrom` characters and groups
- marked speech blocks
- groups beginning or ending a block
- whole-block deletions
- inserted editorial notes

A transferred or flattened DOCX can preserve only a narrow strike subset while a real tracked-edit document encodes much broader sentence, question/answer, or whole-block deletions. Compare semantic deletion plans; do not assume same filename stem means same edit scope.

Also classify relocation separately from deletion. Red destination text plus a struck/red source often means “move this retained passage,” not “remove it from the program.” A correct move removes the source occurrence and reinserts the same audio at the destination, so its net runtime contribution is approximately zero. Deleting the source without reinsertion creates an order defect and biases the generated runtime shorter; it cannot explain an output that is already too long.

Verify every alleged reference artifact before using it: probe media duration, inspect document text/markup, and confirm it is a cut output rather than the original recording, an empty export, or an unrelated example. Directory names such as `완료` and filename labels such as `수정 후` are claims, not evidence.

## 3. Align competing deletion plans independently

Extract each document’s deletion groups using the same speaker/timestamp parser and align each plan independently to the same word-level ASR timeline. Report:

- aligned group count and review count
- unioned deletion duration (not sum of runs or overlapping ranges)
- predicted output duration
- difference from the generated output and claimed runtime
- alignment similarity distribution

Do not union two competing document plans unless evidence says one is an additive supplement. Usually they are alternative edit decisions; compare them side by side.

## 4. Falsify common hypotheses quantitatively

### Unremoved pauses

Run `silencedetect` at multiple declared thresholds and minimum durations. Intersect silence intervals with retained intervals from the manifest. Report both raw retained low-energy duration and a realistic trim policy that leaves a short tail per gap.

Use an aggressive threshold as an upper-bound stress test. If even the unsafe upper bound is below the unexplained delta, pauses cannot be the sole cause. Note that high thresholds can classify quiet speech as silence.

### Boundary or timestamp drift

Measure:

- timestamp-to-aligned block-start offsets
- initial-to-final alignment union difference
- total boundary slack around first/last aligned words

For partial deletions, prefer paragraph-constrained alignment over fuzzy-matching each deletion against a broad time window:

1. Use the DOCX timestamp and the next paragraph timestamp only to define a local search window; display timestamps are often floored.
2. Align the complete source paragraph to the local ASR character stream.
3. Map each deletion's normalized source offsets through that alignment to ASR word boundaries.
4. Run an independent prefix/suffix-anchor method as a sensitivity check and report the resulting union-duration range.
5. Flag low-similarity occurrences, but also state whether they change the interval union. A dubious short occurrence contained inside an adjacent deletion can be semantically wrong yet runtime-neutral.

Small local offsets cannot explain a multi-minute global discrepancy. Account for crossfades explicitly. If `N` unioned cut intervals create `N` joins and each join overlaps by `x` seconds, predicted output is:

`source_duration - cut_union_duration - N * x`

The accumulated contribution can be decisive: 29 joins at 100 ms remove 2.9 seconds and can turn a near-match into an exact rounded-second reproduction. State the crossfade convention because the DOCX alone does not determine it.

### Mechanical sentence/block expansion

Simulate at least two counterfactuals:

- expand each marked range to ASR sentence boundaries
- delete every marked timestamp block in full

Calculate union duration and predicted output. If either uniformly over- or under-shoots, reject it as a universal rule. A selective human edit plan may still use those operations on specific passages.

## 5. Attribute without overclaiming

Prefer a ranked conclusion:

1. directly evidenced alternate deletion plan
2. selective sentence or question/answer block removal
3. retained-pause trimming
4. boundary/timestamp drift

State how much of the delta each hypothesis explains. If the claimed editor duration is approximate or the actual editor audio/EDL is unavailable, identify the remaining seconds as unresolved rather than forcing exact attribution.

A strong falsification test is: if the independently aligned tracked-edit plan predicts the editor artifact within the stated rounding tolerance, the document-version/edit-semantics explanation is sufficient; otherwise request the actual editor audio or EDL for join-by-join comparison.

## Independent-review conference for disputed attribution

When the user asks agents to confer, do not merely fan out three similar opinions. Use two rounds:

1. Dispatch orthogonal investigators: OOXML/markup forensics, audio-duration and pause/boundary accounting, and verified working-example comparison.
2. Require each investigator to state measured evidence, explained seconds, unresolved seconds, and falsifiable predictions.
3. Feed the three reports into a second adversarial round. Each reviewer must challenge the others’ strongest claim and identify any conclusion that depends on an unavailable editor artifact.
4. The main agent publishes a ranked consensus with `confirmed`, `partially explanatory`, `falsified`, and `unresolved` buckets. Do not synthesize exact attribution from rounded runtime alone.

The conference is complete only when every proposed cause has a duration contribution or a concrete artifact-level test.

## Pitfalls

- Comparing deletion-character totals without mapping them to audio time
- Summing cut durations instead of taking interval union
- Combining two alternative DOCX cut plans and calling the result authoritative
- Treating every low-energy interval as safely removable silence
- Calling an “about N minutes” claim exact to the second
- Concluding “alignment error” before checking whether a broader tracked-edit DOCX exists
