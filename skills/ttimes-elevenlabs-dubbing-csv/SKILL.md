---
name: ttimes-elevenlabs-dubbing-csv
description: Build TTimes dubbing cues from published audio or Studio CSV, clone each speaker from the current episode, and package dubbed audio, synchronized subtitles, thumbnails, titles and descriptions by episode and language.
metadata:
  version: 1.5.7
  platforms: [macos, linux]
  hermes:
    tags: [ttimes, elevenlabs, dubbing, csv, korean, english, timing, subtitles, thumbnail, imagegen]
    category: media
    requires_toolsets: [terminal, file]
---

# TTimes ElevenLabs Dubbing CSV

앞으로 새로 만드는 중국어판의 기본 대상은 대만(zh-TW)이다. 더빙 대본은 대만 표준중국어 구어체로 작성하고, SRT·섬네일·제목·설명은 대만식 번체로 작성한다. 번역 단계부터 대만 현지 용어(登入、帳號、軟體、網路)를 사용하고 음성과 자막에서 용어가 일치하는지 확인한다.

## 이 컴퓨터의 전사 경로

전사·말자막 타이밍·부분 재전사·화자 구분은 ElevenLabs Scribe v2 API와 기존 env만 사용한다. 실행 전 `skills/ttimes-script-and-srt/references/elevenlabs-runtime.md`를 읽는다. 인증·잔액·서비스 오류는 원인을 보고하고 중단한다. 이 규칙이 과거 사례보다 우선한다.

## 회차별 트랙 클론과 음성 납품 (2026-11-24)

- 회차마다 최종 게시본의 음원을 기준으로 화자를 분리한다. 같은 출연자가 재출연해도 해당 영상의 깨끗한 발화들을 초·중·후반에 걸쳐 모아 화자당 클론 하나를 새로 만든다. 실제 게시본에서 추출한 음원이나 동일 음원의 검증된 Scribe v2 결과를 사용할 수 있다.
- 클론 입력에서는 화자 표기가 불확실한 발화, 겹말, 다른 목소리가 섞인 맞장구, 음악·광고·로고를 제외한다. 실제 더빙에서는 들리는 짧은 응답과 대화 순서를 살리고, 확인되는 겹말은 화자별로 합성해 원래 위치와 상대 음량에 배치한다. 제외한 클론 소스 구간과 이유를 기록한다.
- 온라인 클론은 회차 작업용으로 취급한다. 생성할 때 회차 ID·화자·voice_id를 작업 기록에 남긴다. 클론 슬롯이 꽉 차 새 회차를 등록할 수 없을 때는 납품·검증이 끝난 과거 회차 중 이 작업에서 생성한 것으로 확인되는 클론을 오래된 순서로 필요한 수만 삭제하고 다시 등록한다. 진행 중이거나 재작업에 쓰는 클론, 사용자가 별도로 관리하는 음성, 소유·용도가 불분명한 음성은 자동 삭제 대상에서 제외한다. 슬롯 정리는 서비스의 클론에만 적용한다.
- 영어 합성 기본 모델은 Eleven v4(`eleven_v4`)다. 해당 회차의 두드러진 질문·답변 등 각 화자의 대표 발화로 원음과 더빙을 비교한 뒤 전편을 합성한다. 번역은 원문 의미와 실제 말할 시간에 맞추고, 합성 결과의 발음·길이·화자 전환을 검수한다. 다국어 요청은 지정된 언어로만 실행하며 같은 회차 안에서는 화자별 클론을 공유할 수 있다.
- 광고를 따로 요청하지 않으면 광고 구간은 원래 음성과 시간 위치를 유지하고 번역·더빙·자막 생성에서 제외한다. 본편 첫 발화부터 현지화한다.
- 기본 납품물은 더빙 MP3와 최종 더빙 음성에 맞춘 본편 SRT 한 쌍이다. 영상 생략 또는 음성 추출 요청에도 둘을 함께 제공한다. 사용자가 자막을 명시적으로 제외하면 SRT를 생략한다. 영상과 썸네일은 요청 범위에 따라 추가한다.

## When to Use

Use when the user provides either an ElevenLabs Dubbing Studio CSV or only source video/audio and wants a Studio-like dubbing-cue workbook created first.

Legacy Studio schema:

```text
speaker,start_time,end_time,transcription,translation
```

Reference audit-workbook schema:

```text
speaker,start_time,end_time,transcription,edited_transcription,english_translation
```

The user may want the Korean transcript corrected first and natural spoken English written into the fixed cue windows, or may expect the skill to transcribe, diarize, and segment the source before that work begins.

This is the authoritative child skill for **TTimes Korean→English Dubbing Studio CSV and local ElevenLabs API rendering**. It overrides generic subtitle or translation guidance in `media-localization-workflows` where they conflict.

## Core Contract

