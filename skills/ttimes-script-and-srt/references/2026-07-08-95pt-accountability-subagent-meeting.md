# 2026-07-08 — 95점 책임제 + subagent 회의형 TTimes 말자막 교훈

## Context
The user was frustrated that prior TTimes SRT attempts mechanically optimized line length while missing human-readable Korean segmentation, ASR/proper-noun errors, and over-polishing/omission. The user explicitly wants final-deliverable quality, not an 80% draft.

## Durable workflow lessons

### 1. Final editor responsibility belongs to Main Hermes
- Subagents are reviewers, not final authors.
- Never paste subagent `cue 후보` into the final script.
- Main Hermes must decide `채택/보류/반려` for each subagent proposal and is accountable for shipped errors.
- If an automatic segmentation pass creates ugly breaks, it is Main Hermes' fault, not the subagent's.

### 2. Use meeting minutes during long jobs
For long TTimes jobs, report intermediate meeting notes to the user:

```text
[회의록 N]
A 보고: 원문보존/ASR/용어
B 보고: 가독성/분절
C 보고: 95점 게이트/반박검수
Main Hermes 판정: 채택/보류/반려 + 이유
다음 액션
```

This is not optional when the user requests responsibility/accountability or asks to see how subagents influenced the result.

### 3. 95점 gate
- Start at 100.
- Subtract 1 point per visible subtitle error.
- Do not deliver under 95.
- If Hermes claims ≥95 and the user finds 5+ errors, treat the delivery as OUT and redo; do not defend the score.
- If Hermes claims ≥95 and quality is closer to 80 or below, apply stricter process penalty for the next run: sample approval, 98점 gate, second subagent review, and no `완료/최종` wording until user approval.

### 4. Human readability beats regex
Regex lint can help, but passing regex does not mean passing as a caption. The user expects applied Korean judgement, not pattern stuffing.

Bad breaks caught by user:

```text
어떤 / 전쟁
하나하나 좀 / 각개격파해서
설명해주셨던 / 게
애저, AWS, / GCP, 콜로서스
```

Generalize these as:
- Do not split modifier + head noun.
- Do not split dependent noun / bound noun chunks.
- Do not split predicate/complement tails.
- Do not split lists between closely related items when the list fits.
- Do not strand weak words (`어떤`, `게`, `수`, `것`, `거`, `대한`, `대해서`).

### 5. Stable transcript-like base first
The user's preferred default is not polished prose. Build a transcript-preserving stable base, then perform surgical fixes:
- ASR/proper nouns/numbers/units/case particles.
- Obvious 비문.
- 25-char visual overlength.
- Ugly line breaks.

Do **not** summarize, broadly rewrite, or omit spoken content.

### 6. Subagent review structure for long Korean tech videos
At least three roles:
- A: term/proper-noun/number/ASR review.
- B: readability/segmentation review.
- C: 95점 gate / adversarial review.

For high-stakes rework, run a second round after the main integration:
- A2: remaining term/number errors.
- B2: human-eye segmentation errors not caught by regex.
- C2: pass/fail estimated score and OUT risk.

### 7. Meeting report before final delivery
Before final file delivery, report:

```text
자체 점수: __/100
감점 내역: ...
직접 읽은 구간: first/middle/late + term-dense + quote/list sections
기계 검증: cue count, exact body match, overlap, nonpositive, max chars, low-match checked
남은 caveat: ...
```

If this cannot be honestly filled, keep editing.
