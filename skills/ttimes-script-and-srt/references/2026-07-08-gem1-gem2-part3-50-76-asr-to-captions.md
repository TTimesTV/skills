# Gem1/Gem2 ASR → 말자막 변환: part3 50~76분 세션 교훈

## Context

User asked: `part3 50~76분 ASR을 Gem1 최소윤문 후 Gem2 말자막 분절로 변환하고 파일로 저장하라.`

The expected shape was **not** full 95-point SRT generation or timing work. It was an intermediate artifact: plain-text cue bodies only, produced from an existing ASR chunk with the user's Park/Gem workflow.

Input in the session:

- `park_style/chunks/part3_50-76_asr.txt`
- Local brief: `park_style/gem1_gem2_brief.md`

Output produced:

- `park_style/agents/part3_50-76_captions.txt`
- Report: `park_style/agents/part3_50-76_report.md`

## Workflow that worked

1. Load the local Gem1/Gem2 brief if present.
2. Read the ASR chunk.
3. Gem1 pass: do only minimal corrections:
   - obvious ASR errors
   - proper nouns / product names / company names
   - numbers and units
   - spacing, particles, light grammar repair
   - light filler trimming only when clearly redundant
4. Gem2 pass: write **cue body only**, one cue per line:
   - no timestamps
   - no numbering
   - no markdown
   - no blank lines
5. Validate mechanically:
   - line count
   - empty-line count
   - max visible length excluding spaces
   - residual obvious ASR terms
6. Save a short report when the task is a chunk handoff, especially noting uncertain ASR regions.

## Important preference / scope lesson

When the user explicitly says `Gem1 최소윤문 후 Gem2 말자막 분절`, do **not** automatically invoke the full SRT pipeline obligations such as timing refinement, extensive peer review, or 95-point delivery framing unless the user asks for SRT or final delivery. This request class is an intermediate caption-text production workflow.

Keep the response concise: file paths + validation stats + key caveats.

## Segmentation lesson

A simple automated merge pass can improve average cue length, but it can also over-merge discourse boundaries. After any char-threshold merge, inspect representative ranges and split again at:

- speaker turns / reaction boundaries
- question boundaries
- discourse markers: `그러면`, `그런데`, `그래서`, `다만`, `그리고`, `근데`
- transitions from answer to new topic
- quoted speech or joke punchlines

In this session, an initial conservative draft was too short on average (~10 chars). A merge-threshold pass improved average length (~16 chars), but over-merged lines such as `그럼 아, 술을 마시면...` and `...국민성장펀드로부터 그러면...`. Manual split-back produced a safer final average (~14 chars) with max 24 visible chars.

## Useful validation target for this intermediate workflow

For plain Gem2 cue bodies from an ASR chunk:

- Max visible chars excluding spaces: <=25 preferred; 26~28 only if semantically necessary.
- Average visible chars: around 14~18 is acceptable; below ~12 suggests over-segmentation.
- Empty lines: 0.
- Residual term scan should include topic-specific ASR traps.

## Topic-specific ASR traps from this chunk

High-confidence corrections used here:

- `퓨리오스/필요사/프리오스 AI` → `퓨리오사AI`
- `리베리온/리벨룬/이베리언` → `리벨리온`
- `사표나` → `사피온`
- `TPO 모델` → `TPU 모델`
- `쿠다` → `CUDA`
- `그래프코` → `그래프코어`
- `시장 적용률` → `시장 점유율`
- `파트너실` → `파트너십`
- `우구` → `우군`
- `영무 개발` → `연구개발`
- `D2 FS/D2 SF` → `D2SF`
- normalize number/unit forms: `3000억 원`, `6400억 원`, `9000억 원`, `7000억 원`, `3~4조`, `80~90%`, `2~3년`

## Uncertain ASR handling

For ambiguous phrases, do not invent a polished replacement. Preserve the closest transcript-like expression and mention it in the report. Examples from this chunk:

- `테스트까지 갖고 왔는데` near 51:50 was uncertain but left as a minimal contextual repair.
- `주위 생산하고 이런 것들` near 54:38 remained close to ASR because the source was unclear.
- joke-like line `우군을 죽인다고 했네` was preserved as a likely conversational aside.
- `AIG` near 70:70 was corrected to `AI GPU나 메모리` based on local context, but should be treated as a caveated correction.
