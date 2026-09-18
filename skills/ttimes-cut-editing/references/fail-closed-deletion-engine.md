# Fail-Closed OOXML Deletion Engine Preflight

Use this reference when implementing or reviewing a paragraph-level Word Track Changes deletion helper. The key invariant is:

> Any rejected input raises `ValueError` before the paragraph XML changes. Valid empty ranges return the unchanged revision ID and leave XML byte-equivalent.

## Required preflight order

Perform these steps before removing, inserting, or rebuilding any XML node:

1. **Validate metadata**
   - `author`: non-empty string after whitespace check.
   - `change_id_start`: exact `int`, excluding `bool`, and `>= 0`.
   - `changed_at`: `None` or a timezone-aware `datetime` whose `utcoffset()` is not `None`.
2. **Validate paragraph structure**
   - Reject any descendant `w:del` or `w:ins` as an existing revision.
   - Reject direct non-`w:r` text-bearing containers such as `w:hyperlink` containing `w:t`.
   - For each direct `w:r`, permit only direct `w:rPr` and `w:t` children. Reject `w:tab`, `w:br`, `w:instrText`, `w:drawing`, and other unsupported run content.
   - Preserve non-text structural children such as `w:pPr`, bookmarks, and proofing markers.
3. **Collect visible source text and run data**
   - Use only supported direct runs and their direct `w:t` text.
   - Record half-open run offsets and cloned `w:rPr` references without mutating XML.
4. **Validate ranges against visible direct-run text length**
   - `ranges` itself must be a list.
   - Every item must be a tuple/list of exactly two values.
   - Both bounds must be exact integers; reject booleans.
   - Enforce `0 <= start < end <= text_length`.
   - Sort by `(start, end)` so caller order is irrelevant.
   - Reject overlap when `current.start < previous.end`; adjacency is valid.
5. **Handle the no-op boundary**
   - After all validation, if the normalized range list is empty, immediately return `change_id_start`.
   - Do this before indexing a first run, generating a timestamp, or reconstructing runs. This makes empty paragraphs safe and normal paragraphs byte-equivalent.
6. **Mutate only after successful preflight**
   - Rebuild retained `w:t` and deleted `w:del/w:r/w:delText` segments.
   - Assign sequential IDs from `change_id_start`.
   - Convert `changed_at` to UTC and format as `YYYY-MM-DDTHH:MM:SSZ`.

## TDD regression matrix

Add tests in vertical RED→GREEN slices:

- **Ranges:** non-list container, malformed item arity, bool/float/string bounds, negative/empty/reversed/out-of-range spans, unsorted valid spans, adjacency, overlap.
- **Metadata:** empty/whitespace/non-string author; bool/negative/non-integer revision ID; non-datetime and naive datetime.
- **Structure:** existing `w:del`, existing `w:ins`, text-bearing hyperlink, and unsupported direct run children (`tab`, `br`, `instrText`, `drawing`).
- **No-op:** both an empty paragraph and a regular formatted paragraph with structural children; assert exact `paragraph._p.xml` equality and unchanged next ID.

For every invalid case:

```python
xml_before = paragraph._p.xml
with self.assertRaises(ValueError):
    apply_tracked_deletions(...)
self.assertEqual(xml_before, paragraph._p.xml)
```

Do not merely assert an exception: wrong exception types and partial XML mutation are separate regressions.

## Integration probes without producing a deliverable

For engine-only tasks where generating a final DOCX is prohibited:

- Hash the source DOCX before and after work.
- Read `word/document.xml` and `word/settings.xml` directly from the ZIP package.
- Confirm the source has expected baseline counts for `w:del`, `w:delText`, `w:ins`, and `w:trackRevisions`.
- Scan source paragraphs for unsupported text-bearing direct containers and unsupported direct run children.
- Build an in-memory `python-docx` paragraph, apply one deletion, and assert `w:del=1`, `w:delText=1`, and `w:trackRevisions=1` without saving a final artifact.
- Run an independent invalid-input probe that counts both rejected cases and byte-equivalent XML results.
