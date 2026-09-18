# Vertical technical-Short storyboard sketch

Use this reference after a 45–70 second technical script is approved and the PD asks for a visual sketch with STT and editorial captions.

## Deliverable contract

- 12–15 distinct vertical frames for a roughly one-minute Short.
- Exact 1080×1920 (9:16), even when later source footage may be 16:9.
- Text-free generated base image per frame.
- Deterministic Korean overlays: selective editorial caption at the top, source-faithful STT at the bottom.
- One numbered contact sheet and one rough slideshow MP4.
- Silence is acceptable only when this is explicitly an editorial sketch and `STT` means visible speech-caption planning rather than TTS narration.

## Manifest first

Freeze JSON/CSV rows before generating:

```text
id
duration
stt[]
emphasis_or_explainer[]
visual_mechanism
```

The durations must sum to the target runtime. Keep source narration tokens intact in `stt[]`; redesign only boundaries.

## Image generation

1. Generate and approve frame 1 as the style anchor.
2. Use it as the reference for later frame batches.
3. Prompt for large, text-free subjects, limited colors, clean upper caption space, no logos/UI/watermarks.
4. Verify every base image in one contact sheet before captioning.
5. Treat `portrait` as a request, not proof. If the provider returns 1024×1536 (2:3), crop or extend to 864×1536, then resize with Lanczos to 1080×1920. Bias the crop only after visually deciding which side contains critical infrastructure.

## Caption composition

- Put editorial copy in the upper safe zone; use one or two strong lines rather than restating the STT.
- Put STT in a lower high-contrast bar.
- Use a Korean broadcast font such as Gmarket Sans.
- Preserve supplied STT line arrays. If a line does not fit, reduce font size or manually repartition at a grammatical boundary; do not let automatic wrapping strand `아니라`, `작아지고`, `합니다`, `AI 데이터센터`, or another protected chunk.
- For a long final thesis, split by complete relations: `first battlefield / named location / decisive criterion`.

## Rough MP4

Render the captioned stills for manifest durations, usually H.264/yuv420p/30fps and AAC silence when the sketch is intentionally mute.

Concat-demuxer pitfall: repeating the last still to honor its duration can add one extra final-frame hold. Compare ffprobe duration with the manifest sum and trim/render with the exact target duration when needed. JPEG full-range inputs can also yield `yuvj420p`; explicitly convert full→TV range and request `yuv420p`.

## QA

- Contact sheet: all 12–15 frames, readable top copy and STT, no generated text artifacts.
- Per-frame: exact 1080×1920 and no critical crop loss.
- Caption: no clipping, no orphan predicates or protected-phrase splits.
- MP4: expected duration, H.264, yuv420p, 30fps, AAC if present, full decode exit 0.
- Delivery: concise Korean filename, rough MP4 plus contact sheet; individual frames stay internal unless requested.
