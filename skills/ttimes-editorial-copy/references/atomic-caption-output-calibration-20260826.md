# Atomic TTimes caption output calibration

## Trigger

Use for terse, single-object production requests such as `스킬 설명자막`, `드라이버 요인 설명자막`, or a pasted speech beat followed by `질문자막`.

## Explainer output contract

A simple named-term explainer is exactly one physical line in one plain code block:

```text
용어 : 대상이 무엇이며 어떤 목적·방식으로 작동하는지 설명
```

Approved session example:

```text
스킬 : AI 에이전트의 업무 절차·규칙·도구 사용법을 정리한 지침
```

Do not return a standalone title plus multiline body, headings, rationale, alternatives, or prose around the block. Use a multiline concept card only when the PD explicitly requests a detailed/historical card or provides an approved multiline exemplar.

## Question-caption calibration

Find the answer's underlying strategic objective rather than literally compressing every setup clause. For a source beat about a skilled employee leaving and preserving agent-operation continuity, the preferred editorial axis was:

```text
Q. 잘 만든 에이전트를 조직의 자산으로 남기려면?
```

This was preferred over variants focused narrowly on employee departure, maintenance, or handoff. When the PD requests ten candidates, vary the actual editorial axis; after the PD selects one, freeze the selected wording.

## Routing lesson

For one terse caption request, `ttimes-editorial-copy` is the governing skill. Its copy-only atomic contract outranks the broader caption-plan output in `caption-layering-workflow`, even when the broader skill was already loaded earlier in the conversation.
