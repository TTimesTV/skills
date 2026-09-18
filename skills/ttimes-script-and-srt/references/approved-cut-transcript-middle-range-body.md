# Approved cut-transcript middle-range → TTimes body

## Trigger

Use this lightweight route when the user supplies:

- an already approved cut transcript,
- an exact source line range,
- a prior approved SRT/body as the style reference,
- and asks only for a timecode-free `말자막 초벌 body`.

This is not a new ASR, SRT-alignment, or full-body regeneration job.

## Workflow

1. Read only the requested source range plus enough neighboring lines to confirm the true start/end.
2. Read a representative portion of the approved style reference. Measure its practical rhythm rather than copying timestamps or indices.
3. Remove speaker labels, source timestamps, blank lines, SRT indices, and timecodes from the deliverable.
4. Preserve every spoken word and the original order. Treat the approved cut transcript as authoritative; do not summarize, compress, or silently omit repetitions/fragments.
5. Apply only high-confidence corrections:
   - obvious spacing/particle/grammar errors,
   - confirmed person/product/technical-term normalization,
   - notation cleanup needed for a readable subtitle body.
6. Segment by sentence/thought closure and small-sentence readability. Keep predicates, dependent nouns, modifiers, quantities/units, quotations, and technical names attached where possible.
7. Use one non-empty cue body per line. No final prose periods; retain only useful question marks, commas, and quotation marks.
8. Target ≤25 visible characters including spaces; hard max 27 unless the user has approved a protected exception.
9. Save directly to the exact requested path.

## Fidelity check

For an approved transcript, omission control matters more than stylistic elegance.

- Join the selected source utterances after removing speaker/time metadata.
- Join the output body lines.
- Normalize whitespace and harmless punctuation, then compare the two streams with a sequence diff.
- Manually adjudicate every deletion/replacement. Allowed differences should be explainable as term normalization, annotation handling, or a high-confidence correction.
- Parenthetical English annotations require judgment: preserve the spoken form, use the established program spelling, or retain both when editorially necessary. Do not accidentally delete the underlying term.

## Mechanical validation

Report and verify:

- non-empty line count,
- maximum visible length including spaces,
- zero lines over 27,
- zero blank lines,
- zero speaker labels/timecodes,
- zero sentence-final periods.

Run both caption-body and protected-phrase audits. Automated candidates are review prompts, not automatic failures. Read the candidate boundaries manually and repair clear stranded modifiers, objects, predicates, or dependent-noun constructions.

## Useful repartition pattern

When a 28+ line contains a protected phrase, repartition the whole local sentence instead of splitting the protected construction. For example:

```text
BAD
평가받는
이유 중에 하나가 무엇이냐면

BETTER
한 단계 진전을 시켰다고
평가받는 이유 중에 하나가 무엇이냐면
```

Likewise, move material across a three-line window to keep an object and predicate together instead of patching only one boundary.

## Delivery

For a requested rough body, keep the chat response minimal:

- absolute saved path,
- line count,
- maximum line length,
- one short caveat only if something remains uncertain.
