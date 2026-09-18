---
name: ttimes-production-automation
description: Use when mapping TTimes production from shooting through publishing, separating PD and video-editor/designer responsibilities, auditing which skills are operational versus only specified, or designing human-in-the-loop automation across transcripts, cuts, captions, screen composition, NLE, QA, and publishing.
license: MIT
metadata:
  hermes:
    tags:
    - ttimes
    - production
    - automation
    - pd
    - editor
    - workflow
    - human-in-the-loop
    related_skills:
    - ttimes-cut-editing
    - ttimes-audio-rough-cut-rendering
    - ttimes-script-and-srt
    - caption-layering-workflow
    - ttimes-screen-composition
    - ttimes-article-selection
    - ttimes-youtube-timestamps
    - ttimes-youtube-upload-package
  author: Hermes Agent
  version: 1.1.2
---

# TTimes Production Automation

## 자막·자료 선정에서 아카이브까지

이 범위의 작업에는 `../ttimes-screen-composition/references/caption-material-archive-contract.md`와 `references/team-material-archive.md`를 읽는다. 자료 목록은 현재 프로젝트 작업 폴더에 기록하고 후보/선택/실사용 상태를 구분한다. 보관 위치는 현재 작업에서 팀원이 지정한 곳을 사용한다. 이 공유 스킬은 외부 계정 연결이나 자동 업로드를 포함하지 않는다.

## Purpose

Map the TTimes production chain, keep editorial authority separate from technical implementation, and identify automation that can safely accelerate work without turning an LLM or renderer into the PD.

Core boundary:

```text
PD = 무엇을, 왜, 언제 보여줄지 결정
영상편집디자이너 = 승인된 의미를 어떻게 보이게 만들지 구현
자동화 = 반복 작업 실행 + 후보 생성 + 기계적 검수
```

A skill being present does not mean an end-to-end system exists.

```text
skill implemented = Hermes has a repeatable procedure and can produce the artifact
system implemented = inputs trigger execution, IDs and versions persist, approvals are stored, and outputs pass automatically to the next stage
```

Never present a proposed JSON schema, status ladder, or NLE bridge as already implemented.

## When to Use

- `PD와 영상편집디자이너 역할을 나눠봐`
- `어디까지 자동화 가능해?`
- `현재 구현된 스킬과 미구현 개념을 구분해`
- `촬영부터 표출까지 자동화 구조를 짜자`
- `OpenRouter/LLM을 제작 공정 어디에 붙일까?`
- designing manifest, approval, NLE, QA, publishing, or feedback-loop automation

Do not use merely because a technical platform name appears before `설명자막`. See the direct-caption boundary below.

## Direct-caption boundary

A terse command such as `X → 설명자막`, `X -> 설명자막`, `X 설명자막`, or several terms followed by `설명자막` means:

> Write the ready-to-paste explainer caption for X now.

Route wording-only requests to `ttimes-editorial-copy`; use `caption-layering-workflow` for supporting layer grammar. Requests about where and why to place captions/materials start with `ttimes-screen-composition`. Do not interpret the arrow as a request for automation architecture, role mapping, an OpenRouter pipeline, or a JSON schema.

Default response:

```text
X(English, if useful) : 현재 맥락에서 무엇이며 무엇을 연결·처리하는지 한 문장 정의
```

If several adjacent terms are requested, return separate caption blocks. Example:

```text
라우팅(Routing) : 사용자의 요청을 목적·비용·속도·성능 등의 조건에 맞는 AI 모델로 보내는 과정
```

```text
라우터(Router) : 요청의 내용과 조건을 판단해 가장 적합한 AI 모델이나 처리 경로를 선택·연결하는 시스템
```

If the user corrects the interpretation with `뭐하냐`, `설명자막으로 하라고`, or equivalent, reset immediately to caption-only output. Do not defend or summarize the abandoned architecture answer.

## Canonical Production Chain

