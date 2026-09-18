---
name: ttimes-editorial-copy
description: Use when writing or revising TTimes on-screen editorial copy from interview speech, including emphasis captions, one-line explainer captions, selective question captions, quote cards, and short technical labels. Classifies the requested output mode before answering, preserves the source beat's actual contrast and causality, returns copy-only blocks when the PD asks for captions, and separates explanation, transcript cleanup, and fact-checking from screen-copy delivery.
license: MIT
metadata:
  version: 1.0.14
  author: Hermes Agent
  hermes:
    tags: [ttimes, captions, editorial-copy, emphasis, explainer, broadcast]
    related_skills: [caption-layering-workflow, ttimes-screen-composition, ttimes-factcheck-research]
---

# TTimes Editorial Copy

## Overview

Use this skill for the **wording layer** of TTimes production: turning a spoken beat into concise screen copy without silently changing the task into transcript cleanup, technical explanation, or research commentary.

The first operation is always request classification:

```text
무슨 말이지?     → explain the speech
강조자막          → deliver emphasis copy only
설명자막          → deliver one-line definition only
교정              → repair the source sentence
팩트체크          → audit the claim and propose safe wording
```

Adjacent turns do not merge these modes. A prior explanation request does not authorize another explanation when the current request is `강조자막`.

## When to Use

Use for:

- `→ 강조자막`, `-> 강조자막`, or a bare `강조자막`
- `설명자막`
- short question, comparison, thesis, warning, definition, or quote cards
- iterative PD reactions such as `아닌 것 같은데`, `더 쉽게`, or `이 말은 아닌데`
- technical interview speech that needs concise but accurate screen wording

Do not use for:

- spoken-caption SRT segmentation
- full transcript rewriting unless explicitly requested
- screen-layer timing and material placement
- long research reports
- automated fact-check output when the PD asked only for copy

## 1. Classify the Requested Operation

Before drafting, set exactly one mode.

| Mode | Trigger | Output |
|---|---|---|
| `EMPHASIS` | `강조자막` | one code block, normally 1–2 lines |
| `EXPLAINER` | `설명자막` | one code block, normally one definition line; 2–3 lines when a historical program/policy needs goal and mechanism to be intelligible |
| `QUESTION` | explicit question-caption request | one short `Q.` line only when warranted |
| `QUOTE` | verified direct-quote request | exact quote with speaker/source context |
| `EXPLAIN` | `무슨 말`, `무슨 소리` | plain-language explanation, not caption copy |
| `CLEAN_SOURCE` | `원문 정리`, `교정` | cleaned source sentence |
| `FACTCHECK` | `검증`, `맞아?` | verdict and safe replacement wording |

If two modes are explicitly requested together, separate the outputs under short labels. Never infer multiple modes from conversational proximity alone.

Completion criterion: the response shape matches the current turn's trigger, not the previous turn's task.

### General-interview card-news wording calibration

For TTimes general-interview card-news copy, also load `../ttimes-cardnews-imagegen/references/jo-taeho-ep2-general-interview-calibration-20260903.md`.

The user-calibrated preference is not merely `short copy`. It is **concrete, spoken, action-first copy with a decisive payoff**:

- Cover: prefer `credible person + vivid action + practical benefit` over a topic taxonomy. `미국 의대 교수가 말아주는 / 바이브코딩 강의` is calibrated because the person establishes authority and `말아주는` makes the practical delivery vivid. Use one lively expression, not a stack of slang.
- Opening beat: start with what the viewer currently does or what visibly happens. Avoid report-style leads such as `연구팀은 ~를 연구했다`, institutional background, or a term definition when the useful tension can lead.
- Body: use two continuous paragraphs when the argument has two beats. Paragraph 1 shows the mechanism/action; paragraph 2 gives the trap, control rule, or judgment. Do not turn prose into a staircase of short fragments.
- Tone: prefer direct statements and concrete verbs over abstract nouns and generic endings. Avoid `~에 대한 이야기`, `~의 중요성`, `도움이 될 수 있습니다`, `고려해야 합니다` when the source supports a clearer action or judgment.
- Layout-sensitive writing: when left-aligned text looks visually left-heavy, keep the approved alignment and rewrite/reflow for balanced line widths. Do not solve a copy-width problem by silently changing the layout.
- Closing: use a reversal followed by a human-responsibility payoff when source-faithful. `더 많은 일을 맡기는 게 아닙니다 → 어디까지 맡길지 사람이 먼저 정하는 겁니다` is the calibrated rhythm. Emphasize the payoff paragraph, not both premise and payoff.
- Exact retrieval: if asked to reproduce an earlier description or caption, retrieval confidence is part of copy accuracy. If the exact source cannot be found, say so; never draft a plausible substitute and imply it is the original.

