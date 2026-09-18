# User-approved TTimes upload output contract — 2026-07-15

This is a session-specific contract extracted from direct user corrections. The SKILL.md carries the durable rules; this file preserves the concrete rationale and examples.

## Copy-ready formatting

- Every deliverable is in its own fenced `text` block so Telegram exposes a Copy button.
- No bullets, commentary, Markdown emphasis markers, or labels inside the copy block.
- Labels sit outside the block.

## Upload tags (`해시태그` field)

Space-only lists are rejected by the user's upload field. Use comma + one space, and **omit the `#` prefix**:

```text
티타임즈, 티타임즈TV, AI, 데이터센터
```

Generate at least 10 unique, source-supported tags.

Correction recorded 2026-07-23: the user explicitly rejected `#AI, #인공지능` and approved `AI, 인공지능`.

## URL-only mode

Fixed output order:

1. 해시태그
2. 본문 업로드용 타임스탬프
3. 고정 댓글 — 댓글용 타임스탬프 포함

The pinned comment is always last.

## Labeled publishing-bundle mode

When the user supplies `<유튜브 제목>`, `<기사 제목>`, `<유튜브 설명/기사/페북>`, and a YouTube URL, preserve supplied copy exactly and output:

1. 유튜브 제목
2. 기사 제목
3. 기사 내용
4. 해시태그
5. 본문 업로드용 타임스탬프
6. 고정 댓글 — always last

Ignore thumbnail/list title, Naver/Daum title, and landing URL by default unless explicitly requested. Generating a new title/article set from scratch is not yet an approved standard; treat it as a proposal/reference unless the user asks to canonize it.

## Front-ad state

- Recognized AI-leverage or Excel ads use the exact approved template.
- No front ad means no ad copy and no `=================================` separator.
- If the user states there is no front ad or no highlight, that direct production fact overrides inference from recent channel habits.
- Never manufacture `00:16 하이라이트`; chapter 00:00 can be the main program.

## Split-first metadata handoff

Correction recorded 2026-07-23: when the user says `일단 세트부터 나눠줘`, return the supplied publishing fields immediately as separate copy blocks instead of waiting for timestamps. In this explicit partial-handoff mode, include every supplied field—including thumbnail/list title, Naver/Daum title, and the video URL—because the user is asking to split the set they just pasted, not invoking the default omission policy.

Do not rewrite supplied copy. Hashtags, timestamps, and comment can follow as separate partial deliveries when requested.

## Urgent first-cut → final handoff

Correction recorded 2026-07-23: `빨리`, `컷편 기준`, or `앞에 것만` changes the timestamp method but does **not** silently narrow a live upload-package request to timestamps alone.

- Treat the producer's statement that the final is `front ad + highlight + cut body` as authoritative.
- Use the cut video's embedded/manual CC for semantic chapters.
- Inspect only the final prefix and add the body offset.
- Do not start full-final ASR, duration archaeology, or late-body spot checks after the producer says to use the cut timeline.
- Deliver the validated body timestamp block **and the pinned-comment block together**. The user should never need to follow up with `댓글도 줘야죠`.
- Omit the comment only for an explicit `타임스탬프만`, `챕터만`, or `댓글 제외` instruction.

## Timestamp duplication

The same validated chapter list is delivered twice:

- plain list for body upload
- embedded beneath `📌오늘의 주제 모아보기📌` in the pinned comment

The fixed comment footer is:

```text
시청해 주셔서 감사합니다😍
좋아요와 구독은 큰 힘이 됩니다😘
```
