---
name: ttimes-cardnews-imagegen
description: Use when converting a TTimes-style Word manuscript into a sourced 2:3 vertical card-news sequence with image generation. Parses `numbered` manuscript beats, red emphasis runs, section headings, and leading `PXX.` revision notes; expands beats into page-level claims; selects evidence photos/charts versus generated illustrations; uses image_generate for the visual design layer; overlays exact Korean text and data deterministically; and verifies consistency, sources, dimensions, and revision fidelity before delivery.
license: MIT
metadata:
  hermes:
    tags:
    - ttimes
    - cardnews
    - imagegen
    - docx
    - infographic
    - editorial-design
    related_skills:
    - practical-image-workflows
    - ttimes-screen-composition
    - ttimes-factcheck-research
    - docx
  author: Hermes Agent
  version: 1.11.0
---

# TTimes Card-News Production with ImageGen

## 카드뉴스 형식 라우팅 — 제작 전 필수

- 오전 새 뉴스·정책형은 `../ttimes-original-cardnews/SKILL.md` 사용: 4:5 세로·사진 중심·독자 질문 마무리.
- 오후 일반 대담 요약형(김덕중·정지훈·박세준)은 1080×1080 정사각형: 리스트 이미지 풀프레임 표지·출연자 실제 인용 마무리. 아래 2:3 DOCX 설명을 이 형식에 적용하지 않는다.
- `../ttimes-original-cardnews/references/morning-news-vs-afternoon-youtube.md`와 `../ttimes-original-cardnews/references/20260907-approved-production-rules.md`를 읽고 승인본을 재사용한다. 본문 색감 참고를 전체 템플릿 변경으로 확대하지 않는다.
- 특정 시리즈의 별도 승인 레지스트리는 계속 유지한다. 박세준의 사진·색감 예외를 다른 시리즈에 강제하지 않는다.
- 팩트체크만 요청하면 톤/제목 수정 금지. 부분수정은 요청 요소만. 억지 줄바꿈·지면 작업용 표기 금지, 사용자 지정 문장 전체 강조를 보존한다.

## Overview

Use this workflow to turn a long-form Word manuscript into a vertically paginated TTimes-style card-news package. The authoritative source is the DOCX; the design is downstream. The observed production chain is:

```text
Word manuscript
→ source-beat parse
→ page-level editorial architecture
→ source and asset ledger
→ image-generated visual layer
→ exact Korean text/data composition
→ page and sequence QA
→ page-specific revision loop
```

The target visual grammar is a restrained business-report card, not a generic social-media poster:

```text
one page = one primary claim + one primary visual + one highlighted judgment
```

`image_generate` supplies the visual design layer, illustration, atmosphere, and style continuity. It must not be trusted to reproduce long Korean paragraphs, exact chart values, source credits, or page numbers. Those are overlaid from the ledger after generation.

Load `references/reverse-engineered-ttimes-cardnews.md` for the measured corpus grammar and `templates/imagegen-prompt.md` when rendering.

## When to Use

Use when the user provides:

- a report or script DOCX intended to become card news
- `<1>`, `<2>`, … manuscript beat markers
- red Word runs indicating visual emphasis
- leading `P15.`, `P22.` style design correction notes
- a prior TTimes card-news corpus to reproduce with `image_generate`
- a request to make many 2:3 vertical cards, including occasional video cards

Do not use for:

- ordinary presentation decks
- spoken-caption/SRT production
- screen composition against interview footage
- a single standalone infographic without a manuscript sequence
- factual news photography that the user expects to be authentic but for which no real source asset exists

## Production Contract

### 인터뷰 원고 기본값 — 2026-09-29

인터뷰·유튜브 발언 기반 카드뉴스는 `../ttimes-editorial-copy/references/interview-cardnews-article-quotes-20260929.md`를 읽는다. 사용자가 확정한 기본값은 **출연자 이름을 밝힌 기사체 본문 + 실제 핵심 발언의 따옴표 인용**, 마지막은 **출연자 인용문 + 이름·직함**이다. 과거의 기사체·인물 소개 회피나 본문형 마지막 장 선호보다 우선한다. 실제 발언에 없는 조언·해석을 보태거나 진행자 발언을 출연자 말로 합치지 않는다. 현재 회차의 명시 예외와 기존 시각 템플릿은 유지한다. 원고 승인만으로 원음·화자 검증이 완료된 것은 아니다.