Failure signals: accurate but bloodless research-summary prose, definitions before stakes, several short left-stacked lines, generic `중요합니다` conclusions, and invented replacement copy after a failed retrieval.

## Word review caption calibration — 2026-09-17

When writing captions for a screen-composition Word review, place `[강조 자막]` and the useful wording candidate(s) in a parent comment anchored to source speech. Put why this beat and phrasing were selected in a genuine reply. This requested review mode overrides chat-only rules below that suppress rationale and alternatives; ordinary caption-only chat requests keep their concise single-block contract.

- Most emphasis captions use **명사형/개조식**: retain a concrete subject and a readable contrast, consequence or implication. Do not mistake this for lifeless abstract noun titles.
- Use a sentence in quotation marks when emphasizing the speaker's **actual quotation**; match the source exactly. Do not quote a PD paraphrase.
- Symbolic compression such as `전사 도입 ≠ 전 직원 활용` can occasionally fit, but is not the default style or a prohibited form. The user's accepted direction `회사가 AI를 도입해도 / 직원들이 쓰는 건 별개` demonstrates a concrete contrast, not a rule to make every caption conversational prose.
- Offer one candidate when clear; offer more only for meaningful differences in framing. No always-three rule, forced noun/sentence/quote trio, or synonym padding. No fixed candidate maximum inferred from examples.
- Explain the local meaning and why this wording belongs here. For alternatives explain what each foregrounds, briefly. Let actual speech determine number, length and rhythm.
- Read `../ttimes-screen-composition/references/word-review-framing-20260917.md` when combining captions with materials. Current user choices outrank historical broadcast observations.

## 2. Emphasis-Caption Contract

When the PD supplies source speech followed by `→ 강조자막`, `-> 강조자막`, or asks only for an emphasis caption:

- return **only one copyable code block**
- use one or two lines
- add no preamble, apology, rationale, cleaned transcript, technical explanation, or alternatives
- default to concise noun-phrase or clause-like wording
- preserve the beat's actual subject, contrast, and causal direction
- do not strengthen tentative speech into certainty
- do not add numbers, market leadership, attribution, or causation absent from the source

Preferred two-line logic:

```text
cause / condition / contrast
result / judgment / implication
```

### Paraphrase before compression

An emphasis caption should not merely shorten the speaker's nouns in the same order. Before drafting, restate the beat internally as `what remains true / what must change / why it matters`, then write the implication in fresh, immediately readable Korean.

- Preserve a source metaphor only when it sharpens the contrast. Example: `기존 전략의 본질은 그대로 / 콘텐츠의 그릇은 AI가 읽을 수 있게` is stronger than a literal list of `PR·콘텐츠 전략·AI 인식 점검`.
- If the source is abstract or repetitive, do not mirror phrases such as `종합적으로 진단하고 전략을 짜야`; convert them into the concrete editorial action (`트래픽 감소를 인정하고 / 브랜드 스토리가 지속될 전략을 재설계`).
- Keep the causal object explicit: `고객의 검색은 AI로 이동 / GEO를 외면하면 경쟁에서 밀린다` is readable without the surrounding audio.
- Do not manufacture a stronger thesis while paraphrasing. Tentative `~가야 하지 않을까` must not become definitive `수익화의 열쇠는`; use `수익화의 방향`, `~로의 전환`, or another source-faithful level.
- After the PD says `패러프레이징해보지?`, change the conceptual framing rather than merely replacing one or two words. Return only the revised block.

Examples:

```text
콘텐츠가 아직 부족한 프로젝트 아우라
일상형 AI 안경보다 VR에 가까운 경험
```

```text
버드배스 대신 렌즈 내부로 영상 전달
일상용 안경에 가까워지는 웨이브가이드
```

A generic pair such as `콘텐츠 제한 / VR 경험` is too abstract when the source identifies a product and a contrast.

### Strength, texture, and modifier discipline

Do not make emphasis captions so dry that they become bare noun inventories. When the source supports it, preserve or add **one precise adverb/adjective** that communicates degree, breadth, maturity, speed, or texture:

- breadth: `~까지 아우르는`, `폭넓게 연결된`
- maturity/strength: `탄탄한`, `촘촘한`, `강력한`
- timing/degree: `이미`, `빠르게`, `본격적으로`

Prefer:

```text
전기차·글래스·로봇까지 아우르는
탄탄한 제조 생태계를 갖춘 중국
```

