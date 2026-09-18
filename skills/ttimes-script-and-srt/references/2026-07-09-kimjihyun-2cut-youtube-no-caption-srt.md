# 2026-07-09 김지현 2편 컷 — YouTube no-caption TTimes SRT workflow

## Trigger

User provided `https://youtu.be/8w29DoJ1dn0` with `/plan`, then approved execution. Video metadata:

- Title: `김지현 2편 컷`
- Channel: `티타임즈TV`
- Duration: ~27:10
- YouTube captions: none (`has no automatic captions`, `has no subtitles`)

## What worked

1. Create a dedicated workdir under `~/.hermes/work/<date>_<slug>/` with `source/`, `asr/`, `draft/`, `redraft/`, `review/`, `final/`, `scripts/`.
2. Download audio with `yt-dlp -x --audio-format mp3` and verify duration with `ffprobe`.
3. Run MLX Whisper directly on the full 27-minute MP3 with word timestamps:

```bash
mlx_whisper source/<audio>.mp3 \
  --model mlx-community/whisper-large-v3-turbo \
  --language ko \
  --word-timestamps True \
  --output-format json \
  --output-dir asr/
```

4. Validate ASR JSON before editing: segment count, word count, monotonic word timestamps, last word close to source duration.
5. Build a transcript-close caption body, then postprocess into ~16-char average cue bodies with max 27 chars, no final periods, and living subtitle punctuation (`?`, quotes when useful).
6. Patch only high-confidence ASR/term errors. Examples from this session:
   - `웹도독` → `웩더독`
   - `엔스트로픽/엠스트로픽/엔스로픽` → `앤트로픽`
   - `오픈클로` in context of OpenAI → `오픈AI`
   - `젠슨왕` → `젠슨 황`
   - `제번스/재벌스` → `제본스`
   - `하이퍼스켈러` → `하이퍼스케일러`
   - `콜러서스` → `콜로서스`
   - `MP와 같은 하드웨어` → `NPU와 같은 하드웨어`
   - `마이크로는` in Samsung/Hynix/Micron list → `마이크론은`
   - `원가 확신도` → `원가 혁신도`
   - `어플리케이션` → `애플리케이션`
   - `멈추되니까` → `멈추라니까`
   - `슈퍼 의뢰 자세` → `슈퍼 을의 자세`

7. Align final caption body to MLX word timestamps with normalized character-stream fuzzy matching, not proportional time mapping. Validate:
   - SRT cue count == caption body line count
   - SRT bodies exactly equal caption body
   - overlap 0 / nonpositive 0
   - over 27 chars 0
   - final periods 0
   - low fuzzy match 0

## Important lesson: subagent timing

For this user's TTimes 말자막 workflow, subagents are mandatory when invoked in the plan. Do **not** mark `subagent review` as completed or imply their findings were integrated if the background results have not arrived. Either:

- wait for the subagent summaries and integrate high-confidence fixes before final delivery, or
- clearly label the delivery as `Main 검증 선납품본` and say a later `v2` may follow after subagent findings.

Never silently convert an unfinished subagent review into a completed checklist item.

## Quality caveats

- Structural validity is not enough; read beginning/middle/end SRT samples for segmentation rhythm.
- Keep short reaction cues (`왜?`, `맞아요`, `그렇죠`) if they are real fast responses; do not force artificial duration by corrupting neighboring cue timing.
- Split >5s heavy cues into smaller meaning units, then rerun alignment.
