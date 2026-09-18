# Segmentation-first redo after a 45-point failure

## Session signal

A long Korean TTimes-style SRT job produced a file that passed mechanical checks but failed the actual user goal. The user clarified that the assignment was a **분절 업무**. Therefore, if segmentation/readability is bad, the whole score is bad even when SRT timing, 27-char max, and term scans pass.

## What went wrong

Mechanical success was mistaken for deliverable quality:

```text
SRT format/timing: OK
27-char max: OK
body periods: OK
major term scan: mostly OK
segmentation/readability: ~45점
```

Visible bad cue patterns included:

```text
분들도
AI를
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

These are not merely aesthetic problems. They break small-sentence readability because particles, objects, adverbials, or connectors are stranded away from their predicate or meaning unit.

## Correct scoring rule

For an explicit segmentation task:

```text
final score = segmentation/readability score dominated
```

Do not average upward with high mechanical scores. If segmentation is 45, the deliverable is about 45, not 70–90.

## Correct redo workflow

Do not immediately regenerate the full 85-minute file.

1. Archive the failed SRT as a reference only.
2. Extract a short sample, usually 0–3 minutes, from the ASR substrate.
3. Produce **caption body only** for that sample.
4. Keep small-sentence readability first:
   - sentence/thought end → next cue
   - noun/target + predicate/judgment where possible
   - no stranded `AI를`, `분들도`, `저희가`, etc.
   - no object/adverbial/time phrase isolated from its predicate
   - 25-char target / 27-char max, counting spaces
5. Run a quick lint on the sample:
   - max length including spaces
   - orphan cue list
   - very short cue list
6. Ask the user whether the sample rhythm is OK before processing the whole file.
7. Only after approval, split the full job into parts (e.g. 10-minute chunks), have subagents review part drafts, then Main integrates.
8. Align final caption bodies to MLX word timestamps at the end.

## Example: better 0–3 min sample shape

Bad mechanical split:

```text
요새 AI 때문에 아마 리더와 갈등이 있으신
분들도
또 본인이 리더시라고 하면은
AI를
나는 어떻게 쓸까?
```

Better segmentation-first split:

```text
요새 AI 때문에
리더와 갈등이 있으신 분들도 많고
또 본인이 리더시라면
AI를 나는 어떻게 쓸까?
우리 팀은 어떻게 활용해야 될까?
이런 고민이 많으신 것 같습니다
```

Bad:

```text
AI를 그래도 계속
취재하고
쓰는 친구다 보니까
```

Better:

```text
AI를 그래도 계속 취재하고 쓰는 친구다 보니까
주위에서 어려움을 많이 토로하는데
두 가지 같아요
```

## Practical lesson

For long SRT jobs, a `sample-first approval gate` is not optional after a segmentation failure. It prevents repeating the same wrong global rhythm over 60–90 minutes of content.