Over the flatter:

```text
전기차·글래스·로봇까지
제조 생태계를 갖춘 중국
```

The modifier must sharpen a source-backed quality, not add decorative hype. Avoid stacking several generic intensifiers (`압도적`, `혁신적`, `최고의`) or turning `잘 구축됐다` into unsupported market dominance. One well-chosen modifier is usually enough.

Completion criterion: the code block can be copied directly into the production document without deleting assistant commentary.

## 3. Explainer-Caption Contract

Default to one line for a simple technical term:

```text
용어(한자/영문 필요 시) : 한 문장 정의
```

A historical policy, institution, or program may use a compact 2–3-line card when one line would merely rename it:

```text
사업명
출범 시점과 구체적 목표
누가 무엇을 어떻게 했는지
```

A label plus category is **not** an explanation. `G7 프로젝트 / 범부처 국가 연구개발 사업` only repeats metadata and leaves the viewer asking what it tried to achieve. The completed card must provide the missing comprehension: objective, operating actors or mechanism, and intended result. User-corrected exemplar:

```text
G7 프로젝트
1992년 선진 7개국 수준의 기술력 확보를 목표로
정부·기업·연구기관이 핵심기술을 공동 개발한 국가 R&D 사업
```

Examples:

```text
휘도(輝度) : 화면이나 광원이 특정 방향으로 얼마나 밝게 보이는지를 나타내는 수치
```

```text
버드배스(Birdbath) : 디스플레이 영상을 반사·확대해 눈앞에 가상 화면으로 보여주는 광학 구조
```

Rules:

- define the term, not its entire industry history
- explain one concept per line
- use a widely understood Korean phrase before specialist nuance
- do not append examples or caveats unless requested
- return one copyable code block only
- When the surrounding beat contrasts adjacent technologies, include the **decisive positional or architectural differentiator**, not just a generic function. Examples: `GPU 옆에 두던 HBM을 GPU 위에 쌓아` for zHBM; `낸드를 여러 층으로 쌓아 HBM과 SSD 사이에서` for HBF. If the PD corrects a missing axis (`GPU 옆에 아닌`, `HBM과 SSD 사이`, `적층도 있어야`), preserve every requested axis in the next one-line definition instead of shortening it away.
- For memory-hierarchy explainers, answer three checks before delivery: **무엇을 쓰나(매체), 어디에 놓이나(계층·위치), 무엇이 달라지나(속도·용량·거리)**. Omit only an axis that is genuinely irrelevant to the selected beat.

### General-audience technical simplicity gate

For a technical `설명자막`, lead with the object's viewer-facing function, not its construction sequence. Use the shortest familiar nouns that let a non-specialist understand why the object exists.

```text
name → connects/protects/carries/cools/controls what
```

Do not automatically include internal implementation terms such as `플립칩`, `범프`, `솔더볼`, `비아`, `인터포저`, `하이브리드 본딩`, or a full acronym expansion. Add one only when the current beat is specifically teaching that distinction. If the PD says `너무 어려워`, strip the mechanism and retain `대상명 + 기능` rather than defending the detailed definition or merely shortening the same jargon.

Preferred general-audience level:

```text
FC-BGA | 고성능 반도체 칩과 메인보드를 연결하는 기판
```

More detailed bonding language belongs in narration, a mechanism graphic, or a later caption only when requested. For semiconductor package visuals and terminology layers, consult `vertical-technical-short-production/references/semiconductor-integration-and-package-broll.md`.

### Explainer captions with a requested differentiator

- If the PD explicitly asks to include a differentiating term such as `멀티 에이전트`, make that term the grammatical core instead of appending it decoratively to a generic definition.
- Describe what the differentiated system does in parallel or by role (`논문 탐색·분석·검증`) rather than merely saying `AI 기반`.
- Do not infer a multi-agent architecture from a product's generic AI-search page alone. Require the supplied source, product UI, or official documentation to support it; otherwise mark the wording for confirmation rather than laundering the requested term into a factual product claim.

Completion criterion: a general viewer can understand the term without another sentence.

### Structure captions

When the PD asks for a `구조자막`:

- treat it as a numbered or arrow-linked process/stack caption, not an emphasis caption or transcript cleanup
- use `1)`, `2)`, `3)` numbering when requested
- do not force exactly four stages; derive the count from the source logic
- keep each stage as a compact, parallel noun phrase and retain only the mechanism needed to understand the transition
- if the PD supplies a polished `//자막` block, reproduce that wording exactly rather than re-expanding omitted details

User-approved compact pattern:

