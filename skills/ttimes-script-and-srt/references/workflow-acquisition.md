### 1. Source acquisition

If input is a YouTube URL:

1. Fetch metadata.
2. Download best audio with `yt-dlp`.
   - If a playable page yields `No video formats found`, do not immediately ask for a reupload. Compare `yt-dlp --version` with `python3 -m yt_dlp --version`, retry format discovery/download through the newer available invocation, then request a user-provided media file if public access remains unavailable.
   - Treat this as a retry ladder, not a fixed preference for one entry point. If the current module still cannot access the source publicly, ask for the owner-provided MP4/MP3. Do not load personal browser credentials.
3. Check native/auto captions; Korean captions can be used as a transcript/timing substrate when available.
   - **Auto-caption recheck rule:** do not conclude `CC 없음` from one compact metadata print or an early extractor response. Re-inspect the full `automatic_captions` mapping after format discovery/download, explicitly check both `ko-orig` and `ko`, and save the original-language JSON3 once if present. YouTube client/extractor responses can expose a Korean auto track on the later full metadata call even when the first summary appeared empty. Treat this as a discovery retry, not proof that captions were created in the meantime.
   - Keep auto captions as a supporting substrate only; exact cut audio + MLX remains authoritative for words and timing when the caption text is rolling, duplicated, or mangled.
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
- MLX Whisper: use on the actual audio for Korean/English ASR and timing.

`media-localization-workflows`에 기록된 기존 MLX Whisper 경로는 이 Windows 장치에서 사용할 수 없다. 원격 서비스를 임의로 대체하거나 ASR/정렬을 실행했다고 주장하지 말고, 검증된 backend를 명시적으로 선택하기 전까지 dependency gate를 사용한다.

For this user, the approval sample is now **disabled by default**. After `/plan` approval or an execution cue such as `ㄱㄱ`, proceed directly through full-body ASR, review, integration, alignment, and final delivery. Use a 0–3 minute sample only when the user explicitly asks for a sample, when ASR is severely corrupted and a style decision is genuinely required, or when the user reverses this preference. If a sample is explicitly used, apply the dual-ASR gate below.

For an explicitly requested 0–3 minute sample in a no-caption technical interview, use a dual-ASR check before presentation:

- Primary: `mlx-community/whisper-large-v3-turbo` with Korean, word timestamps, and `condition_on_previous_text=False`.
- Comparison: `mlx-community/whisper-large-v3-mlx` on only the sample range.
- Targeted 12–25 second re-ASR for high-risk names, titles, numbers, and malformed phrases.
- Prompt-conditioned recognition is supporting evidence, not proof. Compare model outputs and verify proper nouns from official sources.
- When the comparison restores source wording that Main smoothed away, prefer the actual phrase and redesign only the cue boundary. Typical high-impact distinctions include `모셨습니다/오셨습니다`, `선언적인/선언하는`, discourse markers, hedge wording, and repeated scope words.
- End a nominal 0–3 minute sample at the nearest completed thought if a new question begins just before 3:00; state the actual end time when presenting it.

For 40–60+ minute no-caption Korean dialogue videos with dense technical terms, prefer 5-minute chunked MLX from the start when prior long-file collapse risk is high. Use `condition_on_previous_text=False`, verify that the final real phrase reaches the audio tail, and use 12–25 second targeted clip re-ASR with a narrow initial prompt for ambiguous high-risk phrases. A successful process exit is not proof that the latter half transcribed correctly. **Fail closed on MLX output:** some MLX Whisper CLI failures (missing input, model/Hugging Face authorization failure) can still return exit code 0. After every chunk run, require the expected JSON to exist, be non-empty and parseable, contain segments/words, and cover the expected chunk tail; after a batch, assert the exact expected chunk count before merging. Never mark ASR complete from the process exit code alone. See `references/2026-07-10-long-no-caption-ai-chip-review-workflow.md`.

If one chunk contains a local repeated-token/hallucination hole, repair the **narrow interval** with a second ASR model, then replace both overlapping segments and word timestamps in the merged JSON and regenerate every affected baseline/range derivative. Any draft or reviewer output produced from the pre-repair range is stale for that interval; rebuild the interval from the repaired source and rerun source/omission review on the current candidate hash. Do not merely patch the visible repeated token while leaving a 20–30 second timing hole. See `references/2026-07-20-long-interview-local-asr-repair.md`.

**Correction safety:** avoid broad substring replacements. Use exact phrase replacements with expected occurrence counts, scan for newly introduced corruptions after every pass, and keep refinement scripts idempotent so rerunning an older rule cannot undo a clip-verified correction.

**Reviewer adjudication safety:** subagent corrections are hypotheses, not authority. When a reviewer’s familiar term conflicts with targeted clip ASR, direct source evidence, or sentence syntax, Main must adjudicate and keep the source-backed reading. In particular, distinguish ordinary vocabulary from similar product names (`트레이닝` vs `Trainium`), verify contract direction hidden by Korean particles, and do not treat matching punctuation counts as proof of semantic correctness. See `references/2026-07-10-long-no-caption-ai-chip-review-workflow.md`.
