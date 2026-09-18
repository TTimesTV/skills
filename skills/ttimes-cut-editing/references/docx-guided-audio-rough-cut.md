# DOCX-guided audio rough-cut workflow

Use this when the user supplies an original MP3/WAV and a transcript DOCX whose Word deletion markup is intended as an audio cut list. The output is a rough-cut audio file with the marked speech removed. This is a downstream handoff from transcript editing; it is not the same as generating a tracked-changes DOCX.

## Mode gate and delivery contract

Choose and state the contract before transcription or rendering.

### Mechanical markup execution

Use only when the user explicitly wants the DOCX instructions applied literally.

- Source audio and DOCX are read-only and hash-pinned.
- Cut only speech marked for deletion; do not invent editorial cuts or a target runtime.
- Parse relocation/insertion instructions separately: removing the source occurrence without reinserting it at the declared destination is not a valid move.

### Editor-equivalent content rough cut

Use when the user asks for the result editors would actually make, supplies completed examples, cites a known human-edited runtime, or evaluates the artifact against an editor’s final cut.

- Explicit strikes/deletions are evidence, not the complete editorial plan.
- Build a content-function map and compare repetitions, question/answer dependencies, drift, post-roll, and relocation instructions across the complete transcript.
- Require direct ground truth when available: the editor audio, EDL/XML, accepted transcript, or a verified before/after pair. A folder named `완료` or `수정 후` is not ground truth until media duration and document contents prove that it is the edited output.
- Treat a known human runtime as a discrepancy gate, not a quota. If the generated runtime differs materially, stop delivery and run `runtime-discrepancy-attribution.md` before claiming success.

### Shared delivery rules

- Default final deliverable is the rough-cut audio only. Keep manifests and audits internal unless requested.
- Fail closed on ambiguous or low-confidence alignments.
- Technical checks such as clean joins, zero marked-phrase residue, and exact duration arithmetic prove alignment/render correctness only; they do **not** prove that the editorial scope matches a human editor.
- For a new DOCX format, complete one real one-off job before building a reusable app. Promote the proven rules to an app only after markup, relocation, editorial scope, and alignment semantics have been verified on actual inputs.

## 1. Inspect inputs before transcription

1. List all visible files and distinguish the active matching audio/DOCX pair from folders containing prior examples or completed outputs.
2. Record SHA-256 and size for both active inputs.
3. Run `ffprobe` for codec, duration, sample rate, channels, and bitrate.
4. Compare the audio duration with any duration printed in the transcript. Treat close agreement as provenance support, not as alignment proof.
5. Verify DOCX ZIP integrity and parse `word/document.xml` directly.

## 2. Interpret Word deletion semantics correctly

Deletion candidates may be represented as:

- tracked deletion: `w:del > w:r > w:delText`
- tracked move source: `w:moveFrom`, only when the document’s convention means “remove this speech”
- active strike-through: `w:rPr/w:strike`
- active double strike-through: `w:rPr/w:dstrike`

Do not infer deletion from red text, highlight, comments, insertion revisions, or ordinary formatting. **Do not ignore them either.** Classify non-deletion markup into a separate instruction ledger. In this workflow, red text commonly denotes an insertion or relocation destination, while red+strike text may denote the move source. A relocation is duration-neutral: remove the source clip, reinsert the same clip at the destination, and verify both order and conservation of retained duration. Never count move-source removal as a net content cut.

### Boolean property handling

For `w:strike` and `w:dstrike`, absence of `w:val` means enabled. Values such as `0`, `false`, `off`, and `no` mean disabled. Do not count the element by presence alone.

### Run count is not cut count

Word often splits one visibly continuous strike-through sentence into dozens or hundreds of runs by word, space, punctuation, font, or proofing boundaries. Therefore:

- never report `number of struck runs` as `number of audio cuts`
- concatenate adjacent marked runs into semantic cut groups
- bridge an unmarked gap only when it consists solely of insignificant whitespace
- preserve separate groups when retained lexical text lies between them

For each group record:

- paragraph/block index
- speaker and display timestamp
- marked text
- retained left and right context
- whether the cut begins or ends the speech block
- underlying markup types

Exclude non-audio metadata such as document titles, recording dates, participant lists, and duration lines. If the speaker/timestamp header itself is marked together with the first sentence, remove the header from the text-to-audio query but preserve a `starts_block=true` flag.

## 3. Use transcript timestamps before full ASR search

If the DOCX already contains speaker-block timestamps, use them to constrain alignment windows. Do not ignore a reliable transcript clock and search the entire audio for every repeated phrase.

Recommended sequence:

1. Parse each block timestamp.
2. Estimate its end from the next block timestamp.
3. Add a small tolerance window for transcript drift.
4. Run word-level ASR once for the complete source audio.
5. Search each deletion only inside its block/tolerance window.
6. Use global monotonic order to prevent later cuts from mapping backward.

For Apple Silicon Korean material, prefer MLX Whisper with a high-accuracy model and `word_timestamps=True`. Preserve raw and normalized words with start/end timestamps.

## 4. Align with retained context, not deleted text alone

Normalize Korean spacing, punctuation, case, and obvious ASR token boundaries, but keep the source strings unchanged for audit.

Match:

`left retained context + deleted text + right retained context`

rather than the deleted phrase alone. This resolves repeated fillers and common phrases. Use a monotonic dynamic-programming or sequence-alignment pass across the full transcript, then refine locally within each block’s time window.

### Retained-context anchor-gap is the boundary authority

