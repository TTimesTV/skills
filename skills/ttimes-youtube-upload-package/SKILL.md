---
name: ttimes-youtube-upload-package
description: "Prepare TTimes publication packages and provide a manual YouTube Studio checklist, including playlists, end screens, recording date, metadata, monetization and multilingual tracks. Preserve supplied copy and derive chapters from YouTube CC."
metadata:
  version: 1.6.8
---

# TTimes YouTube Upload Package

## Trigger and deliverable

Use when the user asks for `업로드 작업`, `유튜브 업로드 세트`, asks for hashtags and a pinned comment together with timestamps, or supplies a labeled publishing bundle plus a YouTube URL.

Prepare copy and a [Studio checklist for the editor](references/studio-setup.md). The editor enters, saves, and verifies the settings in Studio using their own account.

The checklist specifies unlisted as the handoff state for a new video. The user handles publication. Keep the current visibility when documenting changes to an existing public video.

Read [current two-block contract](references/user-approved-two-block-contract-20261014.md) for the default deliverable and production-credit lookup. Use `references/pinned-comment-templates.md` for exact approved ad copy. `references/user-approved-output-contract-20260715.md` records historical formatting; its three/six-block defaults are superseded by the current contract.

### Default: title first, then four numbered copy-ready blocks

At the very top, return `유튜브 제목` in its own `text` block, preserving the user's supplied YouTube title. Then return the four numbered blocks below. If the title is absent, identify that missing input without generating a new title unless requested.

1. `유튜브 설명란`: user-supplied introduction verbatim → credits in the order 편집 / 촬영 / 자료 / 진행 / 섬네일 → fixed website and business-contact lines → approximately three relevant `#hashtags` → chapters.
2. `고정 댓글`: exact approved copy for the ad actually present, if any → separator only with an ad → topic header → identical chapters → fixed thank-you lines.
3. `해시태그 — 유튜브 태그 입력란용`: exactly ten unique, source-supported tags on one line, comma plus space separated, without `#`. This separate upload-tag block is now part of the default package; keep the three `#hashtags` inside description and CMS as well.
4. `CMS 미발행 초안 등록용`: copy-ready registration instructions/data for the user's connected CMS workflow. Include supplied article title and body, exactly three hashtags matching the YouTube description, final YouTube URL, list-image status, `표출 설정: 0`, deduplicated internal production contributors with established role titles, five credits, and reference landing URL/title/date. Do not include a separate video ID or embed HTML; embedding is handled by the connected CMS workflow. Follow the exact CMS format in the current contract reference. This clipboard is preparation, not authorization to submit to CMS.

Do not draft an introduction merely from the URL, transcript, thumbnail or title. The user supplies the introduction. If absent, continue chapter/credit work and mark the missing introduction for a draft handoff; do not present a placeholder as publish-ready.

Resolve credits from the shared Google Sheet `월별 일정표`, matching the episode across shooting, editing, materials and thumbnail dates. This source was initially called a calendar by the user, but the verified source is a spreadsheet. Follow the current contract reference for the verified URL and role evidence; ambiguous assignments remain unconfirmed.

When assembling production credits and CMS internal authors, apply [approved names and titles](references/credit-name-titles.md). Preserve full labels such as `박영선 전 장관`, `이중학 동국대 교수`, and `김지현 테크라이터`; confirm the episode assignment separately rather than treating this reference as a presenter roster.

The supplied YouTube title and ten upload tags now have standalone blocks by default. Do not add standalone article or timestamp blocks unless requested. Use supplied article metadata inside the final CMS block without rewriting it. A user request for chapters only still narrows delivery to one chapter block.

### Legacy URL-only split output — only when explicitly requested

Return three copy-ready sections in this fixed order:

1. `해시태그` — one plain-text code block with at least 10 comma-separated upload tags, without `#` prefixes
2. `본문 업로드용 타임스탬프` — one plain-text code block containing only the chapter list
3. `고정 댓글 (댓글용 타임스탬프 포함)` — one plain-text code block containing inferred front-ad copy when present, chapter list, and fixed thank-you lines

The pinned comment must always be the final section.

#### Mid-task scope narrowing

If the user follows a URL-only upload request with `타임스탬프만`, `챕터만`, or equivalent:

- stop hashtag, ad-copy, and pinned-comment assembly immediately
- keep the CC-derived semantic boundary work already completed
- return only one copy-ready timestamp code block
- do not explain the abandoned package workflow or make the user wait for files they no longer requested
- still run timestamp validation before delivery

#### Do not silently drop the pinned comment

A request to hurry the timestamp work (`빨리 줘`, `앞에 것만 하라고`, `컷편 기준으로 해`) changes the **timing method**, not the upload-package deliverable. When a labeled publishing bundle or upload-package request is active:

- return the full description and pinned-comment blocks together as soon as the available inputs validate; use separate timestamps only when explicitly requested
- keep the pinned comment last and use the exact recognized ad template
- omit the pinned comment only when the user explicitly says `타임스탬프만`, `챕터만`, or `댓글 제외`
- never make the user ask a second time with `댓글도 줘야죠`

