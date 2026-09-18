# Post-save package validation and source provenance

Use this when a tracked-DOCX generator claims fail-closed, integrity-pinned, atomic publication.

## 1. Load the exact bytes that were verified

A path hash checked before `Document(path)` is vulnerable to a swap-and-restore race:

1. source path contains pinned bytes A and passes SHA-256;
2. another actor swaps in parseable bytes B;
3. `Document(path)` loads B;
4. actor restores A before the pre-publish recheck;
5. the hash recheck passes while output derived from unverified B is published.

Prevent this by retaining the bytes returned from integrity verification and loading those exact bytes:

```python
from io import BytesIO

source_data = verified_bytes(source_record)
document = Document(BytesIO(source_data))
```

Keep a separate path recheck before publication to prove the protected source currently still equals A. It supplements byte-provenance; it does not replace it. Apply the same rule to any input parsed after hashing: parse the verified byte buffer, not a second path read.

Regression probe: in a disposable fixture, swap the source to a DOCX with one altered unmapped paragraph only during `Document()` loading, then restore it before the post-save hash check. Generation must either load A from the verified buffer or reject; it must never publish the altered paragraph.

## 2. Parse the whole saved package, not only document.xml

`ZipFile.testzip()` proves CRC integrity, not XML well-formedness. `python-docx` may ignore and preserve malformed parts such as `customXml/item1.xml`. A post-save inspector that parses only `word/document.xml` and `word/settings.xml` can therefore publish a syntactically malformed package.

After saving the detached temporary output:

- run ZIP integrity;
- parse every member ending in `.xml` or `.rels` with a non-network, no-entity-resolution XML parser;
- convert `BadZipFile`, missing required members, and `XMLSyntaxError` to the public fail-closed error contract;
- only then perform semantic revision checks and atomic replacement.

Example parser policy:

```python
parser = etree.XMLParser(resolve_entities=False, no_network=True)
for name in package.namelist():
    if name.endswith((".xml", ".rels")):
        etree.fromstring(package.read(name), parser=parser)
```

## 3. Validate revision shape, not only counts and IDs

Matching `w:del`/`w:ins` counts and sequential IDs does not prove valid revisions. A package can retain the same counts while replacing `w:delText` with `w:t`, or placing `w:delText` outside `w:del`.

At minimum require:

- every `w:del` has nonempty direct `w:r` children whose text nodes are `w:delText`, never `w:t`;
- every tracked insertion has the expected `w:ins > w:r > w:t` shape and no `w:delText`;
- no `w:delText` occurs outside `w:del`;
- no nested `w:del`/`w:ins` revisions;
- every revision has valid ID, author, and UTC date metadata;
- package-derived deleted-character count is computed only after these shape checks.

Regression probes should corrupt a real disposable saved package rather than mocking the inspector:

1. rename one `w:delText` to `w:t` while retaining revision count and IDs;
2. replace a non-main XML part with malformed bytes;
3. assert rejection occurs before `os.replace`, an existing output sentinel is preserved, and the temporary file is removed.

## 4. Atomicity caveat

A detached temporary save plus `os.replace` is atomic only after validation is complete. If cleanup itself fails, preserve the primary save/inspection exception instead of masking it with `unlink()` failure. Tests should cover both publication failure and cleanup failure reporting.
