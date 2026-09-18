# Generated-summary OOXML metrics

Use this pattern when a generation command must report facts about the DOCX it actually published, such as the total number of tracked-deletion characters.

## Source of truth

Compute package-derived metrics inside the post-save inspection path, after reopening the detached temporary DOCX and parsing `word/document.xml`. Do not derive them from the manifest, source anchors, in-memory paragraph text, or planned edit ranges: those inputs do not prove what was serialized.

For tracked-deletion characters:

```python
deleted_characters = sum(
    len(text)
    for text in document_root.xpath(
        "//w:delText/text()",
        namespaces={
            "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        },
    )
)
```

This is a Python Unicode character count over every `w:delText` text node in the saved package. It includes whitespace and punctuation. Keep the value an integer and expose it as a top-level field in the real generation summary/CLI JSON. Do not add it to dry-run output unless dry-run semantics explicitly require a planned estimate; package-derived and pre-save metrics must not be conflated.

Preserve existing fail-closed behavior: ZIP integrity, XML parsing, revision counts and IDs, track-revision settings, and atomic replacement must all remain gates around the metric.

## Strict TDD tracer

1. In a real-generation integration test, generate to a temporary custom output path.
2. Reopen that output independently with `zipfile.ZipFile` and `lxml`; do not call the production inspection helper to calculate the expected value.
3. Calculate the expected count from `//w:delText/text()` using Python `len()` and assert equality with `summary["deleted_characters"]`.
4. Run the test and verify the expected RED is a missing/wrong summary field, not a fixture or import error.
5. Add the minimum production calculation to the post-save inspector and include its returned value in the generation summary.
6. Re-run the direct generation test and add the same independent assertion at the CLI JSON boundary so serialization is covered.
7. Run the full suite, syntax compilation, and lint.

The expected value may be a fixed fixture constant or an independently computed package value. Report the fixture's observed value after GREEN so reviewers can compare it with manual probes.

## Artifact-preservation gate

When the real final DOCX is protected, hash it before testing and again after all tests. All generation and CLI probes must target disposable temporary paths. Matching before/after hashes prove the final deliverable was not regenerated while validating summary-only code changes.
