---
name: tracked-docx-rough-cut-editing
description: Author editor-facing Track Changes DOCX files from approved cut decision ledgers, with declarative manifests, speaker-boundary corrections, red move notes, and fail-closed OOXML validation.
version: 1.4.0
metadata:
  hermes:
    tags: [ttimes, docx, track-changes, ooxml, cut-plan]
    related_skills: [ttimes-cut-editing, ttimes-audio-rough-cut-rendering]
---

# Tracked DOCX Rough-Cut Editing

Use this skill when turning an **already approved TTimes cut decision ledger** into an editor-facing Track Changes DOCX. Its primary scope is Word/OOXML authoring, not deciding what viewers should hear. Use `ttimes-cut-editing` for production-speech, retake, redundancy, tangent, narrative, and move decisions. Use `ttimes-audio-rough-cut-rendering` to implement an approved plan as a rough-cut MP3/WAV. Never let DOCX constraints or audio-runtime pressure silently change the approved editorial ledger. These are different acceptance contracts and must never be conflated. Follow `references/docx-guided-audio-rough-cut.md`; do not confuse marked-run counting with audio-cut counting or claim editor-equivalence from technically clean joins. When a generated rough cut differs materially from a human editor’s claimed runtime, stop delivery and follow `references/runtime-discrepancy-attribution.md` to compare alternate DOCX semantics, relocation instructions, verified reference artifacts, and independently aligned plans while quantitatively falsifying pause, drift, and mechanical range-expansion hypotheses. If the dispute is specifically whether the pipeline chose the wrong authoritative DOCX, also follow `references/reference-document-selection-forensics.md`: reconstruct document genealogy from full text, project competing deletion masks onto one transcript, prove the operational selection path from code/manifests, and report nominal plus conservative runtime bounds.

## Operating modes and scope control

Choose the mode **before touching code**. Do not silently promote a document job into a framework project.

### A. One-off DOCX authoring mode — default

Use when the user wants one Track Changes DOCX from a trusted, already approved cut ledger and a working generator exists.

- Treat the approved ledger as immutable editorial authority. This skill may validate reasons and continuity fields but must not invent, widen, shrink, or reorder cuts.
- Run one dry-run, generate once, perform one artifact audit, and deliver.
- Reuse the existing generator without changing production code or expanding its test suite.
- Bound verification to source-hash preservation, declared-operation accounting, Track Changes structure, accepted/rejected simulation, openability, and exact ledger compliance.
- If production chatter, redundancy, narrative priority, or another new content decision is discovered, record it as `editorial_review_required` and return to `ttimes-cut-editing`; do not fix it inside OOXML authoring.
- Treat broader hardening ideas—adversarial TOCTOU, hostile DOCX packages, generalized schemas, reusable CLI features—as separate engineering work unless the current input fails or the user requests production hardening.

### B. Generator engineering mode — explicit opt-in

Use only when the generator is missing required behavior, inputs are untrusted/automated, the user asks for a reusable pipeline, or a real artifact defect cannot be solved by the existing path. TDD, all-part OOXML checks, staged spec review, and code-quality review belong here.

### Scope-stop rule

If more time is being spent on the engine, tests, reviewers, or validation schema than on cut decisions, stop. Return to the last working generator path, label optional hardening separately, and finish the artifact. Never recursively turn each review finding into another review cycle for a one-off document.

### Changed-plan / “start over” rule

When the user asks to change the editorial plan or redo the cut from scratch, stop DOCX authoring and hand the task to `ttimes-cut-editing`. This skill resumes only after a new approved ledger exists. It may regenerate a new versioned DOCX from that ledger, but it must not derive the replacement plan itself.

### Editorial-boundary validation

This skill does not perform content-first cut selection. It validates that the approved ledger carries enough evidence to author safely:

1. every operation has a stable ID, exact source range, operation type, and approval status
2. every `MOVE` has source and destination data
3. unresolved decisions are rejected before mutation
4. the accepted-text simulation preserves the ledger's declared left/right context
5. any newly noticed narrative or production-speech concern is reported back to `ttimes-cut-editing`, not silently edited

See `ttimes-cut-editing` for the actual PD doctrine and `references/workflow-scaling-and-clean-recut.md` only for legacy migration context.

## Core contract

1. Preserve the source DOCX byte-for-byte.
2. Express every deletion in a declarative manifest before editing.
3. Match partial cuts by `block_id` plus exact, unique text anchors.
4. Represent deletions as real Word revision markup (`w:del`/`w:delText`), not red font, strike-through, comments, or silently removed prose.
5. Represent red insertion, relocation, and transition instructions as real tracked sibling paragraphs (`w:p > w:ins`), never as untracked normal text.
6. Fail closed on missing, duplicate, reversed, overlapping, malformed, or stale inputs.
7. Verify both the OOXML package and the editorial read-through before delivery.

