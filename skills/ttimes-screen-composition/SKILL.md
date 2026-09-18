---
name: ttimes-screen-composition
description: Use when a TTimes PD must turn an approved final-cut transcript or cleaned DOCX into an editor-facing screen-composition plan that combines editorial captions and visual materials on the same timeline. Standardizes caption function, material taxonomy, verbal footage briefs, simultaneous layers, timing, collisions, evidence, rights, and inline DOCX instructions. Do not use for spoken-caption SRT, cut decisions, rough-cut audio rendering, or exhaustive asset discovery unless explicitly requested.
license: MIT
metadata:
  version: 0.6.0
  author: Hermes Agent
  hermes:
    tags: [ttimes, screen-composition, captions, footage, inserts, editor-handoff, docx]
    related_skills: [ttimes-editorial-copy, ttimes-script-and-srt, ttimes-cut-editing]
---

# TTimes Screen Composition

## Current review mode — user calibration 2026-09-17

For screen-composition proposals and revisions, use **Word threaded-comment review** by default. Read [caption and material review calibration](references/word-review-framing-20260917.md). This mode takes precedence over the historical inline-only execution grammar below. Preserve approved speech and its formatting; anchor `[강조 자막]`, `[자료]`, or another appropriate proposal comment to the exact relevant speech, and put the local selection reason in a **genuine reply to that comment**. Candidate counts follow the beat; never fill a quota. Do not insert `//자막` proposals into the body in this mode.

Use the historical yellow-object/blue-sync `//자막` and `//NN` grammar when the user explicitly asks for an execution handoff or approved final inline layout, and when parsing old files. Do not silently convert unresolved review alternatives into selected assets. Name a review deliverable `*_화면구성_댓글검토본.docx` or `*_자료설계.docx`.

Start material discovery from the speech's named companies, products, concrete objects, actions, scale and metaphors; identify the specific visible part before choosing a source. Then test its local editorial purpose. Broaden from the named company's official sources to other well-matched official/primary material when needed. A generic viewer-need analysis must not replace searching the actual nouns in the speech. Deliver useful links and inspected scenes, not just company names or search briefs.

Review checks: original speech unchanged; each proposal anchored precisely; every rationale linked as a real thread reply; alternatives are distinct and adaptive; actual source/scene and video source IN/OUT verified or explicitly pending; quotations literal; illustrative sources not promoted to proof. Validate the OOXML threading and, when available, the Word reply collection; PDF alone does not prove comments work.

## Status and evidence

This is a **provisional v0.5 standard** grounded in three materially different user-authored `자료-완료` corpora. The 2026-09-06 update strengthens editorial selection and evaluation; it does not certify unseen-transcript performance.

## 자막·자료·보관 연결 규칙

자막을 넣는 선과 자료 선정에는 `references/caption-material-archive-contract.md`를 필수로 읽는다. 최소 충분한 화면을 선택하고 원본/편집본 시각을 분리한다. 자료의 출처와 사용 구간은 현재 프로젝트의 자료 목록에 남긴다.

## Operational entry: decide the screen, not just the caption

For `어느 부분을 어떻게 구성`, `자료·강조·설명·구조 자막 배치`, or `화면구성`, apply this skill **before** drafting isolated captions or searching assets. A taxonomy explanation is not the requested composition artifact.

1. Read approved speech in context, including the previous explanation and next payoff.
2. Name the viewer's specific unresolved need and compare plausible forms, including staying on the speaker.
3. Select the minimum sufficient composition; state why it belongs on this clause and not its neighbor. `NONE` is a valid decision, not a missing task.
4. Draft wording through `ttimes-editorial-copy`; use C4/C5 for concept/structure rather than forcing everything into emphasis. The former `caption-layering-workflow` is unavailable locally, so use only the current skill's explicit output contract rather than claiming an external layer grammar or renderer.
5. Set the actual speech anchors for entry, change, and exit; review continuity across beats before producing the minimal inline Word.

Read `references/editorial-selection-and-sequence.md` for the choice protocol and cross-beat memory. Read `references/unseen-transcript-calibration.md` only for training/evaluation runs. Do not load every corpus or run a benchmark for an ordinary caption request.

**Rule precedence:** explicit current user decisions → this skill's current execution contract → applicable approved format calibration → historical corpus observations → assistant proposals. An observation is not automatically a new prohibition. Preserve intentional `OPEN` discretion, reuse the same asset ID for the same asset, and never import the spoken-caption character limit into editorial copy. Unknown preference conflicts remain explicit rather than silently becoming house style.

Corpus 1: `_자료-완료_ 박영선-박남규 컷편.docx`

- 989 paragraphs
- 58 explicit `//자막` calls
- 64 visual calls using asset IDs `01`–`48`
- 51 `@@` correction locators
- 7 embedded reconstruction references

Corpus 2: `_자료-완료_ 260723_강정수 2편 컷편.docx`

- 1,091 paragraphs
- 71 explicit `//자막` calls
- 60 numbered material calls, 53 unique assets
- 33 `@@` correction locators
- 1 embedded visual reference
- median material-call length: 22 characters

Corpus 3: `(자료-완료) 임승찬-윤우진.docx`

- 511 paragraphs and 80 timestamp blocks
- 47 explicit `//자막` calls and 1 explainer-caption call
- 4 numbered material calls and 2 profile calls
- 0 explicit `//그래픽` calls
- format: organization/management insight interview built from company cases
- default visual: speaker-led one-man continuity, with conversational captions carrying rhythm, reversal, confession, definition, and conclusion

The second corpus confirmed that the final DOCX is a minimal execution layer, while detailed function/source/search/fact/rights data belongs in an internal ledger. The third corpus corrected an assistant bias toward converting every abstract business relationship into a diagram. In organization/management interviews, the speaker and conversational editorial captions are the default; graphics are exceptional structure tools, not the default response to abstraction.

Read `references/gang-jeongsu-screen-composition-user-calibration.md` for the measured minimal handoff grammar and `references/im-seungchan-yoon-woojin-management-interview-user-calibration.md` for the user-confirmed organization/management interview grammar.