```text
1) LLM 모델의 발전
2) 다양한 MCP 연동
3) 에이전트 구축
4) 워크플로우 완성
```

## 4. Preserve the Source Beat

Atomize the speech internally:

```text
subject
current condition
comparison target
cause
result
speaker confidence
```

Then select the one relationship that deserves screen emphasis.

### Contrast fidelity

If the source says `A보다는 B에 가깝다`, keep the comparison. Do not reduce it to `B형 경험`.

### Causality fidelity

If the source says `콘텐츠가 많지 않아서 VR처럼 느껴진다`, keep condition → judgment. Do not turn it into a product-spec claim.

### Confidence fidelity

Map speaker confidence carefully:

```text
같다 / 보인다 / 가능성 → 가까운, 가능성, 단계
확실하다 / 실제로 → only when source and evidence support it
```

### Attribution fidelity

A company, partner, or product mentioned nearby is not automatically the grammatical subject. Resolve pronouns before putting a company name on screen.

When a group-level caption uses a subsidiary and an infrastructure asset, preserve their grammatical relationship instead of stacking bare nouns or assigning a separate subject to each line. The user-approved pattern is:

```text
SKT를 중심으로 데이터센터 구축에 나선 SK그룹
```

This is preferred over noun chains such as `SKT 데이터센터를 발판으로` or split-subject copy such as `데이터센터 구축에 나선 SKT / AI 풀스택 꿈꾸는 SK그룹`. Keep the group as the main subject and connect the subsidiary with an explicit relation such as `~를 중심으로`.

Completion criterion: the caption remains true if read without the surrounding interview audio.

## 5. Technical-Copy Discipline

For technical topics, normalize terms internally before writing:

```text
component
optical/system architecture
user experience
manufacturing constraint
company/product attribution
```

Do not expose the full audit unless requested. The output contract still governs.

Examples of distinctions:

- same microdisplay does not mean the same optical system or wearing comfort
- a waveguide carries light through the lens; it does not mean the microdisplay panel is physically embedded across the lens
- birdbath and waveguide describe optical delivery structures, not competing display-panel brands
- a sourced public product announcement and a speaker's strategic inference are different claim levels

Load `references/ai-glasses-caption-calibration.md` for the current optical and product-language calibration.

Completion criterion: simplification removes jargon without creating a false architecture claim.

## 6. Handle PD Rejection

When the PD says `아닌 것 같은데`, `그 말이 아닌데`, or similar:

1. identify what the first copy dropped: subject, contrast, cause, confidence, or tone
2. revise the framing rather than merely swapping synonyms
3. preserve the original output mode
4. return only the revised copy when the task is caption writing

Do not defend the first proposal. Do not explain why it was reasonable unless asked.

Completion criterion: the second version changes the editorial interpretation that caused the rejection.

## 7. Question and Quote Discipline

### Questions

Use `Q.` selectively for chapter-driving or genuinely unresolved questions. Do not turn every interrogative sentence into a question card.

#### Question-caption output contract

When the PD pastes a long spoken question followed by `질문자막`, `질문 자막`, or `→ 질문자막`:

