# 2026-07-08 K-startup TTimes SRT trial — cue refinement and delivery preferences

## Context

User tested the new `ttimes-script-and-srt` pipeline on the YouTube title:

`자원을 효율적으로 안전하게! 유럽서 주목하는 K-스타트업` — 티타임즈TV, about 13:27.

Workflow used:

1. Discover exact YouTube video from title with `yt-dlp ytsearch`.
2. Download Korean YouTube captions (`ko`, `ko-orig`) and source audio.
3. Verify audio with `ffprobe`.
4. Run chunked MLX Whisper word timestamps.
5. Generate a TTimes-style `[스크립트].txt`.
6. Generate line-preserving SRT from the script.
7. User judged first SRT roughly 80점: mostly aligned but cue timing/length not precise enough.
8. A refined SRT was produced by rematching cue bodies to word timestamps.

## Durable lessons

### 1. Delivery preference

For this user, default delivery for this class should be:

- script `.txt` as a separate attachment when script is part of deliverable
- `.srt` as a separate attachment
- **do not include validation JSON in a ZIP for the user by default**
- **do not send ZIP unless the SRT/TXT attachment does not appear or the user asks for a bundle**

The user explicitly pushed back on sending ZIPs with JSON: they only wanted the SRT attachment. Keep validation JSON internally if useful, but do not package it for delivery unless requested.

### 2. Cue timing refinement needed for 95점 target

A structurally valid line-preserving SRT is not enough. For a 95점 target, after the first alignment pass:

1. Keep final script non-empty lines as the authoritative cue bodies.
2. Normalize script text and ASR words into character streams.
3. Use sequence matching to map each script line's character range to ASR word-index ranges.
4. For each cue:
   - `start = matched_first_word.start - small_start_padding`
   - `end = matched_last_word.end + end_padding`
5. Resolve overlaps by midpoint/boundary adjustment.
6. Enforce minimum display duration for short lines and a max around 3.5–3.8s for dense Korean captions.
7. Produce a low-match cue list; do not claim those are 95점 without manual/alternative timing.

Useful default pads from the trial:

- start pad: ~0.05–0.08s
- end pad: ~0.14s for short lines, ~0.20s for longer lines
- minimum duration: ~0.75s for very short cues, ~0.95s otherwise
- maximum duration: ~3.2s short cues, ~3.8s longer cues

### 3. Foreign-language reaction segments are high risk

The K-startup video had an English/foreign-language street-reaction segment around 11:40. Korean YouTube captions and MLX Korean ASR both degraded badly. Subagents flagged this as high-risk. Future pipeline should:

- detect non-Korean segments
- prefer native caption word timings if available
- consider English ASR for that clip
- if translating/paraphrasing, align the translated Korean cue to caption/English ASR timing rather than Korean ASR text similarity
- mark these cues as low-match/manual-review candidates

### 4. Subagent usage worked, but main must patch and validate

Subagents were useful as reviewers:

- proper noun / technical term corrections
- line-length/readability problems
- omission/distortion checks

But the main agent must integrate fixes, regenerate files, and validate SRT itself. Do not rely on subagent self-report as proof of final file quality.

### 5. Pitfalls noticed

- Global string replacements can corrupt terms (`ENGIE` became `EENGIEIE` when replacing `NG`). Use word-boundary or ordered replacements.
- Manual line-breaking introduced duplicates like duplicated `PCR` or duplicated `한국`. After line-breaking, run a simple duplicate-neighbor/term scan.
- Validation summary can mention cue count/exact match in chat, but the JSON file should stay internal by default.