Continue recording user corrections by error class; do not generalize topic-specific jokes, positions, or asset preferences into house rules.

### Live PD caption-selection feedback loop

Develop this screen-composition skill from the PD's ongoing caption choices, not only from completed `자료-완료` corpora.

- Use each confirmed emphasis/explainer/question caption to learn **which speech beat deserved an editorial layer**, not merely how the final sentence was worded.
- Record rejected drafts and the PD's redirected focus so later composition selects the right clause, causal axis, and viewer function.
- Keep wording calibration in `ttimes-editorial-copy`; feed the resulting selection rule into this skill's C1–C7 placement decisions.
- A clean cut DOCX with no `//자막`, color, or highlight is not formatting evidence and must not be promoted to a completed screen-composition corpus.
- Only PD-confirmed captions become gold examples; unconfirmed assistant drafts remain working hypotheses.

Current live calibration: `ttimes-editorial-copy/references/lee-jungdae-geo-caption-calibration-20260730.md`.

For returning TTimes guests' profile introductions and the ongoing 박종천 1편 review, read `references/park-jongcheon-live-feedback-20260916.md`. Prefer existing user-provided/broadcast profile cards over automatically reducing a returning guest to a name/title label; retain the scope and unresolved placement choices recorded there.

Read `references/park-namgyu-screen-composition-user-calibration.md` for the first corpus, `references/gang-jeongsu-screen-composition-user-calibration.md` for the second, and `references/im-seungchan-yoon-woojin-management-interview-user-calibration.md` for the third.

## Clarity-first user-review protocol

When learning from or auditing a user-authored `자료-완료` DOCX:

1. Process the formatting-bearing DOCX, not a clean transcript with a similar filename.
2. Parse yellow-highlighted object(s) and the immediately following unhighlighted blue speech as one screen-composition record.
3. Resolve the spoken-caption switch from the dominant readable object: explicit `//자막` and readable article/report/chart layers mean `SUPPRESS`; ordinary video/photo material and non-`//자막` object labels mean `KEEP` by default.
4. Analyze material and caption together when they share a blue sync. Do not finish with disconnected caption and material inventories.
5. Auto-resolve obvious direct B-roll, plain stock, person/history stills, practical big-tech sourcing, explicit editor-discretion calls, and straightforward caption classes.
6. Use independent review only for non-obvious editorial choices; do not convene a deep meeting for every numbered asset.
7. Separate `confirmed by DOCX`, `inferred`, and `unresolved`.
8. Ask the user only when the remaining uncertainty changes screen implementation or editorial meaning. Ask one narrow question at a time and state the best current interpretation first.
9. Never ask the user for a placement already encoded by formatting and adjacency.

High-value question triggers: caption exit vs spoken-caption resumption, object label vs editorial caption, simultaneous vs build/replace behavior, direct quote vs PD summary, evidence vs atmospheric article use, generated-reference status, and non-obvious reuse.

## Overview

Screen composition is not a caption list placed next to a material list. It is a time-based composition contract:

```text
approved speech and story beat
→ visual-need decision
→ editorial caption decision
→ material decision and footage brief
→ simultaneous layer and timing plan
→ fact/source/rights and collision review
→ inline editor-facing DOCX
```

One segment record may contain all of these objects, but the user-confirmed TTimes render switch determines which text layer is visible:

```text
ordinary footage/photo only → material + spoken captions
material + object label without //자막 → material + label + spoken captions
explicit //자막 → material/one-man + editorial caption; spoken audio continues, spoken captions suppress
readable article/report/chart → reading object + source; spoken audio continues, spoken captions suppress
```

Do not render an editorial `//자막` and normal spoken captions simultaneously unless the user explicitly overrides the house rule.

## When to use

Use when the user asks for:

- `화면구성`
- `자료 작업`, `자료-완료`
- editor-facing inline footage and caption instructions
- classification of question, quote, emphasis, explainer, fact, comparison, or process captions
- verbal descriptions of what insert footage should feel and look like
- a final DOCX combining transcript, captions, footage, graphics, sources, and internal notes

Do not use for:

- spoken-caption SRT alone: use `ttimes-script-and-srt`
- deciding what content to cut: use `ttimes-cut-editing`
- rendering an approved cut to MP3: use `ttimes-audio-rough-cut-rendering`
- exhaustive video-link and exact-source-time research unless the user explicitly asks; without selected/delivered assets, produce `자료설계`/`자료요청`, not `자료-완료`

## Role and deliverable contract

Keep production state and filename aligned.

### `자료설계` / `자료요청`

- **Hermes:** judges visual need, drafts caption text, proposes footage type/source/search/include-exclude criteria, and maintains fact/rights state.
- **PD/user:** may approve or select footage.
- **Editor:** is not expected to research unresolved assets from the final timeline.

### `자료-완료`

- Every numbered call points to an actually selected/delivered asset, whether selected by the PD or by Hermes after an explicit exact-asset request.
- The visible DOCX contains only the executable call, exact caption text, exact blue sync, and local exceptions.
- Search terms, candidate families, function/render/status codes, fact reasoning, and rights reasoning remain in the internal ledger.
- If actual selection is incomplete, do not title or report the artifact as `자료-완료`.

The editor implements crop, pacing, compositing, animation, and reconstruction from delivered material. Any unresolved choice that changes the edit stays explicit in the internal ledger or appears as one terse local exception—not as repeated metadata in every visible block.

Completion criterion: the final filename truthfully describes the asset-selection state, and the editor-facing DOCX does not require the editor to convert a research brief into instructions.

## User-review and ambiguity gate

Do not interrogate the PD about obvious direct inserts. Automatically resolve material/caption intent when the DOCX formatting, blue sync, and visible relationship make it clear.

Ask the user when a genuine PD decision cannot be recovered, including replacement vs build, simultaneous vs sequential multi-asset layout, caption/material exit mismatch, evidence-vs-illustration intent, or direct quote vs editorial summary. Ask one narrow question at a time and state the current best inference first.

