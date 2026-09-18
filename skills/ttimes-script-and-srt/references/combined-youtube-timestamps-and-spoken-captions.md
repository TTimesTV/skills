# Combined YouTube timestamps + spoken captions

Use when the user gives a YouTube URL and asks for both `타임스탬프` and `말자막` in one request.

## Routing

Do not force the request into only one skill:

- Generate semantic YouTube chapters according to `ttimes-youtube-timestamps`.
- Generate the full spoken-caption TXT/SRT according to `ttimes-script-and-srt`.
- Deliver them as separate artifacts; chapters are not a substitute for the full spoken transcript.

### Final-URL reset rule

The user's latest explicit routing instruction wins. A common production conversation starts as `기존 컷편 말자막 재활용 + 새 앞광고/하이라이트만 작업` and later becomes `그냥 이 URL 말자막이랑 타임스탬프 다시 해줘`. At that moment:

1. Stop searching for old SRTs, roughcuts, or offset anchors.
2. Use the supplied final YouTube URL as the audiovisual authority.
3. Fetch duration/title/description chapters, acquire final audio, and ASR the final edit.
4. Rebuild captions from the final edit, using old transcripts only as a terminology/correction reference—not as a timeline authority.
5. Keep the response terse; do not narrate the abandoned reuse investigation.

This avoids spending more time proving that old roughcuts differ after the user has explicitly authorized full regeneration.

### Exactly-two-files mode

When the user says `총 2개`, the default pair is:

1. `*_말자막.txt` — timecode-free caption bodies, no speaker names/indices/markdown unless requested. One cue per non-empty line; do not encode one cue as a two-line paragraph because downstream line-preserving SRT workflows treat each non-empty line as a cue.
2. `*_타임스탬프.txt` — copy-ready `00:00 제목` chapter list.

Do not attach corrected JSON, validation logs, Markdown duplicates, or an extra SRT. If SRT is explicitly requested, replace the body-only TXT with the SRT-as-TXT deliverable rather than increasing the count without permission.

## Acquisition fallback

1. Fetch metadata first: title, channel, duration, language, caption availability.
2. Attempt native/automatic captions once when available.
3. If caption download returns a platform rate-limit error such as HTTP 429, do not loop on the same endpoint. Download exact-source audio/video and run MLX Whisper directly.
4. Use `mlx-community/whisper-large-v3-turbo`, explicit source language, word timestamps, and a narrow initial prompt containing the title and high-risk topic terms.
5. Keep raw ASR immutable; write corrected derivatives separately.

## Proper-name and term verification

Before final caption output:

- Search article titles, exact quotations, official bios, and high-quality reprints for names/models that ASR mangles.
- Prefer exact English spelling for hard technical names when Korean phonetics are ambiguous.
- Build a correction ledger and scan the final TXT/SRT for every rejected variant.
- Examples of high-risk classes: person names, model codenames, company officer titles, statistics, publication names, and product capitalization.
- Search-result snippets may locate a source, but use the underlying official/reputable page or several consistent reprints before fixing a disputed term.

## Deliverables and validation

Recommended set:

- `*_타임스탬프.md`: copy-ready semantic chapters.
- `*_말자막.txt`: complete cleaned speech with cue timestamps or body-only form as requested.
- `*_말자막_srt.txt` or `.srt`: editor-facing timed cues.
- corrected JSON stays internal unless requested.

Validate:

- source identity and duration,
- cue/segment counts,
- monotonic nonnegative timestamps,
- SRT structural block count,
- rejected-ASR-token scan,
- chapter starts aligned to actual topic changes,
- explicit caveat when platform captions were unavailable and direct ASR was used.

Do not overstate exact sync if cleaned text was split by proportional interpolation rather than word-level alignment. For a delivery-quality SRT, use the body-first alignment and ASR speech-coverage gates in the main skill.
