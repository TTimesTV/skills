# Approved landscape highlight → vertical sample MP4

Use when the user wants an actual sample MP4 from a YouTube long-form video after a reference Short has shown the desired 3-band wrapper style.

## Scope classification

First classify the task correctly:

```text
existing edited highlight → vertical wrapper = deterministic derivative render
full interview body → choose/reorder/design a new highlight = editorial pipeline
```

Do not describe a successful wrapper sample as proof that autonomous editorial selection, B-roll sourcing, or caption design has been solved.

## Source discovery

1. Inspect YouTube metadata and description chapters before downloading. Many TTimes masters explicitly mark `하이라이트` and the next chapter.
2. Download the specified YouTube URL itself; do not substitute a convenient local video.
3. Treat chapter timestamps as coarse boundaries. Inspect frames, captions, and audio at approximately `start-3s`, `start`, `end-3s`, `end`, and `end+3s`.
4. Record exact source genealogy, hash, actual downloadable resolution, and any mismatch between metadata duration and transcript duration.

## Boundary handling

- Prefer a frame-accurate re-encode for the extracted highlight.
- If the next-program frame appears before the final spoken syllable ends, freeze the last valid highlight frame briefly while continuing the original audio to the natural endpoint.
- Keep freeze duration minimal and record it. This is safer than allowing an unrelated host/intro frame into the derivative.
- Never silently trim a final syllable merely to hit a round chapter timestamp.

Session example:

```text
coarse chapter: 00:26–01:08
verified speech start: 00:26.32
next intro visual: 01:08.59
last valid highlight frame: 01:08.34
final audio endpoint: 01:08.60
output duration: 42.28s
```

## Template-fidelity gate

Before rendering, classify the requested fidelity:

```text
STRUCTURE_MATCH = same 3-band information architecture
VISUAL_MATCH = measured viewport, background, border, label, type hierarchy, colors, and safe areas
PIXEL_IDENTITY = original clean template/project/font assets available
```

If the user says `기존 템플릿과 동일하게`, do not default to a merely similar shell. Use `VISUAL_MATCH` immediately and disclose that `PIXEL_IDENTITY` requires the original MOGRT/PSD/project and font files. Never invent rounded cards, English badges, divider bars, accent colors, or labels that are absent from the reference.

### Reference-shell reconstruction

1. Extract a representative frame from the actual reference Short.
2. Measure the **outer video viewport**, border, label tab, top/bottom boundaries, text baselines, and safe margins. Use audio-aligned frame correlation against the landscape source when possible; a visual estimate may capture only the inner picture, not the outer viewport.
3. Reuse the reference background texture when rights and task context permit, but remove all old static copy before drawing replacement copy.
4. Erase old text with generous masks that include compression glow and strokes. On textured backgrounds, narrow masks create visible rectangular patches; prefer a full-width reconstruction band or proper inpainting, then inspect at native resolution.
5. Cut alpha only for the exact middle viewport; redraw the border and `하이라이트` tab above it so old video/labels cannot leak or duplicate.
6. Render new copy with the closest installed weight and measured size/line spacing. State clearly when the original font is unavailable.
7. Compare reference and output contact sheets side by side before delivery.

One session's first visual estimate (`x≈15–342, y≈230–409` at 360×640) described the inner visible picture. Audio-aligned image matching found the outer landscape window closer to `x≈8, y≈217, w≈345, h≈195`. Preserve this distinction; neither number is a universal template constant.

### Chroma-subsampling dimension rule

For H.264 `yuv420p`, scale the inserted video to even width and height. A measured outer window may be odd-sized; keep the odd outer border geometry, but contain an even-sized 16:9 video inside it and center the residual 1–3 pixels. Asking FFmpeg to pad to a dimension smaller than its chroma-rounded scale output causes `Padded dimensions cannot be smaller than input dimensions`.

## Wrapper implementation

Recommended minimal stack:

