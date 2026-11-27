---
name: ttimes-youtube-upload-package
description: "Prepare TTimes upload packages and guide draft-only registration in YouTube Studio, Naver Blog, and TTimes CMS. Preserve supplied copy, derive chapters from YouTube CC, and verify unlisted or unpublished status."
metadata:
  version: 1.7.1
---

# TTimes YouTube Upload Package

## Trigger and deliverable

Use when the user asks for `업로드 작업`, `유튜브 업로드 세트`, asks for hashtags and a pinned comment together with timestamps, or supplies a labeled publishing bundle plus a YouTube URL.

For a request to register drafts or explain the full process, read the [draft-only publishing workflow](references/publishing-workflow.md). Follow **YouTube Studio → Naver Blog → TTimes CMS**. Use the [Studio checklist](references/studio-setup.md) for Studio fields and end screens.

Use **일부 공개** for YouTube, **미발행 임시저장** for Naver Blog, and **미표출 `0` / 임시저장** with external delivery set to **설정안함** for CMS. `업로드`, `등록`, and `올려줘` authorize only these draft states when actual registration is requested. Confirm the target and draft state before saving, reopen and verify the saved state before continuing, and stop the affected write if either cannot be confirmed. Publication, scheduling, and external delivery require separate explicit authorization. A copy-only request authorizes preparation. Leave comments out of the default registration and package. Prepare a pinned-comment block only on explicit request.

Read the [current copy format and production-credit source](references/user-approved-two-block-contract-20261014.md). Use `references/pinned-comment-templates.md` for exact ad copy when requested. `references/user-approved-output-contract-20260715.md` records historical formatting.

### Default: title first, then three numbered copy-ready blocks

At the very top, return `유튜브 제목` in its own `text` block, preserving the user's supplied YouTube title. Then return the three numbered blocks below. If the title is absent, identify that missing input without generating a new title unless requested.

1. `유튜브 설명란`: user-supplied introduction verbatim → credits in the order 편집 / 촬영 / 자료 / 진행 / 섬네일 → fixed website and business-contact lines → approximately three relevant `#hashtags` → chapters.
2. `해시태그 — 유튜브 태그 입력란용`: exactly ten unique, source-supported tags on one line, comma plus space separated, without `#`. Keep the three `#hashtags` inside description and CMS as well.
3. `CMS 미발행 초안 등록용`: copy-ready registration instructions/data for the user's connected CMS workflow. Include supplied article title and body, exactly three hashtags matching the YouTube description, final YouTube URL, list-image status, `표출 설정: 0`, deduplicated internal production contributors with established role titles, five credits, and reference landing URL/title/date. Do not include a separate video ID or embed HTML; embedding is handled by the connected CMS workflow. Follow the exact CMS format in the current contract reference. This clipboard is preparation, not authorization to submit to CMS.

If the user explicitly requests pinned-comment copy, add it after the description and renumber so CMS stays last. Use the exact approved copy for the ad actually present, if any → separator only with an ad → topic header → identical chapters → fixed thank-you lines.

Do not draft an introduction merely from the URL, transcript, thumbnail or title. The user supplies the introduction. If absent, continue chapter/credit work and mark the missing introduction for a draft handoff; do not present a placeholder as publish-ready.

Resolve credits from the shared Google Sheet `월별 일정표`, matching the episode across shooting, editing, materials and thumbnail dates. This source was initially called a calendar by the user, but the verified source is a spreadsheet. Follow the current contract reference for the verified URL and role evidence; ambiguous assignments remain unconfirmed.

When assembling production credits and CMS internal authors, apply [approved names and titles](references/credit-name-titles.md). Preserve full labels such as `박영선 전 장관`, `이중학 동국대 교수`, and `김지현 테크라이터`; confirm the episode assignment separately rather than treating this reference as a presenter roster.

The supplied YouTube title and ten upload tags now have standalone blocks by default. Do not add standalone article or timestamp blocks unless requested. Use supplied article metadata inside the final CMS block without rewriting it. A user request for chapters only still narrows delivery to one chapter block.

### Legacy URL-only split output — only when explicitly requested

Return the applicable copy-ready sections in this order:

1. `해시태그` — one plain-text code block with at least 10 comma-separated upload tags, without `#` prefixes
2. `본문 업로드용 타임스탬프` — one plain-text code block containing only the chapter list
3. `고정 댓글 (댓글용 타임스탬프 포함)` — one plain-text code block containing inferred front-ad copy when present, chapter list, and fixed thank-you lines

Include the final pinned-comment section when explicitly requested.

#### Mid-task scope narrowing

If the user follows a URL-only upload request with `타임스탬프만`, `챕터만`, or equivalent:

- stop hashtag, ad-copy, and pinned-comment assembly immediately
- keep the CC-derived semantic boundary work already completed
- return only one copy-ready timestamp code block
- do not explain the abandoned package workflow or make the user wait for files they no longer requested
- still run timestamp validation before delivery

#### Preserve an explicit request for comment copy

A request to hurry the timestamp work (`빨리 줘`, `앞에 것만 하라고`, `컷편 기준으로 해`) changes the timing method. If the user also explicitly requested comment copy, return it with the matching description once the chapters validate. A later request for chapters only narrows the output to chapters.

### Legacy labeled publishing split — only when explicitly requested

When the user supplies fields such as:

- `썸네일/리스트 제목>`
- `<유튜브 제목>`
- `<기사 제목>`
- `<네이버 다음 제목>`
- `<유튜브 설명/기사/페북>`
- `<랜딩>`
- YouTube URL

ignore `썸네일/리스트 제목` by default and return these copy-ready sections in order:

1. `유튜브 제목` — preserve the supplied `<유튜브 제목>` exactly
2. `기사 제목` — preserve the supplied `<기사 제목>` exactly
3. `기사 내용` — preserve the supplied `<유튜브 설명/기사/페북>` exactly
4. `해시태그` — comma-separated, at least 10
5. `본문 업로드용 타임스탬프` — a separate code block containing only the chapter list
6. `고정 댓글 (댓글용 타임스탬프 포함)` — only when requested; ad template when present, chapters, thank-you lines

Preserve the supplied titles and body. In this legacy split, return standalone `<네이버 다음 제목>` and `<랜딩>` blocks only when explicitly requested.

### Cross-workflow isolation

Card-news and upload metadata are separate authorities. A carousel cover title, LinkedIn storyline, body copy, or closing quote from `ttimes-cardnews-imagegen` must never replace supplied `<유튜브 제목>`, `<기사 제목>`, `<네이버 다음 제목>`, `<유튜브 설명/기사/페북>`, or `<랜딩>`. When a final video URL arrives, reuse the saved publishing bundle verbatim and change only derived upload fields such as shifted timestamps, hashtags when requested, and the timestamp-bearing pinned comment. Reuse card-news copy only when the user explicitly supplies it again as an upload metadata field.

The timestamp list appears in the full description. If requested, use the same list in the pinned-comment copy. Keep CMS registration data in the last default block.

### Metadata-set-first handoff

If the user says `일단 세트부터 나눠줘`, `문안 세트부터`, or equivalent before timestamp work is complete:

- immediately split the supplied publishing metadata into separate copy-ready blocks
- in this explicit split-first mode, include **all supplied fields**, including `썸네일/리스트 제목`, `네이버·다음 제목`, and the current/final video URL; do not apply the default omission rule
- Preserve supplied editorial meaning, titles, and body structure.
- Before final delivery, correct unmistakable mechanical typos or duplicated syllables in supplied copy (for example `달라야져야` → `달라져야`). Do not knowingly ship a typo merely because the source bundle contained it.
- Do not make stylistic rewrites, factual substitutions, or meaning changes without user approval.
- do not hold the metadata blocks until hashtags, timestamps, or pinned-comment assembly finishes
- leave unfinished hashtags/timestamps/comment work out of that response unless the user asks for it

### Final-link fast handoff

If the user has already supplied the labeled publishing bundle and the first-cut chapters were precomputed, a later message containing the final YouTube URL means **assemble and return the upload package now**.

- Reuse the supplied title/body verbatim and the saved tag/front-ad contract.
- Invoke the timestamp skill's prefix-shift fast path; do not restart semantic chapter research.
- If the producer explicitly says `컷편 기준으로 타임스탬프를 매기고 앞에 것만 더해`, apply the timestamp skill's producer-declared prefix-only override: use first-cut CC chapters plus the detected final prefix, and do not block on full-final ASR or duration-delta investigation.
- Once the applicable prefix-shift gate and validation pass, return the default publication blocks (or the explicitly requested fields). A missing CMS-only input does not delay the completed YouTube blocks; clearly identify the incomplete CMS field.
- Do not interleave long diagnostic narration, repeated progress reports, dependency experiments, or requests for information already provided.
- If a verification issue does not affect whole-second chapters or copy content, record it internally rather than delaying delivery.
- Escalate only a genuine body mismatch, unidentified ad timing, missing requested content, or failed validation.

## Required timestamp workflow

Load and follow the `ttimes-youtube-timestamps` skill first.

- Use YouTube-provided CC: manual `ko` first, then automatic `ko-orig`.
- Select semantic boundaries, not equal intervals.
- Snap to exact CC cue starts.
- Validate first `00:00`, ascending order, 3+ chapters, and 10-second minimum.

## Step 1: infer the front-ad state from the first 90 seconds

Read the first 90 seconds of YouTube CC and classify one of these states.

