# Recent TTimes thumbnail classification — 2026-08-29

## Corpus

Ten newest video entries visible on `https://www.ttimes.co.kr/video` were frozen on 2026-08-29. Each article's embedded YouTube `maxresdefault.jpg` was inspected at 1280×720. Measurements below are visual estimates, not source-design metadata.

| No. | Display-title structure | Estimated size/width | Accent treatment |
|---|---|---|---|
| 01 | two lines: AI report setup → AI-slop leadership cost | about 75–86 px; about 90–96% width scale | white + periwinkle key line |
| 02 | monthly label + four event boxes + synthesis line | label 45–52 px; boxes 50–58; synthesis 72–82 | white boxes + coral/red framing |
| 03 | two lines: memory-demand condition → 300% MLCC/FC-BGA result | about 66–75 px; about 86–93% | white + teal result line |
| 04 | two-line everyday question about laundry-folding robots | about 72–88 px; about 88–95% | white + yellow question line, strong dark outline |
| 05 | small terminology label + two-line explanatory title | label 48–56; title 68–77 | teal label + white title |
| 06 | three-line US/China AI-model comparison | first 65–74; later 59–68; about 85–92% | mint category line + white explanation |
| 07 | three lines: Gemini ranking disappearance → two-part question | about 72–83; about 88–95% | white phenomenon + teal question block |
| 08 | two lines: expert attribution → six promising technologies | about 69–79; about 88–94% | white attribution + teal utility line |
| 09 | two lines: KAIST lab → stock-investing AI-agent experiment | about 68–78; about 86–93% | white subject + electric-blue experiment line |
| 10 | two lines: escaping safeguards → warning question | about 65–76; about 88–94% | white first line + white text on red warning box |

## Stable grammar

- Black/900 Korean neo-grotesque sans; exact internal font file unproven
- left-aligned title block
- meaningful line breaks rather than character-count-only wrapping
- white neutral text plus no more than one main accent family
- at least one contrast device: dark gradient, shadow, outline, label, or box
- subject/action area protected before title placement

## Variable grammar

- one, two, or three main lines
- separate terminology label or multi-event boxes
- font size and horizontal scale
- title anchor and usable width
- accent family: teal, electric blue, periwinkle, yellow, coral/red
- emphasis form: colored line, label, background box, or outline

## Decision sequence

```text
freeze target thumbnail and `_list_` image
→ identify subject-safe and title-safe regions
→ segment title into subject/setup/action/result/question/label
→ test two lines first, then one/three/label/box variants
→ render largest readable Black type into the actual title rectangle
→ rebalance line breaks before shrinking
→ use 88–100% horizontal scale only as mild fit correction
→ choose one accent family from meaning and actual background contrast
→ select gradient/shadow/outline/box treatment
→ inspect at full size and mobile thumbnail size
```

## Palette families observed

- neutral white: `#F7F7F7`–`#FFFFFF`
- mint/teal: roughly `#00DCCB`–`#00F0B5`
- electric blue: roughly `#0870EE`–`#1580FF`
- periwinkle/purple-blue: roughly `#8FA4F5`–`#9AABFF`
- yellow: roughly `#FFE600`–`#FFF200`
- coral/red: roughly `#F5222D`–`#FF5154`

These are observed ranges, not brand constants. Select and verify against the current source image.