- return **only one copyable code block**, with no explanation or alternatives
- use one short `Q.` sentence
- when the spoken request is simply `이게 뭐냐 / 자세히 설명해 달라` about a named term, default to the shortest direct form: `Q. FC-BGA란?` Do not invent extra axes such as structure, role, difference, importance, or reason unless the answer actually centers on them.
- treat `짧고 직관적으로` as a reset to the irreducible question target, not an invitation to preserve a full grammatical sentence. A fragmentary `Q. 용어란?` is acceptable and often preferred on screen.
- find the question's single editorial axis rather than preserving every hedge, compliment, and setup clause
- separate the setup's general thesis from the **final interrogative target**; the latter normally determines what the guest is being asked to answer
- however, when the setup supplies the question's essential transition and evaluative predicate—such as `일본의 장기 우위 → AI 시대 개막 → 삼성전기의 급부상 → 비결`—preserve that time frame and status change. Do not weaken `급부상/우뚝 섬` into generic `주목받음`, and do not narrow the company-level question to a nearby product such as FC-BGA unless the final interrogative names it.
- after `아닌 것 같아` or similar rejection, re-read the **full preceding setup**, not only the rejected caption. Reconstruct `누가 / 어떤 전환기에 / 위상이 어떻게 바뀌었나 / 무엇을 설명해야 하나` before drafting again.
- if the speech asks both about a current gap and what beginners should do, prefer the causal/actionable axis that naturally opens the answer
- preserve the actual subject and direction; do not broaden `기업별 AI 활용 격차` into generic `AI 전략`
- run a **subject–object–verb audit** before delivery. Verbs such as `활용하다`, `적용하다`, and `도입하다` require the named object from the source; `어떻게 활용해야 하나요?` is incomplete if the caption has dropped `GEO`, `AI`, or the relevant tool/technology.
- distinguish **illustrative roles** from the **question's general target**. If the speaker says `예를 들어 마케터다, 블로그 운영자다` only as examples and then asks for field-by-field practical use, do not freeze those examples into the caption subject. Generalize the actor to `기업`, `조직`, or the source-backed umbrella while retaining the explicit object: e.g. `기업은 GEO를 분야별로 어떻게 활용해야 하나요?`.
- distinguish **experience/existence questions** from **method questions**. If the interviewer asks whether a named company has itself encountered a problem (`사내에서도 토큰 맥스·밸류 맥스를 겪었나?`), do not rewrite it as `어떻게 적용·구현하고 있나?`; that presupposes a mature implementation and changes the expected answer. Preserve the named subject and use the source-backed axis: `직접 겪었나 / 필요성을 느꼈나 / 어떤 문제가 있었나`.
- compression may remove spoken examples and hedges, but it must not remove the answer object. Validate the draft with: `누가 / 무엇을 / 어떻게?` If `무엇을` cannot be answered from the caption alone, rewrite.
- if the interviewer asks for a named organization/person/product's case, preserve that name. Do not generalize `라이너는 어떻게 하고 있나?` into `일반적으로 어떻게 해야 하나?`
- when the spoken question is driven by a feared causal chain (`내가 루프를 완성한다 → 그 결과 내 역할이 사라질 수 있다`), preserve both the condition and the self-displacement anxiety. Genericizing it to `인간의 역할은 무엇인가?` changes the question.
- prefer the concrete object named in the speech (`설계자`, `내 자리`, `AI 업무 루프`) over adjacent umbrella terms such as `사람`, `인간`, or `자동화`.
- validate by asking: **Would the guest give the same answer to the caption and the original spoken question?** If not, rewrite
- avoid stacking two questions with `/`, `·`, or repeated question marks
- do not turn an open spoken question into a leading binary choice merely because the speaker mentioned two possible providers, mechanisms, or explanations. If the guest is ultimately being asked `what kind / how does it work / how is it provided`, keep the caption open-ended so it does not feed the answer: e.g. `스마트 라우터는 어떤 방식으로 제공되나?`, not `모델사가 제공하나 / 별도 서비스를 이용해야 하나?`.
- if the PD rejects one question and then requests many alternatives, vary the editorial axis meaningfully—personal fear, occupational role, post-automation role, designer redundancy, or next responsibility—rather than returning ten surface-level synonym swaps. Keep every option within the source's actual causal frame.

Calibrated example:

```text
Q. 기업별 AI 활용 격차, 어떻게 좁혀야 할까?
```

When the PD supplies an answer sequence and requests `1)`, `2)`:

- return one code block containing only the numbered lines
- make the items grammatically parallel and action-oriented
- remove spoken scaffolding such as `첫 번째 주장은`, `그다음에는`, and `고민에 봉착한다`
- preserve the sequence without inventing a later step that has not yet been supplied

Example:

```text
1) 최신 AI 서비스 직접 써보기
2) AI 용어 제대로 이해하기
```

### Quotes

Quotation marks require a verified direct quote. A PD summary or paraphrase is an emphasis/thesis caption, not a quote card.

Completion criterion: quote copy can be traced verbatim; question copy advances the story rather than repeating speech.

## 8. Korean Management-AI Interview Calibration

For abstract AI-adoption interviews, keep the **decision object** and the **operational consequence** concrete.

### Question captions

- A question caption must name the single uncertainty the answer resolves; do not merely combine nearby nouns into a static category.
- Prefer the actual operation (`어떻게 축적·업데이트하고 있나?`) over a vague label (`~을 위한 체계는?`), **but never delete a named case subject to make the wording more generic**.
- For case questions, preserve the named subject first: `라이너는 Company Brain을 어떻게 축적·업데이트하고 있나?`.
- Keep one target and one verb. If the spoken question contains background plus a request for advice, retain the actionable request rather than all the setup.
- If the user changes from `질문자막` to `뭔 소리`, stop caption iteration and explain the speaker's meaning in plain prose before drafting again.

### Emphasis captions

