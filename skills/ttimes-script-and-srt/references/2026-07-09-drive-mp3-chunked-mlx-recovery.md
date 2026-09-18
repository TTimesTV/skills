# 2026-07-09 source MP3 → TTimes SRT: chunked MLX recovery pattern

## Trigger

Use this when a long user-provided MP3/video is being converted to TTimes-style Korean SRT and full-file MLX Whisper shows hallucinated repetition or collapse in the latter half, e.g. repeated `네` segments from ~45–85 minutes even though the audio contains real speech.

## Durable lesson

Do **not** keep editing the full-file ASR if a long section collapses into repeated filler. Treat it as an ASR substrate failure and rerun MLX Whisper in short chunks, then merge timestamps with offsets.

## Proven workflow

1. Use the exact user-provided local source and verify with `ffprobe`.
2. Run full-file MLX once if useful, but inspect time windows after ~40–50 minutes.
3. If a window becomes repeated `네`/filler while audio is not silent:
   - Extract 5-minute WAV chunks with `ffmpeg -ss <offset> -t 300 -ac 1 -ar 16000`.
   - Run MLX Whisper per chunk with word timestamps.
   - Prefer disabling previous-text conditioning if the CLI supports it; if not, chunking alone still prevents long-context drift.
   - Merge segment/word timestamps by adding the chunk start offset.
4. Generate captions from the merged chunked JSON, not from the collapsed full-file JSON.
5. Validate final deliverable:
   - `script non-empty lines == SRT cue count`
   - `SRT bodies == script lines`
   - monotonic, no overlaps, no non-positive durations
   - no sentence-final periods in body
   - no visible-length overflow
6. Spot-check first 3 minutes, a middle block, the previously collapsed range, and the late/end block.

## Extra pitfall: visible length

For this user's bottom TTimes box, count **spaces too** when enforcing 25/27 visible character limits. A cue can pass a non-space character count but still look too wide on screen. If a later term patch makes a body exceed 27 chars, split that cue and renumber; do not patch SRT timecode lines with broad regexes.
