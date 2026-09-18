# Short Technical Script Revision and Ending

Use this note when drafting or revising a 45–70 second TTimes-style technical Shorts script from an official product or architecture announcement.

## Revision contract

- If the PD approves a prefix (`여기까지는 마음에 든다`), freeze that prefix. Replace only the rejected tail unless the PD explicitly requests a full integrated script.
- If the PD asks for the **full script**, return the entire integrated script in one block. Do not return only the changed fragment and make the PD splice it manually.
- When the PD says the script is long or repetitive, remove duplicate explanation beats before shortening individual sentences. Typical duplicates are:
  - `data path is shorter` followed by another paragraph restating `memory and accelerator become one`;
  - `concept/target, not product` repeated after the numbers already say `목표`;
  - company capability listed once as mechanism and again as conclusion.
- Preserve the strongest approved hook and mechanism. Compress the remainder into `metric → architectural implication → final thesis`.

## Technical announcement structure

```text
1. Physical bottleneck viewers can visualize
2. Existing layout
3. One structural change
4. Why that change affects signal/data/heat
5. Vendor-stated targets, clearly framed as targets
6. What competition shifts toward
```

The engineering mechanism must remain the body. Do not replace it with logos, strategy arrows, or generic `AI 패권` rhetoric.

## Caveat placement

A concept-stage announcement still needs claim discipline, but the caveat does not always need a separate dramatic paragraph.

- Prefer embedding status in the metric sentence: `삼성이 제시한 목표는…`.
- Add a standalone `아직 개념 모델` beat only when product maturity is itself editorially important or the numbers would otherwise be mistaken for measured shipping performance.
- Never repeat the same caveat twice. Accuracy should constrain the wording without stopping the narrative.

## Ending discipline

A technical Shorts ending should name the **new competitive axis**, not declare the vendor the winner.

Avoid unsupported victory rhetoric:

```text
삼성이 다음 경기장을 제시했다
판을 완전히 바꿨다
HBM 경쟁을 뒤집었다
```

Prefer a mechanism-grounded shift:

```text
HBM 경쟁의 다음 승부처는
가속기 위 3D 적층입니다
```

or the equivalent pattern:

```text
누가 더 빠른 메모리를 만드느냐에서
누가 가속기와 메모리를 한 몸처럼 묶느냐로
```

## Final check

- Does every paragraph introduce a new fact or implication?
- Is the company named only where it is the actor?
- Are projected figures labeled as goals rather than benchmarks?
- Does the ending follow from the mechanism instead of praising the company?
- If `full script` was requested, is the whole integrated script present?
