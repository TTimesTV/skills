---
name: ttimes-youtube-upload-package
description: 'Build the TTimes YouTube upload package from a video URL and YouTube CC: comma-separated hashtags, separate body timestamps, and a final pinned-comment block with inferred front-ad copy when present. Also preserves supplied publishing metadata fields in labeled-bundle mode.'
metadata:
  version: 1.4.2
---

# TTimes YouTube Upload Package

## Trigger and deliverable

Use when the user asks for `업로드 작업`, `유튜브 업로드 세트`, asks for hashtags and a pinned comment together with timestamps, or supplies a labeled publishing bundle plus a YouTube URL.

Read `references/user-approved-output-contract-20260715.md` for the concrete copy/paste contract and correction history; use `references/pinned-comment-templates.md` for exact approved ad copy.

### URL-only upload request

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

- return both `본문 업로드용 타임스탬프` and `고정 댓글 (댓글용 타임스탬프 포함)` together as soon as chapters validate
- keep the pinned comment last and use the exact recognized ad template
- omit the pinned comment only when the user explicitly says `타임스탬프만`, `챕터만`, or `댓글 제외`
- never make the user ask a second time with `댓글도 줘야죠`

If metadata and tags were already delivered in earlier partial responses, do not repeat them unless requested; finish the remaining pair atomically.

### Labeled publishing bundle + YouTube URL

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

The timestamp list is embedded in the pinned comment and also repeated separately for body upload only in labeled-bundle mode.

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
- Once the applicable prefix-shift gate, timestamp validation, and package validation pass, return all six copy-ready blocks immediately.
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

### D. No front ad

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

## Step 2: generate upload tags

Create 12–18 unique upload tags; minimum 10.

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

## Output shape

For URL-only mode, return three labeled sections in this order:

1. `해시태그`
2. `본문 업로드용 타임스탬프`
3. `고정 댓글 — 댓글용 타임스탬프 포함`

For labeled-bundle mode, return supplied metadata fields first, then hashtags, body timestamps, and the pinned comment last.

Every section must use one fenced `text` code block containing only copy-ready content. Do not make the user remove bullets, quote marks, Markdown bold markers, or explanatory text from inside the copy blocks.

## Validation

Save drafts as:

- `hashtags.txt`
- `pinned_comment.txt`

Run:

```bash
python3 SKILL_DIR/scripts/verify_upload_package.py \
  --hashtags hashtags.txt \
  --comment pinned_comment.txt
```

Quality gate:

- [ ] At least 10 unique upload tags, each separated by `, ` and none prefixed with `#`
- [ ] URL-only mode has three output blocks; labeled-bundle mode has six
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
