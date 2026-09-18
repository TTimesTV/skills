# 2026-07-09 김지현 싱크 MP3 — 분절 재작업, 자막 문법, fuzzy 재정렬 교훈

## Trigger

Use these lessons when a long Korean TTimes-style MP3/SRT job fails because the output is mechanically valid but visually/artistically bad as subtitle segmentation.

This session started with a technically valid SRT that had:

```text
cue count: 2,284
27-char max: pass
timecode overlap: 0
periods: 0
```

But the user scored it about **45/100** because the task was a **분절 업무** and the segmentation/readability was poor.

## Core lesson: segmentation is not text wrapping

The user explicitly reframed the job:

```text
분절은 기계적으로 처리하는 작업이 아니다.
화면을 상상하고, 독자들이 자막 바를 어떻게 바라볼지 생각해야 한다.
예술적인 아키텍처로 접근해야 한다.
```

Operational meaning:

- Do not treat `≤27 chars` as the goal.
- Imagine the bottom subtitle bar as a visual beat.
- Each cue should close a small readable thought where possible.
- The viewer should not need to wait for the next cue to resolve basic grammar.
- Objects, adverbials, time phrases, and connective particles must not be stranded.
- If segmentation quality is 45, the whole deliverable is about 45 even if timing/format/terms pass.

Bad failure examples:

```text
AI를
분들도
취재하고
너희는
받으신 분들은
회사 전체가
중요한 거는
분들을
좀 기록을
분들께서
일반적으로
```

Approved sample style examples:

```text
요새 AI 때문에
리더와 갈등이 있으신 분들도 많고
또 본인이 리더시라면
AI를 나는 어떻게 쓸까?
우리 팀은 어떻게 활용해야 될까?
이런 고민이 많으신 것 같습니다
```

Short cues are allowed when they are self-contained reactions/rhythm, not stranded grammar:

```text
말만
네 말만
맞아요
그렇죠
딱 그거네
네
```

## Required workflow after a segmentation failure

Do **not** immediately regenerate the whole 85-minute SRT.

Use this sequence:

```text
1. Archive failed SRT.
2. Extract 0~3 min ASR sample.
3. Manually create a cue-body-only sample in the desired segmentation style.
4. Ask user approval.
5. Only after approval, split the source into parts.
6. Let subagents make part-level cue-body drafts.
7. Main Hermes must integrate into one rhythm/style.
8. Apply subtitle punctuation as living caption grammar.
9. Align final body to word timestamps.
10. Validate and deliver only *_srt.txt.
```

Subagents are useful as **초벌 노동자/reviewers**, not final editors. Main Hermes remains the single editor responsible for the one-screen-language rhythm.

## Subagent brief pattern that worked better

Split by large time ranges, e.g.:

```text
Subagent 1: 00~30분
Subagent 2: 30~60분
Subagent 3: 60~85분
```

Give each subagent:

- approved sample style
- input ASR part paths
- exact output path
- cue body only, no timestamps/indices/markdown
- 25-char target / 27-char max, spaces included
- ban examples like `AI를`, `분들도`, `이야기를`, `인사이트를`, `데이터`, `수`
- term lists specific to the part

But never trust self-reports. Main must read the output files, run lint, and inspect representative sections.

## Subtitle punctuation correction

The user corrected an overbroad “no punctuation” interpretation.

Correct rule:

```text
Mechanical sentence-final periods/full stops are banned.
Question marks, exclamation marks, commas, and quotes are allowed/needed when they carry subtitle rhythm or meaning.
```

Use punctuation as subtitle grammar:

- `?` for real questions and rhetorical questions.
- `!` sparingly for emphasis.
- `,` for visual rhythm, lists, and contrast.
- `" "` or `' '` for quoted speech, prompts, coined terms, titles, and self-contained embedded text.

Examples:

```text
어느 동네로 오셨어요?
AI를 나는 어떻게 쓸까?
우리 팀은 어떻게 활용해야 될까?
"리더의 AI 노트"
"선무당이 사람 잡는다"
야, 데이터센터 공급이 저렇게나 모자라?
욕심이 생겨요? 안 생겨요?
```

## Timing alignment pitfall: proportional mapping is not enough

A proportional line-count/text-length mapping produced visibly bad placement. Even though the final time reached the right duration after fixes, mid-file cue placement felt off.

Do not use simple proportional mapping as the final timing method for a heavily resegmented long script.

Better method:

1. Build normalized caption character stream from final cue body lines.
2. Build normalized ASR character stream from word timestamps with `char -> word index` mapping.
3. Use `SequenceMatcher(..., autojunk=False)` or another sequential fuzzy matcher to align caption chars to ASR chars.
4. For each cue, map its caption char span to ASR char span, then to first/last word timestamps.
5. Add small padding (`start -0.04s`, `end +0.12~0.14s`).
6. Resolve overlaps by trimming the previous cue, not by pushing the global timeline forward.
7. Report low-match cues separately.

A successful fuzzy realign in this session produced:

```text
cues: 2,839
body_match: true
overlap: 0
nonpositive: 0
max chars: 27
question marks: 218
quote lines: 14
avg direct match ratio: ~0.98
low-match cues: 1
last time: 01:25:05,940
```

## Validation signals to report

For final delivery, report briefly:

```text
cue count
body line count
SRT body == caption body
27-char overflow count
overlap/nonpositive counts
question mark / quote counts when punctuation was part of the correction
low-match count if fuzzy alignment used
last time
```

Do not overclaim 95점 from mechanical validation alone. If the user says the placement/배치 is off, treat timing alignment as failed and redo with fuzzy string/word matching.