See `references/ooxml-validation.md` for XML structures, application order, and verification probes. See `references/speaker-correction-boundaries.md` for the reusable punctuation/newline boundary policy, moved-text normalization, global ID preflight, and regression matrix. See `references/fail-closed-deletion-engine.md` for paragraph-structure preflight, exact range/metadata validation, byte-equivalent no-op handling, and XML-unchanged regression probes. See `references/structural-boundaries-and-atomic-commit.md` for direct-child boundary preservation, detached-output atomic commit, late-failure regression probes, and two-save OOXML round-trip coverage. See `references/tracked-instruction-paragraphs.md` for the exact `w:ins` paragraph shape, fail-closed validation matrix, vertical TDD tracers, and ZIP round-trip probes. See `references/integrated-application-ledger.md` for real block-to-paragraph mapping, global revision-ID accounting, speaker-move OOXML, accepted/deleted text ledgers, and atomic final generation. See `references/independent-final-audit.md` for a source-first final audit that reconstructs source→final paragraph identity, verifies every cut independently, estimates runtime two ways, and catches narrative/whitespace defects that a self-consistent manifest can preserve. See `references/generated-summary-ooxml-metrics.md` for saved-package-derived summary metrics, independent RED→GREEN assertions at generation and CLI boundaries, and final-artifact hash preservation. See `references/final-state-rerun-and-validation-report-freshness.md` for the final-state rerun gate, exact plan-command checks, and the self-invalidating validation-report failure pattern. See `references/independent-plan-compliance-review.md` for requirement-to-evidence tracing, validation-discovered semantic corrections, semantic-versus-physical deletion ranges, staged stale-artifact handling, and explicit output-field audits before regeneration. See `references/post-save-package-validation-and-source-provenance.md` for verified-byte loading, swap-and-restore race prevention, all-part XML parsing, revision-shape validation, and malformed-package publication probes. See `references/docx-deletion-markup-forensics.md` when Word appears to show more deletions than the audio manifest or a delivered runtime is materially longer than an editor-reported cut; it covers all-part markup classification, style inheritance, nested run containers, paragraph-mark strike semantics, color-versus-relocation evidence, exact manifest reconciliation, and crossfade-aware duration accounting.

## Workflow

### 1. Freeze inputs

- Record SHA-256 and byte size for the source DOCX and transcript data.
- Retain the exact verified source bytes and load the document from that byte buffer; do not hash a path and then reopen it for parsing.
- Never edit the source path in place.
- Put the intended output at a distinct path.
- Record a schema version and hashes for the manifest and transcript source so a stale manifest cannot be applied silently.

### 1.5. Verify the approved ledger before authoring

Do not select cuts here. Confirm that the approved ledger maps to the frozen source and contains stable operations, exact anchors, left/right retained context, move destinations, and no unresolved editorial decisions. Build the accepted-text simulation from the ledger and verify declared continuity; if the ledger itself breaks a referent, causal chain, or Q/A dependency, fail closed and return it to `ttimes-cut-editing` rather than repairing the story inside this skill.

### 2. Build a declarative cut manifest

Use stable logical block IDs. Recommended cut modes:

- `whole_block`: delete the speaker/timestamp line and body for one block.
- `substring`: delete from one inclusive exact anchor through another.
- `substring_to_end`: delete from one exact anchor through block end.

Each cut should carry:

- unique `id`
- integer `block_id` (reject booleans explicitly)
- `mode`
- required anchor fields
- concise editorial `reason`

For a one-phrase deletion where start and end anchors are identical, require an explicit policy such as `single_exact_text_when_anchors_equal`. Do not rely on a generic second-anchor search.

### 3. Validate before document work

Resolve every cut to a half-open source-text range `[start, end)`.

Validation rules:

- Block IDs are exact integers; `True` must not alias block `1`.
- Cut IDs are non-empty strings.
- Modes are strings from a closed set.
- Anchors must be non-empty and occur exactly once, including overlapping occurrence detection.
- End anchors must follow the complete start anchor.
- Whole-block cuts cannot coexist with another cut in the same block.
- Partial ranges in the same block must not overlap.
- Validation must not mutate the manifest or transcript blocks.

Keep normalization pure: return deep-copied cut entries with resolved semantic `start` and `end` offsets. Do not rewrite those offsets to clean up joins. Immediately before OOXML preflight, derive a separate physical deletion range that may include only the boundary separator whitespace required to prevent leading, trailing, or doubled accepted whitespace. Recheck overlap on those expanded physical ranges, and verify accepted-plus-deleted nodes reconstruct the original paragraph exactly. The independent audit policy is detailed in `references/independent-final-audit.md`.