- `내 업무에서 AI로 어디까지 끌어낼 수 있나` means **personally testing what level of useful output the model can produce in one's own work**. Do not turn it into the broader and different claim `업무를 확장한다`.
- For enterprise-adoption beats, preserve the concrete gate and the operational change. If the speech says approval takes a long time but usage is loosened afterward, do not write a vague metaphor such as `긴 과정만 통과하면 / 열리는 AI 활용`. Name the actual contrast: `도입까지 오래 / 승인 이후 활용 범위 확대`, while preserving hedges such as `~같다` when needed.
- When the PD rejects an adoption caption as `별로`, re-atomize it as `decision or approval gate → post-approval operating freedom`. Do not merely swap `통과` for another metaphor; replace the editorial axis with the concrete corporate mechanism.
- `전사 도입` and `전 직원 활용` are different states. When the source says many employees still do not use the tool, preserve the non-equivalence rather than reducing it to generic adoption difficulty.
- For industry/workforce comparisons, state the operational denominator before the result: e.g. fewer PC-based workers → relatively lower average AI usage. Keep `상대적으로` or the speaker's equivalent scope limiter; do not turn a contextual average into an industry-wide absolute.
- When speech contrasts abstract jargon with concrete deliverables, preserve the mechanism: **seeing concrete deliverables enables faster executive judgment**. Shorten wording before deleting that consequence.
- Prefer literal, immediately readable wording over umbrella abstractions such as `내재화`, `체계화`, or `확장` unless the speaker actually means them.
- For numbered process graphics, keep the items parallel without deleting their objects: `AI 서비스 사용 → 조직에 맞는 용어 정의 → 기존 시스템 연결 → AI 전환` is safer than four opaque nominalizations.
- For AI-stack progressions, use the user-approved compact pattern in `Structure captions`; do not re-expand omitted mechanisms after the PD has approved the shorter structure.
- When the PD says `너무 길어`, shorten the current interpretation. Do not introduce a new metaphor, causal claim, or headline frame while compressing.

See `references/korean-ai-management-caption-calibration-20260730.md` for source-to-copy examples and rejected phrasings.

For enterprise-AI rollout, employee-usage gaps, MCP, and token-consumption beats, read `references/korean-enterprise-ai-caption-calibration-20260803.md`. For the current token-efficiency vocabulary, smart-routing questions, fraction-to-impact captioning, and SWE-Pruner caption cautions, also read `references/token-efficiency-caption-calibration-20260804.md`. For hardware-industry interviews that move from Japanese incumbency to an AI-era Korean rise, Chinese catch-up, or an upstream-materials-versus-advanced-platform contrast, read `references/hardware-industry-interview-caption-calibration-20260807.md`. When the PD says `이런 식으로` and supplies a two-line relationship, preserve that syntactic skeleton with minimal edits; do not replace it with `대가`, `비용`, or another evaluative metaphor absent from the requested framing.

### Search-behavior testimony calibration

When a speaker moves through `personal experience → tool/mechanism → improved result quality → broad user behavior change`, do not automatically compress the whole sequence into a generic `AI와 문답` caption. Follow the exact clause the PD selects:

- a personal memory gap can support a textured experiential hook
- a quality-improvement clause should preserve `better results → user-perceived behavior change`
- if the PD redirects focus to the latter clause, drop nearby tool lists and mechanisms rather than carrying them into the revision
- keep unapproved working drafts separate from PD-confirmed gold copy
- distinguish `search demand` from `website traffic`: users may still seek answers while resolving them inside AI. Treat brand absence from that answer layer as a discovery/consideration gap, not proof that demand disappeared.
- separate `being mentioned by AI` from `click/purchase monetization`; do not let one caption imply that presence alone restores conversion.
- preserve tentative strategic language. A speaker's `~가야 되지 않을까` supports a direction or hypothesis, not a definitive formula such as `수익화의 열쇠는 X`.
- when the source contrasts nonstandard labels such as `비주얼 차원` and `전문 주제 차원`, normalize both onto one explicit axis before captioning (`image/video appeal` versus `accumulated topic expertise`). Do not repeat an ambiguous label as if viewers already know the distinction.

For a line that extends a statistic or comparison from the preceding beat, perform an **implication pass before wording**:

```text
measured population / denominator
what the current line says is missing from that measurement
new conclusion created by the omission
```

Caption the new conclusion, not the surface action. Example: `users bypass Google for standalone AI` may not be mainly about bypass behavior; in context it can mean that a Google-only click study excludes those users and therefore may understate the total traffic loss. If the PD says the copy is long and then says the implication is wrong, do not merely shorten nouns—reset to `EXPLAIN`, state the statistical implication plainly, and draft again only after the meaning axis is correct.