```text
촬영 준비
→ 본 촬영
→ 원본 인제스트·백업
→ 멀티캠·음원 싱크
→ ASR·화자 분리
→ 컷 전 DOCX
→ PD 컷편집
→ 최종 컷 승인·동결
→ 러프컷 구현
→ 말자막·정제 DOCX
→ 강조·설명자막
→ 기사·자료화면 선정
→ 화면구성 DOCX
→ 자료·그래픽·자막 구현
→ 음향·색보정·마스터링
→ 팩트·오탈자·저작권 QA
→ 제목·썸네일·챕터·업로드 패키지
→ 비공개 업로드·실플레이어 QA
→ 예약 공개
→ 유튜브·홈페이지·포털·SNS 표출
→ 성과 분석·후속 수정
```

`업로드 완료`와 `표출 완료`를 구분한다. 표출은 공개면에서 제목, 썸네일, 자막, 챕터, 고정댓글, 링크, 화질이 실제로 정상 노출되는지 확인한 뒤 끝난다.

## Role Contract

### PD owns

- story axis, message, question structure, and claim strength
- KEEP/CUT/MOVE/retake decisions
- facts, caveats, counterarguments, article and asset approval
- caption need and final wording
- what appears, when it appears, and why
- title/thumbnail promise and final publication approval
- performance interpretation and follow-up decision

### Video editor/designer owns

- ingest implementation, proxies, multicam and waveform sync
- physical timeline edits after approval
- shot/reaction choice within the approved story
- crop, layout, typography, motion, graphic construction
- visual hierarchy, safe areas, pacing, audio mix, color, render
- technical display QA

### Automation may own without new editorial judgment

- file naming, checksums, backup verification, proxy generation
- ASR, diarization, transcript/DOCX generation
- approved-ledger rough-cut rendering
- caption alignment and deterministic validation
- chapter/package assembly
- codec, duration, overlap, missing-file, and delivery checks
- analytics collection

### Automation may draft but PD must approve

- cut candidates
- emphasis/explainer captions
- article and footage candidates
- screen-composition first drafts
- title/thumbnail copy
- fact-risk flags and performance diagnosis

Never let an implementation component invent a new content cut or silently alter an approved caption.

## Implementation Maturity Audit

Use three labels:

- `OPERATIONAL`: repeatable skill produces and verifies a real artifact
- `PARTIAL`: drafting/specification works, but no persistent automated handoff
- `CONCEPT_ONLY`: proposed schema, state machine, NLE bridge, UI, or service does not exist

Typical current classes:

```text
OPERATIONAL
ASR·화자분리, 컷 전 DOCX, PD 컷 DOCX, 승인 오디오 러프컷,
말자막/SRT, 기사 선정, 유튜브 챕터, 업로드 문안

PARTIAL
강조·설명자막, 화면구성, 자료 추천, 제목·썸네일 전략

CONCEPT_ONLY unless verified live
cross-stage manifest, SEG/CAP/ASSET IDs, approval database,
card ingest, multicam NLE automation, caption-template insertion,
asset-rights database, integrated final QA, CMS publishing, analytics feedback loop
```

Inspect actual tools/files before changing a label. Do not infer implementation from a skill description alone.

## Explaining the actual rendering stack

When the user asks `영상 편집이 Python 말고 뭐였지?` or refers to tools used in a prior build, answer from the actual project stack before listing generic alternatives. Do not turn a recall question into a survey of Remotion, Premiere, Resolve, or other unused tools.

For a typical deterministic TTimes Shorts build, distinguish roles clearly:

```text
Python = orchestration, timing, manifests, command generation
FFmpeg = actual video/audio composition, mixing, tempo, encode
Pillow = caption PNGs, typography, static graphics
OpenCV = frame inspection, masking, pixel comparison, limited inpainting
NumPy = image/audio array calculations supporting QA and transforms
```

These are cooperating layers, not mutually exclusive editing products. Also disclose when OpenCV inpainting was exploratory or rejected because it changed approved texture/framing; do not imply every named tool remained in the final accepted path.

## Automation Prerequisites

### 1. Canonical source and genealogy

For each stage, name one authoritative input and freeze its hash. Do not chain from whichever filename looks newest.

### 2. Stable IDs

Use IDs only when a real manifest persists them:

```text
SEG-0001   speech segment
CUT-0001   editorial operation
CAP-0001   editorial caption
ART-0001   article evidence
ASSET-0001 footage/still/report
GRAPHIC-0001 recreated graphic
```

A sample JSON containing these fields is a design proposal until a writer, validator, and read-back test exist.

