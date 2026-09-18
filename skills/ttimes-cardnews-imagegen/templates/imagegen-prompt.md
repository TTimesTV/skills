# Image-generation prompt templates

Use one page per call. Attach 1–3 approved cards of the same template family as style references.

## Common style block

```text
Create the visual design layer for one premium Korean business-report card-news page.
Portrait composition. The final delivery will be center-cropped to an exact 2:3 ratio, so keep every important subject and visual element inside the central 2:3 safe region and leave generous top and bottom crop tolerance.

Style: restrained Korean corporate strategy report, warm ivory paper background, near-black ink, muted burnt-orange editorial accent, subtle beige-gold ornaments, crisp geometric spacing, high-end editorial photography or clean data-report framing, no playful social-media stickers, no neon tech clichés, no fake UI, no decorative clutter.

Important: do not render Korean paragraphs, chart values, source credits, page numbers, logos, or fake newspaper text. Leave clean negative-space regions for exact typography and data to be added later. No watermark. No gibberish glyphs.
```

## D1 — data/chart base

```text
[COMMON STYLE BLOCK]

Template: data/chart page.
Reserve a clean black ornamental title plaque near the upper area, with no lettering.
Reserve a large rectangular chart area in the upper-middle part of the 2:3 safe region.
Keep the lower 40–45% as calm ivory negative space for body copy and one orange judgment line.
Keep a small clean lower-right zone for source credit and page number.
Do not invent chart lines, labels, values, legends, axes, or logos.
```

## P1 — sourced photo page

```text
[COMMON STYLE BLOCK]

Template: factual photo page.
Use the attached real source photo faithfully in the upper 42–50% of the central safe region.
Crop without altering the identity, event, uniforms, logos, or factual scene.
Preserve faces and direct gaze or movement toward the text area when possible.
Leave the lower area clean for exact body copy and one highlighted judgment.
Do not synthesize extra people, signs, military equipment, products, or event details.
```

## Q1 — person/quote page

```text
[COMMON STYLE BLOCK]

Template: person and quote page.
Use the attached real portrait faithfully. Place the person in the lower-right or lower-left with natural editorial crop and ample negative space facing the subject.
Use a subtle dark-to-ivory tonal transition behind the subject.
Leave large empty space for exact quote, context, speaker identity, and source.
Do not generate quotation text or modify the person's identity.
```

## C1 — dark conclusion page

```text
Create one premium dark conclusion card for a Korean corporate strategy report.
Central 2:3 safe region. Deep navy-black background, cinematic but restrained, low-saturation realistic conceptual imagery representing [CONCEPT], subtle world/industry/financial structure, strong lower gradient for white body copy, one clean region for a gold-orange concluding judgment, no text, no logos, no fake charts, no sci-fi holograms, no alarmist disaster cliché.
```

## S1 — section opener

```text
[COMMON STYLE BLOCK]

Template: section opener.
Reserve space for a large ornate numbered medallion in the upper-left and a bold two-line section title beside it, but do not render text or numbers.
Add a thin elegant gold divider.
Reserve the middle area for one representative chart or map.
Leave lower space for a short section thesis.
The page must feel like a chapter opening, not an ordinary chart page.
```

## Negative prompt checklist

Always prohibit:

- generated Korean body copy
- invented statistics
- fake Bloomberg/Reuters/News1 credits
- synthetic public-figure news events
- tiny illegible labels
- UI dashboards unrelated to the claim
- generic handshake, typing, hologram, or glowing-AI-brain clichés
- ornate decoration that competes with evidence
