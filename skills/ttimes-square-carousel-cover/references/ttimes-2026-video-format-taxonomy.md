# TTimes 2026 video-format and thumbnail taxonomy

## Scope and evidence

- Frozen: 2026-08-29
- Corpus: 42 actual YouTube `maxresdefault.jpg` thumbnails, six each from seven working groups
- Named-series samples:
  - `이중학의 사람과 기술`: `H8lYycctv3E`, `axGKIooHxac`, `klfhUVnc44U`, `6kbZUJTdzZg`, `6JXEAg-ITuQ`, `ys6dWId6hgU`
  - `박영선의 테크토크`: `AxRT8nOVing`, `wbeMT_Rq1Lg`, `j91QxopQEXI`, `jN29A92uusU`, `-1JotnInYm0`, `Hq4CVmPqhGU`
  - `강수진 박사의 프롬프트 엔지니어링의 매직`: `wv20-hGjozA`, `2e2cxM06HMI`, `ugB1UG2wILU`, `3UMvC4YS6Yk`, `kAjlJipOHR8`, `NgkyUXJWYiI`
  - `30년 개발자의 기업 분석`: `vDd6TMC-NuA`, `fwdIXO1DoTo`, `Xh6x_ZfDVyo`, `QZhik3a2qYA`, `4ItKzO4WQ5w`, `Oat-BI_0Vpc`
  - `AI, 안 해보면 모른다`: `iAzLFyLBPpw`, `70cW9o7GKqI`, `5IlNJMffzpw`, `ILzunqw4unI`, `Vqiw5-n9-Gg`, `8hwNZeB_ZgQ`
  - `티타임즈 주간브리핑`: `bpaNj4Mw4lk`, `iOIFL8aAOv4`, `-hAr7RzkeOU`, `1jf7tRd27WI`, `4bYfg8Fs3aY`, `ekjwCiojl6A`
- Confirmed general one-person F1 reference: `dUVHJOpzTBI` — `왜 로봇회사들은 빨래 개기에 집착할까?`; article `https://www.ttimes.co.kr/article/2026082616477775061`; user-confirmed production form on 2026-08-29.
- Additional recent generic/overlap samples: `_A7Zch21Iqs`, `xoVqDbCf0ys`, `vd__njvqkqc`, `hx5TnPMxKU8`, `AhAvCBC9JXE`
- Pixel observations are evidence for visual grammar only. Whether a video is truly a conversation, lecture, or report may still require article/playlist/video metadata.

## 1. Two independent axes

Never use one label for both series and production form.

### Axis A — named-series identity

| Code | State | Thumbnail evidence |
|---|---|---|
| S1 | explicit named series | the same series badge/logo is visibly repeated |
| S2 | implicit named series | fixed person, palette, and layout repeat, but no visible series name |
| S3 | standalone/general | no repeating badge/person/layout contract |
| S4 | unknown | evidence is absent or conflicting |

### Axis B — production format

| Code | Format | Thumbnail cues | Caveat |
|---|---|---|---|
| F1 | one-person expert/explainer | one recurring expert, large title, topic graphic | a guest-only interview thumbnail can imitate F1 |
| F2 | host + guest conversation | two real participants, or host identity in badge plus large guest | two faces can also be news subjects |
| F3 | multi-guest/panel conversation | three or more participants or multiple equally weighted experts | distinguish participants from illustrated news subjects |
| F4 | hands-on demo/tutorial | UI, laptop, tool logo, before/after output, use/workflow wording | one person may appear, but F4 outranks F1 |
| F5 | news/weekly briefing | fixed briefing badge, companies/events as subject, no expert hero | public figures can be news subjects, not panelists |
| F6 | field report/event coverage | event/place/facility evidence, on-site action, field wording | not proven by a generic background photo alone |
| F7 | issue analysis/general report | no presenter hero; company/technology/event montage dominates | common fallback for standalone videos |
| FU | unresolved | thumbnail cannot prove the production structure | inspect article, playlist, or video |