Read `references/lee-jungdae-geo-caption-calibration-20260730.md` for the current user-confirmed example, rejected framing, source hash, and accumulation rules.

## 9. Short Technical Script Revision

For original 45–70 second technical Shorts scripts, apply the same source-beat and overclaim discipline at script scale:

- freeze a prefix the PD explicitly approves and revise only the rejected tail;
- when the PD asks for the **full script**, return the entire integrated script rather than only the replacement fragment;
- when told the script is long or repetitive, delete duplicated beats before line-level shortening;
- let wording such as `삼성이 제시한 목표` carry concept-stage status when sufficient, instead of interrupting the script with a repetitive standalone disclaimer;
- put caveats and counterarguments in the middle `대가` beat. Do not let repeated endings such as `승자라는 뜻은 아닙니다`, `~라고 단정할 수 없습니다`, or `탈락 사유가 아닐 수 있습니다` consume the conclusion and erase the script's thesis;
- end with one direct mechanism-backed claim that answers `그래서 이 영상이 하려는 말은 무엇인가?`. Calibrate certainty through the verb (`노린다`, `겨냥한다`, `평가축이 바뀐다`) rather than closing with mechanical neutrality;
- when a hook metaphor is approved, make it carry the mechanism into the next beat rather than decorate the topic. Example pattern: `서버 창고가 아니라 전기로 지능을 만드는 공장 → 안정적인 전력 필요 → ESS`;
- end on the mechanism-backed competitive shift, not unsupported company-victory rhetoric such as `다음 경기장을 제시했다`;
- keep the physical mechanism—data path, connection density, heat, load, or signal movement—as the body of the short.

### 80점 원고를 90점 이상으로 올리는 훅·유지율 패스

기술적으로 정확하지만 80점 안팎인 45~75초 쇼츠는 대개 사실성이 아니라 **도입 순서**에서 감점된다. 사용자가 `몇 점`, `90점으로`, `특히 훅`, `subagent로 업그레이드`라고 하면 다음을 적용한다.

- 첫 3초에는 배경·시장 필요·원료 풍부함 대신 **충돌 또는 역설** 하나를 던진다.
- 4~6초 안에 기술 대상을 공개하고, 15초 안에 가장 강한 물리적 반전을 배치한다.
- `문제 → 물리적 원인 → 불리함 → 장소/용도 전환 → 평가표 변화 → 대가 → 오프닝 회수` 순서를 기본으로 한다.
- 강한 문장이 후반에 있으면 앞당긴다. 설명을 잘 쓴 것으로 늦은 반전을 정당화하지 않는다.
- 기업·출하량·계약 수치는 현재성을 증명할 때만 남긴다. 이야기의 물리적 축을 끊으면 본문에서 빼고 팩트 메모로 이동한다.
- 90점 판정은 평균으로 부풀리지 않는다. `훅` 또는 `유지율`이 20점 만점에 17점 미만이면 전체 90점 이상으로 판정하지 않는다.
- 사용자가 subagent를 명시하면 `훅 전담 / 유지율 전면 재구성 / PD 채점 / 과장·논리 반대검토` 역할을 같은 고정 사실 브리프로 병렬 실행한다. 모든 결과가 돌아오기 전에는 임시본을 통합 최종본이나 90점본이라고 부르지 않는다.
- 여러 후보를 사용자에게 떠넘기지 말고 Main이 충돌을 판정해 **최종 원고 한 본**만 낸다.

세부 타이밍, 점수 게이트, 소듐이온 ESS 사례의 안전한 물리 프레임은 `references/shorts-hook-90-point-subagent-upgrade.md`를 따른다.

### Concept-sketch mode before research

When the PD says `일단 스케치만`, `나중에 보완`, or otherwise asks for an early meeting draft:

