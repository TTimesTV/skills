# Predicate-attachment TTimes SRT workflow lessons (2026-07-08)

## Trigger

During a long Korean MP3→SRT task, the user rejected multiple drafts because mechanical sentence-first or 27-char packing still produced unreadable cue boundaries, e.g.:

```text
지난주 금요일에 집을 다
그렇게 꾸며놨어요 일하기 적합하게
```

The correction was not merely “split at sentence endings.” The key missing rule was **predicate attachment**: do not strand objects/adverbials/time phrases away from the predicate they depend on.

## Durable workflow

Use this order for this user's TTimes / spoken Korean subtitle work:

```text
1. MP3/source acquisition and ffprobe confirmation
2. MLX Whisper ASR with word timestamps
3. Build a source-faithful transcript first; do not caption-pack yet
4. Minimal correction: ASR, particles, obvious grammar, terms, proper nouns, numbers
5. Sentence/thought boundary split: if a sentence/thought ends, usually move next sentence to next cue
6. Predicate-attachment pass: object/adverbial/time phrase must attach to its predicate unless it is a deliberate topic marker
7. Small-sentence readability: cue should read like noun/target + verb/judgment where possible
8. Adhesive-word protection: do not strand discourse markers, degree adverbs, demonstratives, connective endings, auxiliaries
9. 25-char target / 27-char max; 28+ forbidden
10. Subagents review only; Main Hermes integrates and owns final script
11. Align final script to MLX word timestamps
12. Verify and deliver only *_srt.txt unless user asks for script text
```

## Segmentation priority

```text
1. Sentence/thought boundary
2. Predicate attachment
3. Small-sentence readability
4. Meaning closure / human readability
5. Adhesive-word protection
6. Spoken rhythm
7. 25-char target / 27-char max
```

## Predicate attachment rule

A cue should not consist only of an object, adverbial, time phrase, or modifier whose predicate is in the next cue.

Bad:

```text
지난주 금요일에 집을 다
그렇게 꾸며놨어요 일하기 적합하게
```

Better:

```text
지난주 금요일에
집을 다 일하기 적합하게 꾸며놨어요
```

Also bad:

```text
소프트웨어나 이런 것 쪽으로 많이
다뤘었는데

주위 친구들도 너무나
전문가예요

확실히
구분이 잘 안되는 느낌이 들고
```

Better:

```text
소프트웨어나 이런 것 쪽으로 많이 다뤘었는데
주위 친구들도 너무나 전문가예요
확실히 구분이 잘 안되는 느낌이 들고
```

## Sentence ending rule nuance

The user wants sentence/thought endings respected:

```text
아직 버전 아니에요?
아, 끝난 거 아니에요?
```

Avoid merging separate sentences just because they fit under 27 chars. But sentence-first splitting is not enough: if splitting leaves `집을 다`, `많이`, `확실히`, `할 수`, etc. stranded, reattach to the predicate or restructure within source-faithful wording.

## Subagent review brief requirements

Subagents must be explicitly told to check this class of failure, not only terms/lints:

```text
Read each cue as if it appears alone on screen.
Flag any cue that is only an object/adverbial/time phrase without its predicate.
Flag predicate tails separated from their object/adverbial.
Short cues are allowed only for greetings/replies/topic markers, not stranded grammar fragments.
Find sentence-end + next-sentence merges when they hurt readability.
Check proper nouns/terms/numbers, but do not rewrite broadly.
```

Subagents are reviewers/advisers, never final section writers. Main Hermes keeps one global voice and integrates only high-confidence corrections.

## Delivery preference

Default delivery is only the final, cleanly named `*_srt.txt`. If the user asks, provide timecode-free text. Do not include internal reports, JSON, or long meeting notes unless explicitly requested.

## Product-name preference

For Korean spoken subtitles, keep common spoken Korean product names in Korean unless asked otherwise:

```text
재미나이 -> 제미나이
not: Gemini
```

Keep established acronyms/brand forms where natural:

```text
AI, GPU, NPU, TPU, HBM, D램, LPDDR, AWS, TSMC, NotebookLM, 오픈AI, 챗GPT, 클로드, 퍼플렉시티
```

## Verification checklist

Before delivery:

```text
script lines == srt cues
SRT body exact match
27자 초과 = 0
sentence-final periods = 0
overlap = 0
nonpositive = 0
known bad term variants = 0
보조용언/의존명사 split lint = 0
standalone connector/adverb lint = 0
manual sample: first 30 cues must not contain stranded object/adverbial phrases
```

If the first minute contains a glaring cue like `집을 다`, treat the whole draft as failed and rebuild from the segmentation step, not as a tiny patch.
