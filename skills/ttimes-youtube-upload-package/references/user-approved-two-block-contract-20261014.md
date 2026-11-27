# Current upload contract

Default output order: unnumbered YouTube title, 1. description, 2. ten upload tags, 3. CMS unpublished draft. Include pinned-comment copy only on explicit request. The filename retains the original approval for compatibility.

## Block 1: full YouTube description

Use this order, with blank lines between sections:

```text
[User-supplied video introduction, verbatim]

편집 : [name and established role title]
촬영 : [name and established role title]
자료 : [name and established role title]
진행 : [name and established role title]
섬네일 : [name and established role title]

▶티타임즈 공식 홈페이지
http://www.ttimes.co.kr/index.html
▶비즈니스 문의
ttimes6000@gmail.com

#topic1 #topic2 #topic3

[Validated chapters]
```

The user said they will supply the introduction: never make one up just to complete a package. Preserve their body wording, including book-title punctuation such as `<공부의 미래>`. Supplied thumbnail, YouTube/article titles and landing URLs remain separate metadata; do not insert them into the description or return additional blocks unless requested. If the introduction is absent, make useful progress on credits/chapters and identify the missing input; an explicit practice draft may show a clearly marked placeholder.

Description hashtags have `#` and use spaces, exactly three. Reuse them in the CMS block. The separate upload-tag block has exactly ten comma-separated, no-`#` tags for YouTube's upload-tag field.

## Production-credit evidence