```text
clear from DOCX + established grammar → analyze and confirm automatically
unclear but recoverable from source/formatting → inspect before asking
irreducible PD intent → ask the user clearly
```

Keep the analysis explicit and easy to review: confirmed source grammar, inferred function, remaining uncertainty, then the single question.

## Core segment model

Treat each screen beat as one record with independent objects:

```text
SEGMENT
├─ AUDIO       actual speech, music, silence
├─ SPEECH      spoken-caption layer
├─ EDITORIAL   question, thesis, fact, explainer, structure, quote, identity
├─ VISUAL      one-man, footage, still, article, chart, diagram, graphic
├─ SOURCE      source identity and screen credit
├─ FACT        claim-verification state
├─ RIGHTS      use-rights state
└─ TIMING      start, end, build, replace, persist
```

Do not merge these axes into one label. `company official video` is a source family; `B-roll` is an implementation; `prove the claim` is a story function.

## Workflow

### 1. Freeze the editorial source

Start from one approved final-cut transcript or cleaned DOCX.

- Confirm the cut and move decisions are final.
- Preserve speaker, time, paragraph order, and `@@` corrections.
- Do not invent screen composition against an obsolete pre-cut transcript.
- Freeze the source hash and record the authoritative file.

Completion criterion: no unresolved `CUT`, `MOVE`, or retake decision is being solved inside screen composition.

**Authoritative-source mismatch stop:** if the user says placements or captions are present in the DOCX but the opened file lacks them, stop placement inference. Report the exact path, size, hash, and marker counts; search version history, recovery copies, caches, and alternate files; then ask for the authoritative path or a re-saved/uploaded copy. Do not ask the user for a placement that should be recoverable from the stated source.

#### Source-package topology gate

Before reading numbered assets, classify the actual package:

1. **Inline-complete:** DOCX itself contains `//NN`, `//자막`, formatting, and placement instructions.
2. **Split working package:** the `(자료)` DOCX is a clean or synced cut transcript while numbered media, 말자막, cut audio, articles, and graphics sit beside it.
3. **Reference corpus:** only extracted observations or a prior completed example remain.

#### Synced cut DOCX is a separate upstream artifact

When the user calls a plain `(자료) ... 컷편.docx` a `싱크` result, do not mistake it for a formatting-bearing screen-composition file. The observed sync grammar is exactly:

```text
[화자명 MM:SS]
[해당 승인 발화 한 문단]
[빈 문단]
```

Every speaker change creates a block; a long same-speaker turn is split near a semantic boundary around one minute. The timestamp is start-only at whole-second precision, and the next block start is the implicit end. For Korean-source sync, approved wording is preserved. For English/foreign-source sync, the final DOCX body is a complete source-faithful Korean translation while the English source remains internal; this translation is part of sync, not screen composition. Spoken-caption segmentation and material placement remain separate downstream tasks. Verify OOXML before classification: a synced base may have no colors, highlights, tables, media, comments, Track Changes, `//NN`, `//자막`, or `@@`. Read `references/synced-cut-docx-structure.md` for the measured corpus, canonical block contract, package topology, and `3N-1` paragraph verification. Actual sync production is currently `external_dependency`: `media-localization-workflows` and `references/2026-07-21-english-youtube-korean-sync-docx.md` are not locally available. Read `references/local-dependency-gates.md` to state the required inputs and outputs instead of claiming a sync run.

Inspect DOCX OOXML and related parts before declaring callouts absent; plain-text extraction can omit text boxes, comments, or revisions. In a split package, do not invent missing `//자막` text. Build placement intent from actual media, transcript/말자막 anchors, and neighboring asset IDs, then label each conclusion `Confirmed`, `Strong inference`, `Weak inference`, or `Unresolved`.

For cloud-hosted media, verify byte readability and work from a hashed local copy before describing frames. On macOS File Provider volumes, do not trust logical size alone: inspect flags/allocated blocks, materialize a `dataless` placeholder non-destructively, then re-check blocks before hashing or probing. An empty-file SHA-256 (`e3b0c442...`) on a nonzero logical-size asset is a hydration warning, not a valid source hash. A filename establishes a labeled subject/source, not exact shot content.

When the user asks why existing `01`, `02`, … assets or captions were chosen, follow `references/numbered-asset-intent-audit.md`. For consecutive assets, compare their order against parallel clauses or enumerated speech beats; a 1:1 order match is strong placement evidence but never outranks an explicit inline callout. Treat `material + spoken caption` with no added editorial caption as a valid intentional composition mode. See `references/park-namgyu-asset-03-flood-analysis.md` for a calibrated case covering parallel-clause mapping, location-overlay risk, illustrative-vs-evidentiary use, and File Provider hydration.

For a single numbered video whose scene timing and search rationale must be explained, inspect the complete sequence rather than trusting the filename or approximate user locator. Build a coarse contact sheet, refine promising intervals at 0.5–1.0 second spacing, and record `concept diagram`, `physical demonstration`, `detail`, and `establishing view` separately. Choose the interval that performs the speech beat's viewer function and has usable caption/label negative space. State whether the visual merely illustrates a mechanism or actually proves the spoken claim. See `references/nissan-ao-solar-scene-and-search-analysis.md` for a calibrated EV-roof-solar example, including the correction from an approximate 2:24 locator to the observed 2:42 deployment, arrow-label placement, practical company-video sourcing, and claim-boundary analysis.

When the user explicitly asks to **find exact videos**, not merely recommend source families, search official company/developer channels, fetch timed transcripts, and sort candidates into `clean concept overview`, `actual operational example`, `technical proof UI`, and `cross-domain extension`. Then download only candidate ranges and inspect contact sheets before returning timestamp links. A transcript match alone is insufficient: report visible content, crop/legibility needs, and the claim boundary, and never rename a nearby workflow as the requested one (`order cancellation ≠ refund`, `delivery-date change ≠ refund`). For the reusable Palantir Ontology source bank and a complete worked example covering objects, relationships, state, actions, permissions, validations, and non-commerce extension, read `references/palantir-ontology-official-video-research.md`.

