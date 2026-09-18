# Caption function, render, and timing standard

Status: provisional v0.1, derived from the user-authored Park Nam-gyu `자료-완료` corpus and the 2026-07-17 standardization meeting.

## Three independent axes

```text
C = viewer function: why the text appears
R = render form: how it is presented
D = display behavior: how it changes over time
```

Expression tone is separate:

```text
EMPHASIS | NEUTRAL | EXPLAINER
```

A strongly designed number remains `C3`; a bold direct quote remains `C6`.

## Function taxonomy

### C1 — question and progression

- `C1-Q`: selective question clarification/emphasis
- `C1-TR`: transition or re-entry title

Use `C1-Q` when a long spoken question needs a visible axis, a long answer needs framing, or a strong question refreshes pacing. Do not add `Q.` to every question. Preserve the question's target and scope; do not add a premise or conclusion. Use `?`.

Use `C1-TR` only when viewers may lose the new topic or point of view. It is not automatically the chapter title.

Minimum verification: source-speech comparison; external verification when the question contains a factual premise.

### C2 — thesis and judgment

- `C2-THS`: core thesis or takeaway
- `C2-REV`: reversal, warning, bottleneck, or conclusion contrast

One caption, one conclusion. Preserve actor, target, conditions, probability, and scope. Do not convert `유망하다` to `성공한다`, or `가능성` to `필수`.

Useful structures:

```text
A가 아니라 B
핵심은 B
문제는 B
[actor] + [target/action]
```

Record `AUDIO_REL=PARAPHRASE` when it is a PD summary.

### C3 — fact and evidence

- `C3-EVT`: date/event/milestone
- `C3-NUM`: number/statistic/scale

For events preserve date meaning: announcement, development, commercialization, approval, and shipment are different.

For numbers require:

```text
value / unit / basis date / population or scope / actual vs forecast / source
```

Keep `%` and percentage points distinct. Preserve calculation formulas and conversion dates. A large number without its subject label is invalid.

### C4 — concept and context

- `C4-TERM`: term/system definition
- `C4-MECH`: mechanism, causality, or missing context

Recommended term form:

```text
용어(English, 한국어 풀이) : 한 문장 정의
```

Explain only the needed boundary: what it is, where used, what distinguishes it, and why it matters. Distinguish essential, typical, and optional components. Do not convert correlation into causality.

Long exact explainer cards are locked screen text. Set `wording_locked=YES_EXACT` and `line_break_locked=YES` when approved.

### C5 — relationship and structure

- `C5-CMP`: comparison and contrast
- `C5-REL`: composition, dependency, hierarchy, flow
- `C5-PROC`: process and sequence

For comparison, both sides must use the same criterion, period, unit, grammar, and information depth. For relationships, arrows must state whether they mean energy, data, ownership, control, or sequence. For processes, distinguish parallel and sequential events; one step should contain one action.

Multiple written steps default to simultaneous display. Use build only when accumulation itself teaches the logic.

### C6 — direct quotation

`C6-QUOTE` is reserved for exact speech or document wording whose expression itself matters.

Required:

- exact source wording
- speaker/author
- source time or document location
- context and date where material
- translation label if the displayed Korean is a translation

Do not put quotation marks around a PD summary or a synthesis of several utterances.

### C7 — identity, labels, and source

- `C7-ID`: person, company, institution, role
- `C7-LBL`: object, component, arrow, or graphic callout
- `C7-SRC`: source, date, basis, credit

Profile form:

```text
이름
소속 · 직함
```

Check the as-of date for positions. Labels remain short noun phrases. Source text must identify the actual origin, not `인터넷`, `뉴스`, or `유튜브`.

## Render forms

| Code | Form |
|---|---|
| `R1` | top/middle short overlay |
| `R2` | thesis/emphasis headline |
| `R3` | information/explainer card |
| `R4` | full-frame graphic |
| `R5` | split comparison |
| `R6` | quote card |
| `R7` | profile lower-third |
| `R8` | object label/callout |
| `R9` | source credit |

Function is invariant across rendering choices.

## Display behavior

| Code | Behavior |
|---|---|
| `D0` | all lines/items appear together; default |
| `D1` | sequential; previous item leaves |
| `D2` | build; previous items remain |
| `D3` | replace A with B in the same place |
| `D4` | fixed title/axis while values change |
| `D5` | full structure remains; spoken item highlights |

Line breaks are layout, not animation. No display instruction means `D0`.

## Relationship to audio

```text
EXACT        actual speech text
CLEANED      source-close correction
PARAPHRASE   editorial compression
CONTEXT      external explanatory context
DIRECT_QUOTE verified source quotation
LABEL        identity or graphic label
```

Spoken captions allow only `EXACT` or meaning-preserving `CLEANED`. Added captions may use the other relations but need appropriate verification.

## Spoken-caption coexistence

```text
KEEP | SUPPRESS | RELOCATE | HOLD | N/A
```

TTimes rule learned from the user-authored DOCX:

```text
highlighted material only before blue sync → spoken captions KEEP when the material has no substantial readable text
highlighted //자막 before blue sync → spoken captions SUPPRESS for that sync
material + //자막 before the same blue sync → show material + editorial caption; suppress spoken captions
readable article/headline capture → treat as a caption-like reading layer; spoken captions SUPPRESS by default
small object label/callout without //자막 → spoken captions KEEP
```

The spoken audio continues, and spoken captions resume after the editorial/article reading range ends. Small source credits and logos do not automatically suppress spoken captions.

Do not show:

- speech + long explainer + separate emphasis
- speech + long quote + duplicate emphasis
- two independent information cards
- the same sentence as speech, quote, and emphasis

If speech and screen text duplicate:

1. preserve as `C6` and explicitly suppress/relocate the duplicate speech display, or
2. compress to a distinct `C2` takeaway, or
3. remove the added caption.

## Verification levels

| Level | Minimum evidence |
|---|---|
| `V0` | editing and spelling check |
| `V1` | speech/source manuscript comparison |
| `V2` | reliable external source |
| `V3` | primary source plus basis check |
| `V4` | legal/rights/high-risk approval |

Minimums:

- C1: V1; factual premise V2+
- C2: V1; external factual conclusion V2+
- C3: V3
- C4: V2; numbers/medical/legal/safety V3+
- C5: V2; numerical comparison V3
- C6: V3
- C7-ID: V2
- C7-LBL: V1–V2
- C7-SRC: V3

## Decision tree

```text
follows actual speech? → spoken-caption layer
identifies person/object/source? → C7
exact source expression? → C6
external date/number/event evidence? → C3
comparison/relation/process? → C5
term/mechanism/context? → C4
main thesis/reversal/judgment? → C2
question/transition? → C1
none → likely no editorial caption
```

Classify by what the text actually does on screen, not how visually loud it looks.

## Required handoff fields

```text
caption_id
anchor/time
function_primary
function_secondary (optional)
tone
render_code
display_code
exact_screen_text
line_break_locked
wording_locked
time_in/time_out
speech_caption_mode
screen_zone
material_id and relation
AUDIO_REL
verification_level/status/source
editor_action
prohibited_action
```

Conditional fields include comparison axis, unit/basis, sequence map, quote speaker/source time, profile as-of date, callout target, rights, safe-area note, and `@@` correction provenance.
