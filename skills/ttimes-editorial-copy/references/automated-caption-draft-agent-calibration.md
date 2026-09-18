# Automated Caption Draft-Agent Calibration

Use this reference when designing or reviewing an agent that reads a Final Script and returns structured caption candidates under a fixed JSON schema such as `blockIndex`, `subtitle`, `type`, `reason`, `reasonShort`, and `sourceText`.

## Core principle

Do not let a broad caption taxonomy become a quota. The agent must first classify the **source beat's role**, then select only the screen layer that helps that beat:

1. interviewer question → normally one `C1` question caption
2. answerer's key claim or implication → normally one `A1` emphasis caption
3. term whose meaning is necessary for the current beat → one `B2` explainer
4. explicit source-backed list or sequence → one `C4` structure caption
5. no added comprehension or editorial value → no candidate

The preferred defaults are `A1`, `B2`, `C1`, and `C4`. Other codes remain available but are exceptions, not categories to fill.

## User-calibrated forms

### Emphasis

Normally one or two lines. Use a concrete relationship, usually:

```text
cause / condition / contrast
result / judgment / implication
```

Prefer one complete line when a second line would repeat it. Keep subject, object, direction, and confidence. Do not use `=`, `≠`, `→`, `↑`, or `↓` decoratively.

Approved style class:

```text
zHBM은 위로 쌓아 데이터 이동거리 단축
HBF는 적층 낸드로 HBM의 용량 확장
```

### Explainer

Default to one line:

```text
대상 : 목적·기능·작동
```

Do not create an explainer merely because a term appears for the first time. Create it only when the current scene is difficult to understand without it. Avoid title-plus-body cards and specialist-on-specialist definitions.

Approved style class:

```text
드라이버 요인 : 매출·성과의 변화를 이끄는 핵심 선행요인
```

### Question

Use one short, non-leading `Q.` caption preserving the answer target. Strip setup, compliments, hedges, and illustrative examples. Do not answer the question in advance.

```text
Q. 에이전트 운영 노하우를
어떻게 조직에 남길까?
```

### Structure

Use `1)~N)` only when the speaker actually gives stages, criteria, or a list. Never infer a process from an interviewer merely asking how something should be done.

## Candidate density

- default: 0–1 candidate per source block
- maximum: 2 only when they perform genuinely different layers, such as question + emphasis or explainer + emphasis
- never generate paraphrase variants merely to reach `1.5–2×` volume
- omission is preferable to generic or unsupported copy
- reaction, speech-bubble, quote, comparison, and action-tip candidates require a source-backed editorial reason; do not generate them because those type codes exist

## Question-before-answer safety

For an interviewer question block, do not invent the guest's coming answer. Common forbidden inventions include:

- manuals, documentation, handoff systems, or knowledge sharing not yet stated
- numbered steps not present in the source
- absolute principles such as `개인 의존도 제거`
- stronger labels such as `핵심 인재` when the source says only `직원`
- stronger verdicts such as `무용지물` when the source says only `문제가 있다`

## Fixed-schema field semantics

- `blockIndex`: source-block index, not candidate serial number. Multiple candidates from one source block share the same value.
- `subtitle`: final copy. Represent a planned two-line caption with ` / ` when the JSON contract does not support literal line breaks.
- `type`: the actual editorial function, not a diversity target.
- `reason`: one concise sentence explaining why this caption helps the scene. Do not defend unsupported inference.
- `reasonShort`: use a small controlled vocabulary such as `핵심 함의`, `질문 축`, `용어 이해`, `구조 정리`, `직접 인용`, `비교 강조`, `행동 지침`, or `팩트 확인 필요`.
- `sourceText`: exact contiguous source wording. Do not combine distant clauses or add words.

## Duplicate and overclaim gate

Before output, reject a candidate when any is true:

- it is a synonym variant of an existing candidate
- it converts a question into an answer
- it creates a definition merely to use `B1`
- it creates a causal chain merely to use `C5`
- it converts tentative speech into certainty
- it introduces a solution, stage, metric, attribution, or company relationship absent from the source
- it is only a generic management slogan

Example of a bad candidate cluster from one question beat:

```text
좋은 에이전트도 운영 방법을 모르면 무용지물
도구의 질 ≠ 조직의 지속성
조직 지속성 = 개인 의존도 제거
① 운영 매뉴얼 작성 / ② 인수인계 체계 / ③ 지식 공유
```

These are not useful diversity: they repeat one idea, intensify the source, or answer the question prematurely.

## Model setting

For a small constrained draft model such as Claude Haiku, start with `temperature: 0.1`. Raise temperature only after source fidelity, duplicate control, and schema compliance are stable. Diversity is not a substitute for editorial judgment.