Before OOXML mutation, map logical blocks to real DOCX paragraph pairs from the **actual transcript schema**. If the source has numeric `start` seconds but no display timestamp, floor seconds and derive the header label; never invent or assume a missing `timestamp` field. Scan forward for exact header/body pairs, reject ambiguity, and record resolved paragraph indices. Preflight the actual target paragraphs for supported direct-run structure.

### 4. Correct speaker boundaries separately

Do not disguise diarization corrections as editorial cuts. Use a separate `speaker_corrections` section.

For moving a sentence from the end of one block to the beginning of the next, define the operation explicitly, for example:

- `mode: move_text_to_target_prefix`
- source and target block IDs
- exact unique sentence
- replacement speaker and display timestamp
- timestamp policy

Apply the correction to an in-memory deep copy first. Assert:

- every block is a dict with an exact integer ID, and all block IDs are globally unique even when unreferenced
- correction lists contain only objects with non-empty, globally unique correction IDs before the first operation runs
- moved `text` is non-empty and exactly trimmed; reject padding rather than silently normalizing it
- exactly one source match, using the same moved-text value for search, duplicate detection, deletion, and insertion
- no duplicate already in the target
- block count, order, and IDs remain unchanged
- only source and target blocks differ
- source-span deletion strips only adjacent ASCII space/tab and never removes surrounding newlines
- target-prefix insertion preserves the complete existing target string exactly; add one ASCII space only when its first character is not whitespace
- source/target surrounding punctuation and text remain intact

### 5. Apply OOXML revisions

`python-docx` does not expose Track Changes deletion APIs. Manipulate paragraph XML directly:

- retained text: `w:r > w:t`
- deleted text: `w:del > w:r > w:delText`
- add `w:id`, `w:author`, and UTC `w:date` to each `w:del`
- clone the original `w:rPr` so font and size survive
- set `xml:space="preserve"` where boundary spaces matter
- enable `w:trackRevisions` in `word/settings.xml`

For multiple cuts in one paragraph, apply ranges in **descending source-offset order** or rebuild the paragraph from a single segmentation pass. Never apply ascending offsets to a mutating text representation.

Before reusing a deletion helper, inspect the source run-child tags. Synced transcript DOCX files may store the speaker, timestamp, and several body lines in one paragraph using manual line breaks (`w:br`). A helper that calculates offsets or rebuilds runs from `w:t`/`w:delText` only will silently drop those line breaks and misalign `python-docx` offsets, because `Paragraph.text` represents each `w:br` as `\n`. For these files, either use a line-break-aware one-off segmenter that tokenizes `w:t` and `w:br` (counting each break as one source character) or normalize a protected working copy before editing. Wrap deleted breaks inside the same `w:del`, preserve retained breaks as direct `w:br`, and require Reject All reconstruction to reproduce every original newline exactly.

For whole-block deletion, mark both speaker/timestamp text and body text as revisions. Leaving structural blank paragraphs is acceptable if the accepted-deletion read-through remains clean.

Maintain one global monotonically increasing revision-ID ledger across cut deletions, speaker-move deletion/insertion, header replacement, and editor-note insertions. Every helper should return the next unused ID; verify uniqueness and the expected final range in `document.xml`.

### 6. Insert tracked editor instructions

Use a new direct sibling paragraph for non-source instructions such as:

- cold-open-to-main transition
- relocation instruction
- jump-to-closing instruction

Required OOXML shape:

- optional deep-copied `w:pPr` from the reference paragraph, as the first child
- `w:ins` with unique `w:id`, non-empty `w:author`, and UTC `w:date`
- exactly `w:ins > w:r > w:rPr > w:b + w:color[@w:val='FF0000'] > w:t`
- no duplicate normal direct `w:t` outside the insertion revision
- `xml:space="preserve"` when the exact instruction begins or ends with whitespace

Prebuild and validate the detached paragraph completely, then commit with exactly one `addprevious` or `addnext`. Return the inserted `Paragraph` and next unused revision ID so callers can chain unique IDs. Existing `w:del`/`w:ins` inside the reference paragraph are allowed because the operation inserts a sibling and must leave the reference XML byte-equivalent.

Do not put instructions inside `w:del`, and do not silently add them as untracked normal runs.

### 7. Verify the artifact

Run all gates before delivery:

- source SHA-256 unchanged
- manifest and transcript hashes match pinned values
- generation loaded the exact verified source bytes rather than reopening the source path after hashing
- every declared cut applied exactly once
- ZIP integrity passes
- every `.xml` and `.rels` package member parses with network/entity resolution disabled
- `w:del` and `w:delText` exist with legal direct-child shapes; no `w:delText` occurs outside `w:del`
- `w:trackRevisions` exists exactly once
- red instruction count and text match the manifest
- full-block deletions cover both header and body
- no placeholder speaker labels remain
- styles/fonts are preserved
- the document opens with a native OS converter or Word-compatible parser

