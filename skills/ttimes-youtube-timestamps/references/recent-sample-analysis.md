# TTimes YouTube timestamp house style — recent sample analysis

## Sample

- Channel: 티타임즈TV (`UCelFN6fJ6OY6v8pbc_SLiXA`)
- Collection date: 2026-07-15
- Scope: 10 most recent long-form uploads
- Durations: 18:15–55:59, median 25:23
- Published manual chapter lines: 85 total
- Main-body chapter lines after the first two intro slots: 65
- Korean CC: 2 videos had manual `ko`; the remainder used YouTube `ko-orig` automatic captions

## Quantitative pattern

- Chapters/video: 7–10, average 8.5
- Main-body title length: median 18 Korean characters, mean 19.15, range 6–38
- Question-form titles: 20 of 65 main-body titles
- Boundary types: question/topic setup 29/65 (44.6%); answer/core-thesis start 27/65 (41.5%); scene move, introduction, and internal pivots made up the remainder
- English or named entities appeared in 36/65 titles (55.4%); explicit hook words appeared in 15/65 (23.1%)
- First main-body chapter median start: 1:34
- Main-body spacing: median 4:00, mean 4:23, range 0:10–10:05
- Nine of ten videos used `00:00 course/promo → 00:16 or 00:17 highlight`
- The on-site K-water episode used `00:00 highlight → 00:29 intro`

The 10-second main-body spacing outlier was a guest introduction followed immediately by the first substantive question. Spacing is subordinate to editorial structure.

## Boundary-selection pattern

### Interview/talk videos

Published boundaries usually land when:

1. The host begins the setup for a new question or topic.
2. The answer opens with a distinct new thesis, conclusion, or named case.
3. A speaker reframes with `그러면`, `그렇다면`, `이제`, `결국`.
4. The named company, technology layer, risk, or market actor changes.

The sample split was nearly even: question/topic setup 44.6% and answer/core-thesis start 41.5%. If the question already carries the chapter promise, anchor to the first setup sentence—not the final question mark. If the question is generic or mixed with the previous section and the answer opens with the exact title thesis, anchor to the answer.

Examples:

```text
02:06 AI칩이란?
06:58 주요 AI칩 메이커는?
```

At 02:06 the host asks how AI chips differ from GPU/HBM. At 06:58 the discussion pivots from chip function to the companies and major players. The titles compress viewer questions rather than copying transcript sentences.

### Field/on-site videos

Boundaries land at a location move, new facility/process demonstration, or operational handoff.

```text
04:47 AI (水)운영·관리 총괄하는 중앙조정실 탐방
```

The CC transitions into moving to and explaining the central control room.

## Title-writing pattern

- Preserve central entities: `세레브라스`, `리벨리온`, `퓨리오사AI`, `실리콘 포토닉스`.
- Prefer a viewer question when the segment is organized around one.
- Use contrast/stakes when supported: `AI 버블 vs AI 슈퍼사이클`.
- Use a compact thesis when the answer is the hook: `암묵지의 데이터화가 AX의 큰 장벽`.
- Parentheses are occasional clarifiers: `(Feat. SMR, PV+ESS)`.
- Preserve useful punctuation: `?`, `?!`, quotes, `↑`.
- No final periods.
- Correct CC errors and proper nouns.
- Avoid generic labels such as `AI 이야기`, `두 번째 주제`, `향후 전망`.

## Intro/highlight rule

Do not blindly hard-code `00:16 하이라이트`. It appeared in nine of ten recent videos because those edits shared a template. CC alone may not identify a promo montage. Inspect the first 90 seconds and classify promo, highlight, intro, and body.

## Candidate algorithm evaluation

The helper scores 10-second candidates using lexical shift across ±55-second windows, question/transition markers, nearby caption gaps, and local maxima. Against 65 published body boundaries:

After reducing automatic-CC pause to a weak feature capped at 0.03:

- within ±45 seconds: 51/65 (78.5%)
- within ±60 seconds: 61/65 (93.8%)
- within ±90 seconds: 65/65 (100.0%)
- median nearest-candidate error: 20 seconds

Automatic CC durations can overlap, so pause must never determine a boundary by itself. Candidates are a recall-oriented source pack, not final timestamps. Snap the final timestamp to the first exact CC cue of the selected question, transition, or scene handoff.

## YouTube official requirements

Source: https://support.google.com/youtube/answer/9884579?hl=en

- First timestamp starts at `00:00`.
- At least 3 timestamps in ascending order.
- Every chapter is at least 10 seconds.
- Manual chapters override automatic chapters.
