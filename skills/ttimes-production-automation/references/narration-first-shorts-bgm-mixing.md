# Narration-first Shorts BGM mixing

## Use case

A short engineering explainer already has approved picture order, narration, and burned speech captions, but feels empty. The user asks for a playable BGM version rather than recommendations.

## Editorial sound brief

Default industrial-documentary bed:

- 100–110 BPM restrained electronic pulse
- low machinery hum/drone
- sparse low kick or bass pluck
- occasional metallic off-beat tick
- small filtered-noise swells at major visual or argument transitions
- no vocals; very little melody

Useful generation prompt:

```text
Instrumental industrial documentary underscore, dark and restrained,
low electronic pulse, subtle metallic percussion, deep machinery hum,
minimal melody, gradually building tension, clean modern technology atmosphere,
no vocals, no cinematic orchestra, no aggressive cyberpunk synth.
```

The picture still carries the physics. Music supplies continuity; optional scene-specific effects such as bubbles, fan airflow, or a low impact can be added only at meaningful moments.

Treat procedural/synthesized music as a temporary proof of mix, not as style authority. If the PD rejects the feel and chooses to generate or source a new track, replace it cleanly from the narration-only master; do not defend the old bed, stack both tracks, or keep polishing a rejected direction. When the user asks for a generation prompt, return a copy-ready prompt with immediate rhythmic entry, section-by-section energy, speech-frequency space, exact target duration, and explicit negative constraints.

## Duration fitting

Lock picture and narration speed before generating music whenever possible, and request the exact target duration. Never choose narration speed merely to rescue a short BGM file.

Use the measured duration mismatch ratio:

```text
absolute mismatch <= 5%  → subtle `atempo` adjustment
mismatch > 5%            → musical crossfade extension, loop, or regenerate
large structural mismatch → regenerate to target duration
```

For a small mismatch, stretch the BGM rather than the narration. For a larger extension, repeat a musically compatible late section with a real crossfade and fade the final tail; do not append silence or hard-loop at the file boundary. Re-measure the extended BGM alone before ducking.

## Level strategy

1. Measure narration-only integrated loudness and true peak.
2. Normalize or gain-stage the BGM by itself, usually around 12–18 dB below narration.
3. Apply light sidechain compression to the BGM keyed by narration.
4. Mix without changing the approved narration gain unless a measured peak problem requires it.
5. Measure the final program again. A small integrated-loudness rise is acceptable if speech remains dominant and true peak has safe headroom.

Validated example:

```text
narration-only: about -15.7 LUFS
BGM-only: about -27.9 LUFS
final mix: about -15.3 LUFS
final true peak: about -3.7 dBTP
```

These are example measurements, not universal delivery standards.

## FFmpeg stereo ducking pattern

```bash
ffmpeg -y -i "$video" -i "$bgm" \
-filter_complex "
  [0:a]pan=stereo|c0=c0|c1=c0[voice];
  [1:a][voice]sidechaincompress=
    threshold=0.08:ratio=3:attack=15:release=300:makeup=1[duck];
  [voice][duck]amix=inputs=2:duration=longest:
    dropout_transition=0:normalize=0,
    alimiter=limit=0.94,
    apad=pad_dur=0.05,
    atrim=duration=${DURATION}[a]
" \
-map 0:v:0 -map '[a]' \
-c:v copy -c:a aac -b:a 192k -ar 48000 -ac 2 \
-movflags +faststart "$output"
```

Set `DURATION` from the approved video duration. Adapt threshold and BGM level after listening; the filter values are a tested starting point.

## Frame-preservation pitfall

Do not append `-shortest` automatically. In the validated case, narration/BGM ended only milliseconds before the 30fps picture, yet `-shortest` removed the last video frame. Fix by:

- mixing with `duration=longest`;
- padding and trimming audio to the approved video duration;
- omitting `-shortest`;
- confirming the final frame count equals the input.

For strict proof that picture was not altered, compare decoded raw-frame hashes:

```bash
ffmpeg -v error -i "$input"  -map 0:v:0 -f hash -hash sha256 -
ffmpeg -v error -i "$output" -map 0:v:0 -f hash -hash sha256 -
```

When `-c:v copy` and duration are preserved, the decoded hashes should match.

## Required QA

- ffprobe: duration, 1080×1920, 30fps, H.264/yuv420p, stereo AAC 48kHz
- input/output frame count equality
- decoded raw-frame hash equality when video is stream-copied
- full decode with no errors
- narration-only, BGM-only, and final loudness/true-peak measurements
- beginning and ending audio inspection; no abrupt BGM cutoff
- burned-caption readability unchanged
- final SHA-256

If platform upload times out, use the separate large-media transport recovery in `artifact-delivery-verification`; do not conflate audio-master approval with delivery compression.
