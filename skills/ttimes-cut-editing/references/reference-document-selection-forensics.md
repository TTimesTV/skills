# Reference-document selection forensics

Use this when the question is not merely “were the marked cuts extracted correctly?” but “did the pipeline choose the correct edit document?” This is a provenance and causal-attribution audit; keep all source DOCX/audio files read-only.

## 1. Separate extraction correctness from reference correctness

A manifest can exactly reproduce every mark in one DOCX and still be wrong because that DOCX was not the authoritative cut plan. State these as separate propositions:

1. **Extraction fidelity:** the generated manifest matches the selected document.
2. **Reference authority:** the selected document represents the intended human edit.

Never use proof of (1) as proof of (2). A large runtime mismatch is a mandatory trigger to reopen reference selection.

## 2. Establish document genealogy from reconstructed transcript text

For every candidate DOCX:

- hash and size-pin it;
- parse `word/document.xml` directly;
- reconstruct the full transcript by including normal text plus `w:delText`/`w:moveFrom` text;
- separately reconstruct accepted text by excluding tracked deletions;
- preserve paragraph breaks, manual line breaks, speaker labels, and timestamps;
- compare the ordered speaker/timestamp paragraph sequence and normalized full transcript across candidates.

Strong same-recording evidence is:

- identical ordered speaker/timestamp paragraphs;
- exact full-transcript equality after restoring tracked deletions;
- exact normalized alphanumeric equality as a secondary check.

This distinguishes an original, a strike-marked review copy, and a tracked-edit cut document even when filenames or ZIP packaging differ. Core properties and modified timestamps are supporting evidence only; they do not override exact text genealogy.

## 3. Compare deletion plans as masks, not only counts

Once full transcript identity is established, project each document’s deletion semantics onto the same character sequence:

- strike/double-strike mask for flattened review copies;
- `w:del`/`w:moveFrom` mask for tracked-edit documents.

Report:

- marked text characters, breaks, and alphanumeric characters;
- contiguous speech groups and revision-node counts separately;
- intersection, A-only, B-only, and union character counts;
- percentage of each plan covered by the other.

Low mutual coverage proves the documents are **alternative edit decisions**, not additive supplements or a simple flattened copy. Do not union them unless an explicit instruction says they are cumulative.

## 4. Prove the operational selection path

Inspect the actual pipeline artifacts for direct evidence of which document was treated as authoritative:

- hard-coded DOCX paths in alignment/extraction scripts;
- source path and SHA-256 pinned in the final manifest;
- forensic audit scope;
- whether alternate matching DOCX files were inventoried before generation.

Phrase the conclusion carefully: code and manifests can prove the **operational cause** of selection. They usually cannot prove the developer’s private intent. Prefer “the pipeline selected A because its path was hard-coded and B was not compared” over speculation about psychology.

## 5. Quantify the causal runtime bridge

Align each competing plan independently to the same ASR word timeline. For each plan compute interval union and predicted output:

`predicted_output = source_duration - deletion_union - crossfade_total`

Then compare:

- delivered A output versus target;
- A deletion union versus B deletion union;
- delivered A output versus B-predicted output.

A particularly strong causal pattern is when:

`B_union - A_union ≈ delivered_A - target`

and B’s predicted output lands within the target’s stated rounding tolerance.

Keep pre-crossfade and post-crossfade arithmetic separate. Count crossfades from keep-segment joins, not deletion groups.

## 6. Use conservative confidence bounds

Do not hide low-confidence ASR alignments merely because the all-ranges union matches the claimed runtime exactly.

Report both:

- **nominal estimate:** all independently aligned ranges;
- **conservative estimate:** only high-confidence ranges, with disputed ranges excluded.

Calculate how much of the runtime gap the conservative estimate explains. If it still explains nearly all of the discrepancy, the wrong-reference conclusion is robust even if exact frame boundaries remain unresolved. Request the actual editor audio or EDL only for the final join-level seconds.

## Prosecutorial conclusion structure

For concise adversarial reporting, present:

1. verdict;
2. same-recording/genealogy proof;
3. semantic difference between documents;
4. runtime equation and causal bridge;
5. operational wrong-selection evidence;
6. confidence limitation and conservative bound;
7. source hashes and explicit no-modification statement.

## Pitfalls

- Calling a strike-only review copy a flattened tracked-edit document without mask-overlap evidence
- Treating more cut groups as more aggressive editing; many micro-cuts can remove less time than fewer whole-passage cuts
- Comparing deletion-character totals without projecting both plans onto the same transcript
- Inferring authority from directory placement alone when a file explicitly named `컷편집` or a tracked-edit variant exists
- Claiming exact causality from a nominal ASR union while suppressing manual-review spans
- Modifying source documents during a forensic audit
