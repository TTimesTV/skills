---
name: ttimes-script-and-srt
description: "Use when the user wants Hermes to create a TTimes-style Korean subtitle script from MP3/video/YouTube, then optionally generate a line-preserving SRT. Covers source acquisition, MLX Whisper ASR, YouTube captions, term correction, readable line-breaking, subagent review, and final validation."
license: MIT
metadata:
  version: 1.0.9
  author: Hermes Agent
  hermes:
    tags: [media, subtitles, srt, ttimes, mlx-whisper, youtube, korean-caption-script]
    related_skills: [ttimes-youtube-timestamps, ttimes-youtube-upload-package, ttimes-editorial-copy, ttimes-screen-composition]
---

# TTimes Script and SRT Pipeline

## Purpose

Create the user's `[스크립트]` from only an MP3/video file or YouTube link/title, then optionally turn that script into a line-preserving SRT.

This skill retains the spoken-caption workflow formerly paired with `media-localization-workflows`. Its unavailable local source-acquisition, ASR, alignment, and sync portions are explicitly gated in `references/local-dependency-gates.md`; do not treat that historical relationship as an installed dependency.

## Core Mental Model

```text
source media / YouTube
→ transcript substrate: YouTube captions if useful + MLX Whisper ASR
→ term/proper-noun correction
→ TTimes-readable `[스크립트].txt`
→ line-preserving SRT aligned to real audio
→ validation + delivery
```

Important distinction:

- `[스크립트]` is the authoritative subtitle body text.
- MLX Whisper / YouTube captions are substrates to create or time that script.
- SRT body lines must equal the final script lines exactly unless the user asks otherwise.

### User default: 군더더기를 걷어낸 말자막 (2026-09-16)

이 사용자의 말자막은 **음성을 기준으로 뜻과 말투를 살리되, 입말의 군더더기는 기본으로 제거**한다. 새 말자막 작성에서는 별도 요청을 기다리지 않는다. 이 규칙은 아래와 과거 references의 추임새·반복 전부 보존 지침보다 우선한다. 싱크/원문 전사에는 적용하지 않으며, 사용자가 명시한 원문 그대로 보존·이미 승인된 body 그대로 배치 요청은 따른다.

- `어`, `음`, `아`, `뭐` 같은 추임새, `네네`, `그렇죠`, `맞습니다` 같은 단순 맞장구, 더듬음·말 다시 시작하기의 불필요한 반복을 제거한다.
- **`한`, `좀`, `이제`도 반드시 검토해 군더더기 용법은 제거**한다. `한 3시간` → `3시간`, `한 200명 정도` → `200명 정도`, `좀 더 정리` → `더 정리`, `이제 AI를 쓰면` → `AI를 쓰면`. 수량 앞의 습관적인 `한`을 ‘대략이라는 뜻이 있다’는 이유만으로 일괄 보존하지 않는다. `약간`, `이렇게`, `뭔가` 등도 문맥상 군더더기면 정리한다.
- 문자열 일괄 삭제는 금지한다. `일을 한 사람`의 동사, `GPU 한 대`의 실제 개수, `한 번`, `좀 전`, 시간 전환을 뜻하는 `이제부터`와 실제 답변·부정·조건·핵심 수량은 보존한다. 정리 후 조사·띄어쓰기와 문장 연결을 확인한다.
- 내용을 요약하거나 새 문장으로 쓰지 않는다. 의미 있는 연결어·강조 반복·주장 강도는 유지하고, 의미 단위로 나눈 뒤 실제 컷 음성에 맞춘다.
- 승인 본문을 타이밍만 배치할 때 다시 정리하지 않는다. 이후 사용자가 군더더기 삭제를 요청하면 본문과 SRT를 함께 갱신하고, 본문만 바뀐 cue의 기존 타임코드는 유지한다. 사용자가 지정한 납품 폴더가 있으면 그 SRT도 같은 버전으로 교체한다.

### User default: fast output-first order

For this user, the job's core is **minimal transcript correction + artistic spoken-caption segmentation, completed quickly**. Use this order by default:

```text
Whisper full transcript + word times
→ Main creates one complete minimally corrected, fully segmented body output
→ one parallel review generation
→ Main applies only confirmed findings in one batch
→ inspect changed windows and their outer seams only
→ freeze the complete body TXT
→ map those exact frozen lines to word timestamps
→ mechanical validation and immediate delivery
```