- `yt-dlp`: source and metadata
- FFmpeg/FFprobe: extract, composite, encode, decode-test
- Pillow: Korean static title overlay PNG
- YouTube captions or MLX Whisper: boundary and wording verification

Render order:

```text
1080×1920 background
+ scaled 16:9 highlight viewport (contain; no face crop)
+ approved top/bottom transparent title overlay
+ original highlight audio
→ H.264 yuv420p + AAC + faststart
```

Do not assume the viewport fills the full width just because it is 16:9. Measure the reference Short. In one observed 360×640 reference, the visible central content was approximately `x=15–342, y=230–409`; use this only as a reference-specific measurement, not a universal TTimes rule.

Likewise, measured `-13.5 LUFS` on one reference is a matching clue, not a channel-wide mastering standard unless confirmed across more masters.

## Copy discipline

- Derive eyebrow, headline, bottom hook, and CTA from source-supported wording.
- Avoid adding performance comparisons, price multiples, percentages, universals, or causal claims merely to make the sample punchier.
- If no PD is present, choose a conservative source-supported draft and mark it as prototype copy.

## Mandatory QA gates

### Artifact gate

- file exists and is non-empty
- duration in expected range
- exact 1080×1920 output
- target FPS
- H.264, `yuv420p`, AAC, audio present

### Decode gate

```bash
ffmpeg -v error -i sample.mp4 -f null -
```

Require exit code 0 and an empty error log.

### Visual gate

Generate a 2-second contact sheet plus start/middle/end frames. Inspect:

- Korean text clipping and spelling
- central-video aspect distortion
- unintended black frames
- caption legibility
- next-chapter/intro leakage
- safe-area collisions

### Audit gate

Store:

```text
sample.ffprobe.json
sample.sha256
technical_qa.json
visual_qa.md
contact_sheet_2s.jpg
```

A subagent's claim that the file exists is not sufficient. The parent must re-read the reports, rerun FFprobe/hash/decode checks, and inspect the contact sheet before delivery.

## Subagent handoff

The implementer subagent's final objective must name the exact absolute `sample.mp4` path and require real values for size, duration, resolution, codecs, SHA-256, decode exit code, and QA status. Subagents cannot deliver to Telegram; the parent verifies and sends the dated Korean display filename with a platform receipt.

## Telegram delivery

Use a dated Korean display filename for the user-facing attachment while retaining canonical `sample.mp4` internally. Current Hermes CLI attachment syntax is a `MEDIA:` directive in the message body, not `--media`/`--caption` flags:

```bash
hermes send --to 'telegram:<chat_id>' --json \
  'MEDIA:/absolute/path/YYMMDD_한국어 제목.mp4'
```

Require `success` plus a real delivery receipt/message ID. If Hermes reports `cron_auto_delivery_duplicate_target`, it intentionally skipped the duplicate send; put the same `MEDIA:/absolute/path` directive in the parent session's final response so auto-delivery carries the artifact. Do not report the skipped call as a sent attachment.

## Common failure modes

- Treating `기존 템플릿과 동일하게` as permission to make a thematically similar shell.
- Adding rounded cards, badges, dividers, or brand accents that do not exist in the measured reference.
- Confusing an inner-picture estimate with the outer video viewport and border geometry.
- Using narrow text-erasure masks that leave old glyph glow or visible rectangular reconstruction patches.
- Stretching into an odd-sized `yuv420p` window instead of containing an even-sized video inside the measured outer frame.
- Stopping at a plan instead of producing the MP4 after execution is approved.
- Using chapter timestamps without inspecting actual frame/audio boundaries.
- Letting the next host/intro frame leak into the Short.
- Trimming the final spoken syllable to avoid that leak instead of using a short frame hold.
- Stretching 16:9 content to fill 9:16.
- Calling an approximate brand recreation an exact template match when original fonts/assets are unavailable.
- Reporting local creation as successful Telegram delivery without a `message_id`.
