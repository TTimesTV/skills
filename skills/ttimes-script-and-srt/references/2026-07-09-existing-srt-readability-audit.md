# Existing TTimes SRT readability audit mode (2026-07-09)

## Trigger

Use this when the user asks to **검수 / review / audit** an existing Korean TTimes 말자막 SRT draft for readability and segmentation errors, especially when they did not ask to regenerate or rewrite the file.

## What worked

1. Treat the task as an **audit**, not a rebuild.
   - Do not edit the SRT unless the user explicitly asks for fixes to be applied.
   - Report concrete cue numbers and replacement suggestions.
2. Parse the SRT mechanically first:
   - cue count
   - first/last cue
   - selected time windows requested or inferred
   - visible-length checks
   - periods/full stops in body lines
   - obvious orphan cue bodies such as `AI를`, `저희가`, `충분히`, `역사`, `로우`, `지금 더`, `내려와야`, `생각을`, `대표를`.
3. Inspect representative windows, not just regex hits.
   - For long files, a useful default sample is: first 5 minutes, one middle 10-minute block, one late 10–15-minute block.
   - When the user only asks for a quick 검수, a sampled audit with clear caveat is better than pretending to have fully reviewed every cue.
4. Categorize findings into:
   - orphaned particles/objects/adverbs/connectors
   - speaker-turn/question-answer packing in one cue
   - sentence-final period/full stop violations
   - ASR/proper-noun/number/unit errors
   - phrase/predicate split problems
   - ending-section mechanical splits.
5. Provide **actionable rewrite candidates** in Korean, grouped by cue range.
   - Keep the response concise. The user wanted 검수, not a long process report.
   - Say whether files were modified.

## Common lint patterns from this audit

Examples of errors to flag:

```text
AI를 / 데리고 일할 수 있지
저희가 / 주가의 향방을...
지금 더 / 지어져야 되는 상황이고
가격이 / 어떻게
충분히 / 경청하고
역사 / 이래로
로우 / 리턴이었고
생각을 / 해요
대표를 / 만난 이유는
```

ASR/proper-noun traps seen in AI/semiconductor discussion:

```text
잠재매주 -> 잠재 매출
웹도독 -> 웩더독
하이니스 -> 하이닉스
지퓨 -> GPU
출원하건대 -> 추산컨대 (context-dependent)
D램은 만들 -> 예전에 만들던 D램은 (context-dependent)
8명 -> 89조 (context-dependent)
펫 -> 팹
필리퍼레이아이 -> 피지컬 AI
구근 -> 국운
사이마리 -> SMR
XAI -> xAI
```

## Suggested audit output shape

```text
검수 완료. 파일은 수정하지 않았습니다.
대상: <path or filename>
범위: <sample windows or full scan>

핵심 발견
- ...

수정 제안
### 첫 5분
- cue 9~16: 문제 ... / 제안 ...

### 45~55분
- cue ...

파일 변경
- 없음
```

## Pitfall

Do not overclaim full 95-point review when only sampled windows were inspected. Say exactly what was scanned mechanically and what was manually reviewed.
