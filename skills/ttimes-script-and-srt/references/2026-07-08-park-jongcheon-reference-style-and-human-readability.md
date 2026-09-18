# Park Jongcheon reference-style TTimes caption workflow (2026-07-08)

## Trigger

The user compared a later AI-chip SRT attempt against `250708_박종천_AI데이터센터_인지부채_srt.txt` and said the Park Jongcheon version was not perfect but was much faster and substantially better in practical quality. The user then corrected the workflow and readability approach with high frustration.

## What the user liked in the Park Jongcheon reference

Measured profile of the reference file:

```text
cue count: 830
avg visible chars: ~17.1
max visible chars: 33
over25: 133
over28: 67
<=7 chars: 72
```

Important interpretation: the user's preferred “accurate” feel was **not** strict mechanical 25-character compliance. It was a transcript-close, rhythm-preserving, lightly edited broadcast caption style.

## Updated style law

Use this priority order for this user's TTimes 말자막:

```text
meaning closure
→ protected phrase / grammar preservation
→ speaker rhythm and broadcast function
→ on-screen dwell time
→ character count
```

The user later clarified:

- 25 characters should still be the normal target.
- 27 visible Korean characters is the practical max.
- But do not destroy human readability to hit 25.
- User will point out issues; treat those corrections as style law and patch accordingly.

## Workflow law

Do **not** have subagents write final caption chunks for this task class. That caused tone drift and inconsistent rhythm.

Correct roles:

```text
Main Hermes:
- reads the full ASR/media flow
- owns the single editorial rhythm
- creates the transcript-close Gem1/Gem2-style script
- integrates corrections
- aligns to MLX timestamps

Subagents:
- review terms/numbers/proper nouns
- review human readability and cue boundaries
- review omissions/distortion
- do not author final cue files by chunk
```

If speed matters, use subagents as reviewers while Main keeps authorship. Splitting the whole 75-minute video into part1/part2/part3 and letting subagents generate caption bodies produced a result that the user said felt wrong.

## Gem1 equivalent

Minimal correction only:

- obvious ASR errors
- particles/endings/spacing that make Korean ungrammatical
- proper nouns, product names, numbers, units
- light filler cleanup only when meaning/rhythm is unaffected

Do not:

- rewrite the speaker into formal prose
- summarize
- omit cut-edit fragments just because they look rough
- flatten the speaker's joke/analogy/rhythm

## Gem2 equivalent

Segment by human readability, not word packing.

Bad pattern seen in failed output:

```text
오늘 또 바이라인 네트워크의 심재석 대표님 그리고 최용식
아웃스탠딩 창업자님 모셨습니다. 안녕하십니까?
```

User-preferred pattern:

```text
오늘 또 바이라인네트워크 심재석 대표님
그리고 최용식 아웃스탠딩 창업자님 모셨습니다
안녕하십니까?
```

Why: it respects broadcast function and semantic blocks:

```text
[소속+이름+직함]
[그리고 소속+이름+직함+진행 멘트]
[인사]
```

## Protected broadcast-function patterns

### Speaker/guest introduction

Prefer:

```text
오늘 또 [소속+이름+직함]
그리고 [이름+소속+직함] 모셨습니다
안녕하십니까?
```

Avoid splitting between a person's name and affiliation/title.

### Questions

Prefer:

```text
일단 [개념]이라는 단어 자체가
좀 궁금하거든요
```

### Topic transitions

Keep the setup and topic pivot readable:

```text
그래서 오늘은 [주제]에 대해
한번 살펴보도록 하겠습니다
```

### Lists and terms

Keep list items and fixed terms together when possible:

```text
구글, AWS, 마이크로소프트
트레이니엄과 인퍼런시아
MTIA와 마이아
1조 3000억 원
80~90%
```

## Filename lesson

Do not expose internal workflow labels like `Gem1Gem2`, `refstyle`, or `박종천식` in the deliverable filename unless explicitly requested. Use human-facing topic names:

```text
YYMMDD_AI칩_GPU일변도_소버린AI_srt.txt
```

## Failure mode to avoid

Bad loop:

```text
ASR 전체 → strict char packing → subagents author chunks → Main concatenates → repeated lint/FAIL → global patching
```

Better loop:

```text
ASR/media → Main transcript-close stable script → Gem1 minimal correction → Gem2 human-readable segmentation → subagent review only → Main patch → MLX alignment → deliver *_srt.txt
```
