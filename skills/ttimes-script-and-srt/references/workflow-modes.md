## Pipeline

### 0. Fast existing-ASR chunk mode

When the user asks for a named part/time range already present as an ASR chunk — e.g. `part1 00~25분 ASR을 Gem1 최소윤문 후 Gem2 말자막 분절로 변환하고 파일로 저장하라` — do **not** automatically run the full source acquisition / ASR / subagent / SRT timing workflow. Treat it as a lightweight chunk conversion task:

1. Read the local project brief if present, especially `gem1_gem2_brief.md`.
2. Read the requested ASR chunk from the existing workspace.
3. Apply Gem1 minimal correction while staying transcript-close: obvious ASR errors, particles, spacing, acronyms, proper nouns, numbers/units; no summary, invention, or broad rewrite.
4. Apply Gem2 spoken-caption segmentation: cue body only, one line per cue, no timestamps/indices/markdown, meaning-closed chunks, and the user's current visual max rule (usually ≤25 visible Korean chars unless the project brief says otherwise).
5. Save as a plain `.txt` caption-body file under the project's existing convention, and optionally save a short adjacent report with counts, corrected terms, and caveats.
6. Run a mechanical check for line count, blanks, max/average visible length, and uncorrected ASR-corrupted terms.

Pitfall: if a draft is too short on average, an automated merge pass can help, but it often over-merges speaker turns, questions, discourse markers, topic transitions, quotes, and joke punchlines. After any merge pass, inspect representative ranges and split back at boundaries like `그러면`, `그런데`, `그래서`, `다만`, `그리고`, `근데`, and question/answer turns. For cue-body-only Gem2 files, an average around 14~18 visible chars with max ≤25 is usually safer than chasing maximum packing.

See `references/2026-07-08-part-asr-gem1-gem2-chunk-workflow.md` for a concrete pattern and validation snippets. See `references/2026-07-08-gem1-gem2-part3-50-76-asr-to-captions.md` for a later 50~76분 chunk example with merge/split-back lessons, topic-specific AI-chip ASR traps, and uncertain-phrase reporting. See `references/2026-07-09-60-85-asr-cue-body-validation.md` for a 60~85분 cue-body-only run with a compact validation snippet, final metrics, and examples of merging tiny orphan fragments without over-polishing. See `references/2026-07-09-approved-sample-style-30-60-asr-cue-body.md` for the approved-sample-style 30~60분 existing-ASR cue-body pattern: combine multiple ASR chunks into one body-only file, validate max/average length plus isolated-fragment/adhesive checks, and respond with only the saved path and brief stats.

### 0a. Approved-cut transcript section → cue-body first draft

When the user asks for a named episode's `승인 컷 원고` and a bounded section such as `후반 구간` to become a TTimes `말자막 초벌 body`, use a lightweight accepted-transcript route rather than full ASR/alignment/subagent regeneration:

1. Read the exact requested transcript range plus minimal boundary context, and read a representative approved/final body or SRT from the same series for rhythm.
2. Keep only the requested range. Remove speaker names, timestamps, and blank structural lines, but preserve the order and **every spoken token** inside the range—including fillers, repetitions, acknowledgements, discourse endings, and self-repairs—unless the user explicitly authorizes cleanup.
3. Apply transcript-close correction and artistic cue segmentation; do not summarize, broadly rewrite, remove repeated words, convert colloquial constructions into cleaner prose, or pull material from outside the requested range. In this strict approved-cut mode, the general optional filler-removal rule does not apply.
4. Save one plain TXT with one non-empty cue body per line.
5. Revalidate after every spacing or terminology patch because even `한번` → `한 번` can push a cue over the visual maximum.
6. Run a normalized source→body sequence diff before finalizing. Join the approved source utterances after removing speaker/time metadata, join the body lines, normalize only harmless whitespace/punctuation plus an explicit correction ledger, and manually adjudicate every deletion, insertion, or replacement. Final residual differences must be explainable orthography/spacing corrections—not omitted speech. Typical forbidden losses include `뭐`, `어`, repeated `네`, `보면은`, `그러면은`, and a self-repair such as `위로 위로금`.
7. Before reporting completion, assert no blanks, no speaker/timestamp hits, no sentence-final periods, and no lines above the current project maximum; manually inspect every over-25 line and adjudicate protected-phrase audit hits.
8. Deliver only the saved path and terse line/max-length metrics unless the user requests a preview or report.

For concrete workflows, see `references/2026-07-21-approved-cut-back-half-body.md` for the bilingual-term and late-range case, `references/approved-cut-transcript-middle-range-body.md` for the source-fidelity diff and three-line repartition pattern, and `references/2026-07-21-approved-cut-front-range-token-preservation.md` for strict all-token preservation and normalized diff adjudication.

