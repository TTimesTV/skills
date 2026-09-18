# Existing SRT reaction/filler cleanup

Use when the user likes an existing TTimes body/SRT but says interjections, reaction turns, or habitual words such as `한`, `좀`, `이제` are too frequent. New caption generation already uses the cleanup default in SKILL.md; this reference describes updates to approved artifacts.

## Scope

This is a **targeted cleanup of an approved SRT**, not a transcript rebuild. The user-provided/uploaded file is the authority for this pass, even when a local file has the same basename.

## Classification

Remove when explicitly authorized:

- Leading filler: `네, 사실…` → `사실…`
- Mid-sentence filler: `찾기 위해서 네, 그 일을…` → `찾기 위해서 그 일을…`
- Trailing filler: `그렇죠, 네` → `그렇죠`
- Standalone reaction cue: `네`
- Repeated pure reactions: adjacent `네, 맞습니다` / `네, 맞습니다` → one `맞습니다`, or remove both when the user asks for aggressive reaction cleanup
- Other standalone phatic reactions when the user's request clearly covers them: `맞습니다`, `그렇죠`, `맞아요`, `그럼요`, `알겠습니다`, repeated `아니죠`
- Habitual wording: `한 3시간` → `3시간`, `한 200명 정도` → `200명 정도`, `좀 더 정리` → `더 정리`, `이제 AI를 쓰면` → `AI를 쓰면`. Do not stop after removing only `어/음/네`.

Preserve:

- Numeral `네`: `네 가지`, `네 명`
- Content-bearing homographs: `일을 한 사람`, `GPU 한 대`, `한 번`, `좀 전`, temporal `이제부터`. Inspect context rather than deleting matching substrings. Keep substantive uncertainty, conditions, and quantity ranges.
- Semantically necessary question/answer turns: `그거 됩니까?` → `됩니다`
- Content-bearing summaries or reformulations: `그 역할이군요`
- Closing thanks unless the user asks to strip the closing: `감사합니다`
- `네` that genuinely changes polarity, commitment, or speaker-turn meaning

## Safe procedure

1. Parse SRT blocks and inspect every candidate, including `네/한/좀/이제`, with previous/current/next cue context.
2. Exempt numeral `네` and substantive answers before editing.
3. Remove filler tokens locally; never global-replace the substring `네`.
4. Remove now-empty reaction cues.
5. Scan a second reaction lexicon (`맞습니다`, `그렇죠`, `맞아요`, `그럼요`, `알겠습니다`, repeated `아니죠`) and manually adjudicate each hit.
6. Renumber cues sequentially. Preserve surviving cue timestamps exactly; deleted reaction speech may intentionally create an unsubtitled gap.
7. Update the companion body TXT if present; assert body lines exactly equal SRT bodies. Validate sequential indices, unchanged surviving timecodes, non-positive durations, overlaps, max text length, spacing, and remaining filler candidates. Keep raw ASR immutable and update any user-designated delivery copy.
8. Deliver one clearly named replacement file, not a chain of variants.

## Reporting

Briefly report:

- Number of `네` removals
- Number of standalone reaction cues deleted
- Explicit preserved exceptions (`네 가지`, substantive Q&A, closing thanks)
- Final cue count, max length, overlap count
