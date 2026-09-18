# OOXML Track Changes and Validation Reference

## Namespaces

```python
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}
```

Use `docx.oxml.ns.qn()` when creating attributes and elements through `python-docx`/lxml.

## Tracked deletion shape

```xml
<w:del w:id="1" w:author="Hermes 컷편집" w:date="2026-07-14T00:00:00Z">
  <w:r>
    <w:rPr>...</w:rPr>
    <w:delText xml:space="preserve">deleted source text</w:delText>
  </w:r>
</w:del>
```

Retained text remains:

```xml
<w:r>
  <w:rPr>...</w:rPr>
  <w:t xml:space="preserve">retained text</w:t>
</w:r>
```

Enable revision tracking in `word/settings.xml`:

```xml
<w:trackRevisions/>
```

## Safe paragraph segmentation

Given one original paragraph text and non-overlapping deletion ranges:

1. Sort ranges by `(start, end)`.
2. Assert `0 <= start < end <= len(text)`.
3. Assert each `start >= previous_end`.
4. Emit retained segment before each range as `w:t`.
5. Emit each deleted segment as one `w:del/w:delText`.
6. Emit the final retained tail.
7. Clone original run properties into every emitted run.

This single-pass rebuild avoids index drift. If editing existing runs in place instead, process ranges in descending offset order.

## Full-block deletion

For a two-paragraph logical block:

- Wrap all text runs in the speaker/timestamp paragraph as tracked deletions.
- Wrap all text runs in the body paragraph as tracked deletions.
- Preserve paragraph properties and spacing.
- Do not rely on deleting only the body; accepted-deletion output would leave orphan headers.

## XML verification probe

```python
from pathlib import Path
from zipfile import ZipFile
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ns = {"w": W}

with ZipFile(Path(output_docx)) as zf:
    document = etree.fromstring(zf.read("word/document.xml"))
    settings = etree.fromstring(zf.read("word/settings.xml"))

tracked_deletions = document.xpath("//w:del", namespaces=ns)
deleted_text = "".join(document.xpath("//w:delText/text()", namespaces=ns))
normal_text = "".join(document.xpath("//w:t/text()", namespaces=ns))
track_setting = settings.xpath("//w:trackRevisions", namespaces=ns)
red_notes = document.xpath(
    "//w:r[w:rPr/w:color[@w:val='FF0000']]/w:t/text()",
    namespaces=ns,
)

assert tracked_deletions
assert deleted_text
assert len(track_setting) == 1
```

## Accepted-deletions simulation

Normal `python-docx` APIs may omit revision text inconsistently. Treat OOXML as authoritative:

- **retained read-through:** concatenate `w:t` nodes outside `w:del`
- **deleted ledger:** concatenate `w:delText` under each `w:del`
- **all-markup audit:** preserve document order while tagging retained/deleted/red-note segments

For each declared cut, assert its exact source substring appears in the deleted ledger associated with the expected paragraph/block. A global substring assertion alone can pass if the same phrase was deleted in the wrong place.

## Package checks

```bash
unzip -t output.docx
textutil -convert txt -stdout output.docx >/tmp/readback.txt
```

`textutil` is an opening/readback smoke test, not proof of revision correctness. XML assertions remain the final structural authority.

## Integrity ledger

Record at minimum:

```json
{
  "schema_version": 1,
  "source": {"path": "...", "sha256": "...", "bytes": 0},
  "integrity": {
    "manifest": {"path": "...", "sha256": "...", "bytes": 0},
    "source_json": {"path": "...", "sha256": "...", "bytes": 0}
  },
  "output": {
    "path": "...",
    "sha256": "...",
    "bytes": 0,
    "tracked_deletion_count": 0,
    "deleted_character_count": 0,
    "red_note_count": 0
  }
}
```

Recompute source and input hashes immediately before generation and source hash again after generation. Abort on any mismatch.