The job is exactly:

```text
raw Studio CSV
→ source-faithful Korean cleanup in transcription
→ cue-duration-aware spoken English in translation
→ deterministic CSV rebuild
→ immutable timing/speaker check
→ replaceable local cue rendering
→ exact-duration background/SFX mix
→ forced-aligned US English SRT
→ image-generated English thumbnail with deterministic text/logos
→ package QA and delivery
```

For an ordinary dubbing request, deliver one episode folder. For each requested language, put the final dubbed MP3, synchronized SRT, localized thumbnail, copy-ready YouTube title and full description together in that language’s subfolder. Keep the title/description clipboard page at the episode root and production intermediates under work/. Match the video ID, original thumbnail and published metadata to the same episode before localization. Verify all five files per language and link the episode folder at handoff. Honor narrower requests such as a clone only or a Studio CSV only.

### Immutable fields

For an existing Studio export, never change, reorder, merge, or split:

- row count and row order
- `speaker`
- `start_time`
- `end_time`
- header names and header order

Do not move text to a neighboring row merely to improve English rhythm. If a translation cannot fit, compress wording inside that row without losing the row's core meaning.

In source-media bootstrap mode, cue boundaries are created during diarization/ASR review. Once the named-speaker cue plan is frozen, speaker, start, end, order, and cue count become equally immutable for correction and translation.

### Editable fields

- `transcription`: corrected Korean source transcript
- `translation`: natural timing-fit English dubbing line

Keep the original CSV untouched. Write a new final CSV plus a machine-readable QA report.

## Three production modes

### A. Studio round-trip mode

Use the immutable five-column contract above when the deliverable returns to ElevenLabs Dubbing Studio. Row count, speaker, start, end, and order never change.

### B. Local replaceable-render mode

Use this when the user wants local generation, individual cue replacement, model A/B testing, or a final MP3 assembled outside Studio.

```text
Studio CSV source cues
→ clean spoken English
→ optional local speaker subclips
→ one generated file per local clip
→ measured duration fitting
→ fixed 19:19/actual master timeline
→ background/SFX bed extraction
→ ducked final mix
```

Rules:

- Preserve every original source cue ID. Normal clips are `001`, `002`, etc.
- Only a source row proven to contain multiple speakers may become local subclips such as `045a/045b/045c`; do not alter the Studio round-trip CSV for this purpose.
- Keep `spoken_english` separate from model-specific input such as `v3_prompt`.
- Store `voice_id`, model ID, TTS speed, raw/fitted duration, source cue, start/end, and hashes in a manifest.
- Save every raw and fitted clip so `cue_026` can be regenerated and replaced without rerendering the other clips.
- Local subclip boundaries derived from text length remain `BOUNDARY_CHECK` until verified against the actual audio.

### C. Source-media bootstrap mode

For this user, transcription, targeted re-transcription, and speaker diarization use ElevenLabs Scribe v2 API with the existing env. Read `skills/ttimes-script-and-srt/references/elevenlabs-runtime.md` before execution. Use GPT Sol for Korean correction and English translation; verify speaker mapping independently.

Use this when no Studio CSV exists. Read and follow:

```text
references/source-media-to-dubbing-cues.md
```

The skill must acquire the exact source, diarize speakers, transcribe raw Korean, map speaker clusters from evidence, and create the same six-column cue workbook used as the production reference. Dubbing cues are **not subtitle cues**: split on speaker changes, keep continuing technical speech in coherent long units, preserve short reactions that carry conversational meaning, and keep every cue below 25 seconds.

Default artifact chain:

```text
source media
→ raw diarization JSON
→ raw ASR clips/segments
→ named-speaker cue plan
→ six-column Korean/English workbook
→ QA JSON
→ local replaceable-render mode
```

Do not require the user to prepare a CSV when the media itself is available.

## Model choice

- `eleven_flash_v2`: English-specialized, clearer and more stable English pronunciation; no v3 audio tags. Use it for explicitly requested alternatives to the default v4 render.
- `eleven_v3`: multilingual and more expressive; supports sparse audio tags such as `[curious]`, `[amused]`, and `[thoughtful]`. Tags are optional, not a quota. Do not add them to ordinary technical exposition.
- Do not mix models within one episode unless an audible A/B test proves that timbre and cadence remain consistent.
- A voice name ending in `EN` does not make v3 an English-specialist model; model and clone training language are separate concerns.
- For acronyms and brands, audition the exact clone/model combination. Use prompt-only spelling or a pronunciation dictionary when `HBF`, `zHBM`, `SK hynix`, `eSSD`, `LPU`, etc. drift.

## 번역할 때 맞장구와 발화 구간 판단 (영어·중국어·일본어)

