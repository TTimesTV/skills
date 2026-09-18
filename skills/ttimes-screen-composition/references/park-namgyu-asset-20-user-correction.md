# Park Nam-gyu asset 20 — persistent graphic with A/B/X callouts

Date: 2026-07-17

## Source sequence

```text
material: perovskite ABX3 crystal-structure graphic
caption 1: 페로브스카이트 = 결정구조(ABX₃)
caption 2: A = 유기 양이온 / B = 금속 양이온 / X₃ = 할로겐 음이온
caption 3: ABX₃ 원소 조합을 바꿔 효율·안정성·빛 흡수 범위를 조절할 수 있다
```

## User-confirmed implementation

The base crystal-structure graphic remains on screen. The A, B, and X information is not presented as three independent full caption cards. Arrows and labels point to the corresponding locations on the same graphic as the narration explains them.

```text
persistent base: ABX3 crystal graphic
callout 1: arrow to A + A explanation
callout 2: arrow to B + B explanation
callout 3: arrow to X + X explanation
conclusion: same structure remains while composition-change effect is summarized
spoken captions: SUPPRESS while explicit //자막 graphics are active
```

General lesson: classify editorial function separately from render form. Text marked `//자막` may be implemented inside a persistent graphic as object callouts rather than as an independent overlay card.
