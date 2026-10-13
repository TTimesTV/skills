# YouTube clip archive: Obsidian + Google Drive

Use this workflow when Hermes cuts a YouTube segment for a TTimes production and the result should remain searchable and reusable.

## Architecture

```text
YouTube URL = immutable source reference
Google Drive = verified relevant candidate clips, including not-yet-selected materials
Obsidian = request, source times, decisions, provenance, Drive link, reuse history
```

For this user, TTimes production records belong under the top-level Obsidian root `50_TTimes`, not `30_Finance`. Keep existing canonical source notes where they already live; link them from `50_TTimes` rather than bulk-moving or duplicating them.

The global entry point is:

```text
50_TTimes/TTimes 홈.md
50_TTimes/클립 라이브러리.md
```

## Minimum clip record

- deterministic `clip_id`
- YouTube URL and video ID
- official source title and channel
- user's cut request
- exact source IN/OUT
- actual downloaded/rendered IN/OUT when handles differ
- scene purpose and selection reason
- local output path
- Google Drive file ID and `webViewLink`
- file size, duration, SHA-256
- upload read-back size and MD5
- related project and prior-use history
- status: `pending_media_recovery`, `verified_local`, or `verified_drive`

Never infer missing source times from the clip duration. Ask one short clarification only when the exact source interval or target project cannot be recovered; otherwise execute without requiring the user to restate an implementation brief.

## Safe procedure

1. Resolve the YouTube video ID and existing canonical source note.
2. Cut the requested segment; retain handles only when the editing need justifies them.
3. Run `ffprobe`; require a playable stream and positive duration.
4. Compute SHA-256 and register the local artifact in the ledger and Obsidian.
5. Upload only verified media to the app-owned Drive folder.
6. Read back Drive size, MD5, file ID, and `webViewLink`.
7. Mark `verified_drive` only after local/remote size and MD5 agree. Selection status (candidate/selected/used) is independent of integrity status. Archive relevant acquired candidates before PD approval; never delete solely because they were not selected.
8. Regenerate `50_TTimes/클립 라이브러리.md` and verify unique clip IDs and valid source-note links.

## Google Drive permission boundary

Use a dedicated OAuth token with:

```text
https://www.googleapis.com/auth/drive.file
```

This permits access only to files created by the app or explicitly opened for it. Do not reuse a broad full-Drive token for the clip library. Do not implement delete, trash, public-share, or permission-changing commands.

OAuth scope is only one safety layer: the connector itself must expose only create/list/get/upload operations needed by this workflow.

## Failure states

If the local file is missing, unplayable, or a cloud placeholder:

- preserve source/request metadata as `pending_media_recovery` when useful;
- record no verified media SHA for the unavailable underlying clip;
- do not upload it;
- replace the same ledger item after recovering a playable file and exact times.

Do not report a pending metadata record as a completed Drive archive.

## Obsidian link rule

Generate vault-root-relative wiki links when the index and canonical source live in different top-level folders:

```text
[[30_Finance/.../canonical source note|Source title]]
```

A path relative to `50_TTimes` can silently lose or break the link. Verify the rendered link target after moving the index.

## Completion gate

- clip ledger has no duplicate IDs;
- source URL parses to the recorded video ID;
- verified media passes `ffprobe` and positive-duration checks;
- Drive read-back size and MD5 match;
- Obsidian global index is under `50_TTimes`;
- canonical source note link resolves;
- no delete/share/permission operation occurred.
