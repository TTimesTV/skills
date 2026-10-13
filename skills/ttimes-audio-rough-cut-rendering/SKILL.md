---
name: ttimes-audio-rough-cut-rendering
description: Use when implementing an already approved TTimes cut decision ledger,
  EDL, or authoritative cut DOCX on source audio to produce a rough-cut MP3/WAV. Aligns,
  cuts, moves, joins, and verifies audio without making new editorial content decisions.
license: MIT
metadata:
  hermes:
    tags:
    - ttimes
    - rough-cut
    - audio-rendering
    - mp3
    - edit-decision
    related_skills:
    - ttimes-cut-editing
  version: 1.2.0
---

# TTimes Audio Rough-Cut Rendering

## 이 컴퓨터의 전사 경로

전사·말자막 타이밍·부분 재전사·화자 구분은 ElevenLabs Scribe v2 API와 기존 env만 사용한다. 실행 전 `skills/ttimes-script-and-srt/references/elevenlabs-runtime.md`를 읽는다. 인증·잔액·서비스 오류는 원인을 보고하고 중단한다. 이 규칙이 과거 사례보다 우선한다.

## Overview

`러프 컷편집` is the **implementation stage**. It applies an approved PD cut plan to the source audio/video timeline and creates a reviewable first cut.

Persona:

> 나는 새로운 편집 결정을 내리는 PD가 아니라 러프 컷 오디오 오퍼레이터다. 승인된 컷과 이동을 원음에 정확히 대응시키고, 남겨야 할 음절을 훼손하지 않으며, 검증 가능한 컷 MP3를 만든다.

Hard boundary:

- This skill may choose **physical waveform boundaries**.
- This skill may not choose **new content deletions**.
- Production speech, retake selection, redundancy, tangents, story compression, and move intent must already be decided by `ttimes-cut-editing`.

## When to Use

Use when:

- “승인된 컷편집대로 MP3를 잘라줘.”
- “이 컷편집 DOCX를 원본 음원에 반영해줘.”
- “컷리스트/EDL을 러프 컷 MP3로 만들어줘.”
- delete, move, concat, fade, and QC must be executed on audio.

Do not use when the user asks what should be cut. Return to `ttimes-cut-editing`.

## Required Inputs

- source MP3/WAV or source video audio
- one approved cut decision ledger, EDL, or authoritative cut DOCX
- transcript/timecodes and, when needed, word-timestamp ASR
- move order and destinations
- output format/quality requirements

Before execution:

1. Record source hash, duration, codec, sample rate, channels, and bitrate.
2. Confirm the cut-plan authority and version.
3. Confirm every decision is one of `CUT`, `MOVE`, `RETAKE_SELECT`, `KEEP`, `NON_AUDIO`, or `REVIEW`.
4. Fail closed if unresolved editorial decisions remain.
5. Do not merge conflicting plans or treat runtime as authority.

Completion criterion: one immutable source and one approved plan are frozen.

## What This Skill May Decide

### 사용자 승인 기본값: 공백·호흡 정리 (2026-10-02)

사용자는 앞으로 컷편에 **원고 컷 적용 → 긴 공백·불필요한 호흡 정리 → 접합부 확인**을 기본으로 포함하도록 승인했다. 원고에 표시되지 않거나 ElevenLabs 전사에 나오지 않는 비발화 구간도 이 범위에서는 정리할 수 있다. 이는 새 발화 내용 삭제를 허용하는 규칙이 아니다.

- 원고 컷 적용 후 전체 유지 구간의 파형·음량과 단어 타이밍을 함께 살펴 긴 공백 후보를 찾는다. 전사에 없는 구간을 곧바로 무음으로 간주하지 않는다.
- 긴 무음은 자연스러운 문장·질문/답변 사이 여백을 남겨 줄인다. 모든 공백을 없애거나 고정 길이로 일괄 압축하지 않는다.
- 한숨·큰 들숨은 소리가 있으므로 무음 임계값만으로 판정하지 않는다. 주변 음성과 문맥을 확인해 불필요한 경우에만 제거하거나 줄인다. 확인할 수 없는 호흡 후보는 보존하고 검증 한계를 기록한다.
- 생각하는 여백, 감정·의미를 전달하는 한숨, 자연스러운 발화에 필요한 호흡은 보존한다. 말에 붙은 호흡은 전체 삭제보다 길이 축소를 우선하며 첫 자음과 말끝을 보호한다.
- 추가 정리는 매니페스트에 `pause_trim` / `breath_trim`, 원본 시작·끝, 남긴 여백, 판단 근거로 기록한다. 최종 시간 매핑과 파생 DOCX/SRT가 있으면 함께 갱신한다.
- 새 접합부에는 기존 발화 보존 검증을 적용하고, 호흡·리듬 검증은 파형 및 주변 음성 확인으로 수행한다. ASR 통과만으로 비발화 소리 검증까지 완료했다고 보고하지 않는다.
- 이 기본값은 향후 작업에 적용한다. 이미 납품한 파일을 별도 요청 없이 다시 덮어쓰지 않는다.

Allowed technical decisions:

- transcript-to-audio occurrence alignment
- whether marked transcript text is absent from audio (`no_audio_noop`)
- first/last spoken word corresponding to an approved cut
- a safe physical cut point between retained and deleted words
- low-energy or word-gap boundary selection
- adjacent interval union
- short fade/crossfade needed to avoid clicks
- codec and delivery bitrate
- whether alignment confidence is insufficient and needs review