For **detection only**, normalize obvious CC/ASR variants and timing debris before matching. Examples include `AI 전함`↔`AI 전환`, `진호`↔`진화`, `T타임즈`↔`티타임즈`, duplicated second labels such as `0:1111초`, and spacing variants. This normalization must never alter the user-approved pinned-comment template: copy the approved wording, line breaks, contact details, and URL exactly from `references/pinned-comment-templates.md`.

### Front ad 1 — Snowflake World Tour Seoul 2026 recap live seminar

This is the producer-designated `앞광고 1`. The user confirmed the campaign ended on **2026-10-02 KST**. It is no longer a default active campaign. Preserve its historical template; use it only when an actual old video or a direct producer statement confirms this ad.

Signals include several of:

- `데이터는 다 모아뒀는데, 왜 AI가 못 찾죠?`
- `AI 에이전트가 당장 쓸 수 있는 데이터는 다릅니다`
- `총 19시간 30여 개 세션`
- `90분으로 압축`
- `스노우플레이크 월드투어 서울 2026`
- `리캡 라이브 세미나`

Use the exact template in `references/pinned-comment-templates.md` under `Front ad 1 — Snowflake World Tour Seoul 2026 recap live seminar`.

The approved opening chapter is:

```text
00:00 스노우플레이크 리캡 라이브 세미나
```

### Front ad 2 — 2027 IT trend course

This is the producer-designated `앞광고 2`.

Signals include several of:

- `2027년 AI 에이전트가 모든 것을 집어삼킨다`
- `AI 에이전트가 바꿀 2027년 완벽 가이드`
- `내년 사업 전략 수립`
- `AI 10대 아젠다`
- `김지현 테크라이터`
- `에이전트는 2027년 어디까지 가능할까?`

Use the exact template in `references/pinned-comment-templates.md` under `Front ad 2 — 2027 IT trend course`.

The approved opening chapter is:

```text
00:00 2027 IT 트렌드 강좌
```

### A. AI leverage course

Signals include several of:

- `단순한 리서치와 보고서 초안`
- `AI 레버리지 전략`
- `업무의 임팩트`
- `의사결정의 밀도`
- `입체적 보고서`
- `전략 옵션`
- `초격차 제안서`

Use the exact template in `references/pinned-comment-templates.md` under `AI leverage course`.

The opening chapter is normally:

```text
00:00 20강으로 완성하는 실습형 AI 레버리지 강좌 소개
```

Use the exact existing description line when available.

### B. Excel automation course

Signals include several of:

- `엑셀 자동화`
- `파일 합치기`
- `시트 통합`
- `피벗`
- `차트 자동 생성`
- `폴더 구조 생성`
- `데이터 시각화`

Use the exact template in `references/pinned-comment-templates.md` under `Excel automation course`.

The opening chapter is normally:

```text
00:00 엑셀 자동화 강좌 오픈
```

Use the exact existing description line when available.

### C. 2027 AX strategy conference

Signals include several of:

- `AX 패러다임이 바뀌고 있습니다`
- `AI로 얼마나 가치를 창출`
- `성과를 어떻게 측정`
- `ROI 제고`
- `2027 AX 전략 컨퍼런스`
- `새롭게 제기되는 AX 과제`
- `자세한 사항은 댓글을 참조`

Use the exact template in `references/pinned-comment-templates.md` under `2027 AX strategy conference`.

The opening chapter is:

```text
00:00 2027 AX 전략 컨퍼런스
```

### D. PA | AI Connect 2026 conference

Recognize `사람만 관리하던 HR은 끝났다`, people analytics, HR/agent leadership, and Offpiste/ACG/TTimes joint-host signals. Automatic CC may misrecognize `2026` as `2016`; the approved campaign is PA | AI Connect 2026. Use the exact user-supplied template under that name in `references/pinned-comment-templates.md`, including its full tracked application URL. Opening chapter: `00:00 PA | AI Connect 2026 컨퍼런스`. Do not assign a numbered ad designation the user has not supplied.

### E. No front ad

If the final upload begins with highlight or the main program and contains no course ad, omit:

- all course-ad copy
- the `=================================` separator

When requested, the pinned comment starts directly with:

```text
📌오늘의 주제 모아보기📌
```

Do not invent a course ad because similar recent videos had one.

### Unknown front ad

If CC clearly contains another ad but it does not match a saved template:

- identify the advertised product/course from CC
- search the current/past TTimes description or source supplied by the user for exact approved copy and URL
- do not invent price, phone, email, purchase URL, benefits, or promotional claims
- request the approved promotional text only if the user asked for comment copy and the text is unavailable. If the ad identity is clear, finish the description chapters independently.

## Step 2: three description hashtags and ten upload tags

