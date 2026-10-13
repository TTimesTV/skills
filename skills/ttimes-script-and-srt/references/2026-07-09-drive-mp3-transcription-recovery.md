> 실행 경로(2026-09-22): 전사·부분 재전사는 [ElevenLabs API + 기존 env](elevenlabs-runtime.md)를 따른다. 아래 사례의 청크 크기·과거 실행 결과는 현재 API 실행 지시가 아니다. 장편도 원본 업로드가 기본이며 확인된 누락 구간이나 서비스 제한이 있을 때만 분할한다.

# 2026-07-09 Drive MP3 → TTimes SRT: ASR recovery pattern

## Trigger

Use this when a long Google Drive MP3/video is being converted to TTimes-style Korean SRT and ASR shows hallucinated repetition or collapse in the latter half, e.g. repeated `네` segments from ~45–85 minutes even though the audio contains real speech.

## Durable lesson

Do **not** keep editing the full-file ASR if a long section collapses into repeated filler. Treat it as an ASR substrate failure and rerun ASR in short chunks, then merge timestamps with offsets.

## Proven workflow

1. Download exact Drive source and verify with `ffprobe`.
2. Run ASR once if useful, but inspect time windows after ~40–50 minutes.
3. If a window becomes repeated `네`/filler while audio is not silent:
   - Extract only the confirmed missing interval, retaining enough adjacent speech and its absolute offset.
   - Run ASR per chunk with word timestamps.
- 전사 요청의 지원 옵션과 실행 명령은 `elevenlabs-runtime.md`를 따른다.
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

## Drive download fallback used

If `gdown --fuzzy` is unsupported or the Drive file triggers a virus-scan warning page, extract the file id and run:

```bash
python3 -m gdown 'USER_CONFIGURED_CLOUD_REFERENCE<FILE_ID>' -O input.mp3
```

Then verify the resulting file with `file` and `ffprobe` before ASR.
