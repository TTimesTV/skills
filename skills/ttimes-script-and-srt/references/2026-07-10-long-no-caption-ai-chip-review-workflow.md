# Long no-caption AI-chip video: review-intensive SRT workflow

Use for 40–60+ minute Korean YouTube dialogue/keynote videos with no native captions and dense company/product/number terminology.

## Durable workflow

1. **Prefer chunked MLX from the start when prior long-file collapse risk is high.**
   - 5-minute mono 16 kHz chunks.
   - `word_timestamps=True`.
   - `condition_on_previous_text=False`.
   - Merge word/segment timestamps by chunk offset.
   - Verify the last real spoken phrase and final ASR word reach the audio tail; a successful process exit alone is not ASR integrity.

2. **Create a video-specific glossary before aggressive correction.**
   - Extract terms from transcript and verify names/products/numbers against current primary or reputable sources when needed.
   - For an AI-chip episode, examples included TPU, Trainium, Inferentia, MTIA, Maia, Cerebras, Tenstorrent, SambaNova, Groq, Graphcore, Rebellions, FuriosaAI, RNGD, CUDA, sovereign AI.

3. **Use guarded replacements only.**
   - Do not globally replace a short token that can occur inside a correct word. Example: replacing every `출원` with `추론` can corrupt `매출원` into `매추론`.
   - Prefer exact phrase replacements with `count == expected_count`; fail if zero or ambiguous.
   - Make refinement scripts idempotent. A stale rule such as `꼬신다 → 합친다` can silently undo a later clip-verified correction when the script is rerun.
   - After each pass, scan both known-bad variants and newly introduced outputs.

4. **Targeted clip re-ASR for ambiguous high-risk phrases.**
   - Locate the timestamp in the close transcript.
   - Extract a 12–25 second clip with context before and after.
   - Re-run MLX with a narrow initial prompt containing nearby entities/terms.
   - Preserve the actual colloquial wording when the clip confirms it, even if a polished paraphrase sounds cleaner.
   - If the short ASR still cannot disambiguate a phrase, leave it for manual/subagent review rather than inventing meaning.

5. **Orphan repair by rebalancing, not blind merge.**
   - Detect cues ≤5–7 visible characters.
   - Preserve genuine reactions/greetings (`안녕하세요`, `그렇죠`, `감사합니다`).
   - For predicate tails such as `합니다`, `있는지`, `건가요?`, combine with the previous cue, then split the combined phrase into two balanced 8–27 character cues.
   - This can reduce dozens of machine-wrap orphans without creating 27+ character cues.

6. **Review long holds separately from text length.**
   - After fuzzy word alignment, list cues over 5 seconds.
   - Prefer semantic resegmentation where possible.
   - Only cap a small excess caused by silence/tail padding after checking that spoken words are not cut.

7. **Question validation must count both cues and punctuation characters.**
   - `sum('?' in line for line in lines)` counts cues containing a question, not total question marks.
   - Compare `sum(line.count('?') for line in lines)` to the source when two questions may share one cue.

## Review gate

Before delivery:

- Run three subagent reviews: terms/numbers, segmentation/readability, omission/distortion.
- Do not mark review integrated until summaries arrive.
- Main applies only high-confidence findings and reruns alignment from the final body.
- Check first, middle, late samples plus all term-dense and low-match cues.
- Validate body equality, sequential indices, overlap 0, nonpositive 0, 27-char max, dead final periods 0, and long-hold list.
- If the user asks for extra review, do not send an apparently final artifact while subagent review is pending; label any necessary early file as a Main-validated preliminary.

## Reviewer-adjudication pitfalls

Subagent output is advisory, not a source of truth. Main must adjudicate conflicts against the audio, direct sources, and syntax before patching.

- **Do not normalize to the most familiar brand by reflex.** In one AI-chip episode, a reviewer proposed `SemiAnalysis`, but targeted clip ASR repeatedly produced `실리콘 애널리틱스` and a direct search found the matching `Silicon Analysts` source/statistics. Keep the source-backed name rather than the reviewer’s familiar guess.
- **Separate generic vocabulary from product names.** `이 트레이닝이 쓰이는 건 아니고` referred to model training in context; changing it to `트레이니엄` would create a false proper noun. Require syntax and nearby referents, not phonetic similarity alone.
- **Contract direction matters.** Genitive ASR such as `엔비디아의 기술 라이선스를 판매` may reverse who sold technology to whom. Verify the actual deal, then minimally repair to the correct direction (`엔비디아에 … 판매`) rather than preserving a factually inverted particle.
- **Punctuation counts are not semantic validation.** Matching 45 question marks between transcript and draft does not prove all are real questions. Repair artifacts such as `상장도 성공적으로 했습니다 그런데?` into a completed statement plus the actual following question; separately count question-containing cues and total `?` characters.
- **When targeted re-ASR remains phonetically ambiguous, use context conservatively.** Prefer a minimal source-backed repair (`적지는데` → `적자였는데`, R&D/양산 context `추진을 받을` → `지출이 불어날`) and avoid polished invention. If no unique reading is defensible, preserve/flag rather than guess.
- After integrating reviewer findings, do not rerun a stale earlier refinement script unless it is idempotent and its replacement direction has been audited; an old script can silently undo clip-verified wording.