- 한국어 원전사에는 모든 반응을 남긴다. 번역할 때는 앞뒤 화자의 말을 읽고, 듣고 있다는 표시로 반복하는 “네, 네”, “그렇죠”는 해당 언어에서 자연스러우면 생략한다. 질문에 대한 답, 사실 확인, 반박, 발언권 전환에 의미가 있는 반응은 그 기능에 맞는 한마디로 살린다. 생략한 맞장구는 합성과 더빙 자막에서 함께 빼고, 원래 구간과 생략 이유는 작업 기록에 남긴다. 다른 화자의 대사를 그 자리까지 늘리지 않는다.
- 번역을 쓰기 전에 원 발화자의 시작·끝, 의미 있는 쉼, 비교·예시·결론이 나오는 시점을 표시한다. 각 언어의 자연스러운 속도로 이 구간에서 말할 문장을 쓴다. 긴 설명은 중간 의미 단위까지 맞추고, 원문 한 문장이 두 작업 구간에 걸치면 함께 읽어 결론을 너무 일찍 말하지 않도록 한다.
- 생성 후 같은 화자의 원음과 더빙에서 실제 말이 시작하고 끝나는 시각, 중간 핵심 구절의 시점을 비교한다. 화면이 있으면 입을 열고 닫는 순간과 대조하고, 음성만 있으면 원 발화 시각을 사용한다. 의미 있는 말이 남았는데 더빙이 먼저 끝나거나 다음 화자에게 넘어가면 번역부터 다시 쓴다. 원문에 있는 대비와 구체적인 예를 복원하고, 무의미한 맞장구나 긴 정적을 추가해 초수를 채우지 않는다. 의도적으로 생략한 청취 반응은 발화 누락과 구분한다.

### 발화 길이에 맞는 번역과 금액 현지화

- 원문보다 더빙이 일찍 끝나면 한국어 원음에서 그때 전달하는 비교·예시·강조가 무엇인지 찾고, 같은 순간에 들리도록 문장 안의 정보 순서와 호흡을 다시 짠다. 앞 구간에서 다음 구간의 결론까지 말했으면 두 구간을 함께 편집한다.
- 시간이 모자라면 질문, 확인, 새 정보, 인용 등 그 말의 역할을 먼저 파악한다. 이미 제시한 숫자의 재확인은 짧은 자연스러운 표현으로, 처음 제시하는 금액과 단위·연간/월간 구분은 명확하게 옮긴다. 같은 화자의 인접 절은 문맥을 보되 다른 사람의 시간을 빌리지 않는다. 자연 속도로 합성해 구간과 실제 밀도를 다시 확인하고 배속은 마지막 미세 조정에만 쓴다.
- 원화 금액은 영어판 USD, 일본어판 JPY, 대만판 TWD(별도 요청한 중국 본토판은 CNY)로 환산한다. 별도 지정이 없으면 한국어 원본 영상의 공개일을 기준으로 공신력 있는 일별 기준환율과 고시 단위(1엔/100엔 등)를 확인한다. 해당일 고시가 없으면 직전 고시값을 쓰고 실제 적용일·출처·원금액·환산 전후 수치를 작업 기록에 남긴다. 원화 액면 자체가 논점이면 원화를 살리고 현지 통화 상당액을 보조한다.
- 같은 금액은 회차 안에서 같은 환산값으로 읽고 표기한다. 근삿값임을 자연스럽게 밝히고 해당 언어에서 읽기 쉬운 자리로 반올림한다. 기본은 유효숫자 두 자리 안팎으로 하되 비교 순위·배수·월간/연간 관계와 원문의 정밀도를 보존한다. 비율과 합계는 반올림 전 금액으로 검산하고, 반올림이 관계를 흐리면 한 자리를 더 남긴다. 더빙·자막·설명에 나오는 대응 금액을 함께 대조한다.

### 대담의 웃음과 말 속도