### 0a-1. Bounded merged raw-ASR range → body 초벌

When the user names a short range such as `00:00~07:00` in an existing merged raw ASR and asks for an `원문 밀착 티타임즈 말자막 body 초벌`, use a lightweight range-drafting route rather than full media acquisition, ASR regeneration, SRT alignment, or final-candidate peer review:

1. Read the exact ASR range plus minimal boundary context, then read the project's `glossary.txt` and `correction_ledger.tsv` before writing.
2. Treat confirmed ledger forms as authoritative. Keep explicitly unresolved terms conservative; do not guess a polished replacement.
3. Produce one non-empty cue body per line with no timestamps, speakers, indices, markdown, or blank separators.
4. Preserve claim order, modality, meaningful repetition, reactions, and colloquial tone. Correct only confirmed terms, obvious recognition errors, spacing, particles, and clearly broken syntax. This is a first draft, not a summary or rewrite.
5. Segment as small readable sentences and protect subject–predicate, object/adverbial–predicate, adnominal–noun, dependent-noun, auxiliary-verb, number–unit, and fixed technical-name chunks.
6. Target ≤25 visible characters and enforce a practical maximum of 27, counting spaces and Latin characters. Remove sentence-final periods but retain useful question marks, commas, and quotation marks.
7. Run `audit_caption_body.py` and `audit_protected_phrase_splits.py`, then manually adjudicate every candidate. Do not paraphrase merely to make a regex warning disappear; redesign boundaries first. If a long proper noun forces a local syntax repair, make the smallest meaning-preserving change and never strengthen a hedge (`~라고 봐요`, `~일 수도 있습니다`) into a categorical claim.
8. Verify UTF-8, non-empty line count, max/average length, no blank lines, no timestamps/speaker labels, no sentence-final periods, no lines above 27, and SHA-256.

Detailed bounded-range checklist and a validated technical-interview example: `references/bounded-raw-asr-range-body-first-draft.md`.

For a longer bounded range such as 20 minutes with an existing transcript-close baseline, read `references/2026-07-23-bounded-20min-body-draft.md`. It adds exact end-boundary handling, confirmed-vs-likely ledger discipline, output-only file scope, the failure modes of both per-line and whole-stream automatic segmentation, multiword-term protection, manual all-boundary adjudication, and the terse path/metrics/hash handoff.

### 0b. Existing SRT readability audit mode

When the user asks to `검수하라`, `review`, `가독성/분절 오류를 봐라`, or otherwise audit an already-created Korean TTimes SRT draft, do **not** assume they want a rebuild or file modification. Treat it as a lightweight reviewer task unless they explicitly ask to apply fixes.

Recommended flow:

1. Parse the SRT mechanically: cue count, time range, selected sample windows, visible-length warnings, sentence-final periods, and obvious orphan cue bodies.
2. Manually inspect representative windows. Default if no range is specified: first 5 minutes, one middle 10-minute block, and one late 10–15-minute block. State the inspected scope; do not overclaim full 95-point review from a sampled audit.
3. Flag concrete cue ranges with rewrite candidates, grouped by time/window.
4. Focus findings on TTimes readability failures: stranded particles/objects/adverbs/connectors, speaker-turn/question-answer packing in one cue, predicate/meaning splits, sentence-final periods, and ASR/proper-noun/number/unit errors.
5. Keep the user-facing report concise and actionable. Include whether any file was modified; normally it should be `없음` unless the user asked for edits.

See `references/2026-07-09-existing-srt-readability-audit.md` for lint patterns and an output template.

### 0b-1. Immutable full-candidate final-audit mode

When the user asks for `전 구간 최종 통합 검수`, `fresh review`, or a final audit of a named immutable candidate, the sampled-audit default above does **not** apply. Freeze and verify the candidate hash, inspect every cue and every adjacent boundary, and independently audit source fidelity, segmentation/protected phrases, intra-cue grammar, and terminology/numbers against the approved transcript, ASR/audio, glossary, and correction ledger.

Do not edit the candidate unless the user separately asks for fixes. Report exact current strings rather than relying on line numbers, exclude unresolved audio ambiguities from confirmed findings, and verify that section counts sum to the stated finding total. Recheck the immutable candidate hash after report creation.

For a heavily corrected candidate, complete the independent all-cue/all-boundary read first, then optionally diff its immediate predecessor as a **regression locator only**. Re-read every changed hunk on the current hash and check the fidelity/segmentation trade-off in both directions: a restored quantifier or scope token (`대부분의`, `한`, `약`, negation, modality) can create a new protected-phrase split under the 27-character box, while a boundary repair can silently delete that token and broaden the claim. Never derive the verdict from an old report or predecessor diff.