Verified shared source: [월별 일정표](https://docs.google.com/spreadsheets/d/1GD39SPe_GAzaBctj4hYjc1qpMtucCWDN2Onht_pN7VM/edit#gid=1752956629).

The user initially called it Google Calendar, but it is a native Google Sheet. Prefer connected Drive/Sheets tools; use the relevant skills and read metadata before bounded reads. On 2026-10-14 the active tab was `2026년`, sheetId `1752956629`; future runs must resolve current tabs and headers from metadata rather than assuming this tab forever.

Rows are dates and personnel are column headers. The `기사 마감 예정` column identifies upload/milestone timing. Establish each role across the same episode's production history, not solely its upload-day row:

- 편집: episode-labelled 컷편 / 진행 / 수정 / 최종본 / 마감 tasks under a video editor's column.
- 촬영: an explicit 촬영 task for that episode, usually on an earlier date.
- 자료: an explicit 자료 / 자료 완 task; do not treat the editor's 마감 entry as material research.
- 진행: the episode's presenter in the introduction or an explicit producer-supplied credit. A schedule cell saying 진행 usually means work in progress, not on-camera presentation.
- 섬네일: an explicit episode-labelled 섬네일 / 썸네일 task. Do not assign the usual designer when the row does not support it.

Match guest combinations and part numbers so similarly named episodes do not share credits by accident. Expand abbreviated personnel names through actual headers. Use established role titles, not guessed occupational labels. If multiple people share a role or evidence is ambiguous, state the uncertainty rather than silently selecting one. User-provided exact credits override inferred assignments.

Reference example verified in this session: Koo Bon-kwon, `DcTNTwbz_uI`: 편집/촬영 정지원 PD, 자료/진행 이사민 기자, 섬네일 박수형 영상디자이너. These are that episode's credits, not defaults for other videos. Park / Yoo: editing 정지원, filming 장민주, materials 박성수, presenter 박영선 전 장관, thumbnail 이소민 영상디자이너 (user confirmed).

User correction (2026-10-15): Park Young-sun's presenter credit must be exactly `진행 : 박영선 전 장관` in both YouTube description and CMS credits. Do not shorten it to `박영선`. She is an external presenter, so this does not add her to the internal CMS-author list.

Canonical credit-label lookup is now [credit-name-titles.md](credit-name-titles.md), including user-approved affiliation/professional labels for 이중학 and 김지현. Read it when assembling credits; it does not replace episode-specific staff assignment evidence.

## Pinned-comment copy on explicit request

Use the exact ad corresponding to the actual final video, then:

```text
[Approved ad copy, only if the video has that ad]

=================================

📌오늘의 주제 모아보기📌

[Exactly the same chapters as block 1]

시청해 주셔서 감사합니다😍
좋아요와 구독은 큰 힘이 됩니다😘
```

Without an ad, start directly at the topic header and omit the separator. Ad/highlight timing comes from the actual video, never another episode. Snowflake ended on 2026-10-02 and is inactive by default. PA | AI Connect 2026 and 2027 IT trend templates are available, but neither is assumed without source evidence.

## Delivery and scope

Return the user's YouTube title first in its own copy block, then the numbered description, ten-tag, and CMS blocks. When comment copy was requested, add it after the description and keep CMS last. Labels stay outside the `text` fences. Reuse user-approved chapters for the same final video when no chapter rewrite is requested. Preparing copy does not authorize editing a platform, posting comments, or changing the shared schedule. Follow the [draft-only workflow](publishing-workflow.md) for actual registration requests.

## Top title and upload tags

The top `유튜브 제목` block preserves the supplied YouTube title, not the thumbnail or article title. Generate a title only when the user explicitly asks.

The `해시태그 — 유튜브 태그 입력란용` block contains exactly ten unique source-supported tags, separated by comma and space, without `#`. Keep the separate three description/CMS hashtags. Use relevant topics, central guests/entities and channel tags.

## Final block: CMS unpublished-draft registration clipboard

The user has a Gemini workflow connected to the CMS and wants a clipboard that supplies the registration data and controls video embedding. Draft registration defaults to `표출 설정: 0` (미발행 임시저장 초안), never public publication.

Include:

- User-supplied article title (not the YouTube or thumbnail title).
- Current final YouTube URL only. Do not add a separate video-ID field.
- User-supplied article body verbatim. Do not replace it with a new summary or the full YouTube description containing website links, hashtags and chapters.
- A separate `해시태그:` field immediately after the article body: exactly three relevant hashtags, with `#` prefixes and spaces between them, matching the three description hashtags. Do not append them to the article prose or use the comma-separated upload-tag format.
- Do not include iframe/embed HTML in this clipboard. The user explicitly removed that field; the connected CMS workflow handles embedding from the video URL.
- Exact list-image path/reference supplied or verified for this article. File size and dimensions are reported only after actual inspection. Do not invent a path, assert '검증 완료', or substitute another episode's image.
- Display setting `0`.
- Internal CMS contributors are the deduplicated internal staff appearing across the five credits, including the thumbnail designer. List names with established role titles on one comma-separated line, without role assignments or guessed CMS IDs. For Koo Bon-kwon the approved line is `정지원 PD, 이사민 기자, 박수형 영상디자이너`. Do not count an external presenter/guest as internal staff merely because they appear in the credits.
- All five production-credit roles. Use verified professional titles; Gemini's sample calling 박성수 'PD' is not authority for that occupational label. Missing thumbnail credit remains unconfirmed.

Keep the final clipboard self-contained so it can be pasted into the connected Gemini/CMS workflow. Do not put '등록할까요?' / '등록해라고 지시하면 전송' or a claimed completion inside this prepared clipboard. The user decides when to pass it to their registration workflow. Actual CMS submission is a separate action requiring a user request and supported access.

If the article title/body or list image is missing, preserve completed work and indicate the specific missing field. The approved image placeholder is `사용자가 별도 제공 예정. 현재 파일 미제공.` Do not claim image validation before receiving/inspecting it.

### Exact CMS clipboard shape — user correction

```text
아래 정보를 CMS 미발행 초안 등록 데이터로 사용하세요.
기사 제목과 본문은 수정하지 마세요. 표출 설정은 0입니다.

기사 제목:
[Supplied article title]

유튜브 영상:
[Final video URL]

기사 본문:
[Supplied body verbatim]

해시태그:
#topic1 #topic2 #topic3

리스트 이미지:
[Verified supplied image or the approved missing-image text]

표출 설정:
0 — 미발행 임시저장 초안

CMS 내부 작성자:
[Deduplicated internal staff, with established role titles, comma-separated]

제작진 크레딧:
편집 : [credit]
촬영 : [credit]
자료 : [credit]
진행 : [credit]
섬네일 : [credit]

참고 랜딩:
[URL]
-> [Existing reference article title] ([Publication date])
```

Reference landing is contextual information, not the new article title and not authorization to overwrite that existing article. Use the user's supplied landing title/date when provided; otherwise look them up if needed rather than inventing them. Koo Bon-kwon approved reference: `https://www.ttimes.co.kr/article/2026012916427722022` → `AI 때문에 의사, 변호사 전문직도 양극화한다 (2026년 1월 29일)`.

## Approved full-package example: Snowflake recap

User approved the three-block package for `https://youtu.be/ar5KU9S6838` with `굿!! 스킬 저장` on 2026-10-14.

- Description: user-supplied introduction, five credit roles, fixed links/contact, `#스노우플레이크 #AI데이터 #데이터분석`, then the same episode's published 16 chapters. This is a 78-minute recap; do not apply the shorter-interview nine-chapter calibration as a quota.
- Credits: `편집 : 박선희 영상디자이너, 강기훈 PD`, `촬영 : 강기훈 PD`, `자료 : 홍재의 기자`, `진행 : 홍재의 기자`, `섬네일 : 이소민 영상디자이너`. Preserve both credited editors. The public video's exact credits can resolve assignments that the schedule alone leaves unclear.
- Pinned comment: no front ad in this video, so start directly at `📌오늘의 주제 모아보기📌`, then identical chapters and the fixed emoji thank-you lines. Snowflake as the main program topic does not mean the old Snowflake seminar ad is present.
- CMS title: `데이터는 다 있는데, AI가 못 알아들을 땐 어떻게 해야하나?`; use the supplied article title rather than the YouTube title.
- CMS hashtags (subsequent user addition): `#스노우플레이크 #AI데이터 #데이터분석`, in their own `해시태그:` field after the article body.
- CMS internal authors: `박선희 영상디자이너, 강기훈 PD, 홍재의 기자, 이소민 영상디자이너`. Deduplicate people, not roles. The result can have four people; never force it to exactly three authors.
- List-image field: `사용자가 별도 제공 예정. 현재 파일 미제공.` User-provided thumbnail composition instructions are not an image file and do not authorize generating/replacing the list image.
- Reference landing: `https://www.ttimes.co.kr/article/2026073017177713959` → `사내 에이젠틱 AI는 삼성전자와 뉴욕거래소를 어떻게 바꿨나? (2026년 7월 30일)`.

These names, hashtags and chapters belong to this specific episode. Reuse the approved output structure, not its personnel or ad state, for other videos.
