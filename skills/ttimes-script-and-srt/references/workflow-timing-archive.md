### 7. SRT generation

If the user asks for SRT, use an explicit **body-first review gate**. Do not review or rewrite prose inside timestamped SRT blocks when a timecode-free body TXT can be used. The editing order is:

```text
extract/build timecode-free cue-body TXT
→ review and normalize Korean sentences/segmentation using only that TXT
→ freeze the approved body TXT as the sole text authority
→ align the frozen lines to ASR word timestamps
→ validate SRT bodies equal the frozen TXT exactly
```

Reason: indices and timestamps distract reviewers from bad Korean, orphan cues, predicate separation, and sentence-boundary packing. The body TXT should be made fully readable before timing work begins. If text changes after alignment, return to the body TXT, fix it there, and regenerate timing; do not patch the SRT body in place.

**Baseline and drift guard:** preserve an immutable transcript-close body before editing, then record line/character/question counts plus number/unit and term inventories. “Normalize bad Korean” locally; do not silently turn it into summary or polished-prose compression. After every major Main pass, compare the current candidate to baseline. Character reduction around 5%+ or cue-count reduction around 8%+ is a mandatory omission/over-polish review trigger, not something to dismiss as filler removal. Precise source details must survive (`69% 이상` must not become `약 70%`). Use exact phrase replacements with expected occurrence counts where practical.

Before freeze, run the reusable `scripts/audit_caption_body.py` against the timecode-free TXT and manually adjudicate every short-cue hit. See `references/body-first-normalization-and-stale-review-guard.md` for the full baseline manifest, reviewer-freshness, drift, body-freeze, and alignment gates.

Then:

1. Treat the final script non-empty lines as cue bodies.
2. Align those lines to MLX word timestamps / caption timing substrate.
3. Generate an initial SRT.
4. Run a **cue timing refinement pass** before delivery for this user's 95점 target:
   - Build a normalized script character stream from final script lines.
   - Build a normalized ASR character stream from MLX word timestamps with char→word index mapping.
   - Map each script line's character span to an ASR word-index range using sequence/fuzzy matching.
   - Recalculate cue `start` from the first matched word and cue `end` from the last matched word.
   - Apply small Korean 말자막 padding: start ≈ -0.05~0.08s, end ≈ +0.12~0.22s.
   - Resolve overlaps by midpoint/gap rules.
   - Enforce readable duration: short cues ≈ >=0.7~0.9s when possible; general max ≈ 3.5~4.2s.
   - Inspect low-match cues separately, especially foreign-language, noisy field-interview, or heavily corrected proper-noun segments.
   - Treat this first timing pass as a **body-feedback gate**, not merely a timestamp check. Inspect every cue under about 0.7s: if it exposes a broken predicate, dependent noun, adnominal+noun chunk, or orphan transition, fix the timecode-free body and regenerate all timing. Preserve genuinely short reactions/emphasis rather than merging them mechanically.