Before delivery, exact-search every quoted current string, verify unique resolution or include disambiguating context, and label correction types honestly: `boundary-only` only for token-preserving moves; lexical changes required by the visual limit are `minimal lexical/boundary repair` with source evidence. Count independent bad boundaries separately even when one shared correction block repairs the whole span, and compare suspicious loanword transliterations with ASR/English even if the glossary has no entry. If the user assigns `분절 검수만` and only the immutable body is available, keep the verdict role-bounded: inspect all cues/boundaries, provide exact current multiline strings plus token-preserving ≤27 redistributions, validate preservation after whitespace normalization, reject fixes that merely create another protected split, and do not imply source/term/factual review. See `references/immutable-full-candidate-final-audit.md` for both the full four-axis contract and the segmentation-only immutable-audit report gate.

For a **post-merge regression audit** after dozens of prior findings were applied, never assume the old report's proposed redistribution is safe or authoritative. First inspect every current cue/boundary independently; then use predecessor→current diff only as a locator and re-read every changed window plus its outer seams. Test whether each fix repaired its named split by creating another one—for example `관형격 / 중심 명사`, `관형절 / 명사`, `대비 / 비교 대상`, `정도부사 / 서술어`, or `관형어 / 피수식어`. Confirm a regression only when a token-preserving within-limit redistribution is materially better; long constructions with no split-free ≤27 solution should not be overcounted. Run unique exact-match, normalized-token preservation, proposal-length, arithmetic, and opening/closing-hash checks. Detailed checklist and recurring bulk-fix regressions: `references/post-merge-segmentation-regression-audit.md`.

When the immutable candidate also contains a later **source-correction generation**, verify prior segmentation fixes in two forms: exact proposal matches where wording is unchanged, and structurally analogous current splits where one source-backed lexical token changed. Then independently audit the entire assigned range so residual pre-existing defects are not hidden by changed-window review. Report retained prior fixes separately from new current-hash findings. See `references/late-section-post-source-correction-segmentation-audit.md` for bounded-range arithmetic, source-edit regression families, and the structured report validation gate.

For a **bounded final segmentation regression audit** such as `전반 cue 1~983 + seam 983-984`, do not limit the fresh verdict to predecessor diff windows or protected-phrase regex hits. After the all-cue/all-boundary read, enumerate every adjacent pair whose merged visible length is within the current maximum and manually judge whether the existing split unnecessarily separates a subject/topic/adverbial/reason clause from its predicate or leaves a non-sentence fragment. Separately scan every cue for a question mark followed by more text to catch packed question→answer or echo→answer beats while excluding indirect quotations such as `"...?"라고`. Classify each hit with its previous/next cue: a reporting suffix is a non-finding, but a completed question followed by the start of its answer is blocking when a token-preserving ≤27 redistribution cleanly separates the beats. Recheck predecessor-fix and later source/term-edit windows with both outer seams, but count only current-hash defects. Verifying that every prior proposal still exists is necessary but does not certify zero new findings, and an assignment label such as `0건 수렴검수` is an acceptance target—not a verdict to force. If a bilingual term or long name has no clean token-preserving ≤27 alternative, document the tradeoff as a non-finding rather than proposing a new broken boundary. Scope arithmetic, candidate-generation passes, and reporting checks: `references/exhaustive-bounded-final-segmentation-regression-audit.md`. Concrete residual-question example and convergence gate: `references/2026-07-23-front-half-zero-convergence-question-answer-scan.md`.

### 0c. Speaker-diarized DOCX mode is a separate deliverable

If the user asks to replace Clova Note, preserve speaker names/timestamps, create a 컷편집 원고, or generate a cleaned work DOCX, do **not** force the source into subtitle-body lines. 로컬 `media-localization-workflows` 의존성이 없으므로 이 경로가 실행된 것처럼 주장하지 말고 `references/local-dependency-gates.md`의 synced-DOCX `external_dependency` gate를 반환한다:

- MLX Whisper ASR + separate speaker diarization
- source-close speaker/timestamp DOCX for pre-cut review
- Word Track Changes rough-cut handoff
- cut MP3 → separate 말자막 SRT and cleaned DOCX

The pre-cut DOCX must preserve repetitions, restarts, reactions, and rough fragments that may become cut points. The later SRT may be tightly segmented, but the DOCX should retain sentence and speaker-turn continuity. Share one terminology/correction ledger across both outputs; never reuse SRT line breaks as DOCX paragraph architecture.

When a cut manifest corrects a diarization boundary by moving a sentence between speaker blocks, implement and test that operation first as a deep-copying pure data transform, separate from DOCX/OOXML and CLI code. Validate exact integer IDs (`bool` excluded), unique source text, target duplication, mode/policy, declaration order, and input immutability; integration tests must read protected fixtures without writing them. See `references/pure-speaker-boundary-manifest-corrections.md` for the contract, TDD sequence, and SHA-based fixture-safety gate.