In default mode, put three relevant `#hashtags` on one space-separated line inside the description and reuse those same three in the CMS block. Also provide exactly ten comma-separated, no-`#` tags in the upload-tag block. Preserve user-approved hashtags for the same episode when available.

Create exactly ten unique upload tags by default. A different count requires a user request.

Composition:

- 2–4 broad topics: `AI`, `인공지능`, `반도체`
- 4–8 specific entities/technologies from title and CC
- 1–3 people/company names when central
- channel tags: `티타임즈`, `티타임즈TV`

Rules:

- The user calls this section `해시태그`, but the copy-ready values must **not contain the `#` character**.
- Put all tags in one copy-ready code block.
- Separate every tag with a comma and one space: `AI, 인공지능, AX`.
- Do not use space-only separation; the upload field can merge or misread it as one entry.
- Use one line unless it becomes unreadably long; two lines are acceptable.
- Remove internal spaces when the tag is conventionally one token.
- Correct CC misspellings before using names.
- Do not include people/companies mentioned only incidentally.
- Avoid duplicates, unsupported trend tags, and vague spam tags such as `추천`, `대박`, `필수시청`.
- The front-ad course does not need to dominate tags unless the video itself is about that course.

**User correction:** Never answer with `#AI, #인공지능`. The approved shape is `AI, 인공지능`.

## Optional: assemble pinned-comment copy on request

### With a recognized front ad

```text
[exact approved ad template]

=================================

📌오늘의 주제 모아보기📌

[description-ready timestamp list]

시청해 주셔서 감사합니다😍
좋아요와 구독은 큰 힘이 됩니다😘
```

### Without a front ad

```text
📌오늘의 주제 모아보기📌

[description-ready timestamp list]

시청해 주셔서 감사합니다😍
좋아요와 구독은 큰 힘이 됩니다😘
```

Formatting rules:

- Preserve approved ad line breaks, punctuation, emoji, phone, email, and purchase URL exactly.
- Separator is exactly `=================================`.
- Keep one blank line before and after the separator.
- Keep one blank line after the topic header and before the thank-you lines.
- Do not add analysis, evidence notes, CC caveats, or file paths inside the copy block.

## Output shape — default

Return four fenced `text` blocks in this order: `유튜브 제목` at the top, then `1. 유튜브 설명란`, `2. 해시태그 — 유튜브 태그 입력란용`, `3. CMS 미발행 초안 등록용`. Labels, evidence, uncertainty and file links stay outside the copy blocks, except clearly marked missing fields in an incomplete draft. Respect an explicitly narrower request.

### Explicit legacy split output

For URL-only mode, return the applicable labeled sections in this order:

1. `해시태그`
2. `본문 업로드용 타임스탬프`
3. `고정 댓글 — 댓글용 타임스탬프 포함`, only when requested

For labeled-bundle mode, return supplied metadata fields first, then hashtags and body timestamps. If requested, add pinned-comment copy last.

Every section must use one fenced `text` code block containing only copy-ready content. Do not make the user remove bullets, quote marks, Markdown bold markers, or explanatory text from inside the copy blocks.

## Validation

Save default drafts as `youtube_description.txt`, `final_timestamps.txt` and `hashtags.txt`. Validate the chapter list with the timestamp skill's verifier. Check user-supplied body preservation, credit evidence and actual ad state. When comment copy was requested, also save `pinned_comment.txt` and verify it uses exactly the same chapters as the description.

Run:

```bash
python3 SKILL_DIR/scripts/verify_upload_package.py --hashtags hashtags.txt
```

Add `--comment pinned_comment.txt` only when validating requested comment copy.

Quality gate:

- [ ] Default output has the supplied YouTube title first, followed by description, exactly ten upload tags, and the CMS draft
- [ ] Description introduction is user-supplied and preserved, not newly invented
- [ ] Production credits follow the current evidence and fixed field order
- [ ] CMS block preserves supplied article title/body, uses display setting 0, and does not claim registration or image validation without evidence
- [ ] Description includes fixed website/contact lines and about three `#hashtags`
- [ ] Upload-tag block has exactly ten unique tags separated by `, `, without `#`
- [ ] Legacy three/six-block splits are used only when explicitly requested
- [ ] If the user narrowed the request to `타임스탬프만/챕터만`, package assembly stopped and exactly one validated timestamp block was returned
- [ ] Default registration and package exclude comments. Requested comment copy has matching chapters, the approved ad copy and separator when applicable, the topic header, and the exact thank-you lines.
- [ ] Supplied YouTube title, article title, and article body are copied exactly
- [ ] Thumbnail/list title is ignored unless explicitly requested
- [ ] Correct ad state inferred from first 90 seconds
- [ ] Timestamp list passes YouTube chapter validation
- [ ] Every output block can be copied and pasted without editing
