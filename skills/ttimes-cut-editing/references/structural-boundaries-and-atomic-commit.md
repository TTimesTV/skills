# Structural Boundaries and Atomic OOXML Commit

Use this note when a `python-docx` paragraph-level Track Changes helper must preserve non-text direct children and remain unchanged after failures that occur late in output construction.

## Relative-position invariant

Treat each direct non-`w:r` child as a structural boundary at its current visible-text offset. Relevant children include `w:pPr`, `w:bookmarkStart`, `w:bookmarkEnd`, `w:proofErr`, and comment-range markers.

1. Snapshot direct children in original order and record the visible-text offset at each structural child.
2. Split the paragraph into consecutive direct-run regions separated by those children.
3. Rebuild each run region independently, cloning `w:rPr` into retained and deleted runs.
4. Reinsert cloned structural children in original order between rebuilt regions.
5. Reject a deletion that strictly crosses a boundary: `start < boundary < end`.
6. Permit a range whose start or end equals the boundary exactly.
7. If no structural boundary intervenes, one deletion may span multiple original runs: emit one `w:del` containing multiple formatted `w:r` children.

Expected sequence:

```text
before:   pPr, r, bookmarkStart, r, bookmarkEnd
after:    pPr, r, bookmarkStart, r, del, r, bookmarkEnd
reopened: pPr, r, bookmarkStart, r, del, r, bookmarkEnd
```

## Atomic construction and commit

Do not remove original runs and then continue building revisions. XML attribute creation or UTC conversion can still fail and leave an empty `<w:p/>`.

Required order:

1. Validate metadata, paragraph structure, and ranges.
2. Return immediately for valid empty ranges, preserving exact XML and the next revision ID.
3. Convert `changed_at` to UTC. Convert `OSError`, `OverflowError`, and `ValueError` into the public `ValueError` contract.
4. Build every `w:t`, `w:del/w:r/w:delText`, revision attribute, cloned `w:rPr`, and cloned structural child in a detached container. An XML-forbidden author control character must fail here.
5. Commit only after the complete output exists, using one direct-child replacement such as `paragraph._p[:] = output_children`.

## Regression probes

Follow RED→GREEN for each bug before changing production code.

- Bookmark relative order: assert before, after, and save/reopen order.
- Structural crossing: assert `ValueError` and exact XML equality.
- Exact-boundary start/end: assert the deletion is allowed.
- XML-invalid author such as `"editor\x00"`: assert `ValueError`, exact XML equality, and unchanged `paragraph.text`.
- A timezone-aware `datetime.min` with a positive offset: assert UTC overflow becomes `ValueError`, with exact XML and text unchanged.
- Two-save OOXML round trips: separately cover whole deletion, multiple ranges and IDs, multi-run formatting, whitespace `xml:space="preserve"`, and `w:pPr` plus bookmark order. Use save → `Document(saved)` → save again → inspect `word/document.xml` and `word/settings.xml` in the ZIP.

Do not merely assert that an exception occurred. Exception type, byte-equivalent XML, and unchanged visible text are separate guarantees.
