# YouTube `/plan` routing and dual-ASR sample gate

Use this pattern when a user provides a YouTube interview/cut URL and invokes `/plan`, then identifies the job as Korean TTimes 말자막.

## Route before planning

- A bare video URL plus `/plan` does **not** imply screen composition.
- If the user says `말자막`, `SRT`, `자막 작업`, or the immediate context is cue segmentation/transcript correction, route to `ttimes-script-and-srt`.
- If the deliverable is still genuinely unclear, ask one brief question: `말자막 SRT, 화면구성, 요약 중 어떤 작업인가요?`
- Do not create a detailed screen-composition plan and ask the user to correct the task class afterward.

## Plan and execution boundary

For 말자막, the user's current default is **no sample gate**:

1. Plan exact-source acquisition.
2. Plan MLX word-timestamp ASR.
3. Plan full-body transcript-close correction and segmentation.
4. Add fresh reviews: source fidelity, cue boundary/internal grammar, terminology/numbers, and omission/distortion.
5. Main integrates the full body, aligns it, and completes all validation gates.
6. On `ㄱㄱ`, execute the full workflow through final delivery. Use a 0–3 minute sample and hash freeze only if the user explicitly requests it or ASR corruption forces a style-recovery sample.

## Exact-source acquisition retry ladder

Before concluding that a playable YouTube source has no downloadable formats:

1. Compare `yt-dlp --version` and `python3 -m yt_dlp --version`.
2. Run format discovery with the newer invocation, commonly:
   ```bash
   python3 -m yt_dlp -F 'URL' --no-warnings
   ```
3. If public access remains unavailable, use a media file supplied for this task.
4. Download a named audio format and verify title, duration, size, and bitrate with `ffprobe`.
5. Ask for the owner-provided MP4/MP3 if the current module cannot fetch the public source. Do not load personal browser credentials.

This is a retry pattern, not a durable claim that either CLI entry point is always better.

## Dual-ASR sample audit

For a technical Korean interview sample:

- Primary timing substrate: `mlx-community/whisper-large-v3-turbo` with Korean, word timestamps, and `condition_on_previous_text=False`.
- Comparison pass: `mlx-community/whisper-large-v3-mlx` on only the sample range.
- Targeted pass: cut 12–25 second clips around high-risk names, numbers, book titles, and malformed grammar.
- A prompt-conditioned ASR output is supporting evidence, not proof; confirm proper nouns with official sources and compare unprompted/contextual outputs.
- Prefer direct source wording over smoother editorial rewrites. A comparison pass is especially valuable for distinctions such as `모셨습니다/오셨습니다`, `선언적인/선언하는`, missing discourse markers, and restored hedge/filler wording that changes tone.

## Reviewer role boundary and arbitration

The three reviewers do not have equal authority over body wording:

- **Source-fidelity reviewer:** may propose token changes only with audio/ASR evidence, a quoted current string, and a time range.
- **Segmentation reviewer:** is token-preserving by default. It may move cue boundaries and living punctuation, but must not silently add an implied verb, replace a noun, remove repetition, or strengthen a claim merely to make the sentence smoother.
- **Terminology reviewer:** may normalize verified names, titles, acronyms, numbers, and units; it must not rewrite surrounding syntax.

Reject segmentation suggestions that invent or substitute wording such as `도입하는`, `방식 자체`, `DX에서`, or `핵심 내용` when those words are absent from the source. Treat them as diagnostic comments, not paste-ready captions.

When fidelity and readability conflict, classify the issue before editing:

1. Clear ASR/proper-noun error → correct from direct/official evidence.
2. Mechanical particle collision or unmistakable delivered-caption grammar error → make the smallest local correction and record it.
3. Speaker's awkward lexical choice, repetition, hedge, or self-correction → preserve it unless the user explicitly approves normalization.
4. Boundary/readability problem → keep the token sequence and redesign cue boundaries first.

A clean paraphrase is not automatically a valid 말자막 correction. Main Hermes owns the arbitration and must explain any deliberate token change in the correction ledger.

## Fresh-review rule

Record candidate path, line count, and SHA-256 when dispatching reviewers. If Main materially revises the sample afterward, the old review is stale. Re-run all three reviews on the latest hash before presenting the sample. When an older review arrives late, treat line numbers as hints, exact-search its quoted current string, and apply only findings still present in the delivery candidate.

## Sample presentation

- Present body lines only, without timecodes.
- State sample end time when it ends before the nominal 3:00 mark to preserve a complete thought.
- Do not attach internal ASR JSON, ledgers, manifests, or draft files.