A high-scoring fuzzy match can still choose an earlier occurrence or swallow the first retained word—especially with short fillers and pairs such as `이제/이거를`. Treat deleted-text matching as supporting evidence only.

1. Align the suffix of the retained left context near the candidate.
2. Align the prefix of the retained right context after it.
3. The audio words strictly between those two retained anchors are the deletion.
4. For block-start cuts, use the DOCX timestamp plus the right retained anchor.
5. For block-end cuts, use the left retained anchor plus the deletion match or next block boundary.
6. Resolve repeated exact phrases by timestamp proximity and monotonic order within the paragraph.

### A DOCX deletion can be an audio no-op

Struck text may be a transcript correction or duplicate that was never spoken. Example:

```text
DOCX: 58년에 [뱅가드] 미국의 뱅가드 인공위성에…
Audio: 58년에 미국의 밴가드 인공위성에…
```

If aligned retained anchors are adjacent with no spoken words between them, classify the item as `no_audio_noop`. Never delete the nearest similar retained occurrence merely to satisfy the DOCX string. Every DOCX group must resolve exactly once as `applied`, `no_audio_noop`, or unresolved manual review.

For uncertain openings or very low-level speech, re-transcribe a short focused clip, inspect short-window amplitude, and optionally amplify a diagnostic copy. Prompt-induced ASR text is not proof that speech exists.

Confidence policy should be explicit. Example:

- high confidence: automatic cut candidate
- medium confidence: inspect waveform/audio preview before applying
- low confidence: do not cut automatically; request a manual time decision

Never use exact-text failure as permission to guess. Korean spacing differences, transcription corrections, and duplicated words are expected.

## 5. Choose audio boundaries conservatively

- Start from the first and last aligned spoken-word timestamps.
- Prefer the midpoint between adjacent retained/deleted words or a nearby low-energy point.
- Do not apply a fixed large padding that removes retained syllables.
- Handle laughter, breaths, and fillers only when they are clearly subordinate to the deleted passage; text silence does not imply audio silence.
- Merge overlapping or near-touching cut ranges before rendering.
- Use short fades or a very short equal-power crossfade to prevent clicks, without overlapping intelligible retained syllables.

## 6. Render from the complement

Build a declarative audio cut manifest first. Compute retained intervals as the complement of the union of all confirmed cuts. Render with FFmpeg `atrim`/`asetpts` and concat or short crossfades. Never destructively edit the source.

A manifest entry should include:

- cut ID
- DOCX block/group identity
- deleted text and retained contexts
- audio start/end
- alignment confidence and evidence
- boundary adjustment
- status: `applied`, `no_audio_noop`, or `manual_review`

Before rendering, fail closed unless:

- source MP3 and DOCX hashes match the pinned values
- every cut ID is globally unique and the DOCX cut count is exact
- no item remains `manual_review`
- every audio range satisfies `0 <= start < end <= source_duration`
- overlaps, reversals, and touching-range merges are explicitly accounted for
- every `no_audio_noop` has retained-anchor/audio evidence

Calculate expected duration before rendering:

```text
expected_before_crossfades = source_duration - union(cut_intervals)
expected_final = expected_before_crossfades - crossfade_duration × join_count
```

## 7. Verify the final artifact

Before delivery:

- source audio and DOCX hashes unchanged
- every DOCX cut group appears exactly once in the manifest
- no low-confidence cut was applied automatically
- cut ranges are ordered, non-overlapping after union, and within duration
- output opens with `ffprobe` and fully decodes through FFmpeg with exit 0
- output duration equals source minus unioned cuts, adjusted for crossfades
- re-transcription does not contain the marked passage except where identical words legitimately occur elsewhere
- compute every output join time from the cut/keep ledger, extract several seconds before and after each join, and re-transcribe those join clips
- verify retained left/right context remains in order around every join; review low-context-similarity joins and every `no_audio_noop` independently

Join-local verification is stronger than globally searching a full-output transcript because the same phrase may legitimately occur elsewhere. However, it remains a **mechanical alignment check**. When an editor-equivalent result is required, also compare against the actual editor artifact or EDL: total runtime, retained-section order, moved passages, and join-by-join content. If the actual editor artifact is unavailable and a material runtime gap remains, label the cause unresolved and request that artifact instead of declaring `정상 음성 오삭제 0` as proof of editorial correctness.

## 8. App promotion path

After one or more real pairs pass audit, a local app can expose:

- audio and DOCX upload
- extracted cut-group preview
- alignment confidence table
- before/after audio previews around each join
- manual timestamp correction for low-confidence groups
- rough-cut render and download

Do not hard-code one document’s paragraph layout, speakers, filenames, cut count, or duration into the app.

## Common pitfalls

- Starting work without distinguishing literal markup execution from editor-equivalent content editing
- Treating zero deletion residue and clean joins as proof that the human editor’s broader cut scope was reproduced
- Delivering despite a material gap from a known editor runtime without first attributing the discrepancy
- Assuming a `완료` folder, `수정 후` filename, or same-stem MP3 is an edited reference without probing its duration and contents
- Deleting a red/struck move source but failing to reinsert the retained clip at the red destination
- Treating every struck Word run as an independent cut
- Counting title/date/participant-list formatting as speech cuts
- Assuming `python-docx Paragraph.text` exposes tracked deletions
- Ignoring embedded transcript timestamps and relying only on global ASR search
- Matching a repeated filler without left/right retained context
- Deleting marked text from the DOCX instead of deleting the corresponding audio
- Starting with a reusable app before observing the actual Word markup
- Reporting success from a duration change without listening to every join