### User-approval learning loop

For title, body-copy, page-count, emphasis, and visual-concept decisions, load `references/user-approval-pattern-learning.md` and `references/editorial-preference-snapshot.json` before proposing candidates. Use same-format repeated approvals to rank proposals, but current explicit instructions always win. Never treat silence as approval.

After each explicit approval, rejection, or user rewrite, append one structured event to `references/editorial-approval-ledger.jsonl` with `scripts/record_editorial_approval.py`. At episode completion, regenerate the preference snapshot. A hard user rule applies immediately; a softer taste signal becomes a format default only after appearing in at least three independent episodes. This learning loop must capture the delta between the assistant proposal and the user's final wording, not only the final artifact.

For an uncertain visual concept, propose 3–5 concise concepts before generation. Once the user selects one or directly says `ㄱㄱ`, generate only the selected concept. Rank by whether the core action and responsibility are understandable before reading the card copy.

If the user rejects a generated visual as `직관적이지 않다`, `축축하다`, or asks for a metaphor before drawing, freeze image generation. Explain the mechanism as one physical analogy, contrast it with neighboring concepts, and obtain approval before generating again. A later `ㄱㄱ` approves only the currently shown concept or preview; it does not unlock unrelated copy, layout, or already locked cards.

### Approved format registry

Load `references/approved-format-registry.json` before designing an 이중학, 박영선, 원맨, or 일반 대담 square carousel. These four formats are user-approved templates. Reuse the registered cover/body/closing architecture and do not redesign the skeleton merely because the episode topic changes. Episode-level visuals, copy, emphasis position, and approved palette details may vary; structural changes require new user approval.

#### 이중학의 사람과 기술 — approved template

- Load `references/people-and-technology-square-carousel-template.md` and the registered approved assets.
- Preserve the approved natural upper visual + navy lower information panel, sharp square numbering, periwinkle title/highlighter, no body logo, and verified guest-quote closing.
- Preserve the approved information density and typography measured from the 이중학–윤명훈 cards: body title about 74px and body/highlight 35px. Do not normalize this template to 80/40.

#### 박영선의 테크토크 — approved template

- Load the registered 박영선 cover/body assets and `references/ttimes-series-carousel-architectures-2026.md`.
- Preserve the approved technology/industry evidence hierarchy, teal/navy information panel, sharp square numbering, body-title/body hierarchy from the approved renderer, no body logo, and verified guest outlook closing.
- Do not normalize the approved Park typography or density to another format merely for cross-series uniformity.

#### 원맨 해설형 — approved template

- Load `references/one-person-square-carousel-template.md` and `references/assets/approved-one-person-laundry/approval_manifest.json`.
- Fixed body skeleton: 1080×1080, visual:text 540:540, `1·2·3` square badge crossing the boundary, separate title then body, body title 74px, body/highlight 35px, approximately 95–115 Korean characters, no body logo.
- Fixed treatment for the approved laundry layout: title/badge/divider use official TTimes red `#E30613`; inline highlighter uses yellow `#FEF601` with black `#070707` text; source illustration colors remain unchanged.
- Body visuals use one natural coherent illustrated scene and one action; no captured video frame, ghosted states, collage, repeated limbs, or fake photoreal CGI.
- Manuscript text contains paragraphs, not hand-inserted display line breaks. Automatic wrapping must preserve Korean grammatical cohesion with non-rendered keep-together spans.

#### 일반 대담형 — approved template

