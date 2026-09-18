# Approved-cut front range: strict token-preserving cue body

## Trigger

Use this pattern when the user asks for the front or another bounded section of an already approved cut transcript as a timecode-free TTimes 말자막 초벌 body and explicitly requires actual spoken order/words to be preserved.

## Durable lesson

`승인 컷 원고` is already editorially accepted. In this route, segmentation may change but lexical content is frozen by default. “Meaning preserved” is not enough: fillers, repetitions, acknowledgements, colloquial endings, and self-repairs are part of the approved speech unless the user explicitly requests cleanup.

Forbidden silent cleanup examples:

- deleting `뭐`, `어`, repeated `네`, or repeated `막`
- `영화 보면은` → `영화 보면`
- `월드 모델을 설계를 하려면` → `월드 모델을 설계하려면`
- `앉아 가지고` → `앉혀서`
- `돼 가지고` → `돼서`
- `위로 위로금` → `위로금`

Allowed default corrections are narrow:

- spacing/orthography: `배송완료` → `배송 완료`, `게이트 키퍼` → `게이트키퍼`
- punctuation useful for viewing
- explicit, obvious ASR/grammar correction recorded in a small normalization ledger

## Workflow

1. Read the exact source range and small boundary context.
2. Exclude metadata-only rows: speaker/timestamp headers and blanks.
3. Draft cue-body lines in source order; one non-empty cue per line.
4. Segment by thought closure and protected phrase attachment, counting spaces in width.
5. Keep ≤25 where practical and ≤27 as the practical maximum.
6. Run body lint and protected-phrase candidate audit.
7. Run a normalized token sequence diff between source utterances and the concatenated body.
8. Inspect every non-equal opcode. Restore accidental deletions and wording substitutions; allow only ledgered spacing/orthography differences.
9. Re-run width and punctuation checks after every patch.

## Normalized diff design

- Strip only speaker/timestamp metadata and editorial parenthetical English expansions when those are not spoken.
- Normalize punctuation and whitespace.
- Apply an explicit correction ledger symmetrically to source and body before comparison.
- Compare token sequences with order preserved.
- Treat every `delete`, `insert`, and `replace` as review-blocking until adjudicated.

A high similarity ratio alone is not an acceptance gate. A 99% ratio can still hide dropped fillers or a meaning-changing rewrite. Acceptance is based on reviewing every residual diff block.

## Mechanical acceptance checks

- no blank lines
- no speaker/timestamp metadata
- one cue body per line
- zero lines above 27 characters, spaces included
- zero sentence-final periods
- question marks retained for real questions
- every residual normalized source/body difference explained by the correction ledger

## Delivery

Unless requested otherwise, respond only with the saved path and brief metrics: cue count, maximum length, over-limit count, blank count, and period-ending count.
