# Approved 박영선의 테크토크 square cover — MLCC·FC-BGA

## Status

- User approval: 2026-08-29
- Series: `박영선의 테크토크`
- Production format: host 박영선 + guest 박철민 대담
- This reference is the **series-specific cover authority** when it conflicts with generic TTimes cover defaults.

## Source lock

- YouTube: `https://youtu.be/NjvhhBT8xA0`
- Article: `https://www.ttimes.co.kr/article/2026082717417774738`
- Article `_list_`: `https://img.ttimes.co.kr/img/202608/2026082717417774738_list_24212.jpg`
- Downloaded `_list_` SHA-256: `85083b07dcf0d9162d02936c9c45be9d97ad365f8410aae11a090e93c7193fd0`
- YouTube maxres SHA-256: `ac13605caf4163515f2c2fa4750d367667825af3a068473d408ae1ec56d8f243`
- Approved 1080×1080 cover: `assets/approved-park-tech-talk-mlcc-fcbga-cover.png`
- Approved cover SHA-256: `70551267b29eb731490c1eb056bb5ca4f06e6f2ebf6a8cfc913380b5d27e1d07`

## Approved cover grammar

> Historical approval note: this artifact records the approved episode composition. Future and remade square cards use the global 80px cover title and upper-right TTimes logo. Series-specific variation is graphic layout only.

```text
exact article `_list_` image
→ center square crop
→ restrained dark lower gradient
→ official TTimes logo at upper-right
→ large two-line title across the lower field
```

### Fixed series rules

1. Do not generate or reinterpret the cover visual with ImageGen.
2. Use the exact article `_list_` image and preserve its guest-on-right / technology-on-left composition.
3. **Do not add** the `박영선의 테크토크` badge or typed series name to the square card cover. The YouTube badge is a typography/layout reference only.
4. Do not add guest name, role, date, source, subtitle, or any lower-left profile label.
5. Use the target YouTube thumbnail's lower two-line title structure unless the episode's actual wording cannot fit without harming the face or core object.
6. Neutral/setup line: white. Main claim line: teal/cyan. Recalibrate exact teal for the target image.
7. **No fluorescent marker, colored text box, opaque key-line rectangle, or background plate on the cover title.** Color the glyphs only.
8. Protect the guest's face. Lower torso overlap is acceptable only when it follows the target thumbnail's original lower-title structure and remains readable.
9. Use the official TTimes logo at the **upper-right** for this series. This overrides the generic upper-left logo starting point.
10. Title line count is normally two for this series, but wording and the current thumbnail remain the authority; do not mechanically force unrelated episodes into this exact phrase length.

## Approved episode treatment

```text
1행 — MLCC와 기판 없으면
       white, ordinary glyphs, no plate

2행 — AI 반도체는 절대 못 만듭니다
       teal, ordinary glyphs, no plate
```

The approved wording is episode-specific. The reusable rule is the visual hierarchy and the absence of added badge/profile/highlighter—not copying this wording into another episode.

## Rejected variants and lessons

- Added `박영선의 테크토크` text at upper-left → rejected.
- Added `박철민 삼성전기 상무` at lower-left → rejected.
- Replaced the target thumbnail hierarchy with an arbitrary four-line title → rejected.
- Used the numerical title `메모리 수요 50%…300%…` after the user selected a stronger exact technical thesis → rejected.
- Put a teal rectangle/highlighter behind `절대 못 만듭니다` → rejected.
- Final approved cover uses white first line + teal second line with **no title boxes**.

## QA checklist

- [ ] Exact matching `_list_` provenance and SHA recorded
- [ ] Center square crop preserves guest face and technical objects
- [ ] No series badge/name added
- [ ] No guest profile or visible source/timecode
- [ ] Official TTimes logo upper-right
- [ ] Target-thumbnail lower two-line structure preserved
- [ ] White setup line + teal claim line
- [ ] No title highlighter/box/plate
- [ ] 1080×1080
- [ ] Visual QA: no clipping; face unobstructed
