# Korean AI-management caption calibration — 2026-07-30

Session-specific evidence for `ttimes-editorial-copy`. These examples calibrate interpretation; only explicitly accepted wording should be treated as gold copy.

## 1. Long spoken question → one editorial axis

Source asks about large differences between companies and what early-stage users should do.

Strong compression:

```text
Q. 기업별 AI 활용 격차, 어떻게 좁혀야 할까?
```

Lesson: remove compliments and hedges, but retain the gap plus the actionable verb.

## 2. Named-company case question

Source meaning: a Company Brain must accumulate and update continuously, which may require communication and reporting systems to change; **the actual question asks how Liner does this in practice**.

Rejected because it reduced the question to a static generic category:

```text
Q. Company Brain을 위한 소통·보고 체계는?
```

Also rejected because it generalized away the named case:

```text
Q. Company Brain은 어떻게 계속 업데이트할까?
```

Corrected direction:

```text
Q. 라이너는 Company Brain을 어떻게 축적·업데이트하고 있나?
```

Lesson: separate the setup's general thesis from the final interrogative target. If the interviewer asks for a named company's case, preserve that company and ask about its actual practice. A more operational verb does not compensate for deleting the requested subject.

## 3. `어디까지 끌어낼 수 있나`

Context: before Company Brain/system integration, executives should personally use the frontier model and determine what level of useful output it can produce in their own work.

Incorrect interpretation:

```text
AI로 내 업무를 어디까지 확장할지
```

Why wrong: `업무 확장` adds a strategic-growth meaning absent from the speech. The intended object is the model's capability and practical range in the executive's existing work.

Safer direction:

```text
내 업무에서 AI의 활용 범위부터 확인
```

## 4. Abstract jargon versus deliverables

Source logic:

```text
스킬·MCP·Company Brain 같은 신조어만으로는 이해하기 어렵다
→ CEO가 구체적인 산출물 수준에서 이해하면 빠르게 의사결정할 수 있다
```

An expanded caption such as `구체적인 산출물 / 빠른 의사결정의 출발점` was rejected as too long. The concise revision was:

```text
추상적 개념보다
구체적인 산출물로 판단
```

Lesson: retain the contrast and decision object; if the PD says it is too long, compress without adding another metaphor.

## 5. Numbered AI-transformation process

Source sequence:

1. directly use current AI services
2. define new AI terms to fit the organization's existing language and system
3. connect agents to legacy systems
4. reach AI transformation

Clear literal labels are safer than abstract nominalizations:

```text
1. AI 서비스 사용
2. AI 용어를 조직 체계에 맞게 정의
3. 에이전트를 기존 시스템에 연결
4. AI 트랜스포메이션
```

When a graphic needs a title, use the destination and sequence directly:

```text
AI 트랜스포메이션으로 가는 4단계
```
