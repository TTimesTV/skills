# Source Media → TTimes Dubbing Cue Workbook

Use this mode when the user provides only a video/audio/YouTube source and expects the assistant to create the same dubbing-cue structure that ElevenLabs Dubbing Studio would normally export.

## Output schema

Default reference workbook schema:

```text
speaker,start_time,end_time,transcription,edited_transcription,english_translation
```

Field meanings:

- `speaker`: mapped person name, not anonymous diarization label;
- `start_time`, `end_time`: exact source/published-cut timeline;
- `transcription`: immutable raw ASR draft for audit;
- `edited_transcription`: conservative Korean correction used for translation;
- `english_translation`: natural spoken English fitted to the cue window.

For a legacy five-column Studio import, derive:

```text
speaker,start_time,end_time,transcription,translation
```

using `edited_transcription → transcription` and `english_translation → translation`. Never discard the six-column audit workbook.

## Reference distribution

The supplied production reference contained:

- 83 cues;
- 2 speakers;
- minimum 0.965 s;
- median 13.260 s;
- mean 13.444 s;
- maximum 24.980 s;
- no cue at or above 25 s;
- short cues mainly represented reactions or interruptions.

Validated source-only test on `AhAvCBC9JXE`:

- source duration 883.612 s;
- 2 diarized speakers;
- 116 raw acoustic turns;
- 78 final dubbing cues;
- median 12.160 s;
- mean 11.376 s;
- maximum 23.760 s;
- immutable mismatch 0;
- English hard/soft overfit 0 after short-reaction handling.

These are calibration evidence, not universal quotas.

## Artifact chain

Preserve each stage independently:

```text
source media + metadata + SHA-256
→ exact 16 kHz mono analysis WAV
→ raw anonymous diarization JSON
→ raw ASR segments and clips
→ speaker-mapping evidence
→ dubbing-cue segmentation plan
→ Korean correction/English translation ledger
→ six-column XLSX + CSV
→ QA JSON
```

Never overwrite raw diarization or ASR with the corrected candidate.

## Speaker diarization and mapping

- Diarization labels are acoustic clusters, not names.
- Map clusters to names only from introductions, stable interviewer/guest roles, title/outro, and visible/audio evidence.
- Preserve short interruptions and questions as separate cues.
- Treat overlapping clusters as review candidates. They can represent real crosstalk, duplicated acoustic detection, music, or boundary smearing.
- Do not assign both overlapping cues the same words merely because an automatic caption display spans both windows.

Required stack for this user:

```text
MLX Whisper transcription (local)
→ `pyannote/speaker-diarization-community-1` (local)
→ same-speaker merge plan
→ targeted MLX Whisper re-transcription on low-confidence names/numbers/overlaps (local)
→ GPT Sol Korean correction and English translation
```

Do not use Qwen3-ASR or another local LLM for transcription, correction, or translation unless the user explicitly overrides this requirement for that job. A context glossary is supporting evidence, not permission to force a term into the transcript.

## Dubbing-cue segmentation contract

These are generation/editing units, not reading subtitles.

1. Split at every confirmed speaker change.
2. Keep a continuing speaker in relatively long, coherent cues rather than splitting every sentence.
3. Hard maximum: less than 25.0 seconds.
4. Practical center: roughly 10–15 seconds for technical exposition.
5. Merge consecutive same-speaker turns when:
   - no other speaker intervenes;
   - gap is normally no more than about 0.8 seconds;
   - merged duration remains under 25 seconds;
   - the boundary does not hide a meaningful pause or topic pivot.
6. Preserve sub-3-second reactions, acknowledgments, questions, and interruptions when they are genuine.
7. For an over-25-second acoustic turn, split first at silence or clause boundary. Even time slicing is only a provisional fallback and remains `BOUNDARY_CHECK` until audio review.
8. Do not move speech into a neighboring cue merely to make English easier.
9. Cue timestamps should cover actual speech, not caption display duration.
10. Intro teasers, main interview, and outro stay on the same published timeline unless the requested deliverable explicitly removes them.

## Transcription and correction

- Use ASR to create `transcription`; do not invent a cleaned script first.
- Correct only high-confidence ASR errors in `edited_transcription`.
- Automatic YouTube captions may be retained as independent secondary evidence, never pasted as unquestioned truth.
- Preserve hedges, repetitions, self-repairs, modality, and unfinished speech.
- Verify proper nouns, model names, numbers, and technical terms with audio plus authoritative spelling when possible.
- If two ASR passes agree on an awkward phrase and audio remains unclear, preserve it and mark low confidence instead of rewriting it into smooth Korean.

## Translation fit

- Translate `edited_transcription`, not raw ASR.
- Preserve every fact, number, qualifier, question, and incomplete ending.
- Prefer natural spoken US English, not subtitle compression.
- Preferred density for ordinary cues: no more than about 2.9 words/s.
- Hard ceiling for ordinary cues: 3.2 words/s.
- Sub-2-second reactions/fragments are judged by natural delivery, not prose WPS thresholds.
- Real TTS duration remains the final fit test.

## Workbook construction

- Preserve exact six-column order.
- Use real Excel time values with `[h]:mm:ss.000` formatting in XLSX.
- For CSV, use deterministic `HH:MM:SS.mmm` timestamps and UTF-8 with BOM when Korean Excel compatibility matters.
- Freeze the header row, enable filters, wrap long text, and keep one cue per row.
- Do not add internal confidence/notes columns to the production six-column sheet. Put them in QA JSON.

## Blocking QA gates

- exact output header and column order;
- all cue IDs accounted for exactly once in the internal ledger;
- named speaker on every cue;
- monotonic valid time ranges and `end > start`;
- every cue under 25 seconds;
- non-empty raw Korean, edited Korean, and English;
- no embedded newlines in production cells;
- no immutable speaker/time mismatch after correction/translation;
- no unexplained duplicate text across overlapping cues;
- no ordinary cue above the English hard-fit ceiling;
- XLSX and CSV both open and contain identical cue counts;
- source/output hashes recorded.

## Low-confidence handling

Do not block the entire workbook for one unclear fragment. Deliver the workbook only if:

- the ambiguous cue is explicitly listed in QA;
- its audio clip and competing ASR evidence are retained;
- no smooth replacement has been invented;
- the user can identify the exact row immediately.

The cue must be rechecked before paid TTS rendering or final publication.
