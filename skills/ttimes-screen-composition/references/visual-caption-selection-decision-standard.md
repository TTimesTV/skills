# TTimes visual-form and caption-selection decision standard

Status: provisional gold from the Park Nam-gyu user-authored screen-composition corpus and direct user corrections through 2026-07-17.

## 1. Start from the viewer task

Do not begin with a source or file format. Ask what the viewer must do in this beat.

```text
recognize a moving action, place, process, or application → VIDEO
identify a person, historical object, event, or fixed subject → PHOTO
see that a claim, rumor, policy, market event, or corporate exit was reported → ARTICLE
verify a number, ranking, trend, comparison, or authoritative finding → REPORT/DATA
understand an invisible mechanism, structure, relationship, or hypothetical future scene → GRAPHIC
understand/feel the speaker without added help → ONE-MAN / NO MATERIAL
```

A source company may be selected for footage abundance and quality. Source identity does not automatically become the story's subject.

## 2. When to use video

Use video when motion or real-world context carries information:

- a machine, robot, vehicle, production line, installation, launch, charging, coating, stacking, or storage process
- an operating facility, disaster scene, industrial scale, place, or atmosphere
- an application whose physical integration is clearer in motion: a solar panel sliding from a car roof
- ordinary B-roll that directly covers a spoken noun or situation

Video can be:

- `DIRECT_VISUALIZATION`: the spoken object/action is visible
- `PROCESS`: a sequence or mechanism is visible
- `APPLICATION`: a real use case is visible
- `GENERAL_INSERT`: a related, clean shot covers the speech and changes rhythm

Source selection priority for ordinary inserts:

```text
relevant scene availability
→ clean production quality
→ recognizable and searchable official channel
→ editability and shot variety
→ exact company semantics only when the story requires it
```

Google, NVIDIA, Tesla, CATL, Nissan, Figure, Qcells, Hanwha, Samsung, and similar official channels can function as practical footage libraries. A CATL ESS-project video may supply a solar-panel passage without claiming CATL manufactured the panels.

Do not use video as evidence of a claim it merely illustrates.

Spoken captions:

- footage only → KEEP
- footage + short object label/callout → KEEP
- footage + editorial `//자막` → SUPPRESS
- footage continues after editorial caption ends → resume spoken captions immediately

## 3. When to use a photo

Use a photo when a fixed identity or historical reference matters more than motion:

- person/profile/researcher
- historical satellite, invention, building, product, or document
- one exact event/object for which moving footage is unavailable or unnecessary
- side-by-side identity/comparison

A photo answers `who/what was it?`, not `how did it work?` unless converted into an annotated graphic.

Use a label/profile when identity would otherwise be unclear. A small label can coexist with spoken captions. A large editorial card suppresses them.

## 4. When to use an article capture

Use an article when the visual claim is:

```text
this was reported
this issue entered public discussion
this company announced/exited/started something
several separate corporate cases support the same market claim
```

Evidence boundary:

```text
article proves the existence and wording of the report
article does not automatically prove the underlying claim is true
```

Examples:

- Musk-perovskite article: proves that an interest story was reported, not Musk's actual interest
- Samsung/SK/LG solar-withdrawal articles: each contributes a different company exit; three simultaneous captures show ecosystem contraction

Article crop requirements:

- outlet
- company/actor
- readable headline or relevant sentence
- date when material
- no crop that changes qualification or context

Composition:

- article is a caption-like reading layer → spoken captions SUPPRESS by default
- article over a background visual → background + article; spoken captions SUPPRESS
- multiple articles: simultaneous when each is one component of a single evidence bundle; sequential when chronology or stepwise comparison is intended; ask if unspecified

## 5. When to use a report or data visual

Use a primary report, official table, dataset, or chart when the claim depends on:

- exact quantity, percentage, capacity, efficiency, cost, market size, ranking, or forecast
- comparison across countries, companies, technologies, or years
- trend, distribution, or causal/technical evidence
- an authoritative institutional finding

Prefer a report/data source over an article headline when the number itself is central.

Do not place a dense report page on screen by default. Extract and recreate only the required evidence:

```text
claim label
+ value/unit
+ basis date/scope
+ comparison axis
+ source
```