Completion criterion: the artifact carrying placement/caption authority is identified, and no filename-, approximate-time-, transcript-only-, or reference-only inference is presented as observed screen fact.

### 2. Map story beats before choosing assets

For every beat record:

- transcript anchor and source time
- question, thesis, mechanism, evidence, example, implication, or transition
- what the viewer must understand or feel
- whether the speaker's face/reaction is itself the strongest visual

Begin discovery with the concrete referents in the speech and the visible detail being discussed. Evaluate the viewer function alongside this search; do not attach random official footage merely because a company is named.

**Practical sourcing heuristic:** for a generic illustrative insert, the PD may deliberately use a famous big-tech company's official footage because Google, NVIDIA, Tesla, and similar companies publish abundant, clean, broadcast-usable-looking video. Treat this first as a footage-discovery and production-quality shortcut—not automatically as brand symbolism, endorsement, evidence, or a cross-asset narrative. Infer strategic meaning from the chosen company only when the placement, caption, or user confirms it.

**Complexity-atmosphere heuristic:** a dense enterprise-software UI may be selected as background footage solely to make an organization, business process, or decision environment *feel operationally complex*. Do not require every visible metric, chart, model, tab, or object to correspond literally to nouns in the speech. Classify this as `ILLUSTRATE/ATMOSPHERE`, not `PROVE`, when the viewer is not expected to read the interface and the intended message is the accumulated impression of many variables, states, evaluations, or controls. Preserve spoken captions by default; do not add explanatory labels that turn atmospheric complexity into a false product-feature claim. Use `references/background-insert-visual-rhetoric.md` for the selection questions, default composition, and dense-enterprise-UI pattern.

Completion criterion: every candidate screen instruction is linked to a specific speech anchor and editorial goal, while practical source convenience and atmospheric UI density are not over-interpreted as evidentiary or literal semantic intent.

#### Format-first rule: organization/management insight interview

When the transcript is an organization/management interview built from company cases, apply the user-confirmed `임승찬·윤우진` grammar before the general visual-need gate. Read `references/im-seungchan-yoon-woojin-management-interview-user-calibration.md`.

Default hierarchy:

```text
speaker/reaction
→ conversational editorial caption
→ profile/logo/company or service explainer
→ selected real material
→ graphic only when a relationship cannot remain clear through speech and captions
```

Rules:

- Treat one-man continuity as an active composition choice, not an empty screen waiting to be covered.
- Preserve speech character. Prefer a vivid direct phrase, reversal, confession, analogy, question, or concrete operational change over a polished report-like noun phrase.
- Do not replace several concrete operational beats with one abstract diagram when the sequence of captions is the actual interview rhythm.
- Establish people, unfamiliar companies, and services early with profiles, logos, short explainers, or actual screens before declaring a large abstract thesis.
- Leave cautious observations and personal judgments on the speaker when an assertive caption would make them look like a program-level fact.
- Use a graphic only when the viewer must retain multiple nodes, order-dependent steps, a comparison axis, a denominator-bearing number, or a cross-paragraph method at the same time.
- If a caption and graphic restate the same thesis, keep the form that better serves the beat; do not use both by default.
- The planner fixes the core message, indispensable relationship, numbers, and sources. The designer decides position, icons, color, detailed layout, and motion unless one of those choices changes meaning.
- For Word proposal review, anchor the proposal to the original speech and add the selection reason as a genuine threaded reply, following the current review mode. For an explicitly requested inline execution edition, rationale may instead be anchored to its production object. Do not repeat boilerplate about exact sync or designer discretion in every comment.

Failure signal: a management interview starts to read like a strategy report because most abstract sentences have become arrows, stages, matrices, or framework cards. Return to the speaker and rebuild the rhythm from the user's caption voice.

### 3. Apply the visual-need gate

Set one value:

- `REQUIRED`: necessary to understand, prove, compare, quantify, identify, or show a process
- `OPTIONAL`: useful for rhythm or immersion but not required for comprehension
- `NONE`: one-man continuity or the speech itself is stronger

Recommend material when the beat contains an abstract invisible mechanism, a specific person/company/place/product, evidence, scale, history, process, or comparison.

Prefer `NONE` when the line is already concrete, emotional, quotable, or strong on the speaker's face. Do not use handshake, money-counting, generic typing, or futuristic hologram stock merely because a related noun was spoken.

Completion criterion: every visual call has an independent story function; decorative filler is removed.

### 4. Classify editorial captions by function

Spoken captions are a separate layer. Classify only added screen text.

| Code | Function | Typical subtypes |
|---|---|---|
| `C1` | question/progression | `Q` question, transition/re-entry |
| `C2` | thesis/judgment | core claim, reversal, warning, conclusion |
| `C3` | fact/evidence | date/event, number/statistic |
| `C4` | concept/context | term definition, mechanism/causality |
| `C5` | relationship/structure | comparison, system relation, process/sequence |
| `C6` | direct quotation | verified verbatim speech or document quote |
| `C7` | identity/label/source | profile, object label, source credit |

`강조` and `설명` are not top-level classes. Store them as expression tone:

```text
tone = EMPHASIS | NEUTRAL | EXPLAINER
```

A number can be emphatic or neutral; a comparison can be explanatory; a direct quote can be visually emphatic while remaining `C6`.

Rules:

- One primary function per caption; one secondary function only when necessary.
- `Q.` is selective, not automatic for every question or chapter transition.
- Use quotation marks only for a source-verified direct quote.
- A PD summary is `C2` or `C5`, never `C6` merely because it sounds quotable.
- Long explainer wording marked exact is not shortened, split, or polished by the editor.
- Multiple written lines display simultaneously by default.

**User-calibrated caption-intent hard gate:** a taxonomy label alone does not justify a caption. Before adding one, state what the screen gains at that exact moment and what is lost if the caption is absent. Keep it only when it performs at least one concrete job:

- creates a setup/payoff or visible reversal
- preserves a distinctive direct phrase, emotion, humor, confession, or speaker character
- makes a number, contrast, or relationship intelligible that speech alone does not hold clearly
- carries one indispensable question across a long or complex answer
- creates an actionable warning or ending beat

