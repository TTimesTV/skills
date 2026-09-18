# No-sample long-form cut-video SRT from an approved cut transcript

Use this pattern when the user provides a 30–50 minute no-caption YouTube cut video and an approved tracked-cut transcript already exists locally.

## User contract

- Current default: `/plan → no sample → full-body work → whole-file review → final *_srt.txt`.
- Do not stop at a 0–3 minute approval gate unless the user explicitly asks for a sample or severe ASR corruption makes style recovery unavoidable.
- Deliver only the final `*_srt.txt`; keep ASR JSON, ledgers, reviewer reports, and intermediate bodies internal.

## Source hierarchy

1. The exact current cut video's audio is authoritative for what was actually spoken and retained.
2. The accepted tracked-cut transcript is the preferred textual substrate for wording, names, technical terms, and edit decisions.
3. MLX ASR is a timing and audio-verification substrate; it may restore speech omitted by the document but must not restore material deleted from the actual cut video.
4. Older full interview/restored transcripts are context only. Never reinsert a deleted source block merely because it is present in the uncut transcript.

## Workflow

1. Download the exact URL and verify title, duration, size, and bitrate with `ffprobe`.
2. For a 35–45 minute no-caption Korean technical interview, run 5-minute MLX chunks from the start with Korean, word timestamps, and `condition_on_previous_text=False`.
3. Verify every 5-minute window has plausible word density, no repeated-segment collapse, and the final real phrase reaches the audio tail.
4. Extract the accepted transcript's speech body by removing only speaker/time headers and blank lines. Preserve its accepted edit order.
5. Build a terminology ledger before segmentation. For ambiguous names/numbers/states, use 12–30 second targeted clips with a second Whisper model; prompt-conditioned output is supporting evidence, not proof.
6. Split the accepted transcript into bounded preliminary drafting ranges only if useful. Range workers may create token-close cue-body drafts, but Main owns the whole-file rhythm and final wording.
7. Audit every range seam. Blank stretches caused by tracked deletions can hide one or two retained paragraphs just outside a worker's line range. Compare source line intervals explicitly and insert any retained seam text before concatenation.
8. Concatenate to one working body and apply the user's rules: source-close minimal correction, sentence/thought boundary first, small-sentence readability, predicate attachment, protected Korean phrase adjacency, 25-char target/27-char practical max, living punctuation, no final periods.
9. Compare normalized body text against both the accepted transcript and MLX words. A high ratio is not sufficient, but large source-side delete/replace blocks expose omissions and over-polishing.
10. Create a content-addressed immutable reviewer snapshot with path, line count, and SHA-256. Review source fidelity, every cue/boundary plus intra-cue grammar, terminology/numbers, and omission/distortion.
11. If Main edits materially after snapshot creation, treat that review as stale: apply findings only by exact quoted current string, then run a fresh review on the intended delivery hash.
12. Align the current body to MLX word timestamps and calculate ASR word-midpoint coverage plus spoken gaps. Feed meaningful uncovered speech back into the body, then regenerate alignment from scratch.
13. Freeze only after exact body equality, sequential cues, no overlaps/nonpositive durations, all 28+ lines resolved, and every material spoken gap adjudicated.

## Coverage-gate lesson

An accepted cut transcript can still omit short audible phrases. Preliminary alignment may reveal meaningful uncovered speech such as:

- a missing predicate tail (`밸류` vs `밸류입니다`)
- a short reply (`몰라요`)
- a clipped question (`요 다음…` vs audio-confirmed `이 다음은 뭡니까?`)
- a duplicated but meaningful state assertion (`상태를 갖자` / `상태를 보유하자`)

Do not fill gaps mechanically. Inspect the local ASR/audio:

- Restore a phrase when it adds actual spoken meaning or completes grammar.
- Extend timing rather than add a cue for harmless repetition already represented nearby.
- It is acceptable to omit a meaningless filler or duplicated discourse token if meaning and rhythm are preserved.
- Never bridge by midpoint if that exposes the next idea early or leaves the prior cue lingering.

## Technical-term arbitration

- Direct audio can preserve an awkward source phrase; do not silently replace it with a cleaner claim.
- The accepted transcript can supply a verified correction where ASR mangles names or English terms.
- If the accepted transcript and two ASR passes disagree on a number, preserve the accepted editorial number only when the audio does not disprove it, and do not invent a unit such as `%`.
- If a tracked insertion translates an English state name, keep the English term when it disambiguates the intended state, but record unresolved semantic risk in the internal ledger.

## Efficiency and failure prevention

- Batch independent reads, audits, and reviewer tasks.
- Reserve tool-call budget for fresh-hash review, final alignment, and final verification; repeated progress-only checks are lower priority.
- Do not call a preliminary body final merely because cue count, max length, and overlap checks pass.
- If execution limits interrupt after drafting but before fresh review and final alignment, report the exact unfinished gates and resume from the saved working body; never deliver the preliminary SRT as final.
