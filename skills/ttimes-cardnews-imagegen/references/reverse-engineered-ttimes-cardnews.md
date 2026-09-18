# Reverse-engineered TTimes card-news calibration

## Corpus inspected

- Source: `2026 하반기경제동향_원고_보고용.docx`
- DOCX: 194 paragraphs, no tables, no embedded images, one section
- Main paragraph style: `Normal`
- Source font: `LG스마트체 Regular`
- Red runs: 73 runs; these identify selected emphasis phrases
- Leading bold revision notes: `P15.`, `P16.`, `P22.`, `P24.`, `P27.`, `P28.`
- Source markers: `<1>` through `<28>`
- Design corpus observed: page 06; pages 07–13; page 15 video; pages 16–35; pages 37–41
- Missing from the supplied visual corpus: pages 14 and 36
- Still images: 23 at 533×800 and 9 at 600×900; all exactly 2:3
- Video card: H.264, 214×320, 5.55 seconds, 33.33 fps, no audio

This is a calibration corpus, not a universal content template. Preserve the process grammar; do not hard-code its economic claims.

## Source-to-design semantics

### Word structure

```text
[leading PXX revision notes]
[project title]
[subtitle]
<N> [optional section heading]
[body paragraphs]
<N+1>
...
<끝>
```

Observed semantics:

- red Word text becomes the principal orange/gold emphasis in the design
- black Word text becomes ordinary body copy
- `<N>` is a source beat, not always the visible output page
- a source beat can be expanded into several cards when it contains several visuals or claims
- revision notes at the beginning were added after an initial design pass

## Observed visual grammar

### Base palette

- warm ivory background
- near-black title and body
- muted burnt-orange editorial judgment
- beige/gold ornament
- purple/red reserved for chart scenarios or danger
- deep navy/black used for synthesis and final questions

### Core page types

1. **Section opener**
   - numbered ornamental medallion
   - large section title
   - representative chart or map
   - introductory body and highlighted thesis

2. **Data page**
   - black ornamental title plaque
   - chart/map/table in the upper-middle region
   - body below
   - orange interpretation
   - source and page number at lower right

3. **Photo page**
   - source photo in upper 40–50%
   - lower explanatory text
   - one orange conclusion
   - source at lower right

4. **Person/quote page**
   - person at bottom or side
   - quote/context in the remaining negative space
   - quote or interpretation accented

5. **Video page**
   - same frame as photo page
   - only the upper media window moves
   - body, highlight, credit, and page number stay static
   - short silent loop

6. **Dark conclusion page**
   - full-bleed darkened photo or generated conceptual scene
   - white body
   - gold/orange final judgment
   - used as a structural mode switch near the end

## Photo-selection grammar

Prefer direct correspondence:

```text
named person → real person photo
named event → actual event photo/video
named company/product → official or editorial source image
location or route → map
scale or trend → chart
direct quote → source person/document
abstract risk or synthesis → generated illustration or licensed stock
```

The corpus relies primarily on sourced editorial, official, institutional, and stock assets rather than generated faux-news photography. Preserve that evidence boundary.

## Text hierarchy

1. section title
2. chart/photo title or quote
3. body copy
4. orange/gold editorial judgment
5. source and page number

The orange line is not decoration. It is the page's editorial verdict. Reading only orange lines should recover the sequence's main argument.

## Pacing

Alternate visual families to reduce fatigue:

```text
chart → photo → chart → person/video → chart → dark synthesis
```

Do not enforce mechanical alternation when the argument needs consecutive data pages. Instead avoid more than three visually identical pages in a row unless explicitly approved.

## Known risks

- chart labels can become too small on 2:3 mobile cards
- source credits were visually consistent but sometimes too small for evidence review
- a subset shown as a stacked addition to its total can imply double-counting
- long body paragraphs can turn the upper photo into decoration
- page counts above 35 require strong section resets and short claims

## Calibration test

A new sequence matches this grammar when:

- every page has one claim and one dominant visual
- all source-red emphasis survives as exact accent copy
- real evidence remains real and traceable
- generated art is limited to illustration/design functions
- the contact sheet shows a consistent ivory/black/orange system
- section openers and dark conclusions are immediately identifiable