- Load `references/general-interview-square-carousel-template.md`, `references/general-interview-production-profile-20260831.json`, and `references/assets/approved-general-interview-linkedin/approval_manifest.json`.
- Use LinkedIn blue UI only: `#0A66C2`, pale blue `#DCE6F1`, slate `#38434F`, off-white `#F3F6F8`. Do not mix McKinsey navy or BCG green.
- Preserve exact `_list_` and official source-photo colors; do not tint real people or the official TTimes logo.
- Representative body geometry is a 500px visual over a 580px off-white information surface, with the frozen 92×92 boundary badge, 74px title, 35px body/highlight, and approximately 95–115 Korean characters. The 480–520px visual range is allowed only to balance a specific claim.
- Apply the 2026-08-31 production rules: x=70 text axis; one-line title down to 88% horizontal scale then grammatical two-line fallback; regular body weight 560 without bold; only the exact highlight span uses weight 720 + pale-blue marker + 3px blue underline; balanced paragraph and bottom spacing.
- New body core visuals must use `image_generate`. A coded/Pillow illustration may be a private layout draft but is not a final visual. Generate without text and add exact Korean deterministically only when needed.
- Closing uses a separate LinkedIn-blue editorial background, verified 50px centered quote, balanced exact-span highlighter, 30px `이름 · 직함` profile, and official logo at bottom center.
- The frozen five-card exemplar is `references/assets/approved-general-interview-linkedin/kim-jihyun-tokenomics-20260831/`; its page count is episode-specific, while its visual skeleton and typography are reusable.
- Card-news copy is isolated from upload metadata. Never overwrite supplied YouTube title, article title/body, Naver/Daum title, or landing URL with a carousel title or storyline.
- For the 2026-09-03 general-interview calibration covering conversational copy, balanced two-paragraph body flow, metaphor-first image approval, Figma-style visuals, locked-card scope, and upload-description retrieval, load `references/jo-taeho-ep2-general-interview-calibration-20260903.md`.

#### General-interview wording and reflow calibration

- Prefer `specific person/credibility + concrete action + viewer benefit` over a report-style topic label. A single lively verb may carry tone; do not stack memes or hype.
- Begin body copy with the reader's current behavior, a concrete scene, or an operational contrast. Do not lead with `연구팀은 연구했다`, a taxonomy, or a textbook definition when the card's actual hook is practical.
- Use two continuous paragraphs when the approved card calls for two beats: mechanism/action first, then trap/control/judgment. Store paragraph strings without hand-inserted display breaks and let the renderer wrap them.
- If left-aligned copy looks piled up on the left, preserve the approved alignment and skeleton. Rebalance sentence length and grammatical wrap points so lines extend naturally across the card; do not switch to centered copy or redesign the layout unless explicitly approved.
- End with a decisive human-responsibility judgment when that is the interview's thesis. Avoid dissolving the conclusion into generic `중요합니다`, `필요합니다`, or `고려해야 합니다` wording.
- When a closing card is approved, lock its exact quote, emphasis paragraph, profile line, and layout. A later request targeting one body card does not reopen the closing.

#### ImageGen-only and Figma-style gate

- When the user says `image gen만`, the semantic visual in the image slot must come from image generation itself. Do not add local explanatory capsules, arrows, labels, boxes, or fake UI afterward to rescue an unclear image. Deterministic card-template layers—approved page number, title, body, highlight, source, and logo—remain allowed.
- `피그마 스타일` means a bright, dry, crisp 2D vector language, not merely a white background around glossy 3D objects. Prompt and verify solid fills, simple geometry, restricted vivid palette, generous whitespace, and clear relationship lines; forbid photoreal CGI, isometric depth, gradients/gloss when flatness is required, glass/metal shine, fog, neon, dark scenes, and wet materials.
- For related mechanism cards, define one shared palette, outline weight, icon grammar, and crop ratio. Verify each generated base at the actual card crop and inspect the sequence contact sheet; a good uncropped source can still fail at 1080×500.
- The visual must communicate its core action before the body is read. For paired concepts, make the contrast structural: e.g. `artifact keeps circulating` versus `external rules fix the available branches`.

### Global square typography gate

For every 1080×1080 TTimes carousel, load `references/ttimes-square-global-typography-contract.md`. The global values are cover title 80px, closing quote 50px, and profile 30px. Body typography follows the user-approved format template: 이중학–윤명훈, 원맨, and 일반 대담 use 74px body titles with 35px body/highlight; 박영선 preserves its registered approved renderer. The latest user-approved format templates override the older provisional 80/40 body rule.

### Mandatory subagent editorial conference

When a video needs a new cover title or storyline, load `references/subagent-editorial-conference-protocol.md` and run independent story, source-verification, and mobile-copy subagents followed by a chair synthesis. The sequence is mandatory: source → subagent conference → title-first final script → user script approval → design. Do not render the full carousel before this gate. Page count remains variable; the closing quote must resolve the selected cover title and storyline.

### Full-sequence storyboard approval gate

After the cover angle/title is selected, prepare the **entire planned carousel** as one text-only storyboard and obtain user approval before generating any image. For a five-card package, present Cards 1–5 together in exact display order.

Every card entry must show all four fields explicitly:

