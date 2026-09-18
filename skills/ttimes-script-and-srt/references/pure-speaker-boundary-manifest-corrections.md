# Pure speaker-boundary corrections for cut-edit manifests

Use this pattern when diarization assigns a boundary sentence to the wrong speaker block and a manifest declares a move such as `move_text_to_target_prefix`.

## Recommended pure API

```python
apply_speaker_correction(blocks, correction) -> deep-copied corrected blocks
apply_speaker_corrections(blocks, corrections) -> declaration-order result
```

Keep this layer separate from DOCX/OOXML editing and CLI behavior. It should transform in-memory block dictionaries only.

## Transformation contract

For one correction:

1. Find exactly one `from_block` and one distinct `to_block`.
2. Require the declared text to occur exactly once in source text.
3. Reject the operation if target text already contains the same phrase.
4. Remove the phrase from source text and normalize only the resulting boundary whitespace.
5. Prefix target text with the moved phrase using one boundary space.
6. Replace target `speaker` and `timestamp` with manifest values.
7. Preserve block count, order, IDs, all unrelated fields, and all unrelated blocks.
8. Never mutate `blocks` or `correction`; return a deep copy.

## Validation traps

- Check IDs with `type(value) is int`; Python `bool` must not alias block `1` or `0`.
- Validate malformed/list IDs before hashing or indexing so callers receive `ValueError`, not incidental `TypeError` or `StopIteration`.
- Require non-empty, non-whitespace strings for correction ID, moved text, speaker, and timestamp.
- Reject unknown/duplicate/same source-target IDs, unsupported mode/policy, missing/duplicate source text, and duplicate target text.
- The plural wrapper must require a list and apply corrections in declaration order; later corrections may depend on earlier text moves.

## Strict TDD and fixture safety

1. Record SHA-256 for protected source DOCX, source JSON, manifest, and validation JSON.
2. RED: start with a two-block in-memory example.
3. GREEN: implement the minimum pure move.
4. RED again: add the validation matrix and a real-manifest integration test.
5. GREEN: run the whole target suite and `py_compile`.
6. Run the real correction in memory and inspect source tail, target prefix, speaker/timestamp, block count, and ID order.
7. Recompute protected-file hashes and require exact equality. Integration tests must only read these files; never write transformed output back to them.

This pattern lets later DOCX-rendering code consume a validated corrected block list without coupling text-boundary logic to OOXML operations.
