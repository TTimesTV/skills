# 2026-07-09 김지현 싱크 — 분절 실패 복구와 재정렬 교훈

## Context

Long source MP3: `260708_김지현 싱크.mp3`, about 85 minutes. Initial full-file MLX ASR collapsed around 47 minutes into repeated filler (`네`), so chunked MLX ASR was required. The first delivered SRT passed mechanical checks but failed the user's real task: TTimes-style subtitle segmentation.

## Key user correction

The user clarified that this class of work is not mechanical wrapping or SRT generation. It is **artistic architecture of the subtitle bar**: imagine the viewer's eyes landing on each cue, how meaning closes in that visual beat, and how the next cue opens.

For tasks framed as `분절 업무`, the overall score is dominated by segmentation quality. Do not average high timing/format/term scores with low segmentation. If segmentation is 45, the deliverable is about 45 even when timecodes and 27-char limits pass.

## Failure pattern

The failed version had no overlaps, no 27-char overflow, and no final periods, but contained many cue fragments such as:

```text
AI를
분들도
취재하고
너희는
받으신 분들은
AI는
회사 전체가
중요한 거는
분들을
좀 기록을
분들께서
일반적으로
```

These are not just ugly short lines; they force the viewer to wait for the next cue to resolve grammar. They fail small-sentence readability.

## Correct sample-first workflow

When a previous output fails or style calibration is uncertain:

1. Do not rebuild the full 60–90 minute SRT immediately.
2. Extract a 2–3 minute sample from the ASR.
3. Write cue-body-only text in the intended style.
4. Ask the user for approval.
5. Only after approval, split the full job into parts for subagents.
6. Subagents produce partition drafts only; Main Hermes is the final editor and must integrate into one rhythm.
7. Main validates and aligns SRT.

Approved sample style in this session:

```text
요새 AI 때문에
리더와 갈등이 있으신 분들도 많고
또 본인이 리더시라면
AI를 나는 어떻게 쓸까?
우리 팀은 어떻게 활용해야 될까?
이런 고민이 많으신 것 같습니다
```

Important distinction: short reaction cues can stand alone (`말만`, `네 말만`, `맞아요`, `그렇죠`, `딱 그거네`) when they are complete visual beats. Bad short cues are grammatical fragments (`AI를`, `분들도`, `이야기를`, `데이터`, `수`).

## Punctuation doctrine

The rule is **not** “remove all punctuation.” It is “remove dead prose periods.” Subtitle punctuation is part of screen language.

Use when helpful:

```text
?  real questions / 반문
!  limited emphasis
,  lists, contrast, rhythm
" " / ' ' quoted speech, prompts, coined terms, titles, embedded text
```

Examples:

```text
어느 동네로 오셨어요?
AI를 나는 어떻게 쓸까?
우리 팀은 어떻게 활용해야 될까?
"리더의 AI 노트"
"선무당이 사람 잡는다"
```

Do not strip punctuation mechanically. Design it.

## Subagent briefing pattern

Give subagents the approved sample and explicit bans:

- 원발화 보존·최소교정
- 문장/생각 끝나면 다음 cue
- 작은문장성
- 목적어/부사어/시간어 고립 금지
- 접착어 고립 금지
- 공백 포함 25자 목표 / 27자 max
- no timestamps/indices/markdown in cue-body drafts
- ban standalone examples: `AI를`, `분들도`, `너희는`, `이야기를`, `인사이트를`, `데이터`, `수`, `됐든`

Partitioning used here:

```text
00~30분
30~60분
60~85분
```

Subagent drafts improved from ~45 to roughly 70-point material, but still needed Main integration. Subagents are not final editors.

## Alignment lesson

A final cue-body draft with many more cues cannot be aligned by simple proportional time mapping. Proportional mapping caused bad placement even when the last timestamp was clamped correctly.

Use caption-body ↔ ASR word-stream fuzzy alignment:

1. Normalize caption text and ASR words into character streams.
2. Apply term normalization for matching, e.g. `챗GPT→챗지피티`, `AI→에이아이`, `GPU→지피유`, `HBM→에이치비엠`, `D램→디램`.
3. Use sequence/fuzzy matching to map caption character spans to ASR character spans.
4. Convert ASR char spans to word indices and word timestamps.
5. Resolve overlaps by trimming previous cue, not by pushing the whole timeline forward.
6. Report average direct match ratio and low-match cue count.

Good run metrics from this session after fuzzy realignment:

```text
cues: 2839
body_match: true
overlap: 0
nonpositive: 0
max chars: 27
question marks: 218
quote lines: 14
avg direct match ratio: 0.98
low-match cues: 1
last time: 01:25:05.940
```

## Final validation emphasis

Mechanical checks are prerequisites, not quality scores:

```text
script line count == SRT cue count
SRT bodies == script lines
time monotonic / no overlaps / no non-positive durations
27-char max
no mechanical sentence-final periods
question marks and quotes present where rhythm requires
sample windows visually read like a single subtitle-bar architecture
```

If the user says “배치가 안 맞는다,” suspect alignment first. Re-align from the final cue body against ASR word timestamps; do not keep polishing text while timing is wrong.