```text
Card N
- Title: exact displayed title
- Body: exact displayed body copy; `없음` when the format has no body
- Highlight: exact span and its position inside the title/body/quote; `없음` when not used
- Image concept: the concrete textless scene, dominant subject/action, composition, and generation direction
```

- This is a sequence-level placement approval, not a card-by-card approval loop.
- Include the already selected cover title in Card 1 and preserve it verbatim.
- Show how the five cards connect as `cover thesis → evidence/mechanism → conclusion`; remove cards that do not serve the approved angle.
- The user may revise any title, body, highlight, image concept, or page order. Apply those edits and resubmit the complete current storyboard for approval.
- Do not treat approval of the cover title as approval of Cards 2–5 or their image concepts.
- Record the approved sequence and any user rewrite in the editorial approval ledger.
- Do not call `image_generate`, source final visuals, or render cards until the complete storyboard has explicit user approval. Storyboard approval and final visual approval are separate gates.

### Series-specific architecture gate

Before deciding page count or body-card templates, resolve both the named series and production format. A TTimes series is not a palette swap: it changes the editorial sequence, evidence hierarchy, and closing function.

For a stable named series, the named-series template takes precedence over the generic F1/F2 format. Do not invent its palette in advance. Derive the template from at least three representative episodes: exact `_list_`, YouTube thumbnail, and recurring in-video question/caption/graphic layouts. Extract only repeated color, title hierarchy, person placement, information partitions, numbering, and closing function. Prototype cover/body/closing and obtain user approval before registering it.

- `이중학의 사람과 기술`: organizational tension → host framing → guest diagnosis/example → mechanism → leadership trade-off/action → verified guest quote.
- `박영선의 테크토크`: market inflection → technology mechanism → company differentiator → competition/bottleneck → industry implication → guest outlook.
- `강수진`: surprising model behavior → experiment/prompt → result → cause → actionable use rule.
- `30년 개발자의 기업 분석`: company position → business/technical engine → competitors → moat/bottleneck → judgment.
- `전진수의 궁금한 건 못 참아`: use the named-series template only when 전진수 is the recurring host/interviewer. If 전진수 appears as a guest, expert, or co-author in another production, route by that episode's actual series and format. For hosted episodes, derive the visual architecture from recurring official thumbnails and in-video layouts rather than generic one-person or general-interview colors.
- `AI, 안 해보면 모른다`: finished result → tool/input → steps → failure → reproducible settings → verdict.
- `티타임즈 주간브리핑`: event → numbers → stakeholders → implication → next variable; do not force a personality quote.
- `TTimes 일반 대담형`: choose the strongest cover question/thesis first, then build only the independent beats needed to answer it; the verified closing quote must resolve the cover rather than merely sound strong. Page count is variable. Load `references/general-interview-square-carousel-template.md`; prototype cover/body/closing before expanding the sequence.
- The general-interview LinkedIn-blue graphic template is `USER_APPROVED_TEMPLATE`. Preserve the approved 표철민 prototype architecture; do not reuse the rejected earlier 김지현 layout.
- `TTimes 원맨 해설형`: verify F1 from production structure rather than face count, then choose one expert thesis/question and build only the evidence, mechanism, reversal, and verdict needed to answer it. Load `references/one-person-square-carousel-template.md`; page count is variable and the final exact narration must resolve the cover.

For the one-person square format, do not use captured video/broadcast frames as body-card photos. Create separate 1:1 conceptual visuals per body claim, or acquire official source assets when real evidence is required. Generated source visuals and final cards must both be 1:1; overlay deterministic Korean text only after generation.

Load `references/ttimes-series-carousel-architectures-2026.md` for recommended page ranges and full per-series page functions. Treat those ranges as starting points; independent editorial beats determine the final count.

For `이중학의 사람과 기술` square social cards, also load `references/people-and-technology-square-carousel-template.md`. It is the approved visual and delivery contract and overrides generic body-card defaults where they conflict. In particular:

- the body-card count is variable and follows the number of independent editorial beats;
- each body card uses a natural upper image and lower navy text panel;
- body numbering uses sharp square badges, not circles;
- body titles use the cover-linked periwinkle family;
- emphasis occurs inside the body sentence with a full glyph-height periwinkle highlighter and deep-navy text, never as a detached lower-left callout;
- body cards carry neither a series badge nor the TTimes logo;
- the closing uses an audio-verified guest quote/profile and official TTimes logo;
- final delivery attaches every completed image, then gives the copy-ready description and YouTube URL in separate code blocks.