- 대담 원음의 첫 Scribe v2 전사에서 공통 실행기의 `--tag-audio-events`를 켠다. 동일 음원의 이벤트 태깅 전사가 있으면 재사용한다. 기존 단어 전사만 있을 때는 웃음 확인에 필요한 범위만 별도 파일로 조사한다. 전편 검출을 요청받으면 전편을 대상으로 한다. 태깅 여부를 모르는 빈 이벤트 목록으로 ‘웃음 없음’을 판정하지 않는다.
- `words` 중 `type=audio_event`에서 웃음 후보를 골라 원본 기준 시작·끝, 직전 대사, 겹말 여부를 기록한다. 원음과 가능하면 화자별 트랙으로 웃은 사람과 반응 대상을 확인한다. 화자 불명·여럿의 겹웃음은 그대로 표시한다. 웃음 섞인 말투나 약한 웃음은 자동 검출에서 빠질 수 있으므로 농담과 반응이 이어지는 대목은 앞뒤도 듣는다.
- 대사와 분리되는 원본 웃음은 배경 트랙에 이미 남아 있는지 먼저 확인하고 한 번만 믹스한다. 웃으며 말한 대사는 해당 화자의 클론으로 그 말투를 살리고, 실제로 소리 내 웃은 경우에만 별도 웃음을 고려한다. 청자의 웃음은 번역된 농담을 알아듣는 순간과 다음 화자의 진입을 기준으로 배치한다. 최종 믹스에서 누락·중복·한국어 겹침을 확인한다. 기존 단어 공백 차이 검사는 그대로 수행하고, 양쪽에 단어가 없어도 원본의 웃음이 더빙에서 사라진 구간은 별도 수정 대상으로 기록한다.
- 속도는 질문·설명·반전·답변을 의미 단위로 나눠 판단한다. 원화자가 어느 대목에서 빨라지고 어느 숫자·이름·결론에서 천천히 힘을 주는지 번역 전에 표시한다. 웃음·쉼을 제외한 실제 말한 시간과 해당 언어의 발화량을 보고, 같은 언어·같은 화자의 주변 구간과 비교해 유독 몰아치거나 늘어지는 후보를 찾는다. 한국어와 외국어의 글자 수나 단어 수를 직접 비교해 배속을 정하지 않는다.
- 전체 길이와 공백이 맞아도 한 절만 숨 가쁘거나 문장 후반이 처지면 그 대목을 원음과 더빙으로 연속 청취한다. 먼저 정보·숫자·주장 강도를 보존해 자연스러운 길이로 다시 번역하고 합성한다. 기존 속도 조절 범위 안에서 마지막으로 미세 조정하고 최종 MP3의 해당 절과 이웃 절, 갱신한 자막 싱크를 확인한다. 검수 기록에는 공백 검사와 별도로 속도 문제의 언어·시간·판단 근거·처리 결과를 남긴다.

### 한국어 원음 대비 공백 검수

- 각 언어에서 같은 의미 단위와 화자 교대 지점을 대응시킨 뒤, 직전 말이 끝난 시각과 다음 말이 시작된 시각을 한국어 원음과 최종 더빙에서 각각 측정한다. 구간 내부에서 먼저 말을 끝낸 경우도 검사한다. 전체 평균 대신 각 지점의 차이를 작게 유지한다.
- 최종 MP3 본편과 동일 원음의 Scribe v2 단어 시각을 게시 타임라인에 정렬한다. 양쪽의 연속 발화 공백을 각각 시간창으로 잡고 같은 창 안에서 상대 언어의 최장 연속 공백을 측정한다. 밀리초 정밀도로 절대 차이가 1.000초 이상이면 해당 언어는 fail이다. 원음과 일치하는 장표는 보존한다. 광고 등 제외 범위를 기록한다. 단어 누락이나 배경음이 의심되면 실제 파형과 해당 구간 음성을 확인한다.
- 수정 후 최종 인코딩 MP3를 다시 전사하고 전편 양방향 검사를 반복한다. 언어별 위반 건수, 최대 차이, 최악 구간, 최종본 해시와 SRT 대응을 기록한다. 실측 위반이 남으면 후보로 표시하며 자동 검사와 사람 청취 결과를 구분한다.
- 공백 길이와 함께 시작·종료 시각의 차이도 기록한다. 한국어가 계속 말하는데 더빙만 비거나, 반대로 한국어가 쉬는 동안 더빙이 이어지면 번역과 배치를 검토한다. 겹말은 화자별 타임라인에서 별도로 확인한다.
- 장표·컷 전환 등 확인된 편집 공백은 편집 구간으로 표시하고 원래 위치와 길이를 보존한다. 음성만으로 장표 여부를 단정하지 않는다. 박종천 1편 01:04.62~01:08.68은 사용자가 확인한 인터뷰 장표 구간이다.

## Local natural-speed and gap-fit contract

The Studio window is an upper bound and rhythm reference—not a target to fill by slowing every English line. A technically fitting render that sounds dragged is a failure. Freeze cue IDs and source timing, but evaluate delivery from the **generated English audio**.

### Render policy

1. Use natural delivery with the selected model. With a model that supports a speed control, render ordinary English at a natural ElevenLabs speed of **0.90–1.00**; start at `0.95` unless a clone/model audition supports a different value in that band.
2. Do **not** derive a per-cue TTS speed below `0.90` merely to occupy a Korean slot. Do not use the former `0.70`-floor speed plan.
3. Keep post-render `atempo` preferably in **0.95–1.05** and never outside **0.92–1.08** for ordinary speech.
4. If a line still overflows or leaves an excessive new pause at those bounds, rewrite/regenerate the English. Restore source-supported detail, discourse markers, emphasis, or repetition; never add generic padding, invented facts, or stronger claims.
5. A sub-second acknowledgement/interrupted word may be a documented natural-reaction exception. Preserve a recognisable delivery rather than rushing it; retain the exception ID, overflow/overlap amount, and reason in the manifest.

