# Integrated layer, timing, and collision standard

Status: provisional v0.1.

## Layer stack

| z | Layer | Content |
|---:|---|---|
| 10 | `BACKGROUND` | one-man, B-roll, photo, article |
| 20 | `PRIMARY_GRAPHIC` | chart, comparison, mechanism graphic |
| 30 | `GRAPHIC_LABEL` | arrows, parts, numeric labels |
| 40 | `IDENTITY` | profile, place, date |
| 50 | `EDITORIAL` | question, thesis, explainer, fact, quote |
| 60 | `SPEECH` | spoken captions |
| 70 | `SOURCE` | material and quote credit |
| 90 | `INTERNAL` | review marks; never broadcast |

The numbers are logical priority, not fixed software layers.

## Safe zones

Use project templates first. As a draft planning coordinate system for 16:9:

- action safe: x 5–95, y 5–95
- essential text safe: x 7.5–92.5, y 7.5–92
- speech zone: x 10–90, y 77–91
- upper editorial zone: x 10–90, y 9–28
- center card zone: x 12–88, y 20–72

If a graphic occupies the speech zone, resolve in this order:

1. rearrange the graphic
2. temporarily relocate speech captions
3. delay or reduce the editorial caption
4. suppress speech display only as a last visual choice while preserving full SRT/transcript

## Simultaneous composition combinations

Allowed:

- one-man + speech when no `//자막` is active
- B-roll + speech when no `//자막` is active
- B-roll + editorial caption + source, with speech suppressed over the caption sync
- graphic + editorial caption/labels + source, with speech suppressed when an explicit `//자막` is active
- split/PIP + speech when no `//자막` is active

TTimes switching rule:

```text
//자막 active → SPEECH SUPPRESS
//자막 absent → SPEECH KEEP by default
```

Audio continues throughout. Speech captions resume after the blue sync range assigned to the editorial caption.

Conditionally allowed:

- explainer card + B-roll: speech is suppressed; simplify or time-separate if the card itself is dense
- question caption + spoken question audio: suppress spoken captions while the question card is visible
- direct quote + same spoken audio: suppress duplicate spoken captions
- readable article/headline capture + source: suppress spoken captions; the article is the primary reading object
- complex chart + labels: suppress spoken captions when the chart requires reading; keep labels sparse and reveal in sync if needed

Reduce or reject:

- question + emphasis + explainer simultaneously
- long speech + long explainer + changing B-roll
- same sentence repeated as speech, quote, and emphasis
- chart with dense labels plus another long paragraph
- decorative B-roll behind two reading blocks

## Density limit

One frame may contain:

- maximum 2 independent major reading/interpretation tasks
- normally maximum 3 text blocks: speech, one editorial/graphic block, source

Labels that are part of one graphic count as one task if they form a single coherent structure. If viewers must separately interpret several labels, count them accordingly.

Collision priority:

```text
evidence and meaning
→ speech accessibility
→ explanation/context
→ emphasis
→ identity
→ decoration
```

Move explanation to a neighboring beat before deleting evidence. Remove decorative footage before weakening meaning.

## Temporal object contract

Every object has:

```text
start_anchor
end_anchor
mode
persist
replace_target (when used)
```

Defaults:

- speech follows actual speech timing
- editorial text begins with its meaning and ends with the beat
- material exists only over the speech it illustrates/proves
- source appears with the material and never disappears earlier
- multi-line captions are simultaneous
- unchanged claims persist across shot changes rather than flashing again

Do not change fast B-roll while a quote, number, or explainer requires reading.

## Audio relation

```text
EXACT | CLEANED | PARAPHRASE | CONTEXT | DIRECT_QUOTE | LABEL
```

- speech: EXACT/CLEANED only
- emphasis: PARAPHRASE allowed, never stronger than source
- explainer: CONTEXT, independently fact-checked
- quote: DIRECT_QUOTE only
- labels: LABEL

## Status separation

### Asset

```text
RECOMMENDED
PD_SELECTED
DELIVERED
SOURCE_CLIP
REFERENCE_ONLY
RECREATE_GRAPHIC
MISSING_SOURCE
```

### Source

```text
SOURCE_VERIFIED
SOURCE_IDENTIFIED
SOURCE_UNRESOLVED
```

### Fact

```text
FACT_VERIFIED
FACT_QUALIFIED
FACT_PENDING
FACT_CONFLICT
FACT_NA
```

### Rights

```text
RIGHTS_CLEARED
RIGHTS_LICENSED_RESTRICTED
RIGHTS_PENDING
RIGHTS_UNKNOWN
DO_NOT_BROADCAST
```

Identified source, factual relevance, and legal usability are independent. Final blockers include pending/conflicting facts, unknown rights, missing sources, and unverified direct quotes.

## Asset and placement IDs

```text
//12             source asset ID in user-facing DOCX
USE=12-01        first placement
USE=12-02        later placement of the same asset
CAP-027          editorial caption object
```

Repeated source IDs are valid only for the same asset. A different file/source/date/interpretation requires a new ID.

## Inline DOCX object syntax

```text
//12. [USE=12-03] [기능=PROVE] [형식=영상]
[필요도=REQUIRED] [시작=“실제로”] [종료=수치 설명 전]
[자료상태=PD_SELECTED] [팩트=VERIFIED] [권리=CLEARED]

[verbal footage brief]

//자막 [ID=CAP-027] [기능=C3-NUM] [렌더=R3] [등장=D0]
[말자막=SUPPRESS] [문구고정=YES_EXACT] [위치=상단]
전력 수요 1GW

//출처 [FOR=12-03]
출처: ...

//동시표시
자료 + 수치자막 + 출처
//말자막: 해당 파란 싱크 동안 숨김
```

Keep natural-language clarity over code density. Codes are for consistency and validation, not to burden the editor.

## Adversarial gate

Reject or revise when:

- no independent function exists for a caption or material
- viewers face more than two major reading tasks
- image country/date/company/product does not match the claim
- an illustrative image is presented as evidence
- an editorial summary is quote-laundered
- article crop changes the headline/body meaning
- source credit is mistaken for rights clearance
- generated/reference material becomes final without approval
- asset IDs point to different sources
- screen suppression deletes speech from SRT/transcript
- red internal notes or `@@` leak into screen text

## GO conditions

- every object has ID, role, anchor/time, and zone
- simultaneous composition passes density and safe-zone checks
- speech and editorial text have explicit audio relation
- direct quotes and numbers are verified
- source/fact/rights are separate and final blockers cleared
- reused IDs identify the same source asset
- all multi-line animation exceptions are explicit
- current final ledger receives under-visualized, over-decoration, and composition/evidence review
