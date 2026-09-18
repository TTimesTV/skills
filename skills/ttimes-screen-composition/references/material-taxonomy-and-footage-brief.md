# Material taxonomy and footage verbal-brief standard

Status: provisional v0.1.

## Visual need

```text
REQUIRED  needed to understand, prove, identify, compare, quantify, or show process
OPTIONAL  useful for rhythm or immersion
NONE      one-man continuity or speech is stronger
```

No material should exist merely because a related noun appears.

## Six-axis material model

```text
SOURCE × FORM × IMPLEMENTATION × STORY_FUNCTION × STATUS × RIGHTS
```

### Source family

- `COMPANY_OFFICIAL`
- `PERSON_OFFICIAL`
- `INSTITUTION_OFFICIAL`
- `NEWS_ORIGINAL`
- `WIRE_AGENCY`
- `ARTICLE_EDITORIAL`
- `MARKET_DATA`
- `STOCK_LIBRARY`
- `PUBLIC_ARCHIVE`
- `SOCIAL_UGC`
- `INTERNAL_OWNED`
- `REFERENCE_MIXED`
- `GENERATED_AI`
- `UNKNOWN_SOURCE`

YouTube is a platform, not a source family. Record the actual company, institution, person, news agency, or uploader origin.

## Practical big-tech insert sourcing heuristic

For generic illustrative footage, the PD may choose a famous big-tech company's official channel simply because it offers abundant, clean, well-shot material. Google, NVIDIA, Tesla, and similar firms are often efficient footage sources.

Interpretation rule:

```text
famous company + clean official footage
= practical sourcing shortcut by default
≠ proof that the company is the story's representative, winner, causal driver, or strategic through-line
```

Classify such use primarily as `ILLUSTRATE` unless the surrounding instruction explicitly adds `PROVE`, `IDENTIFY`, `BRAND_RECOGNITION`, or another function. Do not invent brand symbolism or continuity with later assets from source identity alone.

The source company does not have to manufacture the depicted object. A CATL ESS-project video may contain a clean solar-panel passage that the PD borrows as a solar insert. Record `source_origin=CATL project footage` and `depicted_subject=solar panels` separately; never convert this into `CATL manufactures solar cells` without evidence. Project videos from familiar companies with well-maintained YouTube channels can be practical substitute footage when specialist company names and channels are hard to navigate.

### Original form

- `MOTION_CLIP`
- `STILL_PHOTO`
- `ARTICLE_CAPTURE`
- `SCREEN_RECORDING`
- `DOCUMENT_CAPTURE`
- `PROFILE_ASSET`
- `DIAGRAM_REFERENCE`
- `CHART_REFERENCE`
- `MAP_REFERENCE`
- `LOGO_MARK`
- `PRODUCT_RENDER`
- `GENERATED_VISUAL`
- `TEXT_QUOTE_CARD`
- `COMPOSITE_REFERENCE`

This is the received material's form, not the final screen form.

### Implementation

- `DIRECT_INSERT`
- `SELECT_EXCERPT`
- `FREEZE_FRAME`
- `CROP_REFIT`
- `SCREEN_CAPTURE`
- `RECREATE_GRAPHIC`
- `TRACE_DATA_REDRAW`
- `COMPOSITE`
- `BACKGROUND_PLATE`
- `GENERATE_FINAL`
- `REFERENCE_ONLY`
- `REPLACE_EQUIVALENT`
- `ONE_MAN_CONTINUITY`
- `EDITOR_DISCRETION`

Generated images and embedded diagrams default to `REFERENCE_ONLY + RECREATE_GRAPHIC`.

### Story function

Primary one required, optional secondary functions:

- `ILLUSTRATE`
- `PROVE`
- `IDENTIFY`
- `EXPLAIN`
- `COMPARE`
- `QUANTIFY`
- `PROCESS`
- `PLACE_ESTABLISH`
- `PERSON_ESTABLISH`
- `TIME_ESTABLISH`
- `EDIT_COVER`
- `RHYTHM_RESET`
- `MOOD`
- `QUOTE_EVIDENCE`
- `TRANSITION`
- `BRAND_RECOGNITION`

When footage covers an edit, prefer a meaningful primary function plus secondary `EDIT_COVER`.

### Progress/status

- `RECOMMENDED`
- `SEARCH_REQUESTED`
- `CANDIDATE_FOUND`
- `PD_SELECTED`
- `DELIVERED`
- `EDITOR_CONFIRMED`
- `APPROVED`
- `REJECTED`
- `BLOCKED`
- `REPLACEMENT_NEEDED`

Selection mode is separate:

- `EXACT`
- `PD_SELECT`
- `EDITOR_SELECT`
- `EQUIVALENT_OK`
- `ANY_USABLE`
- `REUSE`
- `NONE`

`아무 장면`, `대충 인서트`, and `재탕` can be completed instructions when selection mode and minimum include/exclude conditions are explicit.

### Rights