### Group before synthesis

When adjacent local cues are the same speaker, have no meaningful source gap (normally ≤50 ms), and form one continuing sentence or thought, synthesize them as **one group**. Keep every original cue ID/member in the manifest and split only after forced alignment. Do not group separate turns simply because the speaker label matches.

### Measured review loop

After the first natural-speed render, calculate:

```text
raw_duration
fitted_duration
required_atempo_to_target
actual_gap = next_start - (current_start + fitted_duration)
gap_delta = actual_gap - source_gap  # compare matched non-overlapping speech boundaries in the final audio
```

Apply this loop until no ordinary group is pending:

1. Render at the fixed natural TTS speed and measure actual duration.
2. Apply only bounded `atempo`; do not stretch to a utilization percentage by default.
3. If the pause timing departs perceptibly from the matched Korean passage in either direction, or a non-exception group still overflows after the 0.92–1.08 bound, create a source-faithful fit-rewrite batch for that group and rerender it.
4. Independently audit each fit rewrite for omitted facts, invented content, names, numbers, terms, modality, and cue-to-cue handoffs before accepting it.
5. Re-measure the exact new audio. A successful request or a word-count estimate is not proof of natural cadence.

Review targets:

- same-speaker continuation: match the pause at that phrase in the Korean source;
- question→answer: match the source turn transition, including deliberate pauses;
- no unresolved audible discrepancy from the corresponding Korean pause in the final local track;
- report TTS-speed min/median/max, `atempo` min/median/max, count outside the preferred band, pending rewrites, and every short-reaction exception.

## Source-offset and published-cut alignment

- Compare exact source-media duration with the published-cut duration before rendering.
- If a source contains a front ad or bumper removed from the published cut, subtract the exact duration difference from every local start/end; do not use a rounded visual guess.
- Verify first-cue onset, last spoken end, and final master duration independently.
- MP3 delivery duration must be checked with `ffprobe`; pad/trim the final PCM timeline before encoding when necessary.

## Background, effects, and room tone

Dubbing Studio normally preserves and remixes the source background. Plain TTS API output is dry voice plus silence. To reproduce the Studio feel locally:

1. acquire the exact published source audio;
2. with explicit user permission, browser cookies may be used for a blocked public YouTube download;
3. separate vocals from the background/SFX bed (for example, Demucs `htdemucs --two-stems=vocals`);
4. mix the English dub with `no_vocals`, preserving music, transitions, effects, and room tone;
5. duck the background only while English speech is active;
6. mask or reject audible Korean vocal residue rather than calling it intentional ambience.

When using FFmpeg sidechain compression, split the voice stream explicitly:

```text
voice → asplit → [voice_mix] + [voice_sidechain]
background + voice_sidechain → sidechaincompress → ducked_background
voice_mix + ducked_background → amix → limiter
```

Reusing one unsplit voice label can produce a background-only or abnormally quiet result. Verify the final integrated loudness, not just successful command exit. A TTimes spoken mix around `-18 LUFS` is a practical starting point; preserve headroom and inspect the actual master.

## Local verification gates

Before delivery, require all of the following:

- exact source-cue count, generated-group count, and expected speaker/voice-ID counts;
- every raw/fitted group file exists, with original member cue IDs retained in the manifest;
- final timeline has the exact requested duration;
- ordinary TTS speed remains 0.90–1.00 and ordinary `atempo` remains 0.92–1.08; report the preferred-band exceptions;
- no unresolved natural-speed fit rewrite, non-exception overflow, or unexplained added gap above two seconds;
- every sub-second reaction exception is explicitly listed with its overlap/overflow reason;
- loudness and true peak measured on the final background mix;
- targeted ASR on both clean voice and final mix confirms that English remains intelligible over the bed;
- final MP3 SHA-256 recorded;
- individual clips/groups, forced-alignment data, and manifest retained for later one-cue replacement.

## 다국어 더빙 말자막 편집과 검수

각 언어판을 그 지역 시청자가 처음 보는 방송으로 편집한다. 한국어 말자막에서 가져오는 원칙은 ‘한 생각이 끝나면 화면을 넘기고, 긴 생각은 작은 의미 단위로 읽히게 나눈다’는 것이다. 한국어 원문은 뜻·화자·논리의 근거로 쓰고, 화면의 수와 경계는 최종 더빙의 어순·억양과 현지 독자의 읽는 리듬으로 정한다. 같은 대답이 영어에서는 두 장, 일본어에서는 세 장이어도 된다.