Also create an **accepted-deletions simulation** by reading normal `w:t` while excluding `w:delText`. Read every transition around a cut. Technical validity does not prove editorial continuity.

## TDD and review gates — generator engineering mode only

The staged gates below apply **only when production generator code changes**. They are not the default workflow for a one-off editorial artifact.

Build engineering changes in small stages:

1. Anchor and overlap validation
2. Speaker correction pure functions
3. Partial and whole-block OOXML deletion
4. Red-note insertion
5. Integrated generation
6. XML/package/read-through validation

For each stage:

- write a failing regression test
- implement the minimum behavior
- run the full suite
- run a spec-compliance review
- run a separate code-quality review
- after a spec fix, rerun the spec review; after a quality fix, rerun the quality review

Do not move forward with open Critical or Important review findings.

### Recovering a timed-out delegated implementation

A timed-out implementation agent may have left valid partial code and tests behind; do not assume rollback and do not restart blindly.

1. Read the modified production and test files.
2. Run the full suite and syntax checks to establish the actual baseline.
3. Compare implemented tests against the stage checklist and identify the missing slices explicitly.
4. Preserve passing partial work.
5. Dispatch a fresh, narrowly scoped completion task for only the missing fail-closed paths or regression cases.
6. Re-run direct verification, then the same spec/quality review gate.

For OOXML work, always include source-hash verification during recovery so a partial agent cannot silently mutate the protected input.

## Common pitfalls

- Treating literal strike/deletion execution as equivalent to the broader content cut a human editor would make
- Claiming editorial success because all marked phrases disappeared and every join technically decoded cleanly
- Ignoring red relocation instructions in an audio handoff, or deleting the move source without reinsertion
- Trusting a `완료`/`수정 후` label without proving that the artifact is an actual edited output
- Treating a trusted one-off rough-cut as a reusable production framework project
- Expanding scope from editorial decisions into CLI, schema, security-hardening, or test-suite work without explicit user need
- Running multiple serial reviewers after the artifact already satisfies the one-off acceptance checks
- Reusing old cut IDs or editing the prior manifest after the user explicitly asked to start over
- Asking for target duration or cut strength by default, then sacrificing high-value content or retaining low-value filler to satisfy the quota
- Treating runtime and cut count as planning inputs when the user has not supplied a hard operational constraint
- Reading only cut boundaries instead of the complete accepted transcript

- Treating `bool` as an integer block ID in Python
- Letting unhashable malformed IDs leak `TypeError` instead of controlled `ValueError`
- Searching for an identical end anchor after the start anchor
- Applying multiple text offsets in ascending order
- Assuming `python-docx` paragraph text includes tracked deletions
- Treating `ZipFile.testzip()` or `Document(path)` as proof that every XML/relationship part is well-formed; parse all `.xml`/`.rels` members explicitly
- Checking only revision counts and IDs while accepting malformed revision shape such as `w:t` inside `w:del` or `w:delText` outside a deletion
- Hashing a source path, discarding the verified bytes, and reopening the path with `Document(path)`; a swap-and-restore race can publish unverified content
- Claiming success from a visually readable document without inspecting OOXML
- Correcting diarization by silently rewriting unrelated source text
- Treating accepted-text equality with the manifest as proof of editorial cleanliness; the manifest itself may preserve leading, doubled, or trailing separator spaces
- Reporting runtime before the content ledger and full accepted-transcript read-through are complete, or treating a timestamp estimate as a reason to change editorially sound cuts
- Trusting the generation summary as an independent audit instead of reconstructing expected revisions from source + manifest
- Treating a mostly complete generation summary as plan-compliant without checking every explicitly named field; revision-node counts do not substitute for deleted-character counts
- Treating an explicitly stale pre-regeneration final as delivered evidence, or refreshing output/runtime/narrative while leaving stored test counts stale
- Letting one exact-key JSON file serve as both immutable preflight input and a cumulative report; final report fields can invalidate dry-run/generation and make stored test results stale
- Testing a corrected CLI invocation while never running the plan's command verbatim; added required flags are plan-compliance failures until plan and CLI agree
- Delivering the source, temporary files, and logs when the user requested only the final artifact

## Completion criteria

A rough-cut DOCX is complete only when:

- source remains unchanged
- every manifest operation is uniquely accounted for
- every cut has a content-based reason (redundancy, drift, filler, post-roll), not merely a duration-saving rationale
- revision markup is structurally valid
- the complete accepted-deletion transcript reads coherently, with key mechanisms, evidence, limitations, and conversational dependencies preserved
- runtime is calculated and reported only after the editorial ledger is stable
- transition instructions are visible and correctly colored
- the final DOCX opens successfully
- only the requested final artifact is delivered