- `RIGHTS_UNKNOWN`
- `INTERNAL_OWNED`
- `PUBLIC_DOMAIN_VERIFIED`
- `LICENSED_STOCK`
- `OFFICIAL_SOURCE_REVIEW`
- `EDITORIAL_USE_ONLY`
- `PERMISSION_REQUIRED`
- `ATTRIBUTION_REQUIRED`
- `PLATFORM_TERMS_REVIEW`
- `GENERATED_TERMS_REVIEW`
- `DO_NOT_BROADCAST`
- `CLEARED`
- `EXPIRED_OR_RESTRICTED`

Never infer rights from attribution or official origin.

## Footage verbal brief

### Natural-language grammar

```text
[subject] does [observable action] in [setting].
[shot/viewpoint], [camera movement], [time feel], [tone].
Include: [required visible elements].
Exclude: [misleading/clichéd/wrong elements].
Duration: [length or complete action].
Connection: [entry and exit anchors].
Safe area: [space for speech/editorial text].
Source/search/selection: [likely family, terms, final chooser].
```

Required minimum:

1. subject
2. observable action
3. setting/situation
4. include
5. exclude

A noun is not an action. Translate `AI 업무` to an employee entering a document, reviewing output against the source, and correcting it. Translate `배터리 산업` to cells being assembled or inspected on an automated line.

### Shot vocabulary

- `ESTABLISHING`
- `WIDE`
- `MEDIUM`
- `CLOSE_UP`
- `EXTREME_CLOSE_UP`
- `OVER_SHOULDER`
- `POV`
- `TOP_SHOT`
- `DETAIL`
- `SEQUENCE`

Specify only when it changes meaning or caption space. Do not demand an unrealistically exact shot.

### Camera and time feel

Camera examples: fixed, slow push-in, pan, tracking, handheld, gimbal, drone, macro focus, screen recording, unrestricted.

Time-feel examples: real-time, busy work rhythm, slow observation, time lapse, repeat action, start-to-finish process, archive, live-news immediacy.

Do not confuse the scene's rhythm with an instruction to speed-ramp it.

### Tone

Use concrete constraints:

```text
미래적이되 홀로그램·푸른 네온으로 AI를 표현한 클리셰 제외
공식 홍보 영상이어도 과도한 슬로모션·제품 광고식 광택 제외
```

### Include

State what viewers must read:

- actual product or object
- hands/action
- environmental scale
- face/identity
- date/document title
- start and outcome of a process
- user reviewing output rather than passively watching

### Exclude

Prevent wrong selection:

- competitor logos
- country/year mismatch
- generic handshake, thumbs-up, money-counting, typing
- holograms, unrelated robots, crypto tickers
- watermarks and low-resolution reuploads
- unsafe actions or personal information
- footage from the wrong product/process

### Duration and connection

Examples:

- `2~3초 단독`
- `4~6초, 한 동작이 끝날 때까지`
- `총 8초, 2~3개 숏 가능`
- `점프컷을 덮는 최소 길이`
- `수치를 읽도록 최소 3초 유지`

Tie entry and exit to words or story changes:

```text
“실제로”에서 증거 화면 진입
와이드 장소설정 → 제품 detail
기사 헤드라인 → 근거 문장 → redrawn chart
동작 완료에 원맨 복귀
```

### Safe area

Examples:

- lower 25% clear for speech captions
- person left, explainer space right
- article headline top remains uncovered
- subject inside central 60% for crop
- avoid footage whose UI occupies the speech-caption zone

## Material ID and reuse

`asset_id` identifies a source asset. `placement_id` identifies each use.

```text
M007-P01
M007-P02
M007-P03
```

Existing DOCX may repeat `//07.`. This is valid when all occurrences refer to the same file/article/chart source.

Reuse the asset ID for:

- another timecode from the same video
- headline and body from the same article
- another crop of the same still
- full chart then close-up of the same chart

Create a new asset ID for:

- a different episode/file/source/date
- another article or agency
- a separately recalculated graphic
- a materially different generated image
- an asset needing separate rights tracing

Technical crops can be `M012-A/B/C`; a new interpretation or recalculated graphic gets a new primary ID.

## Handoff fields

Required:

```text
placement_id
asset_id
script_anchor
material_need
primary_function
source_family
form
implementation
verbal_brief
include/exclude
duration
selection_mode
status
rights
```

Recommended for video:

```text
subject/action/setting
shot/camera/temporal_feel/tone
entry/exit/connection/safe_area
search_terms_ko/search_terms_en
alternatives/reuse_note
```

After selection:

```text
source_owner/title/date/url
delivered_filename/source_timecode
resolution/orientation
credit_text/rights_note
pd_decision/editor_note
```

## Quality gate

- visual need is explicit
- material has one primary story function
- footage brief contains subject/action/setting/include/exclude
- duration, entry, exit, and safe area exist
- wrong footage can be rejected from the brief alone
- selection owner is explicit
- reuse points to the same asset
- source, fact relevance, and rights are separately verified