1. 질문부터 답변 끝까지 해당 언어의 대사를 먼저 읽는다. 화자 전환, 조건과 결과, 대조되는 두 항, 예시, 농담의 결말을 짚고 전편의 화면 순서를 설계한다. 화자의 말보다 결론을 먼저 보여 주지 않는다.
2. 문장이나 생각이 끝나는 자리를 화면 경계의 첫 후보로 삼는다. 앞 문장을 마친 화면에 다음 문장의 도입부만 붙인 뒤 넘기는 `A. B, / C.`를 발견하면 `A. / B, C.`부터 검토한다. 길면 B와 C를 해당 언어에서 시청자가 한 호흡에 이해할 수 있는 절로 나눈다. 쉼표·마침표는 단서다. 쉼표가 있어도 동사와 목적어가 함께 읽히는 쪽이 자연스러우면 붙이고, 쉼표가 없어도 의미와 발화의 경계가 분명하면 넘긴다.
3. 화면 전환을 정한 다음 같은 화면 안의 줄바꿈을 잡는다. 이름·제품명·수치와 단위·비교 표현을 가능한 한 함께 둔다. 조건이나 화제만으로도 독자가 다음 내용을 자연스럽게 기다릴 수 있는지, 문법의 반쪽만 남아 다음 화면을 봐야 앞 화면을 해독할 수 있는지 구별한다. 글자 수를 맞추려다 짧은 꼬리가 생기면 앞뒤 두세 장을 함께 다시 나눈다.
4. 최종 각 언어 음성과 승인 대사를 대조하고 실제 단어 시작·끝에 SRT를 맞춘다. 깨끗한 보이스 트랙의 단어 시각을 쓰면 최종 믹스에서 다시 확인한다. 질문의 답·반박·발언권 전환인 짧은 반응은 살린다. 정보 없는 호응이 독립 화면으로 번쩍이거나 농담을 끊으면 해당 언어의 대화 관습에 맞춰 처리한다. 기존 더빙에 남은 의미 있는 말을 자막 편의로 삭제하거나, 다른 화자의 대사와 한 발언처럼 붙이지 않는다.

### 시청 언어별 판단 예

- **미국 영어** — 관사와 명사, 전치사와 목적어, 구동사, 조동사와 본동사를 함께 읽게 한다. `Jae-In / Kim`처럼 한 사람의 이름을 화면이나 줄 사이에 찢지 않는다. `I think so. Anthropic could lead, / with …`에서는 짧은 답이 끝난 뒤 설명을 새 화면에서 시작한다. 영어 장편은 한 줄을 우선하고 필요하면 두 줄까지 쓴다. 줄당 약 42자, 화면당 약 1.2~5초, 초당 15~18자는 가독성 점검값이다. 초당 20자를 넘으면 실제 속도로 확인한다.
- **일본어** — 문절과 서술어의 관계를 보고 자른다. `研究者がAI同士を / 話させたらどうなるか。英語を使うでしょうか。`라면 첫 질문을 먼저 완결하고 두 번째 질문에서 넘기는 편이 읽기 쉽다. 조사로 끝난다는 이유만으로 모든 경계를 옮기지 않는다. 자연스러운 화제 제시와 목적어만 화면에 남는 경우를 구별한다. 줄머리의 닫는 괄호·구두점 등 일본어 금칙 처리와 한자·가나·영문 제품명이 섞인 실제 화면 폭도 확인한다.
- **대만 번체 중국어** — 띄어쓰기 개수 대신 어구와 절을 읽는다. 수사·양사·명사, 동사·보어, 고유명사를 보호한다. `所以 Google 也不容易。不過很多人也覺得， / 如果……`라면 앞 판단을 마친 뒤 `不過`부터 새 논지를 시작한다. `如果……就……`는 짧으면 한 장에 두고, 길면 조건을 온전히 제시한 뒤 결과로 넘긴다. 쉼표마다 자르거나 `不過`만 한 장에 남기지 않는다. 기술 용어·약어는 실제 문맥과 현지 업계의 독법으로 확인한다.

### 최종 SRT 검수

언어별 최종 SRT의 **모든 화면과 모든 인접 화면 쌍**을 순서대로 읽는다. 각 화면에서는 문법·지시 대상·수량·부정·직함·용어가 한국어 원뜻 및 최종 더빙과 맞는지 확인한다. 경계에서는 ‘무엇이 끝났고 다음 화면에서 무엇을 새로 받는가’를 본다. 현지 독자가 오해할 표현, 한 화면에 섞인 두 생각, 떨어진 결합구, 순간적으로 깜박이는 호응은 앞·해당·뒤 화면과 실제 속도로 재검토한다. 번역이나 더빙 자체의 오류는 자막 분절 오류와 구별해 기록한다.

한 구간에서 오류가 확인되면 전편에서 같은 유형을 다시 찾고, 수정 후 내보낸 SRT에서 양옆 경계·줄바꿈·표시 시간·겹침·최종 음성 싱크를 재검사한다. 언어별로 검토한 화면 수와 경계 수, 남은 문제의 타임코드를 기록한다. 전체를 검토하고 확인된 오류를 해결해야 분절 검수 pass다. 자동 탐지 결과, 해당 언어를 기준으로 한 편집 검토, 실제 현지인 시사 여부는 구분해 보고한다.

