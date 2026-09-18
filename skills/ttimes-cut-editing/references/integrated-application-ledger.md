# Integrated application ledger

Use this checklist when moving from individually tested OOXML helpers to a real transcript DOCX.

## Prove plan-to-manifest traceability first

Do not let a self-consistent manifest silently become the authority if it may have drifted from the user's approved rough-cut plan. Before implementation:

1. Preserve the approved plan text or a normalized plan ledger alongside the manifest.
2. Compare every cut ID, block/range, mode, reason, speaker correction, editor-note text, and before/after placement against that approved plan.
3. Record the comparison result in validation data (for example, a plan hash plus operation counts), not only manifest/source hashes.
4. Treat any mismatch as a blocking ambiguity; do not resolve it by trusting whichever artifact was generated later.
5. During final audit, validate the DOCX against both the manifest and the approved-plan ledger.

A manifest can pass schema, hash, OOXML, and end-to-end tests while still implementing the wrong editorial decisions. Internal consistency is not editorial authorization.

## Map logical blocks to paragraphs from actual source data

Do not assume the transcript JSON contains a display `timestamp` field. Inspect its schema first. A common shape has numeric `start` seconds only.

When DOCX headers use `[MM:SS] speaker`:

1. Validate `start` as a nonnegative numeric value, explicitly rejecting booleans.
2. Floor to whole seconds rather than rounding.
3. Format cumulative minutes and two-digit seconds.
4. Build the expected header from the derived timestamp plus the exact speaker.
5. Match each expected header and exact body as an ordered pair while scanning the DOCX forward.
6. Fail on missing, duplicate, ambiguous, or out-of-order pairs.

Never map blocks by hard-coded paragraph indices alone. Record resolved indices in the application report so later validation can explain every edit.

## Preflight the actual target paragraphs

Before the first mutation, inspect every header/body paragraph that will be edited:

- no existing `w:del` or `w:ins` unless the operation explicitly supports it
- supported direct `w:r`/`w:t` structure
- no hyperlink, field, tab, break, drawing, or other unsupported text-bearing container
- exact source text equals the transcript block text
- partial ranges are resolved against that exact source text

Do not infer safety from a generic fixture. Probe the actual target paragraphs in the source package.

## Keep one global revision-ID ledger

Use one monotonically increasing ID sequence across all operations:

- cut deletions
- speaker-boundary source deletion
- moved-text insertion
- header replacement deletion and insertion
- red editor-note insertions

For multiple ranges in one paragraph, allocate IDs according to sorted source ranges. Return the next unused ID from every helper and assert final uniqueness in `document.xml`.

## Speaker-boundary correction in OOXML

A logical move usually requires four tracked nodes:

1. `w:del` in the source body
2. `w:ins` at the target body prefix
3. `w:del` for the old target header
4. `w:ins` for the corrected target header

If the moved phrase ends the source paragraph and is preceded by one separator space, include that separator in the tracked deletion so accepted text has no trailing space. Insert the moved phrase plus one ASCII separator before a non-whitespace target body.

Build the expected corrected blocks with the pure speaker-correction function first, then compare them with an accepted-revision text ledger extracted from OOXML.

## Accepted/deleted text ledgers

`python-docx` `Paragraph.text` is not authoritative for tracked revisions. Validate with XML:

- accepted text: ordered `w:t` content not under `w:del`; include `w:t` inside `w:ins`
- deleted text: ordered `w:delText` grouped by revision ID
- editor notes: exact `w:ins/w:r/w:t` strings, color, bold state, and sibling position

Account for every manifest cut exactly once. Whole-block cuts must contribute both header and body deletions.

## Atomic file generation

1. Verify source DOCX, manifest, and transcript hashes and byte sizes.
2. Load and preflight the source.
3. Apply all operations in memory.
4. Save to a temporary DOCX in the destination directory.
5. Reopen it with a Word-compatible parser and parse `document.xml` and `settings.xml`.
6. Verify revision counts, unique IDs, notes, accepted/deleted ledgers, and `w:trackRevisions` exactly once.
7. Replace the destination atomically only after every gate passes.
8. On any error, remove the temporary file and leave the existing destination untouched.

The source path and destination path must never be identical.