Delete the caption when it merely summarizes accurate speech, announces an obvious chapter change, repeats a readable article/graphic, restates the previous caption, or converts an opinion into a polished program thesis. `핵심을 남긴다`, `장을 전환한다`, `결론을 회수한다`, and similar generic rationale do **not** pass by themselves; the rationale must identify a specific editorial effect. Caption count from a gold document is evidence of that document's rhythm, never a quota. When uncertain, keep the speaker face and no editorial caption.

Read `references/caption-function-render-timing-standard.md` for subtypes, writing rules, verification levels, rendering forms, and the decision tree.

Completion criterion: every caption has one clear viewer function, exact screen text, a fact basis, and an explicit relationship to speech.

### 5. Specify materials on independent axes

For every material placement record:

```text
SOURCE × FORM × IMPLEMENTATION × STORY_FUNCTION × STATUS × RIGHTS
```

Minimum fields:

- material need
- asset ID and placement/use ID
- source family
- original asset form
- final implementation
- primary story function
- selection mode
- status and rights

The same asset ID may be reused at several placements. Internally distinguish them as `12-01`, `12-02`, etc. Repeating `//12.` in the DOCX is valid only when every occurrence refers to the same source asset. Different files, sources, events, or independently recalculated graphics require new asset IDs.

Generated images, `지피티 짤`, and embedded diagrams default to:

```text
REFERENCE_ONLY + RECREATE_GRAPHIC
```

unless the user explicitly approves direct final use.

Read `references/material-taxonomy-and-footage-brief.md` for the source, form, implementation, function, status, rights, and reuse standards. Read `references/visual-caption-selection-decision-standard.md` for the user-confirmed decision gate covering video, photo, article, report/data, graphic, no-material, and caption selection.

**User-priority rule for Korean news captures:** when several articles cover the same event with comparable directness, factual accuracy, usable imagery, and publication timing, search and select in this order first:

1. 머니투데이
2. 뉴시스
3. 뉴스1
4. ZDNet Korea(지디넷코리아)

Do not replace a primary source merely to satisfy the outlet order. Official announcements, original research, company/agency disclosures, court or regulator documents, and official event results remain the first source for exact facts. Use another reputable outlet only when the four preferred outlets do not offer an equivalently direct or usable article, or when another outlet has the exclusive interview, result, image, or reporting needed for the exact speech anchor. Record the exception reason in the Word comment or internal ledger instead of silently changing source priority.

Completion criterion: a material can be traced from recommendation through selection, delivery, placement, source, and rights without changing identity.

### 6. Write a verbal footage brief internally, then collapse it after selection

During `자료설계` or exact-asset research, never stop at `데이터센터 영상`, `로봇 자료`, or `관련 공장 인서트`. Use a detailed internal footage brief to find and reject candidates.

Once the asset is selected and the deliverable becomes `자료-완료`, do **not** paste the full brief into the visible Word body. Collapse it to the observed one-line call:

```text
//NN. (subject/file)_source_(source time)_shot note
```

Keep include/exclude criteria, search terms, claim boundary, fact state, and rights state in the internal ledger. Add one terse local warning only when it directly changes the editor's action.

Internal brief schema:

```text
[subject] does [observable action] in [setting].
[shot and viewpoint], [camera behavior], [time feel], [tone].
Include: [required visible elements].
Exclude: [misleading or clichéd elements].
Duration: [length or complete action].
Connection: [entry and exit anchors].
Safe area: [space for speech/editorial captions].
Source/search/selection: [likely family, terms, owner of final choice].
```

Mandatory minimum:

1. who or what
2. observable action
3. space/situation
4. what must be visible
5. what must not be selected

Use concrete action rather than abstract themes. Translate `innovation`, `growth`, `competition`, and `AI work` into observable behavior or a graphic.

Example:

```text
자동차·전자 조립라인에서 사람 옆의 휴머노이드가 부품 상자를 집어
지정 위치에 놓는 반복작업이 한 동작 안에서 보이는 5~7초 중경 장면.
걷기·춤·무대 데모보다 실제 생산라인 맥락을 우선한다.
포함: 로봇 손·관절 움직임과 작업 대상.
제외: SF CG, 춤추는 로봇, 로고만 보이는 홍보 오프닝.
우측 상단에 C2 강조자막을 둘 수 있는 컷을 선호한다.
출처 후보: 해당 기업 공식 YouTube 또는 공장 공식 영상.
```

Do not over-specify a shot that may not exist. Use:

- `STRICT`: the mechanism/evidence requires a specific visible action
- `GUIDED`: include/exclude conditions are fixed; composition remains flexible
- `OPEN`: editor discretion is intentional (`아무 장면`, `대충 인서트`, `재탕`)

`OPEN` is a completed instruction when the permissible range is clear.

Completion criterion: even without a link, the editor can imagine what to search for and can reject a wrong shot.

### 7. Compose simultaneous layers

Recommended logical stack:

| z | Layer | Content |
|---:|---|---|
| 10 | `BACKGROUND` | one-man, B-roll, photo, article |
| 20 | `PRIMARY_GRAPHIC` | chart, comparison, mechanism graphic |
| 30 | `GRAPHIC_LABEL` | arrows, parts, number labels |
| 40 | `IDENTITY` | profile, place/time label |
| 50 | `EDITORIAL` | question, emphasis, explainer, fact, quote |
| 60 | `SPEECH` | spoken captions |
| 70 | `SOURCE` | material and quote credit |
| 90 | `INTERNAL` | review marks only; remove before delivery |

Same-segment combinations are allowed:

- ordinary footage/photo + speech captions when no `//자막` or other dense reading object is active
- material + editorial caption + source, with spoken captions suppressed for that blue sync range
- graphic + short labels + source when the labels are simple callouts; suppress spoken captions when the graphic/chart itself is a primary reading task
- one-man/PIP + material + speech when no editorial caption or dense reading object is active

**TTimes spoken-caption switch:** decide from the dominant readable screen object, not only from the literal marker.