For a Korean-captioned TTimes master with an alternate English audio track, prefer a selectable English SRT/CC track rather than burning a second full subtitle layer into the same video. If an English-burned master is explicitly required, produce a separate English render; do not reduce English below mobile readability merely to coexist with the Korean lower-third caption.

## English thumbnail handoff

The English thumbnail is the final media-localization stage, not a detached design favor. Read and follow:

```text
references/english-thumbnail-workflow.md
```

Core contract:

1. Inspect the original TTimes thumbnail and freeze the approved English copy.
2. When image generation is requested, generate a new **text-free core visual**; do not substitute source inpainting plus replacement text.
3. Use TTimes editorial composition with clean Figma-style vector execution: matte black, high contrast, semi-transparent technical diagrams, fixed three-quarter camera, and restrained color.
4. Add exact words and official logos deterministically after generation. Never trust generated text or generated logos.
5. Match the clean TTimes logo to the reference thumbnail's measured size and position. Do not extract the production logo from a compressed JPEG when a transparent master exists.
6. Keep company logos legible and centered on the relevant architecture. They must not overlap dense chip linework.
7. Do not duplicate technology labels beneath company logos when the approved comparison line already contains them unless explicitly requested.
8. Compared architectures must differ structurally and visually. If HBM and HBF read as the same copper stack, preserve HBM copper/salmon and move HBF to a related gold/amber treatment.
9. Interpret coordinate edits literally: left/right changes x; up/down changes y. If “toward the center” follows “move down,” treat it as vertical unless context proves otherwise.
10. Export and inspect the actual 1280×720 JPEG before delivery.

Retain the generated core, transparent logo sources, composition script, revision outputs, and approved final JPEG so later logo or coordinate edits do not require regenerating the artwork.

## Procedure

### 0. Bootstrap cues when no CSV exists

If the input is source media rather than a Studio export:

1. acquire and hash the exact media;
2. create an analysis WAV;
3. retain raw diarization and raw ASR separately;
4. map anonymous speakers from direct evidence;
5. build source-faithful dubbing cues under 25 seconds using `references/source-media-to-dubbing-cues.md`;
6. freeze the six-column cue plan before correction and translation;
7. write both XLSX and CSV plus QA JSON.

Then continue with the correction, translation, rendering, mix, SRT, and thumbnail stages below.

### 1. Validate and freeze the source

Run:

```bash
python scripts/validate_dubbing_csv.py SOURCE.csv \
  --allow-empty-translation \
  --report source_audit.json
```

Record source SHA-256, row count, headers, speakers, first/last time, and structural findings.

### 2. Correct Korean row by row

Read all rows in sequence so pronouns and technical terms retain context. Correct only high-confidence errors:

- spacing, punctuation, casing, and obvious ASR substitutions
- names, organizations, products, and technical terms verified from the exact video or authoritative source
- canonical spellings such as `HBM`, `HBF`, `D램`, `낸드플래시`, `GPU`, `KV 캐시`

Preserve spoken meaning, modality, examples, repetitions that carry emphasis, and speaker intent. Do not summarize, add facts, or silently strengthen claims. When a term is uncertain, search/verify it before correction; preserve the source form if unresolved.

### 3. Translate for speech, not subtitles

Translate the cleaned Korean into concise natural spoken English.

- Preserve every fact, comparison, number, qualifier, question, and answer within the row.
- Prefer short active clauses and ordinary spoken syntax.
- Use canonical English technical terms and consistent names.
- Remove Korean discourse redundancy only when English would sound unnatural and no meaning is lost.
- Do not add explanatory parentheticals for foreign viewers.
- Avoid slash alternatives, translator notes, brackets, and line breaks.
- Punctuation controls pauses and therefore affects timing; keep it restrained.

### 4. Fit each translation to its fixed window

Compute `duration = end_time - start_time` for every row. Use the fit estimator in `validate_dubbing_csv.py`.

Initial target:

- preferred: estimated speech duration ≤ 92% of the cue window
- acceptable: >92% and ≤100%
- overfit: estimated speech duration >100%
- preferred English density: roughly 2.1–2.7 words/second
- soft ceiling: 2.9 words/second
- hard ceiling: 3.2 words/second

These are pre-generation heuristics, not proof of audio fit. Technical acronyms and punctuation receive extra estimated time. For short reactions, natural delivery outranks forcing the minimum density.

When overfit:

1. remove duplicated framing already implicit in the sentence;
2. replace long nominal phrases with short verbs;
3. use a shorter equivalent while preserving modality;
4. remove optional discourse markers;
5. keep all named entities, figures, comparisons, and causal links;
6. never solve fit by changing the timestamps.