A readable chart/table/report crop is a primary reading object, so spoken captions are normally SUPPRESS. A tiny source line does not itself suppress them.

## 6. When to use a graphic

Use a graphic when the viewer cannot see the concept directly:

- atomic/crystal structure
- energy/data flow
- cause/effect or trade-off
- layer stack and interface
- process stages
- scale or thickness comparison
- hypothetical future application

Generated images and embedded references default to `REFERENCE_ONLY / RECREATE_GRAPHIC`.

Graphics can persist while callouts change. Example:

```text
persistent ABX3 crystal graphic
→ arrow/label A
→ arrow/label B
→ arrow/label X
→ concluding composition-effect message
```

Text inside a graphic may be an object label rather than an independent caption card. Render form and editorial function are separate.

## 7. When to add no material

Use one-man/no material when:

- the speech is already concrete and immediately visual
- facial expression, authority, emotion, hesitation, or reaction is the strongest screen
- an added insert would be generic decoration
- the only available footage implies an unsupported company, place, date, or cause
- the viewer needs to listen rather than split attention

## 8. Caption selection gate

Add an editorial caption only when speech plus visual still leaves a specific viewer task unresolved.

| Need | Caption type | Use when |
|---|---|---|
| fix the next question/axis | `C1-Q / C1-TR` | long or strong question, selective transition |
| leave the conclusion/problem/strategy | `C2-THS / C2-REV` | viewer must retain the takeaway |
| lock an exact date/number/event | `C3-EVT / C3-NUM` | factual evidence is central |
| explain a term or mechanism | `C4-TERM / C4-MECH` | speech assumes unfamiliar knowledge |
| show comparison/relation/process | `C5-CMP / C5-REL / C5-PROC` | A–B relation matters more than nouns |
| preserve exact wording | `C6-QUOTE` | expression/attribution itself matters |
| identify an object/person/source | `C7-ID / C7-LBL / C7-SRC` | screen target would otherwise be unclear |
| nothing is missing | none | do not duplicate speech |

## 9. Caption writing rules

### Question

- not every spoken question
- use when it clarifies a long question, fixes a long-answer axis, or refreshes rhythm
- preserve target/scope; no invented premise

### Thesis/emphasis

- one takeaway
- may be an editorial expansion, but label it `PARAPHRASE / EDITORIAL_EXPANSION`
- do not strengthen possibility into certainty

### Fact/number

- value, unit, basis, date/scope, source
- preserve `about`, `maximum`, `theoretical`, `lab`, `commercial`, and forecast status

### Explainer/term

- define only what is needed for the next speech
- do not dump producer research notes into the final card

### Relation/process

- state what the arrow means: energy, sequence, control, composition, ownership, or cause
- do not turn parallel events into steps

### Quote

- exact wording and attribution
- a reported rumor is not a direct quote
- a PD summary is not a quote even when quotation marks are used for emphasis

### Label

- short noun phrase attached to a visible target
- object label alone can coexist with spoken captions

## 10. Spoken-caption switch

Decide from reading load, not only markers.

```text
ordinary video/photo → KEEP
small object label/callout → KEEP
small logo/source credit → KEEP
explicit editorial //자막 → SUPPRESS
readable article/headline → SUPPRESS
readable report/chart/table → SUPPRESS
editorial caption ends while material continues → resume KEEP on next blue speech
```

Audio always continues. The spoken transcript/SRT remains complete outside this visual switch.

## 11. Final per-beat decision record

```text
blue sync speech
viewer task
material need: REQUIRED / OPTIONAL / NONE
visual form: VIDEO / PHOTO / ARTICLE / REPORT_DATA / GRAPHIC / ONE_MAN
source and practical selection reason
visual story function
caption need and function
exact caption/label text
speech-caption mode
entry/exit and persistence
source/fact/rights state
ambiguity requiring PD answer
```

## 12. Ask the PD only when necessary

Ask one narrow question when the document cannot resolve:

- simultaneous vs sequential multi-asset layout
- replace vs build callout behavior
- article as background texture vs readable evidence
- editorial caption end while material persists
- direct quote vs editorial summary
- source company meaning vs practical footage convenience
- whether a generated/reference image is final or recreation-only

Do not ask about obvious direct inserts, familiar official-footage sourcing, or explicit adjacency that the DOCX already resolves.