### Authoritative artifacts

- **Source DOCX:** exact editorial wording and emphasis authority
- **Manuscript JSON:** parsed source blocks and runs
- **Page ledger:** final page architecture and exact text
- **Source ledger:** data, image, quote, rights, and credit state
- **Generated bases:** image-generated design/illustration layers
- **Final cards:** exact text/data composited over approved visual layers

Never overwrite the source DOCX. Hash it before transformation.

### Quote-to-speaker attribution gate

Before placing any interview quote on a person/closing card, prove the speaker independently from the quote wording.

- A plain transcript paragraph or timestamp sequence without explicit speaker labels is **not** speaker authority. Do not infer the speaker merely because the passage follows a question, appears inside one paragraph block, or sounds consistent with one guest's thesis.
- Resolve the turn from at least one authoritative speaker signal: speaker-labeled transcript, actual audio/video at the quote onset and preceding handoff, production script with speaker styling, or a user correction.
- Record `quote`, `speaker`, `start/end`, `preceding turn`, and `evidence` in the page/source ledger before rendering the profile line.
- Verify the displayed name and current role separately. A correct role does not repair a wrong speaker attribution.
- If attribution is later corrected, mark the old image and manifest `INVALID_WRONG_SPEAKER_ATTRIBUTION`, rename or quarantine the file, and do not silently reuse it as a design base.

Validated failure pattern: in the 이중학–윤명훈 interview, the 05:32–05:47 statement about leaders adding work without subtracting it was incorrectly assigned to 윤명훈 by paragraph-boundary inference; the user confirmed it was 이중학. Treat this as a blocking attribution error, not a cosmetic profile typo.

### Completion states

- `DRAFT`: manuscript parsed; page split not approved
- `DESIGN_PLAN`: page ledger and visual briefs complete
- `ASSET_READY`: evidence assets delivered or generated-illustration briefs approved
- `RENDERED`: all cards built
- `FINAL`: sequence, visual, source, and text QA passed

Do not call recommendation-only cards final.

## 1. Parse the Word Manuscript

Use the included extractor:

```bash
python scripts/extract_cardnews_manuscript.py input.docx -o manuscript.json
```

Interpret the observed DOCX grammar as follows:

| Word element | Meaning |
|---|---|
| leading bold `P15.` lines before `<1>` | post-design revision notes; never card body |
| title/subtitle before `<1>` | project title layer |
| `<N>` | source beat marker, not guaranteed final card number |
| `<N> 1. Section title` | section-opening beat |
| black/default text | body explanation |
| red run | exact emphasis candidate; normally rendered orange/gold |
| paragraph break | rhetorical structure, not automatic card break |

Critical rule: **one source beat may become several design pages.** Do not force a one-to-one mapping between `<N>` and output page numbers.

Completion criterion:

- every non-empty paragraph is accounted for as revision note, title, marker, or block content
- all red runs survive as exact text spans
- first and last markers are recorded
- no leading revision note enters the body

## 2. Build the Editorial Page Architecture

Create the page ledger from `templates/page-ledger.yaml`.

### Page-split gate

Split a source block only when it contains more than one of these:

- independent claim
- independent piece of evidence
- named person/event requiring its own visual
- chart with a separate interpretation
- mechanism requiring a diagram
- transition or conclusion deserving a visual reset

Keep a block together when the second paragraph merely explains the first.

### Page-level writing rule

Each page should have:

1. one primary claim
2. one primary visual
3. one highlighted judgment or question
4. one source-credit area when evidence is present
5. one clear handoff to the next page

Do not add an extra headline if the visual title and orange judgment already compete for attention.

### Story sequence

Build sections as:

```text
section opener
→ problem or question
→ evidence
→ mechanism
→ counterpoint or constraint
→ implication
→ section conclusion/bridge
```

Preserve editorial order across sections. Inside a source beat, a chart and a person/event page may be reordered only when the causal explanation becomes clearer and no quoted chronology is changed.

Completion criterion: reading only the page claims and highlighted lines reconstructs the full argument without reading every body paragraph.

## 3. Select a Page Template

Use one primary template per page.

