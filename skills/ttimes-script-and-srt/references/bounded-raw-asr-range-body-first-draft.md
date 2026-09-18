# Bounded raw-ASR range → TTimes 말자막 body 초벌

Use this pattern when the user names a short time range in an existing merged ASR and asks for an 원문 밀착 `body 초벌`, not SRT timing or a polished final script.

## Proven workflow

1. Read the exact ASR range and stop at the requested boundary. If a source segment starts before the boundary and continues slightly beyond it, include the complete utterance only when cutting it would leave an incomplete thought; do not pull in the next turn.
2. Read the project `glossary.txt` and `correction_ledger.tsv` before drafting. Treat confirmed spellings as authoritative; leave explicitly open terms conservative instead of inventing a correction.
3. Output one non-empty cue body per line with no timestamps, speaker labels, indices, markdown, or blank separators.
4. Stay transcript-close. Preserve claim order, modality, meaningful repetitions, reactions, and colloquial tone. Correct only confirmed terms, obvious ASR recognition errors, spacing, particles, and clearly broken syntax.
5. Segment as small readable sentences. Avoid splitting subject–predicate, object/adverbial–predicate, adnominal–noun, dependent-noun, auxiliary-verb, number–unit, or fixed technical-name chunks.
6. Keep sentence-final periods out. Preserve useful question marks, commas, and quotation marks.
7. Target ≤25 visible characters and enforce a practical maximum of 27, counting spaces and Latin characters.
8. Run both `audit_caption_body.py` and `audit_protected_phrase_splits.py`. Manually adjudicate every protected-split candidate; regex candidates are review prompts, not automatic failures.
9. Verify: UTF-8, no blanks, no timestamps/speaker labels, no sentence-final periods, no line over 27, line count, max/average length, and SHA-256.

## Important fidelity pitfall

Do not solve every split warning by paraphrasing. First try boundary redesign. If a long proper noun makes an intact source construction impossible under 27 characters, use the least meaning-changing local syntax repair and preserve modality (`~라고 봐요`, `~일 수도 있습니다`). Never strengthen a hedge into a categorical claim merely to make one cue shorter.

## Session example

A 00:00–07:00 Korean technical-interview range was drafted from merged raw ASR using a project glossary/correction ledger. The final body had 195 non-empty lines, maximum 27 characters, no timestamps/speaker labels/blank lines/final periods, and only one mechanically flagged transition (`말하자면 이번에는 / 그냥 배를 만든 게 아니라`) remaining after manual adjudication as a valid discourse boundary.
