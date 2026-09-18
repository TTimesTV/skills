---
name: ttimes-square-carousel-cover
description: Build an approved TTimes-style 1:1 carousel cover by using the exact article `_list_` image as the visual source, the corresponding TTimes/YouTube thumbnail as typography calibration, the official TTimes logo, and deterministic Korean title composition. Use this instead of regenerating or reinterpreting the cover with ImageGen.
license: MIT
metadata:
  hermes:
    tags:
    - ttimes
    - cardnews
    - carousel
    - cover
    - thumbnail
    - typography
    - square
    related_skills:
    - ttimes-cardnews-imagegen
    - practical-image-workflows
  author: Hermes Agent
  version: 1.6.0
---

# TTimes Square Carousel Cover

## Purpose

Use this skill for the **cover page only** of a square TTimes card-news carousel.

### Global typography and logo override

All TTimes square-card formats—이중학, 박영선, 일반 대담, 원맨, and new formats—use Noto Sans KR/CJK KR Black `80px` for the cover title. Format identity changes only graphic layout: title position, line count, alignment, color, crop, and composition. Do not change font size to fit. The official TTimes logo is fixed at the upper-right (`x=836`, `y=55`, `width=176` on 1080×1080). Historical approved artifacts with other sizes or an upper-left logo are provenance records, not future defaults.

### Mandatory approved-cover pair comparison

Before every new or remade cover, load `references/approved-cover-pair-global-grammar.md` and the two actual assets `references/assets/approved-lee-junghak-ai-slop-cover.png` and `references/assets/approved-park-tech-talk-mlcc-fcbga-cover.png`. Build a visual contact sheet with the target cover and compare them directly. The shared grammar is exact `_list_`, restrained dark lower gradient, large lower-third title, glyph-color emphasis only, and no invented plate/badge/profile/source. A cover may vary line count, accent color, alignment, crop, and object balance, but may not replace the lower-third hierarchy with a small upper caption or an opaque colored field. Technical `BLOCKING 0` is insufficient without this comparison.

The approved cover contract is:

```text
exact TTimes article `_list_` image
+ official TTimes logo at the upper-right
+ title styling calibrated from the corresponding TTimes YouTube thumbnail
→ 1080×1080 carousel cover
```

Do not confuse the inputs:

- `_list_` image = visual/background authority
- TTimes YouTube thumbnail = title typography, weight, compression, color hierarchy, and shadow reference
- article/user wording = title text authority
- official site logo PNG = logo authority

## Format-classification gate

Before designing the cover, classify the source on two separate axes:

1. **Named series identity** — e.g. `이중학의 사람과 기술`, `박영선의 테크토크`, `강수진 박사의 프롬프트 엔지니어링의 매직`, `30년 개발자의 기업 분석`, `AI, 안 해보면 모른다`, or `티타임즈 주간브리핑`.
2. **Production format** — one-person expert, host+guest conversation, panel, hands-on demo, weekly/news briefing, field report, or general issue analysis.

Do not collapse these into one label. `강수진` is a recurring expert/series identity; `원맨 해설형` is the production form. `박영선의 테크토크` is a named series; its thumbnail may show the host only inside the badge and one large guest, but the production form is still host+guest conversation when source metadata confirms it.

Use `references/ttimes-2026-video-format-taxonomy.md`, built from 42 actual 2026 thumbnails, for series signatures, the thumbnail decision tree, and wording-edit gates.

### Approved 박영선의 테크토크 override

Load `references/approved-park-youngsun-tech-talk-cover.md` whenever the source is confirmed as `박영선의 테크토크`.

This approved series treatment overrides generic cover starting points:

- exact article `_list_` image, center square crop
- preserve guest-on-right / technology-on-left visual composition
- official TTimes logo at **upper-right**
- use the target thumbnail's lower two-line title grammar
- white setup line + teal claim line, adjusted to the actual image
- **no title highlighter, color box, opaque plate, or key-line rectangle**
- **no typed series name/badge** on the square cover
- **no guest profile, role, date, source, or timecode** on the cover
- do not arbitrarily rebuild the episode title into a new multi-line hierarchy

The approved asset is `references/assets/approved-park-tech-talk-mlcc-fcbga-cover.png`. Its wording is episode-specific; reuse the grammar, not the phrase.

### TTimes 일반 대담형 profile

For a general TTimes host–guest interview without a named-series cover identity, load `references/general-interview-cover-profile.json` and invoke the builder with `--profile general-interview`. Use the exact `_list_` visual and the matching YouTube thumbnail's hierarchy. The official TTimes logo is fixed at the upper-right (`x=836`, `y=55`, `width=176` on 1080×1080). Title plates, rounded panels, guest profiles, source labels, and timecodes are blocking errors. A new series may establish new colors and layout, but it may not change the `_list_` cover-only asset role.