| Code | Use | Default composition |
|---|---|---|
| `S0` | cover | large title, subtitle, one symbolic visual |
| `S1` | section opener | numbered ornament, section title, representative chart/map |
| `D1` | data/chart/map | black title plaque, chart, body, orange judgment |
| `P1` | factual photo | upper photo 40–50%, lower body and judgment |
| `Q1` | person/quote | person on one side or lower area, quote and interpretation |
| `V1` | video card | fixed body with a 5–8s silent video in the media slot |
| `C1` | dark conclusion | full-bleed darkened image, white body, gold/orange judgment |

Avoid adding bespoke templates for trivial variation. Reuse the closest template and record only local exceptions.

Completion criterion: each page has one template code and one dominant reading task.

## 4. Decide Evidence vs Illustration

Set `visual_function` before sourcing.

### `PROVE`

Use actual, traceable assets:

- charts, statistics, maps, reports
- named public figures or events
- company announcements and product launches
- direct quotes
- current-news scenes

Rules:

- do not ask image generation to invent chart values
- do not present a generated public-figure/event image as authentic evidence
- do not substitute a nearby event or product because it looks similar
- retain exact source, period, unit, denominator, and credit

### `IDENTIFY`

Use a real source photo or official visual to identify a person, company, place, product, or event. Image generation may assist framing or produce a non-evidentiary background, but the identity-bearing subject must remain faithful.

### `ILLUSTRATE`

Image generation is appropriate for:

- abstract mechanisms
- generic market mood
- supply-chain pressure
- currency or risk atmosphere
- conceptual transitions
- dark conclusion imagery

Label generated art internally as generated. Never attach a false news-agency credit.

### Rights are separate

Track:

```text
source_identified
fact_verified
rights_cleared
```

One does not imply the others.

Completion criterion: every visual is explicitly `PROVE`, `IDENTIFY`, or `ILLUSTRATE`, and generated art is never used as false evidence.

## 5. Establish the Style Bible

Default target:

```text
ratio: 2:3 vertical
final size: 1200 × 1800 px
background: warm ivory #F3F0EA
ink: near-black #1C1B1F
judgment accent: burnt orange #C78335
ornament/gold: #C39A65
conclusion background: deep navy #151A24
```

Typography:

- verify installed Korean fonts before rendering
- use the supplied corporate font when legally available
- otherwise prefer a neutral Korean sans such as Apple SD Gothic Neo or Noto Sans KR
- body and source text must be deterministic, never image-generated glyphs

Visual rhythm:

- left/right safe margin: 8–10% of width
- one chart/photo normally occupies 38–50% of the page
- body is normally 2–4 short paragraphs
- one orange judgment per page
- source and page number stay in a consistent lower-right system
- switch to dark conclusion cards only near the synthesis/end, not randomly

Because the image tool generates 9:16 portrait rather than exact 2:3, compose inside a central 2:3 safe region, then center-crop top and bottom and resize to 1200×1800. Verify actual pixels after saving.

Completion criterion: one approved style reference exists for every template family used in the sequence.

## 6. Generate the Visual Layer

### Consistency protocol

Image generation is stateless. Every call must include:

- the same style prompt
- 1–3 approved reference cards matching the target template
- fixed palette and material instructions
- explicit central 2:3 safe zone
- forbidden elements
- whether text spaces should remain empty

Generate one page per call. Small batch planning is fine; a single prompt should not attempt to render a 40-page sequence.

### Full-generated versus hybrid pages

#### `IMAGEGEN_FULL`

Use only when the card has minimal exact text and no exact data chart. Still overlay title, body, source, and page number afterward.

#### `IMAGEGEN_BASE_EXACT_OVERLAY`

Default for data-heavy and Korean text-heavy pages:

1. generate the background, frame, atmosphere, or textless illustration
2. place real evidence photo/chart/map when required
3. overlay exact title and body from the ledger
4. render red Word spans as orange/gold
5. add source and page number deterministically

Do not regenerate an otherwise approved card merely to fix one typo; patch the text overlay.

### Photos

- actual event/person/company page: source real editorial or official imagery
- abstract page: image-generated conceptual visual is acceptable
- prefer direct subject-action correspondence over generic handshakes, typing, or holograms
- crop faces and gaze toward the text area when possible
- preserve negative space for body and source

### Charts and maps

