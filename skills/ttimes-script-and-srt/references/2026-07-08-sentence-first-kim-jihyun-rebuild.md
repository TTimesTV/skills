# Sentence-first rebuild lesson: 김지현 AI 리더십 SRT (2026-07-08)

## Trigger

During a long MP3 → TTimes-style SRT task, the user rejected versions that satisfied length/lint but merged separate sentences/thoughts into one cue. The correction was explicit: **when a sentence/thought ends, usually move the next sentence/thought to the next cue**. This is not a timing limitation; the line-preserving aligner can rematch after the line count changes.

## Final workflow learned

For this user's long Korean spoken-caption jobs, the order should be:

```text
1. MP3/download/source verification
2. MLX Whisper ASR with word timestamps
3. transcript-close stable text, before caption packing
4. minimal correction only: ASR, particles, names, products, numbers
5. sentence/thought-ending first split
6. small-sentence readability + 접착어 protection
7. 25-char target / 27-char max adjustment
8. subagents as reviewers only
9. Main Hermes integrates high-confidence fixes
10. line-preserving MLX word-timestamp SRT rematch
11. validation
12. deliver only *_srt.txt unless asked otherwise
```

## Segmentation priority

```text
1. sentence/thought ending boundary
2. small-sentence readability: noun/target + verb/judgment/predicate
3. meaning closure
4. 접착어 protection
5. spoken rhythm
6. 25-char target / 27-char max
```

Do **not** merge separate complete sentences merely because the combined cue fits under 27 visible characters.

## Example patterns

Sentence-first split:

```text
안녕하십니까
안녕하십니까
```

Better than:

```text
안녕하십니까 안녕하십니까
```

Sentence/question split:

```text
아직 버전 아니에요?
아, 끝난 거 아니에요?
```

Better than:

```text
아직 버전 아니에요? 아, 끝난 거 아니에요?
```

Preserve small-sentence units:

```text
소프트웨어나 이런 것 쪽으로 많이 다뤘었는데
주위 친구들도 너무나 전문가예요
```

Avoid predicate/adverb stranding:

```text
소프트웨어나 이런 것 쪽으로 많이
다뤘었는데

주위 친구들도 너무나
전문가예요
```

## Subagent use

Subagents are mandatory for this class, but they must be reviewers, not final-script writers.

Good roles:

```text
A: proper nouns / numbers / product names
B: sentence-first readability / 접착어 / over-fragmentation
C: distortion / omission / ASR collapse
```

Bad pattern:

```text
subagent A writes part1
subagent B writes part2
subagent C writes part3
Main concatenates
```

This loses one editorial rhythm.

## Product/name notation learned

For Korean spoken subtitles, do not automatically English-normalize spoken product names. Use Korean forms when that matches the dialogue/user expectation.

```text
재미나이 / 재미나 / Gemini -> 제미나이
체치패티 / 챗집 PT / HHPT -> 챗GPT
크로드 / 클로우드 -> 클로드
퍼플레시티 / 퍼플렉스티 / 퍼블릭시티 -> 퍼플렉시티
노트북의 랩 / 노트북 LM -> NotebookLM
오픈 AI / 오픈클로 -> 오픈AI
```

Keep acronyms as acronyms:

```text
AI, GPU, NPU, HBM, LPDDR, D램, SMR, AWS, TSMC
```

User-specific correction in this session:

```text
김지연 / 김지원 -> 김지현
홍재희 / TTIM 중 -> 티타임즈 홍재의
```

## Validation targets from the successful sentence-first rebuild

The sentence-first rebuild changed the script from ~1650 cues to ~2032 cues. This is acceptable when it follows sentence/thought boundaries.

Mechanical checks to run:

```text
script lines == srt cues
SRT bodies == script lines
27-char overage == 0
sentence-final periods == 0
overlap == 0
nonpositive == 0
bad-term scan == 0 for known ASR variants
보호구 split lint == 0
```

## Pitfalls

- Do not drift into writing rule documents while a user is waiting for the deliverable; use the fast path and update skills after delivery.
- Do not attach reports/JSON/meeting notes unless asked; default deliverable is `*_srt.txt`.
- Do not put internal workflow labels (`Gem1Gem2`, `park_style`, `sentence_first`) into a user-facing final filename unless needed to distinguish revisions.
- Do not claim high quality from numeric lint alone; spot-check sentence boundaries and product/name terms.
