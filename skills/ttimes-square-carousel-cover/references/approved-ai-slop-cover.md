# Approved AI-slop square cover calibration

## Approval state

The user approved the cover produced from the exact TTimes `_list_` visual after rejecting an earlier ImageGen reinterpretation.

Approved instruction distilled from the correction:

> Use the TTimes list image itself as the cover. Add the TTimes logo at the upper-left and add the title using the TTimes thumbnail's font/size treatment.

## Source lineage

- TTimes article: `https://www.ttimes.co.kr/article/2026082717517736372`
- Article title: `AI로 만든 그럴듯한 보고서, AI 슬롭에 리더는 괴롭다`
- Article `_list_` image: `https://img.ttimes.co.kr/img/202608/2026082717517736372_list_76538.jpg`
- Downloaded source size: `1185×997`
- Downloaded source SHA-256: `23cd45eaeb5cff61855e8186c07612e10ffc5c3c150d75ce99c1eeda1a4b75b4`
- Embedded YouTube video ID: `3hilsneulfM`
- Typography reference: `https://i.ytimg.com/vi/3hilsneulfM/maxresdefault.jpg`
- Typography reference size: `1280×720`
- Typography reference SHA-256: `1549f11057eb610c7ec976b9aeaff518fd0c1580b0ad60552c9454c7497df1f5`

## Official logo

- Site asset: `https://menu.ttimes.co.kr/www/images/logo/dark_logo.png`
- Native size: `143×44`
- Rendered width on 1080-square cover: `190 px`
- Position: `(64, 56)`

Despite its filename, this is the light/near-white logo suited to a dark image region. Verify pixels rather than inferring logo color from the filename.

## Typography finding

The exact production font cannot be proven from the raster thumbnail. Visual analysis found:

- neutral neo-grotesque Korean sans
- Black/900 weight
- roughly 88–92% horizontal width
- tight spacing
- square, minimally rounded consonant construction

Closest families:

1. Sandoll GothicNeo Heavy/Black
2. Noto Sans CJK KR Black / Noto Sans KR Black
3. Pretendard Black

The approved reproducible sample used:

```text
Noto Sans CJK KR Black
79 px base size
90% horizontal compression
line 1: #FDFDFD
line 2: #93A6FF
x: 62
line 1 y: 810
line 2 y: 910
soft black shadow: offset 6/7, blur 6
```

## Approved output

- Output path at approval: `PROJECT_ROOT/00_cover_ttimes_list_title.png`
- Skill asset: `assets/approved-lee-junghak-ai-slop-cover.png`
- Size: `1080×1080`
- SHA-256: `2e8c1ab7cf5a1eadb1f2905f7e368bc53f19f46d344fdc61350f05b1965c717d`
- Title:
  - `AI로 만든 그럴듯한 보고서`
  - `AI 슬롭에 리더는 괴롭다`
- Independent visual review: `blocking 0`

## Current global override

This artifact is one of the two mandatory visual comparison references together with the approved Park Young-sun cover. Future and remade square covers use the current global 80px title and upper-right TTimes logo. Preserve this asset byte-for-byte as historical approval evidence; do not edit it to retrofit the new logo position.

## Failure to avoid

The rejected first attempt generated a new symbolic AI-report visual and treated the list image only as a style reference. That violated the source contract. For this cover type, “표지는 리스트 사진을 가져와” means literal asset use, not stylistic imitation.

Do not repeat that failure even when the broader card-news project mandates ImageGen. The mandate applies to newly created body-card visual layers; the cover has a more specific sourced-asset contract.
