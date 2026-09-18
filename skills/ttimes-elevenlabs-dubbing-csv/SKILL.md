---
name: ttimes-elevenlabs-dubbing-csv
description: Build TTimes dubbing cues from Studio CSV or source media, then produce the complete Korean-to-English dub, background mix, US SRT, and English thumbnail package.
metadata:
  hermes:
    tags:
    - ttimes
    - elevenlabs
    - dubbing
    - csv
    - korean
    - english
    - timing
    - subtitles
    - thumbnail
    - imagegen
    category: media
    requires_toolsets:
    - terminal
    - file
  platforms:
  - macos
  - linux
  version: 1.4.0
---

# TTimes ElevenLabs Dubbing CSV

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

When the user requests an English release package, **the thumbnail is part of this skill and part of definition of done**. Do not stop after producing the MP3 or SRT.

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

For this user, the model contract is fixed: use MLX Whisper locally for transcription and targeted re-transcription, use local `pyannote/speaker-diarization-community-1` for speaker diarization, and use GPT Sol only for Korean correction and English translation. Do not upload source audio for cloud diarization. Do not substitute Qwen3-ASR or a local LLM merely for speed or local execution. Verify speaker mapping independently.

Use this when no Studio CSV exists. Read and follow:

```text
references/source-media-to-dubbing-cues.md
```

The skill must acquire the exact source, diarize speakers, transcribe raw Korean, map speaker clusters from evidence, and create the same six-column cue workbook used as the production reference. Dubbing cues are **not subtitle cues**: split on speaker changes, keep continuing technical speech in coherent long units, preserve genuine short reactions, and keep every cue below 25 seconds.

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

- `eleven_flash_v2`: English-specialized, clearer and more stable English pronunciation; no v3 audio tags. Prefer it when English intelligibility and technical acronym consistency matter more than expressive acting.
- `eleven_v3`: multilingual and more expressive; supports sparse audio tags such as `[curious]`, `[amused]`, and `[thoughtful]`. Tags are optional, not a quota. Do not add them to ordinary technical exposition.
- Do not mix models within one episode unless an audible A/B test proves that timbre and cadence remain consistent.
- A voice name ending in `EN` does not make v3 an English-specialist model; model and clone training language are separate concerns.
- For acronyms and brands, audition the exact clone/model combination. Use prompt-only spelling or a pronunciation dictionary when `HBF`, `zHBM`, `SK hynix`, `eSSD`, `LPU`, etc. drift.

## Local natural-speed and gap-fit contract

The Studio window is an upper bound and rhythm reference—not a target to fill by slowing every English line. A technically fitting render that sounds dragged is a failure. Freeze cue IDs and source timing, but evaluate delivery from the **generated English audio**.

### Render policy

1. Render ordinary English at a natural ElevenLabs speed of **0.90–1.00**; start at `0.95` unless a clone/model audition supports a different value in that band.
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
added_gap = actual_gap - max(0, source_gap)
```

Apply this loop until no ordinary group is pending:

1. Render at the fixed natural TTS speed and measure actual duration.
2. Apply only bounded `atempo`; do not stretch to a utilization percentage by default.
3. If the remaining added pause is >2 seconds, or a non-exception group still overflows after the 0.92–1.08 bound, create a source-faithful fit-rewrite batch for that group and rerender it.
4. Independently audit each fit rewrite for omitted facts, invented content, names, numbers, terms, modality, and cue-to-cue handoffs before accepting it.
5. Re-measure the exact new audio. A successful request or a word-count estimate is not proof of natural cadence.

Review targets:

- same-speaker continuation: normally about 0.15–0.8 seconds; inspect anything above one second;
- question→answer: normally about 0.25–0.8 seconds unless source evidence supports a deliberate pause;
- no unexplained added gap above two seconds in the final local track;
- report TTS-speed min/median/max, `atempo` min/median/max, count outside the preferred band, pending rewrites, and every short-reaction exception.

## Source-offset and published-cut alignment

- Compare exact source-media duration with the published-cut duration before rendering.
- If a source contains a front ad or bumper removed from the published cut, subtract the exact duration difference from every local start/end; do not use a rounded visual guess.
- Verify first-cue onset, last spoken end, and final master duration independently.
- MP3 delivery duration must be checked with `ffprobe`; pad/trim the final PCM timeline before encoding when necessary.

## Background, effects, and room tone

Dubbing Studio normally preserves and remixes the source background. Plain TTS API output is dry voice plus silence. To reproduce the Studio feel locally:

1. acquire the exact published source audio;
2. if a public YouTube download is blocked, request a source file supplied for the current task;
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

## English subtitle handoff after dubbing

Do not turn the 5–25 second dubbing clips directly into subtitle cues. Dubbing clips optimize generation and replaceability; subtitle cues optimize reading.

Procedure:

1. freeze the final English voice track;
2. obtain word timestamps from the clean voice track, not from the Korean source timing and preferably not from the background mix;
3. align the approved `spoken_english` sequence to those words;
4. rebuild a separate English SRT;
5. verify it against the final background mix and video.

TTimes long-form English subtitle defaults:

- one line by default, two lines when needed; never three lines;
- soft target around 42 characters per line; do not shrink the font to force a long sentence into one line;
- target roughly 1.2–5.0 seconds per subtitle cue, with longer durations only when reading remains easy;
- target about 15–18 characters per second and inspect anything above 20;
- split at a clause, phrase, or sentence boundary; keep articles with nouns, prepositions with their objects, auxiliaries with their verbs, and names/technical terms intact;
- line 2 may begin with a natural conjunction or clause pivot (`but`, `because`, `while`, `when`, `if`) when that improves syntax;
- subtitle text follows the final spoken English, not the Korean wording; remove v3 delivery tags and internal production notes;
- preserve canonical casing such as `HBM`, `HBF`, `zHBM`, `SK hynix`, and `OpenAI`;
- use the actual English speech onset/end. Never copy Korean SRT timing onto the English dub.

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
- no fit-rewrite group remains pending, no non-exception overflow remains, and no unexplained added gap above two seconds remains;
- each fit-rewrite translation has an independent source-fidelity audit for facts, names, numbers, terms, modality, and cross-cue handoffs;
- final voice/background mix has the exact requested duration and no unexplained gap above two seconds;
- English SRT follows the final spoken words, uses no three-line cues, and passes line-length/CPS checks
- requested English thumbnail is exactly 1280×720, contains exact approved copy, uses clean official logos, and passes visual inspection
