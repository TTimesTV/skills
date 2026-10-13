> 실행 경로(2026-09-22): 전사·부분 재전사는 [ElevenLabs API + 기존 env](elevenlabs-runtime.md)를 따른다. 아래 사례의 청크 크기·과거 실행 결과는 현재 API 실행 지시가 아니다. 장편도 원본 업로드가 기본이며 확인된 누락 구간이나 서비스 제한이 있을 때만 분할한다.

# Local dependency gates

This reference describes unavailable local dependencies. It is not an implementation of ASR, alignment, sync, or a layer renderer.

## Line-preserving SRT alignment

Status: validate the actual alignment implementation against the conditions below; ElevenLabs word JSON is the timing input. A missing historical helper is not an ASR blocker.

Required input:

- frozen body-only UTF-8 TXT, one cue body per non-empty line;
- word-timing JSON with a media duration and word/start/end records;
- an explicit overlap policy and media identity/hash.

Required output before this route can be marked complete:

- SRT whose joined cue bodies exactly match the frozen body under the agreed normalization;
- timing/structure validation report tied to the output hash;
- clear distinction between a mechanical sample and an approved-production result.

Use ElevenLabs API for word timings. Do not regenerate frozen body text or infer timing from text merely to bypass validation.

## Synced cut DOCX

Status: implemented for this user's ordinary `싱크/워딩/클로바노트` request through the ElevenLabs Scribe v2 Speech-to-Text API.

Required input: exact source media, speaker/timestamp requirements, source language, and any approved terminology ledger.

Required output: a Word DOCX using bold `화자명 MM:SS` followed by a source-faithful long-form body paragraph for each speaker turn. Preserve raw ElevenLabs word-timing JSON, source/cut timebase, speaker mapping evidence, and a verification record internally. This is upstream of cue-body/SRT and screen composition.

Return `external_dependency` only when the request requires exact synchronization against a separately approved cut manuscript or a cut manifest whose transformations cannot be derived from the supplied final media.

## Editorial layers

For copy-only emphasis/explainer text, use `ttimes-editorial-copy`. For placement on an already synchronized approved source, use `ttimes-screen-composition`. If a request requires the missing `caption-layering-workflow` grammar or renderer, report `external_dependency`; do not invent an equivalent delivery format.