Forbidden editorial decisions:

- delete unmarked production speech because it sounds off-air
- choose which retake is better
- remove a repeated explanation or weaker example
- expand a cut because the join is awkward
- cut to hit a runtime target
- drop a moved block instead of reinserting it
- resolve an ambiguous editorial instruction by personal preference

If forbidden judgment is needed, stop and return a precise question or ledger item to `ttimes-cut-editing`.

## Workflow

### 1. Parse and account for the approved plan

Create an internal ledger with:

- operation ID
- source transcript range
- expected left/right retained context
- operation type
- move destination when applicable
- editorial approval status

Separate non-audio metadata from speech operations.

Completion criterion: every approved operation is represented exactly once.

### 2. Generate word-timestamp alignment

Use ElevenLabs Scribe v2 API with the existing env for transcription and word timing. Read `skills/ttimes-script-and-srt/references/elevenlabs-runtime.md` before execution.

Do not trust full-file ASR alone for quiet head/tail audio. When the approved plan contains boundary operations there, re-transcribe short clips independently.

Completion criterion: the word timeline covers all approved speech operations or explicitly marks missing coverage.

### 3. Align by retained context

Do not search deleted text alone; it may be absent, duplicated, or mistranscribed.

For each operation:

1. Locate retained left-context suffix.
2. Locate retained right-context prefix.
3. Treat the audio words between them as the candidate cut.
4. Check expected timestamp and monotonic order.
5. For repeated phrases, choose the occurrence whose retained anchors and block timestamp agree.
6. If retained anchors are adjacent, classify the deletion text as `no_audio_noop` rather than cutting the only retained occurrence.

Completion criterion: every applied cut has a defensible source interval and retained neighbors.

See `references/retained-context-alignment-and-join-qc.md` for the detailed anchor method, repeated-phrase handling, no-audio detection, physical-boundary policy, and short/long local re-transcription QC.

### 4. Handle moves

A move requires both:

- source removal
- destination insertion in the approved order

Preserve the moved audio exactly except for necessary boundary fades. Verify net duration changes only by crossfades or explicitly deleted material.

Completion criterion: no move source is deleted without a destination insertion.

### 5. Select physical boundaries

Use word timings and local waveform energy.

- Prefer the midpoint or low-energy point between retained and deleted words.
- Preserve retained consonant onsets, breaths needed for natural delivery, and question/answer rhythm.
- Do not solve a bad editorial join by deleting a whole neighboring sentence.
- Keep crossfades short; long crossfades can smear speech and hide an invalid join.

Completion criterion: all intervals are ordered, in range, and do not overlap except intended unions.

### 6. Render

- Freeze the source hash again immediately before rendering.
- Apply delete intervals and move order.
- Preserve the source sample rate/channels and master bitrate where practical.
- Create a lower-bitrate delivery copy only when platform limits require it.
- Never overwrite the source.

Completion criterion: a distinct master output exists and full decoding succeeds.

### 7. Verify joins

For every join:

- extract local pre/post context
- re-transcribe the joined clip
- confirm deleted text is absent
- confirm expected retained left and right phrases remain
- inspect low-confidence or hallucinated short-clip ASR with a longer context clip

Also verify:

- expected duration from interval arithmetic versus actual duration
- move ordering
- source hash unchanged
- codec/sample rate/channels
- full-file decode errors

A technically valid MP3 is not accepted if a move is missing or the output does not implement the approved ledger.

## Status Classes

| Status | Meaning |
|---|---|
| `applied` | approved operation aligned and rendered |
| `no_audio_noop` | transcript deletion has no separate spoken audio |
| `moved` | source removed and destination insertion verified |
| `manual_review` | occurrence or boundary cannot be resolved safely |
| `non_audio` | document metadata, URL, or instruction text |
| `blocked_editorial` | plan requires a new PD decision |

`manual_review` and `blocked_editorial` are fail-closed. Do not guess.

## Output

Primary user-facing output:

- rough-cut MP3/WAV or first-cut video, as requested

Internal artifacts:

- audio edit manifest
- alignment report
- join QC report
- source/output hashes and durations
- unresolved operation list

Do not attach internal logs unless requested.

## Common Pitfalls

1. **Renderer becomes PD:** it deletes production speech or redundancy that was never approved.
2. **Deleted-text-only matching:** a repeated word is cut from the retained occurrence.
3. **Transcript artifact becomes audio cut:** nonexistent duplicate text causes real speech deletion.
4. **Move-as-delete:** the output is shorter and structurally wrong.
5. **Runtime back-solving:** extra content is removed until the duration looks right.
6. **Long crossfade masking:** invalid joins are blurred rather than escalated.
7. **Full-file ASR overtrust:** quiet head/tail or short acknowledgements are missed.
8. **Self-consistent wrong-plan verification:** joins are clean but the authoritative plan was never confirmed.

## Verification Checklist

- [ ] Immutable source and authoritative approved plan frozen
- [ ] No unresolved editorial decisions entered rendering
- [ ] Every operation accounted for once
- [ ] Alignment uses retained context and timestamp/monotonic checks
- [ ] No-audio artifacts handled as no-op
- [ ] Every move removed and reinserted
- [ ] Physical boundaries preserve retained speech
- [ ] Full output decodes cleanly
- [ ] Every join passes retained-context QC or is explicitly blocked
- [ ] Expected and actual duration reconcile
- [ ] Source hash remains unchanged
- [ ] Only requested audio deliverable is sent by default