```text
active //자막 → SPEECH SUPPRESS
readable article/headline capture used as evidence or caption-like text → SPEECH SUPPRESS by default
material-only footage/photo with no substantial reading → SPEECH KEEP
small object label/callout without //자막 → SPEECH KEEP
small logo/source credit → does not itself trigger suppression
```

Audio continues during suppression. Spoken captions resume after the editorial/readable-article range ends. If a memo says `영상은 계속, 강조자막은 끝`, keep the material on screen but resume spoken captions immediately from the next blue speech block. Material and editorial-caption end points are independent. A highlighted object label/callout such as `(차 지붕 위에) ← 태양광` may coexist with spoken captions.

Hard density rules:

- major reading tasks: maximum 2 per frame
- text blocks: normally maximum 3 — speech, one editorial/graphic block, source
- do not show question + emphasis + explainer simultaneously
- do not show long speech captions and a long explainer card as competing reading blocks
- profile + speech may coexist briefly; add no third editorial block
- remove decorative footage before sacrificing evidence, meaning, or speech accessibility

Collision priority:

```text
evidence/meaning
→ speech accessibility
→ context/explanation
→ emphasis
→ identity
→ decoration
```

Read `references/integrated-layer-collision-standard.md` for safe zones, composition combinations, timing, source/fact/rights states, and adversarial gates.

Completion criterion: the viewer never has to read or interpret three independent primary messages at once.

### 8. Specify temporal behavior

Every screen object has start and end anchors plus one display mode:

- `D0 SIMULTANEOUS`: all lines/items appear together; default
- `D1 SEQUENTIAL`: next item appears after the previous one leaves
- `D2 BUILD`: previous items remain while new items accumulate
- `D3 REPLACE`: same position changes from A to B
- `D4 FIXED_CHANGE`: title/axis remains while values change
- `D5 SPEECH_SYNC`: full structure remains and the spoken item is highlighted

Line breaks are layout information, not animation instructions. Do not infer build or sequential behavior from multiple lines.

For spoken captions record:

- `KEEP`
- `SUPPRESS`
- `RELOCATE`
- `HOLD`
- `N/A`

TTimes default is object-dependent:

```text
ordinary footage/photo only, no //자막 → KEEP
active //자막 over the blue sync → SUPPRESS
readable article/report/chart → SUPPRESS
small object label/source credit only → KEEP
```

Audio continues during suppression, and the complete spoken transcript/SRT remains preserved outside the visual decision. Resume spoken captions when the editorial-caption sync ends.

Completion criterion: the editor knows what enters, persists, changes, and exits, and multiple approved lines are not accidentally animated one by one.

### 9. Verify source, fact, and rights separately

Do not use one generic `verified` flag.

- **Asset:** recommended, selected, delivered, reference-only, recreate, missing
- **Source:** verified, identified, unresolved
- **Fact:** verified, qualified, pending, conflict, not applicable
- **Rights:** cleared, licensed/restricted, pending, unknown, do-not-broadcast

A source being identified does not prove the pictured scene supports the claim and does not clear usage rights.

Final-broadcast blockers:

- `FACT_PENDING`
- `FACT_CONFLICT`
- `RIGHTS_UNKNOWN`
- `MISSING_SOURCE`
- direct quotation without exact source verification

Do not invent clearance. Keep unknown states explicit.

Completion criterion: evidence assets support the exact claim, source and rights are traceable, and unresolved blockers remain visibly blocked rather than disappearing into prose.

### 10. Render the requested DOCX mode

For the default threaded-comment review, follow the current review mode above. The remainder of this section describes historical inline execution handoffs only.

Preserve the user's observed grammar unless a project template says otherwise:

- **base transcript:** black/default text. Do not recolor the whole surviving transcript blue.
- **exact production sync:** only the speech run(s) governed by the immediately preceding yellow object are blue/cyan without highlight. A paragraph may be mixed-run: blue for the active sync range, then black where the object exits.
- **production objects:** yellow highlight + cyan/blue bold. The formatting and adjacency encode placement, so do not repeat start/end metadata in prose unless the sync cannot be encoded at run level.
- **editor-only internal note:** red, never broadcast.
- `@@`: correction locator; remove only the marker from viewer-facing text
- `//NN.`: material asset call
- `//자막`: editorial caption call
- **sync-by-adjacency:** one or more highlighted production objects apply to the immediately following unhighlighted blue/cyan speech block. That blue block is the in/out sync range until the next highlighted object, speaker/time boundary, or ordinary non-blue boundary.
- **mixed-run correction exception:** a blue speech paragraph may contain small yellow-highlighted `@@` correction runs. Those inline correction locators do not turn the paragraph into a production object, do not break the blue sync, and do not shift the material/caption start to the next paragraph. Classify at run level, not by `paragraph contains any highlight`.
- **simultaneous composition:** when a caption block and a material block both appear before the same blue speech block, they are assigned to the same sync and may coexist on screen. Do not analyze them as unrelated lists.

Do not search only for explicit timecodes or marker numbers. Parse the highlighted object(s) and the following blue speech as one screen-composition record.

### Current user-authored minimal handoff grammar

The structured ledger is an internal sidecar, not the visible Word body. In the editor-facing DOCX, encode defaults through formatting and adjacency and write only execution-relevant exceptions.

```text
//자막
Q. 반도체 시장, 공급 부족일까 공급 과잉일까?
[exact governed speech run in blue; black resumes at OUT]

//12. (어드밴싱 AI)_AMD_(~4분 1초~)_그래프 나오는 부분
[exact governed speech run in blue]
```

Rules confirmed from the 2026-07-23 user-authored `강정수 2편 자료-완료` corpus:

- Keep `//자막` as a standalone yellow marker; put exact screen text in the next yellow paragraph(s).
- Keep a material call normally to one line: `//NN. (subject/file)_source_(source time)_shot note`.
- Omit `ID`, function code, render mode, `YES_EXACT`, `REQUIRED/OPTIONAL`, search status, fact state, rights state, explicit IN/OUT, and default speech-caption state from the visible Word body. Retain them in the internal ledger.
- Adjacency gives IN; the blue run range gives duration/OUT; black resumption ends the object.
- `//자막` and readable article/report/chart already imply spoken-caption suppression. State speech behavior only for a genuine exception.
- Use terse natural-language exceptions only: `말자막 위에 로고 작게`, `재탕`, `아무 장면`, `영상 끝?`, arrow/label placement.
- A `자료-완료` document points to already selected/delivered material. Search terms and source-family recommendations belong to a pre-completion research brief, not the final handoff.
- Repeating `//NN` is valid reuse of one selected source asset at different source times.
- If prose cannot communicate the intended frame efficiently, embed a visual reference and let the editor recreate it.

The expanded schema below is for internal ledgers, audits, unresolved cases, or explicit user requests—not the default visible DOCX grammar.

Suggested expanded instruction:

```text
//12. [USE=12-03] [기능=PROVE] [형식=영상]
[필요도=REQUIRED] [시작=“실제로”] [종료=다음 수치 설명 전]
[자료상태=PD_SELECTED] [팩트=VERIFIED] [권리=CLEARED]

야간 데이터센터 서버실에서 작업자가 랙 사이를 점검하는 장면...

//자막 [ID=CAP-027] [기능=C3-NUM] [렌더=R3] [등장=D0]
[말자막=SUPPRESS] [문구고정=YES_EXACT] [위치=상단]
전력 수요 1GW

//동시표시
자료 + 수치자막 + 출처
//말자막: 해당 파란 싱크 동안 숨김
```

Keep a structured internal ledger even when the user-facing DOCX uses natural language. Use `templates/screen-composition-record.yaml` and `templates/inline-docx-instruction-example.md`.

Completion criterion: the editor can determine what appears, when it appears, what text is exact, what can be selected freely, and what must never appear on screen.

## Residual ambiguity opposition review

Use this after the integrated caption/material pass when the user asks for a final 반대검토 of implementation uncertainty. This is not another taxonomy review; it asks only what an editor still cannot execute deterministically.

Inspect, in priority order:

1. two editorial captions attached to one sync where `D0` simultaneous, `D2` build, or `D3` replacement would produce materially different screens
2. explicit notes that a material continues after an editorial caption ends, especially whether spoken captions resume immediately or remain suppressed until the material exits
3. screen text that looks like a caption but lacks `//자막`, especially graphic labels, object callouts, and identity/source text whose speech-caption behavior may differ
4. direct quote plus PD summary in the same beat: determine whether one replaces the other, both coexist, or one is only an internal guide
5. one blue sync carrying multiple production objects whose stacking order or safe zones are not encoded

Question discipline:

- Ask at most 7 questions, highest editorial risk first.
- Each item must be one exact, answerable sentence anchored to the actual screen text, asset ID, or instruction note.
- Do not ask about conventions already settled by corpus grammar: multi-line text is `D0` by default; explicit `//자막` and readable article/report/chart layers suppress speech for their blue sync; ordinary non-readable footage/photo and unmarked object labels keep speech by default; known editor-discretion transitions remain editor discretion.
- Do not ask abstract taxonomy questions when only a temporal or stacking decision is missing.
- If the authoritative production-instruction artifact is unavailable and only a clean cut DOCX or extracted observation remains, label the review as partial and do not claim that all caption blocks were inspected.
- A short result with one genuine question is better than padding the list with obvious or already-resolved items.

Completion criterion: every returned question changes an actual editor action, and no returned question merely reconfirms an established default.

## Three independent reviews

### Under-visualized review

Find abstract mechanisms, comparisons, numbers, history, products, places, or processes that remain hard to understand with one-man speech alone.

### Over-decoration review

Find generic B-roll, repeated official montages, visual clichés, needless logos, and captions that merely duplicate speech or visible article/graphic text.

### Composition and evidence review

Audit every segment for:

- layer and safe-area collision
- more than two primary reading tasks
- timing too short to read
- material contradicting the country, time, company, product, or scale of the claim
- PD summary misrepresented as direct quote
- source and rights conflation
- asset-number collision
- red notes or `@@` leaking into final screen text
- unnecessary redefinition, repeated conclusions, stale comparison axes, and inappropriate reuse across neighboring or distant beats; use the concept ledger only for concepts that actually recur

Completion criterion: all three reviews inspect the current final ledger, including sequence continuity, and every finding is resolved or explicitly blocked.

## Output contract

Choose the primary filename from actual production state:

- `*_자료설계.docx` or `*_자료요청.docx`: candidates/search/briefs exist, but one or more assets are not selected and delivered.
- `*_자료-완료.docx`: every numbered call identifies a selected/delivered asset and the body uses the minimal user-authored grammar.

A final `자료-완료` DOCX contains:

- black/default base transcript
- yellow/cyan minimal production objects
- blue/cyan exact governed speech runs, with black resumption as OUT
- standalone `//자막` plus exact screen text in following yellow paragraph(s)
- normally one-line `//NN. (subject/file)_source_(source time)_shot` calls
- only local red exceptions that change the edit

Internal artifacts:

- structured screen-composition ledger
- detailed footage/search briefs for unresolved or audited assets
- caption/material/source/fact/rights inventories
- unresolved blocker list
- source and output hashes

Do not attach or print internal logs, search terms, status codes, function codes, rights reasoning, repeated default speech states, or long IN/OUT anchors in the final Word body unless the user explicitly requests an audit edition. Never overwrite the approved cut DOCX or source transcript.

## Common pitfalls

