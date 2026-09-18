# Tracked instruction paragraphs

Use this checklist when inserting editor-visible red instructions as Word Track Changes insertions.

## Public operation

A useful API shape is:

```python
insert_red_tracked_note(
    reference_paragraph,
    text,
    *,
    position,      # exact "before" or "after"
    author,
    change_id,
    changed_at=None,
) -> tuple[Paragraph, int]
```

Return the inserted paragraph plus `change_id + 1` so multiple notes naturally receive unique IDs.

## Exact OOXML

Create a new direct sibling `w:p`; never rewrite the reference paragraph.

```xml
<w:p>
  <w:pPr>...</w:pPr> <!-- only when the reference has one; deep copy -->
  <w:ins w:id="..." w:author="..." w:date="...Z">
    <w:r>
      <w:rPr><w:b/><w:color w:val="FF0000"/></w:rPr>
      <w:t>exact instruction text</w:t>
    </w:r>
  </w:ins>
</w:p>
```

There must be one `w:t` for the instruction and no normal direct `w:r/w:t` duplicate outside `w:ins`. Add `xml:space="preserve"` if the first or last character is whitespace.

## Fail-closed order

1. Validate `text` is a non-empty string. Preserve leading/trailing whitespace rather than trimming it.
2. Validate `position` against a tuple, not a set, so malformed unhashable input produces controlled `ValueError` rather than leaked `TypeError`.
3. Validate revision metadata with a revision-generic helper shared by insertions and deletions:
   - author: non-empty string
   - ID: exact nonnegative `int`; reject `bool`
   - timestamp: `None` or timezone-aware `datetime`
   - convert to UTC; wrap overflow as `ValueError`
4. Build all XML detached from the document. Attribute/text assignment is also XML-validity preflight; normalize XML-invalid author/text failures to `ValueError` where necessary.
5. Deep-copy reference `w:pPr` as the first child.
6. Commit once with `addprevious` or `addnext`.
7. Construct and return `Paragraph(new_p, reference_paragraph._parent)` and the next ID.

On every validation or prebuild failure, assert body child count, order, and serialized XML are unchanged.

## Vertical TDD tracers

Use one RED→GREEN slice at a time:

1. `after`: exact sibling order, nested revision shape, red/bold, metadata, next ID, unchanged reference.
2. `before`: exact sibling order.
3. `pPr`: style/alignment/spacing/line-spacing equality plus deep-copy independence.
4. whitespace: exact text and `xml:space="preserve"`.
5. invalid text and invalid position: exact `ValueError`, body byte-equivalent.
6. author/ID/date/XML-invalid inputs: exact `ValueError`, no mutation.
7. reference containing existing `w:del` and `w:ins`: sibling insertion succeeds and reference XML stays byte-equivalent.
8. integration: insert two real plan strings, save, reopen, save again, inspect ZIP XML.

If a later behavior was accidentally implemented during an earlier tracer (for example `pPr` copying during placement work), remove it, observe the later test fail, then restore the minimal implementation. A final integration test may start green if it only composes already-proven primitives; treat that as round-trip regression coverage, not a reason to manufacture a code change.

## ZIP round-trip probe

After save → reopen → second save, inspect `word/document.xml` and `word/settings.xml` and require:

- exact `w:ins` count
- exact instruction strings and one `w:t` per insertion
- zero normal direct note `w:t` outside insertion revisions
- unique sequential IDs and expected next ID
- exact authors and UTC dates
- one `w:b` and color `FF0000` per insertion
- exactly one `w:trackRevisions`

Finally rerun the full regression suite, syntax compilation, and SHA-256 checks for every protected source DOCX and JSON/manifest input. Temporary DOCX files should stay inside a temporary directory.