### 3. Approval state machine

Recommended state vocabulary:

```text
DRAFT → PD_EDITED → PD_APPROVED → LOCKED → DESIGN_IMPLEMENTED → QA_PASS
```

Implementation requires persistent storage, actor/timestamp provenance, transition rules, and fail-closed behavior. A printed arrow is not a state engine.

### 4. Structured handoff

Minimum caption record:

```text
segment_id, time_start, time_end, source_text, caption_function,
caption_text, fact_basis, source_url, confidence, risk, pd_status
```

Minimum asset record:

```text
asset_id, source_url, local_file, source_time, rights_state,
story_function, placement, pd_status, implementation_status
```

### 5. Design system

Before template automation, freeze fonts, colors, safe areas, text lengths, line rules, article layouts, motion behavior, speech-caption suppression, and exception handling.

### 6. NLE adapter

Identify the actual editor platform and project template before promising timeline automation:

- Premiere Pro
- DaVinci Resolve
- Final Cut Pro

The adapter must support only verified operations such as marker creation, SRT import, placeholder placement, approved cut execution, template text replacement, and render-queue submission.

### 7. Gold corrections

Preserve:

```text
source speech → AI draft → PD correction → approved output → correction reason
```

Useful reason classes include: too long, translationese, factual overclaim, duplicate of speech, weak industrial meaning, term-definition error, poor legibility, layer collision, and footage preferable.

## Safe Build Order

1. project manifest, hashes, and approval persistence
2. existing-artifact adapters for ASR, cut ledger, captions, articles, and chapters
3. structured caption and screen-composition records
4. NLE markers/SRT/placeholders, not automatic final design
5. integrated final-master QA
6. publishing and live-surface verification
7. analytics feedback loop

Do not begin with automated motion graphics or autonomous final-cut decisions. They have lower determinism and higher editorial risk than manifests, approved-cut execution, captions, and QA.

## Long-form → Shorts reverse engineering

When the user provides both a full-video URL and a Short, download and inspect both actual files before describing the production process. Test whether the Short reuses an already-edited cold open with audio/frame matching, then map that cold open back to body ranges. Keep these two automation classes separate:

```text
approved landscape highlight → vertical template wrapper = deterministic derivative automation
full body → select/reorder/design highlight = editorial drafting with PD approval
```

Do not promise autonomous face tracking, B-roll selection, or NLE construction when the observed Short merely nests a completed 16:9 highlight inside a fixed 9:16 shell. Scene-detector hits must be classified as true cuts, graphic-state changes, caption animation, or motion before counting edits. Strong headline claims such as percentages, universals, causality, or sanctions effectiveness remain blocked until fact and PD approval.

Use `references/longform-to-shorts-reverse-engineering.md` for the paired-download, transcript mapping, audio-correlation, contact-sheet, manifest, MVP, and QA workflow.

When the user approves execution and the concrete deliverable is a playable `sample.mp4`, use `references/approved-highlight-vertical-sample.md` for chapter-boundary inspection, brief end-frame holds that preserve final audio without leaking the next intro, Pillow/FFmpeg wrapper rendering, parent-side artifact verification, and Telegram delivery receipts. If the user asks for the `기존 템플릿과 동일한` shell, enter the reference's `VISUAL_MATCH` path before the first render: measure and reconstruct the actual background, viewport, border, label, typography hierarchy, colors, and safe areas rather than inventing a similar design. Reserve `PIXEL_IDENTITY` claims for cases where the original clean template/project and font assets are available.

If the user instead approves a screenshot's visual *feel* and requests a phone-aware branded shell, use `references/mobile-safe-editorial-shorts-shell.md`. It covers separating player UI from actual design, source-grounded top hooks, official channel-logo acquisition, full-width 16:9 plus torn-paper composition, right-rail/bottom-metadata safe zones, quiet lower-brand panels, deterministic Pillow rendering, and phone-size QA. Treat this as a new approved design direction rather than forcing the earlier reference Short's template.

## Physics-first AI engineering Shorts

When a limited generation budget must visualize an industrial or engineering mechanism, route the project through `references/ai-generated-engineering-shorts-pipeline.md`. It covers the topic gate, fact/mechanism lock, narration-plus-shot manifest, pixel-based asset triage, causal reordering, TTS completeness, final-speed lock before captions, generated-footage boundaries, BGM duration fitting, master QA, and PD approval points.

