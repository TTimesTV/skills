> 실행 경로(2026-09-22): 전사·부분 재전사는 [ElevenLabs API + 기존 env](elevenlabs-runtime.md)를 따른다. 아래 사례의 청크 크기·과거 실행 결과는 현재 API 실행 지시가 아니다. 장편도 원본 업로드가 기본이며 확인된 누락 구간이나 서비스 제한이 있을 때만 분할한다.

### 1. Source acquisition

If input is a YouTube URL:

1. Fetch metadata.
2. Download best audio with `yt-dlp`.
   - If a playable page yields `No video formats found`, do not immediately ask for a reupload. Compare `yt-dlp --version` with `python3 -m yt_dlp --version`, retry format discovery/download through the newer available invocation, then try a browser-cookie source if needed.
   - Treat this as a retry ladder, not a fixed preference for one entry point. Ask for the owner MP4/MP3 or Drive link only after current-module and cookie paths fail.
3. Check native/auto captions; Korean captions can be used as a transcript/timing substrate when available.
   - **Auto-caption recheck rule:** do not conclude `CC 없음` from one compact metadata print or an early extractor response. Re-inspect the full `automatic_captions` mapping after format discovery/download, explicitly check both `ko-orig` and `ko`, and save the original-language JSON3 once if present. YouTube client/extractor responses can expose a Korean auto track on the later full metadata call even when the first summary appeared empty. Treat this as a discovery retry, not proof that captions were created in the meantime.
   - Keep auto captions as a supporting substrate only; exact cut audio + ElevenLabs remains authoritative for words and timing when the caption text is rolling, duplicated, or mangled.
4. Verify exact audio with `ffprobe`, including duration, size, bitrate, and title/source identity.

Concrete routing, retry, and sample-gate details: `references/2026-07-youtube-plan-routing-and-dual-asr-sample.md`.

If input is a YouTube title:

1. Use `yt-dlp "ytsearch5:<title>" --dump-json` or equivalent.
2. Prefer exact title/channel match.
3. If ambiguous, ask the user to choose; otherwise proceed with the most exact result and report the chosen title/channel.

If input is MP3/video file:

1. Verify file exists.
2. Run `ffprobe`.
3. Extract audio if needed.

### 2. Transcription substrate

Use both sources when available:

- YouTube captions: useful for timing and text flow, but not blindly trusted.
- ElevenLabs: use on the actual audio for Korean/English ASR and timing.

이 컴퓨터의 전사 실행은 `skills/ttimes-script-and-srt/references/elevenlabs-runtime.md`의 ElevenLabs API + 기존 env 경로를 따른다.

For this user, the approval sample is now **disabled by default**. After `/plan` approval or an execution cue such as `ㄱㄱ`, proceed directly through full-body ASR, review, integration, alignment, and final delivery. Use a 0–3 minute sample only when the user explicitly asks for a sample, when ASR is severely corrupted and a style decision is genuinely required, or when the user reverses this preference. If a sample is explicitly used, apply the dual-ASR gate below.

For an explicitly requested 0–3 minute sample in a no-caption technical interview, use a dual-ASR check before presentation:

- Primary timing substrate: ElevenLabs Scribe v2 API, source language, word timestamps; use the existing env.
- Optional comparison for unresolved speech: ElevenLabs Scribe v1 on only the affected interval.
- Targeted 12–25 second re-ASR for high-risk names, titles, numbers, and malformed phrases.
- Prompt-conditioned recognition is supporting evidence, not proof. Compare model outputs and verify proper nouns from official sources.
- When the comparison restores source wording that Main smoothed away, prefer the actual phrase and redesign only the cue boundary. Typical high-impact distinctions include `모셨습니다/오셨습니다`, `선언적인/선언하는`, discourse markers, hedge wording, and repeated scope words.
- End a nominal 0–3 minute sample at the nearest completed thought if a new question begins just before 3:00; state the actual end time when presenting it.

For long media, use the existing ElevenLabs runtime and validate non-empty JSON, word timestamps, and speech-tail coverage. Split only for service constraints or confirmed missing intervals; preserve absolute offsets and rebuild affected derivatives.

If one chunk contains a local repeated-token/hallucination hole, repair the **narrow interval** with a second ASR model, then replace both overlapping segments and word timestamps in the merged JSON and regenerate every affected baseline/range derivative. Any draft or reviewer output produced from the pre-repair range is stale for that interval; rebuild the interval from the repaired source and rerun source/omission review on the current candidate hash. Do not merely patch the visible repeated token while leaving a 20–30 second timing hole. See `references/2026-07-20-long-interview-local-asr-repair.md`.

**Correction safety:** avoid broad substring replacements. Use exact phrase replacements with expected occurrence counts, scan for newly introduced corruptions after every pass, and keep refinement scripts idempotent so rerunning an older rule cannot undo a clip-verified correction.

**Reviewer adjudication safety:** subagent corrections are hypotheses, not authority. When a reviewer’s familiar term conflicts with targeted clip ASR, direct source evidence, or sentence syntax, Main must adjudicate and keep the source-backed reading. In particular, distinguish ordinary vocabulary from similar product names (`트레이닝` vs `Trainium`), verify contract direction hidden by Korean particles, and do not treat matching punctuation counts as proof of semantic correctness. See `references/2026-07-10-long-no-caption-ai-chip-review-workflow.md`.
