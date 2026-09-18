# 2026-07-08 First full TTimes script→SRT pipeline trial

## Trigger

User wanted Hermes to perform the upstream `[스크립트]` creation too, not only line-preserving SRT sync:

```text
YouTube title/link or MP3
→ transcript substrate
→ term/proper-noun cleanup
→ readable TTimes `[스크립트].txt`
→ line-preserving SRT
```

Test video: `자원을 효율적으로 안전하게! 유럽서 주목하는 K-스타트업` / 티타임즈TV / `NS7CyjCfUw0`.

## What worked

- `yt-dlp "ytsearch5:<title>" --dump-json` found the exact video from title.
- Downloaded YouTube Korean captions plus audio.
- Ran chunked MLX Whisper on the extracted MP3.
- Used YouTube description/tags/chapters as a glossary source: VivaTech 2026, 비전이노베이션, 비전노즐, 하이온, 동애등에, 액침 냉각유, 에어로원, 포네이처스, 나인와트, 옵티, EDF, ENGIE, 슈나이더 일렉트릭, ESCO.
- Final validation shape:
  - script lines = 274
  - SRT cues = 274
  - exact body match = true
  - overlaps/nonpositive = 0
  - max cue duration ≈ 3.74s
  - char sequence ratio ≈ 0.95

## Important lessons

### 1. Metadata glossary must run before line breaking

Correct proper nouns and technical terms before generating subtitle line lengths. Otherwise fixes like `난오 반아나` → `나노바나나` or `동해등해` → `동애등에` change line length after the fact.

### 2. Avoid unsafe global replacement order

A naive global replacement caused `ENGIE` to become `EENGIEIE` after replacing `NG` globally. Do not replace short substrings inside already-correct proper nouns. Use word-boundary/contextual replacement or apply short replacements before/after with guards.

### 3. YouTube captions can be useful but are noisy

Korean auto/native captions had useful flow but contained errors: channel/name mistakes, `비바테크 2016`, noisy `[음악]`, wrong line breaks, and technical-term mistakes. Use them as a substrate, not the final script.

### 4. Foreign-language interview tails are high risk

In this video the French/English visitor reaction around ~11:40 was badly hallucinated by both Korean ASR and auto captions. Options:

- If exact quote matters: transcribe/translate that segment with a language-aware pass or ask user whether paraphrase is acceptable.
- If the user is only testing script quality: mark the segment as the weakest part and deliver caveat.
- Do not pretend the noisy Korean ASR is an exact foreign quote.

### 5. Subagents are best as reviewers, not final file writers

Good roles:

- term/proper-noun correction review
- line-length/readability review
- omission/distortion review against ASR/captions

Main Hermes should still create and validate final `스크립트.txt`, SRT, ZIP, and exact-body checks.

## Output caveat language

For first-pass trials, tell the user clearly:

```text
이번 테스트에서 제일 약한 구간은 11:40쯤 현지 관람객 반응입니다.
YouTube 자막/MLX 둘 다 외국어 발화를 망가뜨려서 보수적으로 한국어 요지로 정리했습니다.
```

## Reusable quality checks

- visible Korean line length: flag >31 visible chars after whitespace removal
- SRT exact body match: `script non-empty lines == cue count` and bodies equal lines
- scan replacements for accidental corruption of proper nouns like `ENGIE`, `EDF`, `ESCO`, `PFAS`