### 5. Build deterministically

Create an edits JSON:

```json
{
  "rows": [
    {
      "row": 1,
      "transcription": "교정된 한국어",
      "translation": "Timing-fit spoken English."
    }
  ]
}
```

It must contain every source row exactly once. Then run:

```bash
python scripts/build_dubbing_csv.py \
  --source SOURCE.csv \
  --edits edits.json \
  --output FINAL.csv \
  --report FINAL.audit.json
```

The builder preserves immutable fields from the source rather than trusting the edits file.

### 6. Validate final CSV

Run:

```bash
python scripts/validate_dubbing_csv.py FINAL.csv \
  --source SOURCE.csv \
  --report FINAL.validation.json
```

Blocking failures:

- header, row count, speaker, start, end, or order changed
- invalid/non-monotonic timecode or `end <= start`
- empty Korean/English field
- newline inside a cell
- translation estimated beyond the hard fit ceiling
- missing edits row or duplicate edit index

Soft warnings:

- estimated speech runs slightly beyond the preferred buffer
- high word density but still under hard ceiling
- unusually sparse translation requiring semantic review

### 7. Audio verification

CSV fit is provisional until generated audio is heard.

For an existing Legacy Dubbing Studio project:

- project discovery, metadata, target SRT, and dubbed audio download may work through the API;
- segment writeback can return `401 closed-beta` on this workspace;
- never claim Studio edits were applied unless the project is read back after save/regeneration;
- if browser access reaches a login wall, stop and ask the user to sign in—never guess credentials.

After regeneration, compare actual segment audio against cue ends. Fix only overflowing or unnaturally rushed rows, regenerate, and recheck.

## Output

For Studio round-trip only, deliver:

1. import-ready UTF-8 CSV with the original five columns
2. QA JSON containing source/final hashes, row count, immutable-field check, missing fields, and timing-fit findings
3. a brief count of `preferred / acceptable / overfit / hard-overfit` rows

Do not deliver a translated SRT instead of the requested CSV. Do not overwrite the user's source export.

For source-media bootstrap mode, deliver the six-column audit workbook and matching CSV:

```text
speaker,start_time,end_time,transcription,edited_transcription,english_translation
```

Also retain raw diarization, raw ASR, named-speaker mapping evidence, cue-plan JSON, low-confidence IDs, and source/output hashes.

For a complete English release package, additionally deliver:

4. clean replaceable-cue English voice master
5. exact-duration English dub + preserved background/SFX mix
6. forced-aligned US English SRT based on the final clean voice
7. final 1280×720 English thumbnail
8. clip manifest, duration/gap/loudness/SRT/thumbnail QA, and hashes where applicable

“Done” means every requested asset exists, opens successfully, and has been checked against the final timeline or canvas—not merely that a script completed.

## Pitfalls

- Treating this as free-running prose translation rather than fixed-window dubbing
- Cleaning Korean so aggressively that it no longer matches the speaker
- Translating each row without reading neighboring context
- Preserving Korean word order and producing stiff English
- Using word count alone as proof of fit
- Changing timestamps to hide an overlong translation
- Importing into Studio and claiming success without readback
- Stopping after dry TTS and omitting the source background/SFX bed
- Building English SRT from Korean cue timing instead of the final English voice
- Treating a requested English thumbnail as outside the dubbing package
- Using generic photoreal AI-chip art instead of TTimes/Figma visual grammar
- Asking image generation to spell final copy or reproduce official logos
- Extracting the TTimes logo from a JPEG and introducing compression dirt
- Moving a logo on the wrong axis or allowing it to overlap chip linework

## Verification

A final candidate passes only when:

- deterministic validator exits 0
- source and candidate have identical immutable fields and row count
- all 83/actual N rows contain non-empty cleaned Korean and English
- no hard-overfit rows remain
- terminology is consistent across the full episode
- generated audio is spot-checked at the densest rows, speaker changes, and grouped same-speaker continuations;
- every ordinary group used TTS speed 0.90–1.00 and `atempo` 0.92–1.08; preferred-band exceptions and every sub-second reaction exception are recorded;
- no fit-rewrite group remains pending, no non-exception overflow remains, and no unresolved audible discrepancy from the corresponding Korean pause remains;
- each fit-rewrite translation has an independent source-fidelity audit for facts, names, numbers, terms, modality, and cross-cue handoffs;
- final voice/background mix has the exact requested duration and source-matched dialogue pauses and confirmed editorial gaps;
- Each requested SRT passes the full native-language editorial and adjacent-screen review above and matches its final dub. Verify English line length, two-line maximum and reading speed when English is delivered.
- requested English thumbnail is exactly 1280×720, contains exact approved copy, uses clean official logos, and passes visual inspection
