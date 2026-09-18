# Park Nam-gyu screen-composition user calibration

Date: 2026-07-17
Scope: user-confirmed examples from `(자료-완료) 박영선-박남규 컷편.docx`.

This is corpus calibration, not a universal rulebook. General rules belong in `SKILL.md`; this file preserves the cases that established them.

## 1. Authoritative DOCX grammar

The document encodes sync through formatting and adjacency.

```text
[yellow-highlighted cyan/blue bold object(s)]
material / //자막 / label / production instruction

[immediately following unhighlighted blue/cyan speech]
sync range for the preceding object(s)
```

- Several highlighted objects before the same blue speech share that sync.
- Red highlighted text is an internal production note, not viewer-facing text.
- Do not infer placement from asset numbering or folder order when the formatting-bearing DOCX is available.
- A clean transcript with the same or similar filename is not a substitute for the formatting-bearing version.

## 2. Spoken-caption switch

```text
explicit //자막 active over blue sync
→ spoken audio continues
→ spoken captions SUPPRESS

material only, no //자막
→ spoken captions KEEP

object label/callout without //자막
→ spoken captions KEEP by default
```

A label such as `(차 지붕 위에) ← 태양광` identifies an object and can coexist with spoken captions. It is not automatically an editorial-caption block.

## 3. Practical footage sourcing heuristic

The source company may be chosen because its official footage is abundant, clean, familiar, and easy to search. Do not invent brand strategy, endorsement, industry leadership, or cross-asset narrative from source identity alone.

```text
relevant subject
+ recognizable source
+ well-maintained official video library
+ usable clean shot
= practical insert source
```

The source company need not manufacture the depicted object. Record source origin and depicted subject separately.

## 4. User-confirmed cases

### Asset 01 — Tesla solar insert

```text
subject: solar cells
source: Tesla footage
reason: famous solar-related company; abundant, clean video; convenient discovery
function: ordinary illustrative insert
editorial caption: none
spoken captions: KEEP
```

Rejected over-reading: planned Tesla→SpaceX future-industry narrative, Tesla solar→Megapack visual ecosystem, or proof of a market claim.

### Asset 02 — SpaceX spacecraft solar insert

Space-industry speech is covered with a SpaceX shot showing solar attached to a spacecraft/satellite. SpaceX is a famous, footage-rich practical source. It is not proof of SpaceX perovskite adoption.

```text
editorial caption: none
spoken captions: KEEP
```

### Assets 03–07 — direct stock inserts

Flood, heat, thermal power, wind, and solar are direct AFP/Pexels stock illustrations of the corresponding speech. Do not convene a deep semantic review for obvious stock B-roll.

### Asset 08 — CATL project footage + editorial caption

Exact block:

```text
//자막
이상 기후 & 전력 부족 대응

//08. (태양광)_CATL_(1분 51초~)_태양광 쫙 깔린 장면 등 아무 장면.. (원맨 구간 X)

[blue sync]
그래서 기후 변화에도 대응을 하면서 그다음에는 AI 데이터센터의 전력 문제 해결
```

The solar passage was borrowed from a CATL ESS-project video because Chinese specialist solar-company names/channels were difficult to navigate, while CATL was familiar and maintained its YouTube materials relatively well.

```text
source_origin: CATL ESS-project footage
depicted_subject: solar panels/cells
company claim: none
composition: solar insert + editorial relationship caption
spoken captions: SUPPRESS
```

Do not infer that CATL manufactures the depicted solar cells.

### Asset 09 — Nissan solar-car footage + object label

Exact block:

```text
//09. Nissan solar roof/sliding footage
(차 지붕 위에) ← 태양광

[blue sync]
앞으로는 또 전기자동차에 대한 어떤 전기 수요
```

The Nissan shot was selected because electric car and solar generation appear together in one immediately understandable scene. Nissan itself carries no deeper strategic meaning.

```text
material: Nissan solar-car footage
label: object callout, not //자막
spoken captions: KEEP
```

### Asset 10 — Figure robot + editorial future thesis

Exact block:

```text
//10. Figure moving humanoid footage
//자막
전기로 움직이는 무기물이 많아질 미래

[blue sync]
현재보다 훨씬 많은 전기 에너지를 필요로 하고
```

The robot concretizes a new electricity-consuming object; the caption generalizes one robot into a future with many electrically driven inanimate objects.

```text
caption primary: C2-THS
caption secondary: C5-REL
audio relation: editorial expansion/paraphrase
spoken captions: SUPPRESS
```

It is illustrative, not proof that humanoids dominate future electricity demand or that Figure is the industry winner.

## 5. Review-effort calibration

Auto-resolve and move on when:

- speech noun/action and footage directly match
- the file is plain stock B-roll
- a famous company is merely a practical source of clean footage
- `아무 장면`, `대충 인서트`, or `재탕` already defines editor discretion

Ask the user only when intent cannot be recovered from the formatted DOCX and established grammar, especially:

- material and editorial caption have a non-obvious relationship
- object label vs editorial caption is unclear
- caption exit and spoken-caption resumption are ambiguous
- multi-line simultaneous/build/replace behavior is not explicit
- direct quote vs PD summary is uncertain
- article capture is evidence vs atmosphere
- generated reference is final vs recreate-only
- repeated asset has a non-obvious reuse purpose

Ask one narrowly scoped question at a time. State the current best interpretation before asking.
