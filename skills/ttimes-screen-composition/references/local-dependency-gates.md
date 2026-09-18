# Local dependency gates

This skill can consume an already synchronized, approved source. It does not create a sync artifact while `media-localization-workflows` and its related reference are unavailable locally.

## Synced cut DOCX gate

Status: `external_dependency`.

Before screen composition starts, provide:

- approved cut source plus the corresponding cut MP3/video;
- source language and required Korean translation policy when relevant;
- speaker/timestamp requirements and any approved terminology ledger.

The upstream result must contain blocks of `[화자명 MM:SS]`, a source-faithful body paragraph, and a blank paragraph. It must state the applicable source/cut timebase and include a verification record. A filename ending in `(자료)` is not evidence that this contract has been met.

Once that artifact exists, this skill may assess placement and editorial layers. Until then, do not substitute spoken-caption segmentation, a plain-text transcript, or a guessed media timeline for sync.
