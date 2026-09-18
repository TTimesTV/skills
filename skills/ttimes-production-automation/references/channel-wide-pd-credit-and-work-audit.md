# Channel-wide PD credit and work audit

Use when auditing every regular video in a channel for a named PD’s explicitly credited work, then downloading and evaluating every confirmed item.

## Scope lock

1. Freeze the authoritative channel tab before collecting metadata.
2. Keep regular Videos, Shorts, and Streams as separate inventories.
3. If the user says Shorts are out of scope, every downstream script must filter against the frozen regular-video ID set—not merely ignore Shorts in the final prose.
4. Report the invariant explicitly:

```text
regular-video total = metadata matched + access unavailable + unresolved
```

Out-of-scope metadata may remain on disk, but it must be excluded from candidate ledgers, completion counts, hashes, rankings, and reports.

## Evidence ladder

Confirm only explicit role evidence:

- `D1`: description line contains the role and explicit identity, e.g. `자료 ... 박성수 PD`.
- `D2`: ending-credit screen visibly links `자료` and the named PD in the same credit entry/block.
- `D3`: opening or in-video role screen does the same.
- `HOLD`: name only, ambiguous title, RA credit, OCR fragments, or role/name in unrelated blocks.

OCR may nominate candidates, never auto-confirm them. Preserve the frame and manually adjudicate the visible credit block. Do not infer contribution from era, style, recurring guests, or graphics.

## Role-specific attribution

- `자료`: score material planning only; emphasis-caption fields are `확인 불가·총점 제외`.
- `글·자료`: do not reinterpret `글` as emphasis-caption ownership.
- `자막·자료` or `자료·자막`: include emphasis-caption selection and wording.
- Joint credits: evaluate the video-level joint result and prohibit object-by-object attribution to one person.

Recommended official formulas:

```text
material-only = (material_selection×25 + speech_sync×20 + evidence_explanation×20) / 65
material+captions = material_selection×.25 + speech_sync×.20 + evidence_explanation×.20 + emphasis_selection×.20 + emphasis_wording×.15
```

Keep all component scores on a 100-point scale even when the report also shows raw 25/20/20 points.

## Full-video review contract

For every confirmed video:

1. Download the actual video.
2. Verify whole-file decode and hash.
3. Generate chronological aids: full CC, fixed-interval frames, scene-change frames, contact sheets.
4. Inspect the entire timeline; aids do not authorize start/middle/end sampling.
5. Record title, URL, upload date, credit evidence, role scope, component scores, total, timestamped strengths/weaknesses, and reusable PD-side improvements.
6. Explicitly exclude speaker quality and video-editor/designer implementation.
7. Run structural and formula QA, but never treat QA alone as proof that the full video was reviewed.

## Resumable ledgers

Persist separately:

- frozen channel inventory
- metadata completeness and access-unavailable ledger
- confirmed and held credit ledgers
- download/package state
- per-video reports
- score ledger and QA result
- opening/ending OCR candidate logs and evidence frames
- checksums

Rebuild candidate ledgers whenever new metadata arrives. Do not let stale candidate counts survive a metadata refresh.

## Robust batch execution

- Process downloads/packages in bounded batches; do not materialize hundreds of frame packages at once.
- A video ID can begin with `-`. Pass it as `--id=<video_id>` rather than `--id <video_id>` so argparse does not interpret it as an option.
- Treat `--ignore-errors` exit status as insufficient. Completion is determined by ID-set difference and categorized access failures.
- Mark terminal access states such as members-only/private/deleted/region-blocked separately; retry transient failures only.
- **Never convert repeated `ACCESS_FAILED` into completion.** Only a successful screen check or a directly verified terminal access state closes an ID. Keep transient failures pending and schedule them after never-attempted IDs so they cannot starve the main queue.
- For thousands of opening/ending checks, use small checkpoint batches and append one JSONL record per attempt. Count completion by the latest terminal status per ID, not raw record count or unique attempted count.
- Protect scheduled and manual scan ticks with an atomic lock. Overlapping `yt-dlp --download-sections` jobs can race on the same `.part` path, producing false `No such file` failures and duplicate records.
- Do not manually trigger a scheduled tick unless the same lock covers both paths. A successful scheduler status proves only that the tick script exited successfully; verify that the terminal-ID count actually increased.
- Separate download failure classes: `.part` path races indicate concurrency, while FFmpeg 403 on a section URL may require a fresh extraction/retry. Neither is evidence that the video lacks a credit.
- If concurrent frame generation causes file-descriptor pressure, stop launching new batches, let bounded work close handles, then resume. The durable rule is bounded concurrency, not that the tool is broken.

## Ledger and validator synchronization

- Rebuild the review ledger from authoritative files rather than incrementally trusting stale rows: confirmed inventory + video existence + package manifest + report existence + QA status.
- Mark `전편검토완료` only when the report exists **and** deterministic QA passes.
- Keep report-section vocabulary machine-stable (for example `잘된 지점(강점)` and `아쉬운 지점(약점)`). If a report is substantively valid but fails only because a heading synonym differs, normalize the heading and rerun the full validator; do not alter scores or findings.
- After each batch, rerun score merge and role-aware validation against the confirmed-credit ledger. This prevents a report from assigning emphasis captions to a material-only credit.

## Final completion gate

Do not publish intermediate counts as final. Completion requires:

- authoritative regular-video population reconciled
- metadata or terminal access state for every ID
- description plus opening/ending checks completed for non-confirmed accessible videos
- OCR candidates manually adjudicated
- all confirmed videos fully reviewed and QA-passed
- ranking, yearly averages, recurring strengths/weaknesses, development trajectory, top 10, and improvement-needed 10 generated from the final score ledger