If metadata and tags were already delivered in earlier partial responses, do not repeat them unless requested; finish the remaining pair atomically.

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
6. `고정 댓글 (댓글용 타임스탬프 포함)` — ad template when present, chapters, thank-you lines; always last

Do not rewrite supplied titles/body, silently substitute the thumbnail title, or merge the two timestamp deliverables unless the user asks. Ignore `<네이버 다음 제목>` and `<랜딩>` in the default output unless the user explicitly asks to output those fields.

### Cross-workflow isolation

Card-news and upload metadata are separate authorities. A carousel cover title, LinkedIn storyline, body copy, or closing quote from `ttimes-cardnews-imagegen` must never replace supplied `<유튜브 제목>`, `<기사 제목>`, `<네이버 다음 제목>`, `<유튜브 설명/기사/페북>`, or `<랜딩>`. When a final video URL arrives, reuse the saved publishing bundle verbatim and change only derived upload fields such as shifted timestamps, hashtags when requested, and the timestamp-bearing pinned comment. Reuse card-news copy only when the user explicitly supplies it again as an upload metadata field.

In default mode, the timestamp list appears in both the full description and pinned comment. The last block is CMS registration data, not a standalone timestamp list.

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
- Escalate only a genuine body mismatch, unknown ad template, missing publishing field, or failed validation.

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

The pinned comment starts directly with:

```text
📌오늘의 주제 모아보기📌
```

Do not invent a course ad because similar recent videos had one.

### Unknown front ad

If CC clearly contains another ad but it does not match a saved template:

- identify the advertised product/course from CC
- search the current/past TTimes description or source supplied by the user for exact approved copy and URL
- do not invent price, phone, email, purchase URL, benefits, or promotional claims
- if exact copy is unavailable, ask for the approved template

## Step 2: three description hashtags and ten upload tags

In default mode, put three relevant `#hashtags` on one space-separated line inside the description and reuse those same three in the CMS block. Also provide exactly ten comma-separated, no-`#` tags in the third numbered block for YouTube's tag field. Preserve user-approved hashtags for the same episode when available.

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

## Step 3: assemble the pinned comment

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

Return five fenced `text` blocks in this order: `유튜브 제목` at the top, then `1. 유튜브 설명란`, `2. 고정 댓글`, `3. 해시태그 — 유튜브 태그 입력란용`, `4. CMS 미발행 초안 등록용`. Each is destination text or instructions, not a conversational approval request. This supersedes older output-count and pinned-comment-last defaults. Labels, evidence, uncertainty and file links stay outside the copy blocks, except clearly marked missing fields in an incomplete draft. Respect an explicitly narrower request.

### Explicit legacy split output

For URL-only mode, return three labeled sections in this order:

1. `해시태그`
2. `본문 업로드용 타임스탬프`
3. `고정 댓글 — 댓글용 타임스탬프 포함`

For labeled-bundle mode, return supplied metadata fields first, then hashtags, body timestamps, and the pinned comment last.

Every section must use one fenced `text` code block containing only copy-ready content. Do not make the user remove bullets, quote marks, Markdown bold markers, or explanatory text from inside the copy blocks.

## Validation

Save default drafts as `youtube_description.txt`, `final_timestamps.txt` and `pinned_comment.txt`. Validate the chapter list with the timestamp skill's verifier, and verify that description/comment contain exactly the same chapters. Check user-supplied body preservation, credit evidence and actual ad state. Do not force description hashtags through the separate upload-tag validator or generate ten tags merely to satisfy it.

For the default ten comma-separated upload tags, save drafts as:

- `hashtags.txt`
- `pinned_comment.txt`

Run:

```bash
python3 SKILL_DIR/scripts/verify_upload_package.py \
  --hashtags hashtags.txt \
  --comment pinned_comment.txt
```

Quality gate:

- [ ] Default output has supplied YouTube title first, followed by description, comment, exactly ten upload tags, and the CMS draft (five copy blocks total)
- [ ] Description introduction is user-supplied and preserved, not newly invented
- [ ] Production credits follow the current evidence and fixed field order
- [ ] CMS block preserves supplied article title/body, uses display setting 0, and does not claim registration or image validation without evidence
- [ ] Description includes fixed website/contact lines and about three `#hashtags`
- [ ] Upload-tag block has exactly ten unique tags separated by `, `, without `#`
- [ ] Legacy three/six-block splits are used only when explicitly requested
- [ ] If the user narrowed the request to `타임스탬프만/챕터만`, package assembly stopped and exactly one validated timestamp block was returned
- [ ] Pinned comment is always the final section
- [ ] Supplied YouTube title, article title, and article body are copied exactly
- [ ] Thumbnail/list title is ignored unless explicitly requested
- [ ] Correct ad state inferred from first 90 seconds
- [ ] Exact approved ad template and URL used
- [ ] No ad copy/separator when there is no front ad
- [ ] Topic header present
- [ ] Timestamp list passes YouTube chapter validation
- [ ] Thank-you lines exactly preserved
- [ ] Every output block can be copied and pasted without editing