The complete timecode-free body output must exist **before** SRT placement. Once frozen, alignment may not rewrite, merge, split, omit, or reorder its lines. Do not repeat full-review generations, re-run ASR, or globally re-optimize boundaries after local fixes unless direct source evidence shows a material omission or meaning error. Subagents review; Main owns the single whole-program rhythm and final integration.

### Route YouTube chapters to the dedicated skill

When the user asks for TTimes YouTube `타임스탬프`, `챕터`, or a `00:00 제목` description list, load and use `ttimes-youtube-timestamps`. Do not improvise chapter generation inside this spoken-caption/SRT skill.

Routing boundary:

- `말자막`, `분절`, `SRT`, `스크립트` → remain in `ttimes-script-and-srt`.
- **`티타임즈 싱크 작업` → 이 말자막 공정을 중단하고 `external_dependency`로 표시한다.** 로컬에 `media-localization-workflows`가 없으므로, 필요한 승인 컷 원고+컷 MP3와 `화자 MM:SS + source-faithful 장문 본문` DOCX/TXT 계약은 `references/local-dependency-gates.md`에서 확인한다. 싱크는 cue-body 분절·글자 수 제한·SRT가 아니다.
- `유튜브 설명란 챕터`, `타임스탬프만` → stop the SRT workflow and route to `ttimes-youtube-timestamps`.
- `타임스탬프와 말자막`, `챕터+SRT`, or an equivalent combined request → use both workflows in one job: semantic chapters from `ttimes-youtube-timestamps`, full spoken-caption TXT/SRT from this skill, and deliver them as separate artifacts. Do not substitute the chapter list for the full speech text.
- **Latest-directive reset:** if discussion begins with old 컷편/말자막 reuse but the user later says `그냥 이 URL로 다시 해`, stop artifact archaeology and offset/reuse experiments immediately. Treat the supplied final URL as the sole audiovisual authority, run the direct final-URL route, and do not keep explaining the abandoned reuse path.
- **Exact deliverable count:** if the user says `총 2개` in a combined request, deliver exactly two user-facing files—normally body-only `*_말자막.txt` and copy-ready `*_타임스탬프.txt`. Keep SRT/JSON/validation ledgers internal unless explicitly requested. Do not silently turn `말자막` into SRT merely because the ASR has word timestamps.
- `해시태그 + 본문 챕터 + 고정댓글` → route to `ttimes-youtube-upload-package`, which must load the timestamp skill first.
- A bare media URL plus `/plan` is genuinely ambiguous among 말자막, 컷편집, 화면구성, and upload-package work. Do not infer 화면구성 merely because the surrounding discussion contains insert research or footage selection. If the user has not named the deliverable, ask one short routing question before writing a plan. Once the user says `말자막 작업`, use this skill's **no-sample full-body SRT plan by default** and mark any previously drafted screen-composition plan as superseded. Use a sample only under the explicit exceptions in §2.

For combined chapter+caption requests, if YouTube caption retrieval returns HTTP 429 or another shared platform rate limit, attempt that caption endpoint only once, then switch to exact-source audio plus MLX Whisper instead of retrying the same caption call. Put title/topic terms in a narrow initial prompt, preserve raw ASR separately, and verify mangled person/model/company names with exact-quote search plus official or reputable source evidence before writing corrected derivatives. See `references/combined-youtube-timestamps-and-spoken-captions.md` for the compact acquisition, correction-ledger, deliverable, and validation checklist.

The dedicated timestamp skill is authoritative for YouTube CC extraction, first-cut→final prefix-offset shifting, semantic chapter boundaries, exact cue snapping, validation, and copy-ready output. The older `references/ttimes-youtube-description-chapters.md` is compatibility context only and must not override the dedicated skill.

## When to Use

Use when the user says:

- `이 영상으로 srt 만들어보자`
- `유튜브로 스크립트 만들어줘`
- `mp3로 스크립트.txt 만들어줘`
- `스크립트 만들고 말자막까지`
- `티타임즈식 말자막`
- `자막 길이 가독성 좋게`

Also use when the user gives only a YouTube title and asks to make SRT; first try to discover the source link via `yt-dlp "ytsearch..."` or other available lookup, and ask only if discovery fails or multiple plausible videos are indistinguishable.

## Required Skills / References

Load and follow:

- 소스 획득, MLX Whisper, line-preserving SRT 정렬, synced-DOCX 생산 전에는 `references/local-dependency-gates.md`를 읽는다. `media-localization-workflows`는 로컬에 없으므로 이 경로는 구현된 것처럼 보이지 않게 `external_dependency`로 남긴다.
- copy-only 강조자막/설명자막은 `ttimes-editorial-copy`, 시간/배치는 `ttimes-screen-composition`으로 처리한다. `caption-layering-workflow`는 로컬에 없으므로 전체 레이어 문법이나 renderer가 있다고 주장하지 않는다.


## 필요한 절차만 읽기

현재 사용자 기본값과 명시적인 요청 범위가 아래 상세 절차·과거 사례보다 우선한다.
새 말자막의 군더더기 정리와 이미 승인된 body의 타이밍만 배치하는 요청을 구분한다.
이 표의 모든 문서를 한꺼번에 읽지 않는다. 아래 코드 표기의 `references/...`는 이 스킬 루트 기준이다.

| 현재 작업 | 읽을 상세 절차 |
| --- | --- |
| 기존 ASR 일부, 승인 컷 구간, 기존 SRT 수정/감사, 화자 DOCX 모드 선택 | [모드 선택](references/workflow-modes.md)에서 해당 소절 |
| 새 URL/미디어, ASR 필요, CC 실패 복구 | [소스·전사](references/workflow-acquisition.md)와 local-dependency-gates |
| 새 말자막 본문 작성·군더더기 정리·고유명사·분절 | [본문 편집](references/workflow-editorial.md) |
| 본문 검토·서브에이전트 검토·수정 후 경계 검사 | [검토와 종료 조건](references/workflow-review.md) |
| 고정된 본문에 시간 배치·SRT 생성 또는 요청된 아카이브 | [타이밍·보관](references/workflow-timing-archive.md)의 해당 부분 |
| 작은 문장성 사례·긴 MP3 ASR 복구·차단 시 처리 | [분절 사례와 복구](references/workflow-segmentation-recovery.md)의 해당 부분 |
| 특정 과거 사례와 비교하라는 요청 | [사례 인덱스](references/workflow-cases.md)에서 관련 사례만 |

새 본문 제작은 본문 편집 → 필요한 검토 → 본문 고정 → 요청된 경우 타이밍 순서다.
승인 body를 그대로 배치할 때는 본문을 다시 정리하거나 분절하지 않는다.
분절은 문장 끝·작은 문장성·서술어 결합·의미·발화 리듬을 우선한다.
시각 길이는 25자 목표/27자 실용 상한이며, 보호구문 28자 이상 예외는 본문 편집 절차의 승인 조건을 따른다.
과거 사례에서 관측된 더 긴 cue가 현재 길이 규칙을 자동으로 대체하지 않는다.

### 9. Deliverables

For script-only:

- `MEDIA:/absolute/path/[title]_스크립트.txt`
- Brief summary: source title, duration, line count, transcription substrate used.

For full pipeline:

- Send only the user-facing artifact(s) actually requested. A bare `말자막`/`SRT` request normally means **one** `.txt` attachment containing the SRT; do not add a separate body/script file unless the user asks for `스크립트`, `타임코드 없는 문장`, or an explicit multi-file package.
- Use the exact user-specified basename. If none was specified, derive a concise `YYMMDD_title.txt` name from the project convention; do not surface internal pipeline labels or force ASCII transliteration.
- If the user asks for `스크립트`, `타임코드 없는 문장만`, or similar, deliver a separate plain script `.txt` with no timestamps/timecodes.
- Do not package validation JSON for the user unless explicitly requested.
- Keep validation JSON/internal reports locally for debugging, but do not attach them in normal delivery.
- Use ZIP only as a last-resort fallback when the requested `.txt` attachment also fails, or when the user explicitly asks for a bundle. ZIP is annoying on mobile for this user, so never make it the first fallback.
- Validation summary in chat should stay brief: cue count, exact body match, overlap status, and any important caveat.

## Quality Gate

Before final response, check:

- Chosen source is correct.
- Audio duration verified.
- Script has no speaker/timestamp clutter unless requested.
- Terms are corrected before line-breaking.
- Lines are readable as TTimes-style Korean captions.
- SRT, if produced, exactly matches script bodies.

### User-facing 95-point acceptance gate