Decision priority: `F4 demo evidence → F5 briefing badge → F6 field evidence → F1/F2/F3 people → F7 issue graphic`.

## 2. Named-series matrix

| Named series | Series axis | Production format | Strong visual identifiers | Variable elements |
|---|---|---|---|---|
| 이중학의 사람과 기술 | usually S1; occasional badge omission | F2 host+guest is the core; some thumbnails look F1 when only guest is shown; F3 possible for multi-guest episodes | purple series badge with host identity, navy/purple field, white + periwinkle title, organization/people/AI themes | guest count, whether host is shown large, title 2–3 lines, topic visual |
| 박영선의 테크토크 | S1 | F2 host+guest; thumbnail often shows host only inside badge and guest as hero | YouTube thumbnail: teal Park badge; square card cover: exact `_list_`, large guest right, technical object left, upper-right TTimes logo, lower white+teal title | guest, industry object, quote/question form; square cover omits badge/profile/title boxes |
| 강수진 박사의 프롬프트 엔지니어링의 매직 | mostly S2 in observed thumbnails | F1 recurring expert/explainer; F4 when the actual UI/output is central | same female expert on right, navy field, green accent, prompt/model concept graphic | title 2–3 lines, model/tool, outfit, whether demo evidence is shown |
| 30년 개발자의 기업 분석 | S1 | F1 recurring expert/company analysis | recurring male expert, `30년 개발자의 기업분석 시즌4` strip, navy + teal, corporate logos/competition | company set, 2–3 lines, expert size/pose |
| AI, 안 해보면 모른다 | mixed S1/S2 because badge is inconsistently visible | F4 hands-on demo/tutorial | tool UI/result/laptop dominates; action/how-to wording; dark navy with teal or magenta | demonstrator, tool, result, badge visibility, accent |
| 티타임즈 주간브리핑 | S1 | F5 news/weekly briefing | fixed `TTimes 주간브리핑` badge, no presenter hero, black/dark blue, company/news montage, red key line/box | companies, event, question/verdict wording |
| 월간 국제정세/월간 테크 등 recurring expert briefing | verify per episode; often S1/S2 | usually F1 expert briefing or F5 thematic briefing | monthly label, recurring expert, topic bundle | palette and number of issues; do not infer without the target thumbnail |
| 일반 원맨 | S3 or S4 | F1 candidate | one expert without reliable series badge | may actually be guest-only F2; verify metadata |
| 일반 대담 | S3 or named series | F2/F3 | two or more actual speakers with dialogue framing | identify host/guest from article or transcript, not face size alone |
| 일반 이슈 영상 | S3 | F7 | no presenter hero, issue/technology montage | palette and title grammar follow the subject rather than a series |
| 현장 취재 | S3 or event series | F6 | real event/location/facility and on-site framing | requires location/event confirmation |

## 3. Thumbnail-only decision tree

```text
A. Is a recognized series badge visible?
   yes → lock named series (S1)
   no  → compare recurring person + palette + layout
          repeated strongly → S2 candidate
          no repetition → S3/S4

B. Is a real UI/output/tool-use action the primary visual?
   yes → F4
   no  → continue

C. Is a weekly/news badge visible and are companies/events the subject?
   yes → F5
   no  → continue

D. Is an event/place/facility clearly documented?
   yes → F6 candidate; verify article
   no  → continue

E. Count actual participants, not depicted news subjects
   0 → F7
   1 → F1 candidate; verify it is not a guest-only interview
   2 → F2 candidate
   3+ → F3 candidate

F. If host/guest or lecture/conversation remains unproven → FU until metadata check
```

Do not classify Elon Musk/company CEOs in a news montage as panelists. Do not classify every laptop image as a demo. Do not call one large guest a one-man program when a named host appears only in the series badge.

## 4. Thumbnail wording-edit gate

### Default: preserve supplied wording

Use the current TTimes thumbnail wording as-is. Do not polish merely because another phrase sounds better.

### Edit only when at least one trigger fires

