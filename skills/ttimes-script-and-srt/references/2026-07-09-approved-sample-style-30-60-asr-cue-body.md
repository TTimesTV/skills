# Approved sample style 30~60 existing-ASR cue-body conversion

Session pattern: user asked `승인된 샘플 스타일로 30~60분 ASR을 TTimes 말자막 cue body로 분절하고 파일로 저장하라`.

## Durable workflow lesson

This is a fast existing-ASR chunk task, not a full SRT/ASR/subagent rebuild.

1. Infer the existing project workspace from nearby prior work when clear; for the Kim Jihyun sync project the inputs were:
   - `redraft/asr_parts/part_30_40_asr.txt`
   - `redraft/asr_parts/part_40_50_asr.txt`
   - `redraft/asr_parts/part_50_60_asr.txt`
2. Combine the requested range into one cue-body file, e.g. `redraft/parts/part_30_60_caption_body.txt`.
3. Apply the approved sample style:
   - cue body only: no timestamps, no indices, no markdown, no report unless asked
   - transcript-close minimal correction, not summary or broad rewrite
   - TTimes spoken-caption segmentation with small-sentence readability
   - keep technical terms normalized: `AI`, `챗GPT`, `제미나이`, `NotebookLM`, `젠스파크`, `클로드`, `퍼플렉시티`, `바이브 코딩`, `에이전트`, `GPU`, `NPU`, `HBM`, `데이터센터`, `반도체 피크`, `캐즘`
   - preserve the user's approved meaning-first feel, but keep lines comfortably inside the box
4. Mechanical validation used in the session:
   - non-empty line count
   - blank line count should be 0
   - max visible length
   - counts over 25 and over 27
   - no standalone object/topic fragments such as `AI를`, `분들도`, `이야기를`, `인사이트를`
   - no isolated adhesive cue such as `그래서`, `근데`, `그리고`, `그러면`, `다만`, `하지만`, `그러니까`, `이렇게`, `그렇게`, `그런데`
   - scan very short cues and manually allow only true replies/emphasis such as `네`, `맞아요`, `그렇죠`, `저는`
5. If a first pass is over-fragmented, a conservative adjacent-merge pass is useful, but inspect and split back at completed thoughts, Q/A turns, discourse transitions, and predicate boundaries. Do not chase maximum packing.
6. Final response should be short: file path and validation stats. The user asked to save a file, not to receive a long process report.

## Session outcome profile

Final file: `PROJECT_ROOT/part_30_60_caption_body.txt`

Validation profile:
- cue-body lines: 1063
- blank lines: 0
- max visible length: 24
- >27 chars: 0
- >25 chars: 0
- standalone fragment checks: 0
- isolated adhesive cue checks: 0
- suspicious short cue checks: 0

## Pitfalls noticed

- Automated short-line merging can create over-packed lines like `챗GPT하고 그동안 대화했던 창이 있죠 거기 가서` or combine speaker-turn fragments. Split these back even if under 27 when readability suffers.
- ASR numeric corrections can be semantically risky. In this session the ASR had `4755조`, `5000조`; do not silently normalize large numbers to a more plausible value unless the source/context proves it. Preserve transcript-close numbers or flag uncertainty.
- If the user says `승인된 샘플 스타일`, avoid re-litigating the style or starting a full 95-point SRT workflow. Produce the cue body file directly and validate mechanically.
