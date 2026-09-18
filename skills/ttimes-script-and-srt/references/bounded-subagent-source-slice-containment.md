# Bounded subagent source-slice containment

## Failure pattern

A long-form caption job asked subagents to draft `00:00~20:00`, `20:00~40:00`, and `40:00~end`. Each brief included both the full timestamped raw ASR and a full timecode-free baseline. The drafters followed the unbounded baseline instead of the requested range, wrote beyond their assigned intervals, and still reported the requested scope as complete. Line counts, max length, and SHA were all internally valid, but the **content scope was false**.

Typical warning signs:

- the supposed early-range draft contains a topic known to occur much later;
- the reported “input end” is relative, ambiguous, or not the actual absolute source timestamp;
- a middle-range draft ends with the program’s closing argument;
- multiple range drafts overlap heavily despite different requested windows;
- output length is implausible for the assigned duration.

## Durable procedure

1. Parse the merged ASR JSON by absolute segment start time.
2. Create physical source files such as:
   - `source_00_10.txt`
   - `source_10_20.txt`
   - `source_20_30.txt`
3. Keep timestamps in each source slice. Record:
   - exact first/last segment timestamps;
   - segment count;
   - character count;
   - SHA-256.
4. Give the drafter only:
   - one exact slice file;
   - glossary;
   - correction ledger.
5. Explicitly forbid reading the full raw transcript, full baseline, or old range drafts.
6. Prefer 5–10 minute slices for 40–60 minute technical interviews. A 20-minute slice may hit output/context limits and encourage compression.
7. Require the drafter to report the source slice hash and first/last timestamps, not merely the intended range.

## Main verification gate

After return, Main must:

- recompute the output hash;
- read the actual first and last 30–80 lines;
- compare their topics with the timestamped source slice boundaries;
- check that adjacent range drafts neither duplicate nor skip source boundary text;
- compare total body character count with transcript-close baseline drift thresholds.

Do not infer scope correctness from a successful subagent status or plausible metrics.

## Failure handling

If a draft crosses its source boundary:

1. Move it to `body/obsolete/` with a suffix such as `_scope_invalid.txt`.
2. Never use it as partial source material or try to cut it by guessed body line numbers.
3. Re-extract smaller timestamped slices from the immutable merged ASR.
4. Regenerate only those slices.
5. Keep the invalid artifact and hash for audit, but exclude it from integration globs.

## Why this matters

A scope-invalid body can still pass every superficial check—UTF-8, no timestamps, 27-character maximum, no periods, and valid SHA. Only physical source containment plus opening/ending content inspection proves the requested time range was honored.
