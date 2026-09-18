# Speaker-correction boundary policy

Use this checklist for pure `move_text_to_target_prefix` operations before any DOCX/OOXML work.

## Canonical moved text

- Require `text` to be a non-empty string.
- Require exact normalization: `text == text.strip()`.
- Reject padded values with `ValueError("text must not have leading or trailing whitespace")`.
- Use that same unmodified value for source search, uniqueness checks, target-duplicate checks, deletion, and insertion. Never search with one normalized value and insert another.

## Source-span deletion

Deletion and target insertion need separate boundary helpers; a generic whitespace-normalizing join is unsafe.

When closing the source span:

1. Remove only ASCII space/tab immediately adjacent to the removed span (`rstrip(" \t")`, `lstrip(" \t")`).
2. Never strip `\n`, `\r`, or other surrounding whitespace wholesale; all newlines outside the moved span must survive.
3. If either surviving boundary already contains whitespace, concatenate directly.
4. If the right boundary begins with punctuation, concatenate directly (`"앞 이동, 뒤" -> "앞, 뒤"`).
5. Otherwise insert one ASCII space between surviving words (`"앞 이동 뒤" -> "앞 뒤"`).

Regression fixtures:

- punctuation: `"앞 이동, 뒤" -> "앞, 뒤"`
- ordinary words: `"앞 이동 뒤" -> "앞 뒤"`
- newlines: `"앞\n이동\n뒤" -> "앞\n\n뒤"`
- source start/end: no accidental leading or trailing ASCII whitespace

## Target-prefix insertion

The existing target string is immutable payload and must remain an exact suffix:

- Empty target: return `moved_text`.
- Target begins with any whitespace: return `moved_text + target_text`; add nothing.
- Otherwise: return `moved_text + " " + target_text`.

Test multiple leading spaces, tabs, and a leading newline. Do not use `lstrip()` on target text.

## Collection preflight

Before applying a correction:

- every block is a dict;
- every block ID has exact type `int` (`bool` is invalid);
- block IDs are globally unique, including unreferenced blocks;
- referenced source and target IDs still resolve exactly once.

Before applying a correction list:

- every item is a dict;
- every correction ID is a non-empty string;
- correction IDs are globally unique;
- run this preflight before executing the first correction.

## TDD and integration gates

Add regression tests before implementation for punctuation, normal spacing, newline preservation, target-leading whitespace, padded moved text, duplicate-target bypass, unreferenced duplicate block IDs, and duplicate correction IDs.

For the real manifest fixture, assert:

- exact block count and ID order;
- exact complete source and target block dictionaries after correction;
- every other block is deeply equal to input;
- input blocks and correction metadata are unchanged;
- source transcript, manifest, validation artifact, and source DOCX SHA-256 values are unchanged.
