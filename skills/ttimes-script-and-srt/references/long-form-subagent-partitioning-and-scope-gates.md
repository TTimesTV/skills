# Long-form bounded drafting and review partitioning

## Why this exists

A 57:30 Korean technical interview exposed two distinct scope/timeout failures that can look successful from subagent summaries:

1. A bounded drafter received both a timestamped raw transcript and an unbounded timecode-free baseline. It ignored the requested range, continued well beyond the boundary, and still reported the requested range as complete.
2. One source/term/number reviewer was asked to audit the full 57:30 candidate plus ASR, captions, glossary, audio, and web evidence. It exhausted the 600-second budget without a report.

## Durable operating rule

### Drafting

- Physically extract exact timestamped source slices before delegation.
- Prefer 10-minute slices for a 40–60 minute technical interview.
- Give the drafter only its slice plus glossary and correction ledger. Never include a full baseline or full raw transcript in the same brief.
- Save each slice hash and first/last ASR timestamp in a manifest.
- Verify actual output opening and ending text. Do not trust the reported range.
- Quarantine scope-invalid drafts under `obsolete/`; never splice them into the final body.

### Review

For a 50+ minute candidate near 1,500–2,000 cues:

- Freeze one content-addressed candidate and keep that same hash unchanged across all review partitions.
- Split source/term/number review into contiguous windows of at most about 30 minutes, preferably aligned with pre-extracted source slices.
- Split segmentation review into roughly 900–1,000-cue responsibilities; assign the seam explicitly.
- If concurrency limits require multiple batches, do not edit the candidate between batches. They are one review generation on one hash.
- For source review, prohibit broad web research inside the timed audit. Give the reviewer local captions, glossary, ledger, targeted ASR clips, and exact audio; Main handles any remaining external verification separately.
- Require exact current text, source timestamp/evidence, and minimal replacement. Read the full report: async headline summaries can invert a from/to correction even when the saved report is correct.

## Main adjudication for ambiguous audio

- A reviewer label such as `canonical` is not enough to override spoken evidence.
- Conflict order remains: exact cut audio / targeted clip ASR → approved transcript → verified correction ledger → readable minimal repair → reviewer preference.
- Re-ASR only narrow high-risk spans (names, numbers, contract direction, corrupted causal clauses) with a second model/configuration.
- When two ASR runs agree on an awkward spoken phrase, preserve it unless syntax/context supplies strong evidence for a recognition error.
- Record repaired text and evidence once; later reviewers should treat that ledger decision as fixed.

## Acceptance gate

Do not integrate until every partition has returned or been explicitly rerun. Then apply all accepted findings in one batch, rerun deterministic body audits, freeze a new hash, and use one bounded regression verifier rather than restarting an unbounded review loop.