Keep this distinct from deterministic `approved landscape highlight → vertical wrapper` rendering. Generated engineering Shorts begin with a new physical explanation and require editorial approval; they are not merely a layout derivative.

## Narration-first Shorts BGM and sound-design pass

Run this only after picture order, narration speed, and burned speech captions are locked. The default aim is not to turn an explainer into a music video; it is to remove deadness while keeping every spoken word dominant.

For industrial/engineering Shorts, prefer a restrained instrumental bed:

```text
low machinery drone
+ minimal electronic pulse
+ sparse metallic percussion
+ small transition swells at editorial pivots
```

Avoid strong melody, vocals, trailer orchestra, bright corporate music, and aggressive cyberpunk arpeggios unless the PD explicitly requests them. Start BGM roughly 12–18 dB below narration and use light sidechain ducking rather than static gain alone. Preserve the original narration loudness instead of normalizing the mixed program from scratch; measure original narration, BGM-only, and final mix separately.

Technical invariants:

- preserve the approved video frames, captions, dimensions, frame rate, and duration;
- upmix mono narration to stereo before mixing when the BGM is stereo;
- do not use `-shortest` blindly: an audio stream a few milliseconds shorter can remove the final video frame;
- after mixing, compare decoded video frame count or raw-frame hash against the approved input;
- verify final AAC layout, whole-file decode, integrated loudness, true peak, and end timing;
- deliver an actual preview mix when the user asks to “깔아봐,” not only search keywords or a music prompt.

The validated synthesis, ducking, frame-preservation, loudness, and delivery workflow is in `references/narration-first-shorts-bgm-mixing.md`.

## Channel-wide credited-work audits

When the task is to find every channel video explicitly crediting a named PD and evaluate all confirmed work, use `references/channel-wide-pd-credit-and-work-audit.md`. It defines tab-level scope locking, explicit D1/D2/D3 evidence, OCR candidate adjudication, joint-credit boundaries, role-specific scoring, resumable ledgers, bounded batch execution, and the final reconciliation gate. In particular, never let Shorts enter a regular-Videos audit merely because their metadata shares a directory.

## Common Pitfalls

1. **Arrow over-interpretation:** `OpenRouter → 설명자막` becomes an automation lecture instead of an OpenRouter definition card.
2. **Skill equals system:** a workflow document is reported as a deployed pipeline.
3. **Proposal equals implementation:** sample IDs/status JSON is described as current infrastructure.
4. **Renderer becomes PD:** technical execution introduces new content cuts.
5. **Designer erasure:** automation produces text and the visual implementation is treated as trivial.
6. **No approval persistence:** PD says yes in chat, but the next stage cannot prove which revision was approved.
7. **Filename authority:** newest-looking DOCX silently replaces the actual approved source.
8. **Upload equals publication:** no live-player or public-surface QA is run.
9. **Premature NLE promise:** automation is designed before identifying the editor platform and templates.
10. **Automatic-CC terminology drift:** chapter copy repeats a phonetic ASR form even though the producer's approved publishing bundle supplies the canonical technology or person name. For publishing metadata and chapter labels, explicit producer terminology outranks automatic CC spelling; CC remains the timing source. If neither producer metadata nor a verified source establishes the term, preserve uncertainty rather than guessing.
11. **Chat-wrapper leakage:** Slack/Telegram routing lines such as `/project-name`, message times, and `@all` are copied into the public upload package. Parse them as operational context only. Preserve an explicit publication schedule in the internal upload ledger, but do not add it as a public title/body/comment block unless requested.

## Verification Checklist

- [ ] Direct caption shorthand was routed to caption output, not architecture
- [ ] PD/editor/automation authority is explicit at each stage
- [ ] Operational, partial, and concept-only states are evidence-based
- [ ] Proposed schemas are labeled as proposals until persisted and tested
- [ ] One canonical source and approval gate exists before execution
- [ ] Automation after approval cannot make new editorial decisions
- [ ] Designer-owned visual and finishing decisions remain explicit
- [ ] Upload and live surfacing are separately verified