- calculate and render exact values outside image generation
- image generation may create the surrounding plaque, frame, paper texture, or background
- include title, unit, basis, period, labels, values, and source from the ledger
- do not use visually stacked bars when the red subset is already included in the black total unless the relationship is explicitly explained

Completion criterion: every generated base has the correct template, safe area, palette, and visual function before exact text is added.

## 7. Compose Exact Korean Text and Data

The final card must be built from ledger text, not OCR-recovered generated text.

Required exact layers:

```text
section/title
chart title and labels
body paragraphs
highlighted judgment
quote and speaker
source credit
page number
```

Red source runs normally become orange/gold but their wording remains exact unless the page ledger records an approved editorial shortening.

If body text does not fit:

1. tighten paragraph spacing within the style range
2. reduce visual height slightly
3. split the page at a semantic boundary
4. request editorial shortening

Do not silently shrink body text until it becomes unreadable.

Completion criterion: exact-text comparison against the page ledger passes and no generated Korean glyph remains in a reading-critical layer.

## 8. Build Video Cards

Use `V1` when a factual person/event benefits from motion.

Default:

- 5–8 seconds
- silent unless audio is explicitly required
- no page pan, zoom, or scroll
- only the media window moves
- body, highlighted line, source, and page number remain fixed
- loop point should not create a distracting jump

Use actual sourced footage for evidence. Do not generate an apparent news clip of a real public figure.

Completion criterion: the card reads as a static page even when the video is paused.

## 9. Sequence QA

### Text QA

- compare every title, body, highlight, quote, value, unit, source, and page number with the ledger
- confirm revision notes are absent
- confirm red emphasis spans became the intended accent, not deletions

### Visual QA

Inspect every page and a sequence contact sheet:

- target is exactly 1200×1800
- no clipped heads, hands, chart labels, or source credits
- no generated gibberish in reading-critical areas
- no more than two primary reading tasks per page
- repeated template use feels consistent but not mechanically identical
- photo/chart alternation supports pacing
- section openers and dark conclusion cards are visually distinct

### Evidence QA

- factual chart values match source
- event/person photos identify the right subject and date context
- direct quotes are verbatim
- generated illustrations have no false agency/source credit
- source identification and rights status remain separate

### Sequence QA

- page numbers are continuous
- section transitions are visible
- pages do not repeat the same claim
- reading only highlights reconstructs the argument
- conclusion answers or reframes the opening question

Completion criterion: zero unresolved text, source, dimension, or sequence errors; visual warnings are either fixed or explicitly approved.

## 10. Apply Page-Specific Revision Notes

Leading `PXX.` notes are a revision queue, not manuscript copy.

Examples:

```text
P15. 그래프 제목을 아래로 바꿔주세요
P22. 점도표를 빼고 ‘연준 기준금리 추이’를 넣어주세요
P24. 출처표기 오타
```

Revision procedure:

1. parse page target and instruction
2. locate stable page ID plus current display number
3. change only the affected visual/text layer
4. rerun exact-text, source, and visual QA on affected pages
5. regenerate the contact sheet if layout or page count changed
6. mark the note resolved in the revision ledger

If inserting or deleting pages, keep stable internal IDs and update all display numbers automatically.

Completion criterion: every leading `PXX.` note is resolved, rejected with reason, or awaiting one explicit decision.

## Output Package

```text
project/
├── source/
│   └── manuscript.docx
├── ledger/
│   ├── manuscript.json
│   ├── pages.yaml
│   ├── sources.csv
│   └── revisions.yaml
├── references/
│   └── style-and-source-assets/
├── generated-bases/
├── cards/
│   ├── 001.jpg
│   └── ...
├── videos/
│   └── 015.mp4
├── contact-sheet.jpg
└── qa-report.json
```

Primary delivery is the final page sequence and video cards. Ledgers remain available for revisions and reuse.

### Existing upload-copy retrieval and epistemic gate

Treat `아까 만든 설명`, `기존 설명`, `에르메스한테 시킨 설명 복붙` as a retrieval request, not permission to draft a replacement.

1. Search the episode workspace, metadata artifacts, and recoverable session records for the exact text.
2. If found, return it verbatim in a copyable block unless the user explicitly asks for revision.
3. If not found, say `기존 문구를 찾지 못했습니다` or `모르겠습니다` and ask the user to paste it or authorize a new draft.
4. Never synthesize a plausible description and present it as the previously authored one.
5. If the user supplies the authoritative wording, preserve it as the metadata source of truth and keep it isolated from carousel copy.

