# Local dependency gates

This reference describes unavailable local dependencies. It is not an implementation of ASR, alignment, sync, or a layer renderer.

## Line-preserving SRT alignment

Status: `external_dependency` while the local `media-localization-workflows` skill and its alignment script are unavailable.

Required input:

- frozen body-only UTF-8 TXT, one cue body per non-empty line;
- word-timing JSON with a media duration and word/start/end records;
- an explicit overlap policy and media identity/hash.

Required output before this route can be marked complete:

- SRT whose joined cue bodies exactly match the frozen body under the agreed normalization;
- timing/structure validation report tied to the output hash;
- clear distinction between a mechanical sample and an approved-production result.

Do not use a remote ASR service, regenerate the body, or infer timing from text merely to bypass this gate.

## Synced cut DOCX

Status: `external_dependency` while the local synchronization workflow is unavailable.

Required input: approved cut source, cut MP3/video, speaker/timestamp requirements, source language, and any approved terminology ledger.

Required output: a DOCX/TXT using `[화자명 MM:SS]`, a source-faithful body paragraph, and a blank paragraph per block; include the source/cut timebase and a verification record. This is upstream of cue-body/SRT and screen composition.

## Editorial layers

For copy-only emphasis/explainer text, use `ttimes-editorial-copy`. For placement on an already synchronized approved source, use `ttimes-screen-composition`. If a request requires the missing `caption-layering-workflow` grammar or renderer, report `external_dependency`; do not invent an equivalent delivery format.
