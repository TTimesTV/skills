# User-authored TTimes caption calibration — 2026-08-27

Use this reference when drafting or reviewing TTimes interview emphasis, explainer, question, quote, reaction, and structure captions. It consolidates the user's own final documents, including the Yoon Myung-hoon and Park Nam-gyu interviews.

## 1. The user's emphasis style is editing copy, not report-summary prose

Prefer a vivid source beat, irony, reaction, contrast, or concrete operational consequence over a polished management-summary sentence.

Approved texture:

```text
오히려 늘어난 복잡성!
산책에서 경주로...
더 할 생각만 하지 뺄 생각은 안하는...
'그건 니가 그냥 알아서 해'
하던대로 하면 결국 우하향
안 할 이유만 잔뜩 늘어나는 데이터 분석의 함정
```

Rejected reframing:

```text
새로운 일 추가 = 기존 일을 뺀다는 결정
동기 부여보다 동기 훼손하지 않기가 중요
자율성 ≠ 목표 부재 / 목적·목표는 명확하게, 방법은 자율적으로
AI 서비스의 현실 / 데모는 완벽하지만 실데이터에서 무너짐
```

Why: these are grammatically polished but flatten the speaker's texture into generic report headings or manufacture a cleaner thesis than the source supplied.

## 2. Multiple captions in one source block are valid when screen functions differ

Do not enforce one candidate per block. The user may deliberately layer several captions at one beat:

```text
훨씬 늘어난 것 같습니다            # direct conclusion
오히려 늘어난 복잡성!               # reversal/reaction
산책에서 경주로...                   # metaphor compression
조율하고 관리하는 업무는 오히려 증가 # operational implication
```

These are not duplicates because they serve different editorial functions. Remove only synonym variants that deliver the same screen beat.

## 3. Directly authored markers in a DOCX are gold, not inspiration

When the authoritative source contains `//자막`, `//용어`, `Q.`, or an explicitly direct-registered caption:

1. Extract it unchanged as the priority candidate.
2. Preserve its punctuation, ellipsis, quote texture, and line logic unless the user requests correction.
3. Do not replace it with a generic paraphrase of the surrounding speech.
4. Add a new candidate only if it serves a genuinely different layer.
5. Treat `//자료`, `//그래픽`, source notes, object notes, and parenthetical editor instructions as production metadata—not caption copy.

Example:

```text
//자막
더 할 생각만 하지 뺄 생각은 안하는...
```

Do not replace with:

```text
새로운 일 추가 = 기존 일을 뺀다는 결정
```

## 4. Question, explainer, structure, and emphasis are distinct layers

### Question

One short, non-leading axis:

```text
Q. AI 도입 후 조직의 의사결정은 어떻게 달라졌나?
Q. 미래 성과를 어떤 지표로 증명할 수 있을까?
Q. 페로브스카이트 상용화의 걸림돌은?
```

Do not pre-answer the question with invented steps.

### Explainer

Viewer-readable `대상 : 목적·기능·작동`, with detail only when the current mechanism requires it:

```text
암묵지 : 문서로 정리되지 않았지만 경험을 통해 몸에 밴 지식과 노하우
AI 슬롭 : AI가 대량으로 생성한 저품질 콘텐츠
트랩 = 전자가 결함에 갇혀버리는 현상
산업 전기화 : 공장과 산업현장에서 화석연료로 만들던 동력과 열을 전기로 대체하는 전환
```

Keep formal definition and spoken metaphor as separate layers.

### Structure

Use only source-backed items, without invented ranks or parenthetical labels:

```text
1) 깡통 에이전트
2) 스킬 장착 에이전트
3) 스킬·페르소나 장착 에이전트
```

## 5. Preserve concrete physical mechanism before numeric inventory

The Park Nam-gyu final document frequently uses mechanism captions instead of dumping figures:

```text
흡광계수가 높아
두께가 얇아도 되는 페로브스카이트

흡광계수가 낮아
두께가 두꺼워야 빛을 흡수하는 실리콘
```

A raw `200~300㎛ vs 0.8~1㎛` candidate may support a graphic, but it must not replace the causal explanation when that mechanism is the scene's teaching point.

## 6. Never glue keywords into fake screen copy

Bad:

```text
AI 데이터센터 전력난 / 우주 산업 확대 태양전지가 다시 각광을 받고 있습니다
지구 온난화 → AI 데이터센터 전력난 태양전지의 역할이 확대되고 있습니다
```

The first is a keyword pile; the second invents a causal chain. Resolve the source into parallel causes and result first:

```text
AI 데이터센터 전력난·우주 산업 확대
다시 주목받는 태양전지
```

Before using `→`, verify that the source explicitly supports left-causes-right. Parallel drivers use `·`, `와/과`, or separate candidates. `/` is not a generic line-break token; use it only for a real comparison or parallel relation.

Reject a candidate when:

- three or more key nouns are concatenated without grammatical relation;
- two lines have no explainable causal, contrastive, definitional, or parallel relation;
- a report ending such as `~하고 있습니다` merely summarizes speech;
- `해결`, `완벽`, `무너짐`, `근본 원인`, or similar wording exceeds the source;
- the candidate collapses multiple visual beats into one mega-summary.

## 7. Symbols are allowed when the relationship is real

Approved:

```text
리더 = 책임을 지는 사람
만드는 사람 ≠ 쓰는 사람
이상기후 = 탄소 배출↑ 때문
화석 연료에서 청정 에너지로!
```

Rejected:

```text
조직 지속성 = 개인 의존도 제거
좋은 에이전트 ≠ 지속 가능한 조직
```

The issue is unsupported logic, not the symbol itself.

## 8. Candidate selection hierarchy

For each source block:

1. Preserve existing direct-registered captions.
2. Find source phrases with memorable voice, irony, reaction, or metaphor.
3. Add question/explainer/structure only when that layer is genuinely needed.
4. Paraphrase minimally when direct speech is too long or context-dependent.
5. Permit multiple candidates only when their screen functions differ.
6. Remove abstract report headings when a concrete source-backed phrase exists.
7. Audit subject, confidence, causality, number, and speaker attribution.