5. Validate:
   - `script non-empty lines == SRT cue count`
   - `SRT bodies == script lines`
   - sequential indices
   - monotonic non-overlapping timecodes
   - no non-positive durations
   - scan very short and very long cues
   - **Distinguish intentional silence from accidental subtitle holes.** A gap is not an error merely because no cue is displayed: real silence, breath, edit pauses, and deliberate visual rests may remain. A gap is an error when ASR/audio confirms actual speech but no subtitle covers it. For every visible gap (default audit threshold: about 0.25 s), check ASR words/audio inside the interval. If the speech merely repeats or continues an adjacent cue, extend that cue's timing; if it contains new meaning, insert a source-close cue. Do not fabricate filler captions solely to force 100% ASR-word coverage. Final gate: zero accidental speech-containing gaps above the visible-gap threshold; intentional silent gaps are allowed. When reporting repairs, separate newly inserted cue text from timing-only coverage fixes.
   - **Mandatory ASR speech-coverage gate:** calculate what percentage of ASR word midpoints falls inside cue intervals, then enumerate every adjacent-cue gap that contains ASR words. Report threshold counts (`>=0.8s`, `>=1s`, `>=2s`, `>=3s`) and the longest spoken gap. `overlaps=0` and `nonpositive=0` do not certify that speech is covered.
   - **Choose the aligner by coverage, not match ratio alone.** When practical, compare at least two diagnostic alignments. A dense character-window aligner can report a higher character ratio and clean overlaps while covering only part of the spoken words because it selects a core span and caps cue duration. Prefer the candidate that preserves exact bodies and materially improves ASR word-midpoint coverage/spoken-gap counts, then manually inspect repeated phrases and low-match technical terms. In one long technical interview, character ratio `0.976` still covered only `69.54%` of word midpoints with 683 spoken gaps, while a lower token ratio `0.936` covered `99.66%` with 7 gaps. Sequence ratio is a text-similarity diagnostic, not a timing acceptance metric.
   - **Frozen approved-body order outranks alignment convenience.** If an approved cue sequence moves a repeated phrase relative to literal speech order, do not rewrite the frozen sample merely to get 100% coverage. Identify the display-order mismatch, preserve the exact body/hash, and use a semantically matching neighbor's true spoken boundary only after checking no early-next exposure or previous-cue linger. Add a cue only for genuinely missing new meaning.
   - Repair each spoken gap by classification: extend neighboring cue timing for repeated/filler speech; insert transcript-close cues only when meaningful source content is absent from both neighbors; preserve genuine silence. Re-run coverage until no material spoken gap remains unreviewed.
   - **Never bridge residual gaps by blindly splitting at the midpoint.** Midpoint filling can make the next cue appear before its words are spoken, leave the previous cue over the next utterance, or reverse the perceived order. For each repaired gap, audit three independent timing failures against ASR/audio: `early_next_exposure`, `previous_cue_lingers`, and `insert_order_or_late_start`. Connectors/repetitions must be assigned to the side they actually belong to; genuine short pauses may remain rather than forcing continuous coverage.
   - **Gap filling must preserve spoken order, not merely eliminate blank time.** Never use blind midpoint bridging across unmatched speech. For every repaired interval, verify that the next cue does not appear before its actual idea/word onset, the previous cue does not linger into the next idea, and inserted cues occur in source order. Avoid anticipatory subtitles that reveal an object or conclusion before the speaker says it. If filler/repetition does not justify a new cue, keep intentional visual silence or extend only the semantically matching neighbor to its true spoken boundary. Recheck timing starts moved earlier or ends moved later by about 2 seconds or more against ASR words/audio.
   - Inserted gap text must remain source-close; do not smooth an unfinished phrase into a stronger claim or add connective meaning not actually spoken. Use targeted clip re-ASR when gap ASR is ambiguous.
   - When repairing only holes, assert all original cue bodies remain an ordered subsequence, renumber, and report only changed intervals, separated into `새 cue 추가` and `기존 cue 타이밍 보완`.
   - See `references/asr-speech-coverage-gap-audit.md` for the failure pattern, audit method, repair classification, and acceptance checks.
6. Delivery preference for this user:
   - Before emitting `MEDIA:`, copy the exact final deliverable to `PROJECT_OUTPUT/` and verify source/destination SHA-256 match.
   - **Filename is an editorial deliverable, not an internal implementation detail.** If the user specifies a basename, preserve it exactly—including Korean, spaces, episode wording, and date prefix. Do not expose internal names such as `gang_jeongsu_ep1_spoken_captions_SRT.txt` or silently substitute a transliterated ASCII slug. Recent approved pattern: `260723_강정수 1편 컷편.txt`; use the analogous `YYMMDD_이름 N편 컷편.txt` when that is the user's requested series convention.
   - If no basename was specified, use the project's established `YYMMDD_title` convention and prefer a concise human-facing title over pipeline labels such as `spoken_captions`, `final_aligned`, or `SRT` unless those words are part of the user's convention.
   - Keep SRT contents in a `.txt` attachment when that is the established mobile-delivery format. Do not tell the user to rename it unless they ask about importing it.
   - If the exact requested basename fails to deliver, first retry the same hash-verified file from `PROJECT_OUTPUT/`. Use a short ASCII transport fallback only after an actual delivery failure, and label it as a transport fallback rather than treating it as the canonical filename. Never regenerate subtitle content merely to troubleshoot transport.
   - Do **not** attach validation JSON by default.
   - Use ZIP only as a last-resort fallback when the requested `.txt` attachment also fails, or when the user explicitly asks for a bundle; ZIP is annoying on mobile for this user. If zipped, include only the requested deliverable(s), not JSON/debug files.

### 8. Team delivery

Deliver the requested final transcript and SRT in the current project's output folder. Include source URL, speakers, scope, and verification status when useful. Reopen the delivered file and verify its body matches the final approved candidate. Personal note-vault archiving and automatic external uploads are outside this shared skill.
