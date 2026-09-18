# Part ASR → Gem1 최소윤문 → Gem2 말자막 분절 chunk workflow

## When this applies

Use this for requests like `part1 00~25분 ASR을 Gem1 최소윤문 후 Gem2 말자막 분절로 변환하고 파일로 저장하라` when the source ASR chunk and a Gem1/Gem2 brief already exist in the project workspace.

This is not the full YouTube/MP3 → ASR → aligned SRT workflow. It is a fast chunk conversion workflow whose deliverable is plain caption body lines only.

## Minimal workflow

1. Load the project brief if present, e.g. `gem1_gem2_brief.md`.
2. Read the specific ASR chunk, e.g. `chunks/part1_00-25_asr.txt`.
3. Produce Gem1 corrected text while staying transcript-close:
   - fix obvious ASR errors, spelling/spacing, particles, acronyms, proper nouns, numbers/units;
   - preserve colloquial wording, order, jokes, cut-edit fragments;
   - do not summarize or invent missing facts.
4. Apply Gem2 segmentation:
   - output cue body only, one cue per line;
   - no timestamps, numbering, markdown, tables, or speaker names unless requested;
   - target meaning-closed cues, not mechanical short fragments;
   - keep within the brief's hard visual rule, usually max 25 visible Korean chars for this user.
5. Save the result in the workspace under the existing convention, e.g. `park_style/agents/part1_00-25_captions.txt`.
6. Run a simple mechanical check:
   - line count;
   - blank count;
   - max/average visible length excluding spaces;
   - scan for known ASR-corrupted tech terms.
7. If useful, save a short report next to the caption file, e.g. `part1_00-25_report.md`, with counts, terms corrected, and caveats.

## Validation commands/patterns

Use a tiny Python check after writing the caption file:

```python
from pathlib import Path
p = Path('part1_00-25_captions.txt')
lines = p.read_text().splitlines()
def n(s): return len(s.replace(' ', ''))
print('line_count', len(lines))
print('blank_count', sum(1 for l in lines if not l.strip()))
print('avg_nospace', round(sum(n(l) for l in lines)/len(lines), 2))
print('max_nospace', max(n(l) for l in lines))
print('over_25', [(i, n(l), l) for i, l in enumerate(lines, 1) if n(l) > 25][:20])
```

Search/scan for common uncorrected ASR patterns in AI-chip videos:

- `HVM` → `HBM`
- lowercase `npu/gpu/llm` → `NPU/GPU/LLM`
- `팸립스` → `팹리스`
- `대악마/대학마` → `대항마`
- `앤스로픽` → `앤트로픽`
- `트레니엄/트레늄` → `트레이니엄`
- `인퍼렌시아/인퍼런시아` → choose one glossary spelling and keep consistent, usually `인퍼런시아`
- `필요사/퓨류사 AI` → `퓨리오사AI`
- `특세시장 공약` → `틈새시장을 공략`
- `단속회사`-like corruption in context → `단순 계산`

## Pitfalls

- Do not invoke the heavy 95-point/subagent/SRT timing workflow when the user only asks for a part ASR chunk converted to Gem1/Gem2 caption lines. The skill's full workflow remains valid for final SRT delivery, but chunk conversion should be lightweight unless the user explicitly asks for deep review.
- Avoid automatic over-merging. A file can satisfy max length while still sounding like unnatural concatenated subtitles. Merge only when the resulting cue remains a meaning-closed spoken-caption unit.
- Preserve edge/cut fragments at the part boundary. If the 25-minute cut ends mid-sentence, keep the trailing partial cue rather than inventing the continuation.
- For uncertain off-mic/opening banter, prefer transcript-close wording and note caveats in the report instead of aggressive reconstruction.