- the text is too long to keep the format's normal visual hierarchy at mobile size
- it exceeds the usable line count and covers a face, UI, product, or key evidence
- the same meaning is repeated
- subject/object is missing and the title is unintelligible
- grammar, spacing, or typo makes the meaning genuinely odd
- the thumbnail text and visual point to different subjects
- the series badge repeats words already wasting title space
- quotation marks appear but the exact speech cannot be verified

### Meaning-preservation invariants

Preserve subject, event/action, causal direction, comparison target, number, unit, period, scope, certainty strength, and question-vs-assertion status.

- If wording is compressed/reordered/paraphrased, remove quotation marks and treat it as an editorial title.
- Use quotation marks only for audio-confirmed exact speech with speaker attribution verified from an explicit turn signal.
- Do not turn `가능하다` into `성공했다`, `왜` into `때문이다`, or a comparison into a winner claim.

### Practical editing order

```text
remove duplicated modifier
→ remove words already present in the series badge
→ remove secondary examples
→ replace long nominal phrasing with the same core verb
→ rebalance semantic line breaks
→ only then change sentence structure
```

### Observed starting ranges, not hard limits

| Series | Starting title treatment |
|---|---|
| 이중학의 사람과 기술 | usually 2 lines, about 24–36 Korean characters; problem → implication; white + periwinkle |
| 박영선의 테크토크 | usually 2 lines, about 22–34; context → technology/claim; white + teal |
| 강수진 | 2 lines preferred, 3 allowed, about 28–42; retain model/problem and actionable implication |
| 30년 개발자 | 2–3 lines, about 28–42; retain company names, competitive structure, judgment question |
| AI, 안 해보면 모른다 | 2–3 lines, about 22–38; result/how-to first, tool name secondary |
| 주간브리핑 | usually 2 lines, about 20–32; event → issue/verdict; second line often red |
| general report | 2 lines preferred, 3 allowed; do not imitate a named-series voice without that series |

These ranges are fit-search starting points only. Current thumbnail and available image space outrank them.

### Approved 박영선 square-cover distinction

The YouTube thumbnail may carry the Park series badge, but the approved square card cover does **not** copy that badge or add typed `박영선의 테크토크`. It uses the exact `_list_` image, official TTimes logo at upper-right, and a lower two-line white+teal title. Cover title glyphs use color only—no fluorescent marker, colored box, or opaque plate. See `approved-park-youngsun-tech-talk-cover.md`.

## 5. Current 이중학–윤명훈 video

This is established from the actual source, not inferred from a different playlist sample:

- Intro authority: `이중학` is host of `사람과 기술`; `윤명훈` is the guest.
- Named series: `이중학의 사람과 기술`
- Production format: `F2 host + guest conversation`
- Card subject/profile: 윤명훈
- Host speech may inform the editorial spine, but a 윤명훈 quote card must contain only an audio-confirmed 윤명훈 utterance.
- Cover identity: preserve the actual `_list_` image; add the `사람과 기술` series identity when required by the card package; use the target/current thumbnail to choose variable title size/color.
- Closing identity: use a verified 윤명훈 quote/profile and the same series palette/badge, not a generic interview closing.

Recommended operational label:

```text
Series: 이중학의 사람과 기술
Format: 진행자 이중학 + 게스트 윤명훈 대담
Card protagonist: 윤명훈
Confidence: confirmed from source intro and production files
```

## 6. Current general one-person reference

- YouTube: `https://youtu.be/dUVHJOpzTBI`
- Article: `https://www.ttimes.co.kr/article/2026082616477775061`
- Title: `왜 로봇회사들은 빨래 개기에 집착할까?`
- Series axis: S3 standalone/general
- Production format: F1 one-person expert/explainer
- Editorial hook: laundry folding is simultaneously a hard humanoid manipulation problem and a safe, repeatable training task.
- Do not reroute it to F4 merely because robot demonstrations appear; the user confirmed that the production form is 원맨, and tool-use tutorial/UI evidence is not the editorial spine.