- do not silently upgrade the task into full research, fact-checking, a polished final script, or rendering;
- provide one recommended **rough 1-minute spine** first, normally as `hook/problem → current solution limit → physical reversal → cost/trade-off → problem return`;
- include approximate beat timings and one visual/mechanism idea per beat so the structure can be judged in a meeting;
- if the PD allows anything under three minutes, keep the 1-minute version as the base and list only the evidence, counterargument, or case-study modules that could extend it to roughly 2–3 minutes;
- choose one strong physical reversal rather than listing chemistry or industry facts. Example class: a property that is fatal in a moving product can matter much less in stationary infrastructure;
- keep current numbers, named-company commercialization claims, and definitive safety/cost claims out of the sketch unless already source-verified. Mark them as later fact-check slots instead of inventing specificity;
- do not ask the PD to choose among many structures when one obvious draft can be supplied. The meeting can decide whether the optional expansion is entertaining enough.
- when the approved script moves into a **vertical visual storyboard**, use the actual Shorts canvas from the start: 9:16. For a 55–70 second technical Short, plan roughly **12–15 distinct sketch frames**, not seven broad images, because real footage and motion graphics will later replace the sketches at a finer cut rhythm.
- freeze each storyboard row as `duration / source-faithful STT / selective emphasis-or-explainer copy / visual mechanism`. Generate base images without text, then add exact Korean captions deterministically so image generation cannot corrupt spelling.
- deliver both a numbered all-frame contact sheet and a rough slideshow MP4. Inspect every STT line break for grammatical cohesion (`창고가 아니라`, `AI 데이터센터`, predicate tails, number+unit) before rendering.
- verify the actual pixels rather than trusting an image provider's `portrait` label. Convert a 2:3 portrait result to exact 9:16/1080×1920 with crop or canvas extension, then recheck that critical subjects remain visible.

See `references/vertical-technical-shorts-storyboard-sketch.md` for the frame manifest, image-generation, deterministic caption-overlay, contact-sheet, slideshow-duration, and QA procedure.

### Demand-first opening after PD correction

When the PD says a required context such as `데이터센터에서 ESS가 필요한 이유가 처음에 나와야 한다`, treat this as a **story-order correction**, not a request to insert one sentence:

- rebuild the first problem around that context and use it again in the ending; do not bolt the context onto an existing technology-first hook;
- state the demand-side problem and the system's bounded role before revealing the candidate technology;
- preserve retention by placing the physical reversal within roughly 15 seconds even after the context moves forward;
- for storage infrastructure, distinguish `generate` from `store and discharge`, and do not imply the system can cover an entire facility indefinitely;
- after any partial correction, return the full integrated script rather than only the changed opening;
- when independent reviewers are used, Main must integrate one final draft and re-score the actual revised version instead of forwarding a reviewer draft unchanged.

Read `references/infrastructure-demand-first-hook-calibration.md` for the reusable sequence, factual safety gates, scoring rubric, and the data-center/ESS calibration example.

Use `references/short-technical-script-revision-and-ending.md` for the compact structure, caveat placement, approved-prefix freeze, and ending calibration.

## Common Pitfalls

1. **Explaining after a caption request:** the code is correct but surrounded by unwanted prose. Fix: caption-only block.
2. **Cleaning the source unasked:** the PD asks for screen copy and receives a rewritten transcript. Fix: classify mode first.
3. **Generic compression:** subject and contrast disappear. Fix: preserve the source relationship.
4. **Overclaiming:** `같다` becomes `주도한다` or `확정`. Fix: preserve confidence.
5. **Technical conflation:** panel, optics, device form, and experience are treated as one layer. Fix: normalize internally.
6. **Nearby-subject error:** a company in the prior sentence becomes the actor of the current claim. Fix: resolve pronouns.
7. **Alternative dump:** several options shift the selection burden back to the PD. Fix: give one best proposal unless alternatives are requested.
8. **Explainer referent loss:** the PD names one product/service and supplies adjacent capability phrases, but the response treats those phrases as separate numbered concepts or defines the category instead of the named product. Fix: resolve the named referent first and synthesize the supplied capabilities into one `제품명 : 한 문장 정의` line. Do not ask what to do when `설명자막` plus the named object makes the target clear.
9. **Defending rejected copy:** rationale replaces revision. Fix: revise silently in the same output format.
9. **Question inflation:** every section gets `Q.`. Fix: reserve it for real progression.
10. **Quote laundering:** a paraphrase receives quotation marks. Fix: require exact-source verification.

## Verification Checklist

- [ ] Current request mode identified
- [ ] Caption-only request returns only one code block
- [ ] Emphasis copy is normally 1–2 lines
- [ ] Explainer copy follows `용어 : 정의`, except historical policy/program cards that need `명칭 → 목표 → 운영 방식` in 2–3 lines
- [ ] Explainer copy adds missing comprehension rather than restating only the user's date, label, or broad category
- [ ] Subject and contrast survive compression
- [ ] Causality and confidence do not exceed the source
- [ ] Technical layers are not conflated
- [ ] No unrequested transcript cleanup or explanation appears
- [ ] Rejected copy is reframed, not merely synonym-swapped
- [ ] For statistical follow-on speech, measured population, omitted population, and the resulting implication were resolved before wording
- [ ] Surface actions or product names did not replace the actual editorial implication
- [ ] A one-line punch was preferred when a second line would only repeat setup or conclusion
- [ ] Direct quotes are verified and questions are selective