### TTimes 원맨 해설형 profile

For verified F1 one-person explainers, load `references/one-person-cover-profile.json` and invoke the builder with `--profile one-person`. A one-person production does not require a presenter face on the cover: preserve the exact `_list_` subject, whether it is a person, robot, product, company, or field scene. Use the target YouTube thumbnail for wording, line hierarchy, and accent color, while the approved 이중학·박영선 pair supplies the square-cover lower-third grammar. Do not copy an opaque/red thumbnail title field into the square cover. Do not invent a person or series badge.

### Thumbnail wording preservation

- Preserve the supplied/current thumbnail wording by default.
- Edit only when it is materially too long for mobile hierarchy, covers key visual evidence, repeats itself, is genuinely unintelligible/incorrect, conflicts with the image, duplicates the series badge, or uses unverified quotation marks.
- If edited, preserve subject, action, causality, comparison, numbers, scope, certainty, and question-vs-assertion status.
- Any compression, reordering, or paraphrase becomes an editorial title without quotation marks. Exact quotes require audio-confirmed wording and speaker attribution.
- Series-specific character/line ranges are fit-search starting points, never hard limits.

## Blocking Rule: Never Regenerate the Cover Visual

The cover is not an ImageGen reinterpretation.

- Fetch and preserve the exact TTimes `_list_` image belonging to the target article.
- Center-crop it to the square presentation used by the site and resize to 1080×1080.
- Add only the official logo, title, and a restrained readability gradient/shadow.
- Do not replace the people, objects, setting, or composition with a generated illustration.
- ImageGen remains mandatory for newly created **body-card visual layers** under the parent card-news workflow, but not for this sourced cover.

This distinction was explicitly approved by the user after rejecting a generated substitute cover.

## 1. Acquire the Two Reference Assets

### A. Visual authority: article `_list_` image

Open the exact TTimes article and obtain its `og:image` or list-page thumbnail URL. Confirm that the filename contains `_list_` and that the article ID matches.

Example pattern:

```text
https://img.ttimes.co.kr/img/YYYYMM/ARTICLE_ID_list_SUFFIX.jpg
```

Hash and record the downloaded source. Do not use a nearby article image or YouTube thumbnail as the background.

### B. Typography calibration: corresponding TTimes YouTube thumbnail

Extract the article's embedded YouTube video ID and obtain:

```text
https://i.ytimg.com/vi/VIDEO_ID/maxresdefault.jpg
```

Use it only to calibrate title typography and color. Do not replace the `_list_` image with it.

## 2. Square Crop

TTimes `_list_` files may not be physically square even when displayed as a 1:1 list image. The approved example was 1185×997.

Default transformation:

```text
center square crop → Lanczos resize → 1080×1080
```

Use center crop by default because it matches ordinary `object-fit: cover` presentation. If the site's rendered square visibly uses a different focal position, reproduce the rendered crop rather than blindly centering.

## 3. Official Logo

Use the actual TTimes logo asset from `ttimes.co.kr`, not typed text.

All 1080-square covers use:

```text
position: x=836, y=55
rendered width: 176 px
preserve aspect ratio
```

Use the light-on-dark/near-white logo variant. Verify that the upper-right logo remains fully inside the safe area and has sufficient contrast.

## 4. Title Typography: Fixed Family and Size, Variable Graphic Layout

The exact internal thumbnail font file is not publicly verifiable from raster pixels alone. The corresponding TTimes YouTube thumbnail visually matches a compressed neo-grotesque Korean Black face.

Preferred order:

1. `Sandoll GothicNeo` Heavy/Black when a properly licensed file is supplied
2. `Noto Sans CJK KR Black` / `Noto Sans KR Black` as the approved reproducible fallback
3. `Pretendard Black` if Noto is unavailable

Do not claim that the website's use of `Noto Sans KR` proves the thumbnail's production font. It only supports Noto as a practical fallback.

### The approved example is calibration, not a template

The first approved AI-slop cover happened to use `79 px`, `90%` horizontal compression, white plus `#93A6FF`, and two lower-left lines. It remains a historical composition reference. New and remade covers use the global `80px` title and upper-right logo; line count, position, alignment, compression within the approved range, and color remain graphic-layout variables.

### Recent-thumbnail classification gate

Before composing a new cover, inspect the target thumbnail plus several current TTimes thumbnails. The 2026-08-29 ten-thumbnail corpus showed these families:

| Family | Structure | Typical emphasis |
|---|---|---|
| two-line thesis | setup/subject → result/question | white base line + one colored key line |
| three-line comparison | category → subjects/condition → result | category or result receives one accent color |
| terminology label + two-line title | small concept label above a larger explanation | label colored; title usually white |
| multi-event digest | several independent event boxes + one synthesis title | white boxes, warning/coral accents |
| warning/question box | neutral first line + boxed final question | red/coral box rather than a fixed text color |

See `references/recent-thumbnail-classification-20260829.md` for the audited examples and measured ranges.

### Fixed 80px line-fit procedure

1. Protect faces, products, logos, and the main action in the square-cropped `_list_` image.
2. Define the actual title rectangle from the remaining simple/low-detail area.
3. Segment the title by meaning: `subject/setup → action/result/question`. Start with two lines, but allow one, three, a small label plus two lines, or event boxes.
4. Render the chosen Black font at exactly 80px. The longest line should occupy roughly 85–95% of the available width without clipping.
5. If the block does not fit, try in this order: better semantic line breaks → tighter line gap → mild horizontal compression → one additional line → editorial wording revision. Do not reduce the 80px font.
6. Keep horizontal scale within roughly 88–100% unless the current reference clearly supports another value. Do not crush a long title merely to preserve two lines.
7. Keep the 80px font fixed across every format; only graphic composition varies.

### Variable color procedure

Use white as the neutral/base line, then select at most one main accent family from meaning **and** background contrast:

| Meaning/background | Candidate family observed in recent thumbnails |
|---|---|
| technology, efficiency, comparison result | mint/teal |
| AI screen or digital experiment | electric blue |
| conceptual AI or organization problem | purple/periwinkle |
| everyday curiosity or playful question | yellow |
| conflict, danger, warning | coral/red, often as a box |

Choose the exact color by sampling the actual background and verifying luminance/contrast. Do not make `#93A6FF` the default. Prefer one colored **line**; use word-level colors only when a full-line emphasis is semantically wrong, and avoid three or more colors in one line.

### Variable position and contrast procedure

- Lower-left is the first candidate, not a mandatory anchor.
- Move to left-middle or lower-center when the subject occupies the lower-left.
- Select among background-matched dark gradient, soft shadow, opaque key-line box, or strong outline according to the image. Use the lightest intervention that keeps mobile-size text readable.
- Bright/complex photography may require an outline or box; dark technical imagery usually needs only a gradient and shadow.

### Wording hierarchy

- Use white for neutral setup/context unless the current thumbnail shows another hierarchy.
- Give one result, reversal, question, number, or utility line the selected accent treatment.
- Treat two lines as the first candidate, not a hard requirement.
- Do not add a subtitle, speaker label, badge, or date unless the user requests it.
- For `박영선의 테크토크`, the approved no-badge/no-profile rule is blocking, and title glyphs must not sit on fluorescent markers or colored boxes.

## 5. Readability Treatment

Preserve the list image and choose the treatment after inspecting it. A restrained lower gradient is preferred for dark/simple imagery, but current TTimes thumbnails also use outlines, term labels, independent event boxes, and red warning boxes where the content/background calls for them. Do not place an opaque box over a face or essential object.

## 6. Reusable Builder

Run:

```bash
python scripts/build_cover.py \
  --list-image /path/to/article_list.jpg \
  --logo /path/to/official_ttimes_logo.png \
  --font /path/to/NotoSansCJKkr-Black.otf \
  --line "AI로 만든 그럴듯한 보고서" \
  --line "AI 슬롭에 리더는 괴롭다" \
  --color '#FDFDFD' \
  --color '#93A6FF' \
  --output /path/to/00_cover.png
```

The example colors reproduce the approved AI-slop cover only. For a new cover, the editorial/visual classification step must choose new `--color` values. The builder auto-fits size and mild horizontal compression unless explicitly overridden.

If `--font` is omitted, the script checks common macOS font locations; on other systems supply --font explicitly. Fail closed if no suitable Black Korean font exists; do not silently use a materially different face.

## 7. QA Gate

Before delivery, verify:

- exact source article and matching `_list_` provenance
- exact official logo asset
- final size exactly 1080×1080
- title text exact, with no invented wording
- logo at top-left, uncut and legible
- title size, line count, position, and accent color justified against the target/current thumbnails rather than copied from the calibration example
- no text clipping or overlap
- no essential face/object blocked by title
- source visual preserved; no generated substitute
- SHA-256 recorded
- visual review reports zero blocking findings

## Approved Calibration

See `references/approved-ai-slop-cover.md` for the approved example, hashes, source URLs, and the exact acceptance history.

See `references/approved-park-youngsun-tech-talk-cover.md` for the approved 박영선 series cover, source hashes, rejected variants, and the no-highlighter series override.