Failure to retrieve is not a blank to fill creatively. Recognizing that the source is unavailable is a required production skill.

### Telegram native-album delivery contract

When delivering two or more static card images in Telegram, send them as **one native Telegram photo album/media group**.

- Use photo media (`InputMediaPhoto` / `sendMediaGroup`), not separate photo messages, documents, a ZIP, or a contact sheet.
- Put every final card in one media group when the sequence has 2–10 images. Preserve the exact page order (`01 → 02 → … → N`).
- Attach the caption only to the first photo so the cards remain one clean album.
- Set `protect_content=false` so Telegram permits normal album saving.
- Verify the API result contains every expected image and that all returned messages share one non-empty `media_group_id`. A successful send call without this equality check is not delivery verification.
- After revisions, resend the complete current sequence as one new album unless the user explicitly requests only the changed page.
- Do not substitute ZIP delivery or document grouping merely to enable batch download. The required UX is Telegram's native photo album: horizontal swiping plus the album-level save action.

For a single image, send one normal Telegram photo. For more than 10 images, split into consecutive native albums of at most 10 while preserving global order, and state the album ranges.

## Common Pitfalls

1. **Marker equals card number:** `<12>` is treated as final page 12. Fix: treat it as a source beat and build output pages independently.
2. **Red means correction/deletion:** red runs are dropped. Fix: preserve them as exact emphasis candidates.
3. **Revision-note leak:** leading `PXX.` instructions appear in the card body. Fix: parse them before `<1>` into a separate queue.
4. **One-prompt sequence:** dozens of pages drift in palette and typography. Fix: one page per call with fixed references.
5. **Generated Korean copy:** paragraph text becomes garbled. Fix: generate the visual base, then overlay exact text.
6. **Generated chart data:** plausible-looking but false labels or values appear. Fix: render exact data separately.
7. **Fake evidence:** a generated public-figure or event scene is credited like a news photo. Fix: use real sourced media for `PROVE`/`IDENTIFY`.
8. **Decorative photo bias:** every abstract noun receives generic stock. Fix: use photos only when they identify or illustrate an observable beat.
9. **Tiny text rescue:** overfull pages are solved by shrinking all type. Fix: reduce visual height, split the page, or shorten with approval.
10. **Source equals rights:** a visible publisher name is treated as clearance. Fix: track source and rights separately.
11. **Random dark cards:** conclusion styling appears mid-argument. Fix: reserve dark mode for synthesis, stakes, or final questions.
12. **Regenerating for typos:** an approved layout changes because one label is wrong. Fix: patch deterministic text layers only.
13. **Bright but still wet:** a white-background image is accepted as Figma style even though it uses glossy 3D, gradients, glass, or isometric depth. Fix: verify flatness and material language, not background color alone.
14. **Post-hoc semantic rescue:** capsules, arrows, labels, or boxes are composited over an unclear generated image despite `image gen만`. Fix: regenerate a self-explanatory core visual; add only approved card-template layers.
15. **Layout overreaction:** left-heavy line wrapping is solved by changing alignment or redesigning the approved skeleton. Fix: preserve layout and rebalance paragraph length and grammatical wraps.
16. **Invented retrieval:** an earlier upload description cannot be found, so a new summary is returned as though it were the old copy. Fix: state that it was not found; never mask retrieval uncertainty with generation.

## Verification Checklist

- [ ] Source DOCX hash recorded and original preserved
- [ ] Leading revision notes separated
- [ ] All `<N>` markers and red runs parsed
- [ ] Page ledger created with stable IDs
- [ ] Every page has one claim, visual, highlight, and template code
- [ ] Every visual classified as `PROVE`, `IDENTIFY`, or `ILLUSTRATE`
- [ ] Real evidence used for factual people/events/data
- [ ] Image generation used for the visual layer with consistent references
- [ ] Exact Korean text and chart values overlaid deterministically
- [ ] Final pages are exactly 2:3 and pixel dimensions verified
- [ ] Source credits and page numbers are readable and consistent
- [ ] Video cards remain legible when paused
- [ ] Text, visual, evidence, and sequence QA passed
- [ ] Every `PXX.` revision note has a recorded resolution
- [ ] Telegram multi-image delivery uses native photo album(s), preserves page order, and verifies one shared `media_group_id` per album