1. **Two-list failure:** caption and material lists exist, but no segment says how they coexist.
2. **Noun-only footage brief:** `AI 자료`, `공장 영상`, `관련 기사` gives no selectable scene.
3. **Caption taxonomy by appearance:** visually bold text is mislabeled as emphasis even though it functions as fact or quote.
4. **Every question gets Q:** pacing becomes repetitive and the question layer loses meaning.
5. **Quote laundering:** a PD summary is placed in quotation marks.
6. **Decorative B-roll:** footage has no role beyond hiding one-man shots.
7. **Three-reading-task overload:** speech, explainer, and chart all demand attention simultaneously.
8. **Line-break animation:** multiple approved lines are shown sequentially without instruction.
9. **Source equals permission:** an official or credited source is assumed legally usable.
10. **Asset-ID collision:** a repeated number silently points to a different file or source.
11. **Reference becomes final:** generated/reference images are broadcast without reconstruction approval.
12. **Internal note leak:** red notes or `@@` appear on screen.
13. **Premature universality:** one corpus-specific joke, position, or visual habit becomes a house rule.
14. **Marker-only parsing:** placement is guessed from filenames or `//NN` text while yellow-highlight/blue-sync adjacency is ignored.
15. **Over-meeting obvious B-roll:** trivial stock or directly matching inserts receive symbolic over-analysis instead of being auto-resolved.
16. **User-known placement question:** the user is asked where an asset goes even though the formatting-bearing DOCX already encodes the sync.
17. **Marker-only spoken-caption switch:** `no //자막` is treated as automatic `KEEP` even though a readable article, report, or chart is already the primary caption-like reading object.
18. **Article flattening:** an article is assumed to be full-screen or sequential when the intended composition may be background person/event footage plus a readable lower article card, or a simultaneous multi-article evidence array.
19. **Ledger leakage:** internal `ID/function/render/status/search/fact/rights/IN-OUT` fields are printed into the editor-facing Word body.
20. **All-blue transcript:** the entire surviving transcript is recolored blue, destroying the user's run-level sync grammar.
21. **False completion label:** recommendation/search briefs are numbered and delivered as `자료-완료` before actual assets are selected and delivered.
22. **Caption-as-graphic-title bias:** most captions merely label nearby materials, leaving strong speech reactions, reversals, definitions, formulas, and conclusions uncaptured.
23. **Uniform two-line bias:** every caption is forced into the same two-line headline structure instead of allowing terse punches and approved longer explainer cards.
24. **Management-interview diagram bias:** abstract business speech automatically becomes arrows, stages, matrices, or framework cards even when the speaker and one vivid caption are stronger.
25. **Report-tone rewrite:** conversational reversals, confessions, and analogies are replaced by accurate but lifeless nouns such as `사업 중심 이동`, `방향 전환`, or `전략 프레임워크`.
26. **Identity skipped for thesis:** profiles, unfamiliar-company logos, and short company/service explainers are omitted while a large abstract opening thesis is added.
27. **Cautious opinion hardened:** a speaker's observation, possibility, or personal judgment becomes an assertive program-level caption.
28. **Comment boilerplate flood:** every Word comment repeats exact-sync and designer-discretion boilerplate instead of briefly explaining the local selection reason and any risky fact scope.

## Verification checklist

### Visible editor-facing DOCX

Apply the current review-mode checks above for a comment review. The inline color/marker checks below apply only to an inline execution handoff.

- [ ] The filename is `자료-완료` only if numbered assets are actually selected/delivered
- [ ] Base transcript remains black/default; only exact governed speech runs are blue/cyan
- [ ] Black resumption correctly marks each production object's OUT
- [ ] `//자막` is standalone and exact screen text follows in separate yellow paragraph(s)
- [ ] Numbered material calls normally fit one line and identify the selected asset/source/source-time/shot
- [ ] No visible `ID`, function/render/status code, `YES_EXACT`, search query, rights state, repeated default speech state, or long IN/OUT anchor remains
- [ ] Reused source assets repeat the same `//NN`
- [ ] Captions were selected independently from speech beats, not used only as material/graphic titles
- [ ] For organization/management interviews, one-man continuity and conversational captions remain the default rather than automatic diagrams
- [ ] Profiles, unfamiliar-company identification, and service explainers appear where they reduce early comprehension cost
- [ ] Graphics are limited to relationships, order, comparisons, denominators, or cross-paragraph methods that speech and captions cannot keep clear
- [ ] Cautious observations remain attributed to the speaker and are not hardened into program-level facts
- [ ] If Word rationale comments were requested, each production object has one short local reason and only risky claims add fact-scope detail
- [ ] Red notes are short, local, and change an editor action
- [ ] Long research/fact/rights reasoning remains in the internal ledger
- [ ] The final DOCX was rendered and visually checked for scan speed, not merely validated as a ZIP

### Internal production ledger

- [ ] Approved source and final cut are frozen
- [ ] Every instruction has a speech/time anchor and editorial goal
- [ ] Every material call passes REQUIRED/OPTIONAL/NONE visual need gate
- [ ] Every editorial caption has one primary C function, R render form, D timing mode, and exact screen text
- [ ] Question captions are selective
- [ ] Direct quotes match source text and speaker
- [ ] Numbers include unit, date/basis, subject, and source
- [ ] Materials separate source, form, implementation, story function, status, and rights
- [ ] Every footage brief contains subject, observable action, setting, include, and exclude
- [ ] Every material placement has a selection owner and duration/entry/exit
- [ ] Same asset ID always identifies the same asset; reuse placements are unique
- [ ] Generated/reference visuals remain REFERENCE_ONLY/RECREATE_GRAPHIC unless approved
- [ ] Simultaneous layer plan is explicit for every composed segment
- [ ] Major reading tasks never exceed two
- [ ] Spoken-caption mode and safe-area behavior are explicit
- [ ] Spoken-caption mode was decided from the dominant readable object, not only the presence of a literal `//자막` marker
- [ ] Article layouts specify full-screen, lower card over background, or simultaneous/sequential multi-article treatment
- [ ] Multi-line text defaults to simultaneous display; animation exceptions are explicit
- [ ] Source, fact, and rights states are separate and final blockers are resolved
- [ ] Red internal notes and `@@` do not enter viewer-facing text
- [ ] Under-visualized, over-decoration, and composition/evidence reviews pass on the final ledger
- [ ] A management-interview pass confirms that captions preserve speech character and do not read like a strategy report
- [ ] The planner did not specify position, icon, color, detailed layout, or motion unless the choice changes meaning
- [ ] Editor-facing DOCX opens correctly and source hash remains unchanged
