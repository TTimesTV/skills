# Human readability + peer-review lessons (2026-07-08)

## Trigger

During two TTimes-style YouTube→SRT jobs, the user rejected mechanically short cue splits such as:

```text
한다는
점이 있고

나눠보도록
하겠습니다

되었다고
볼 수 있고요

할 수
있냐

10위
내에서
```

The correction was not only about dependent nouns. It was about **human readability**: a cue should close a meaningful thought so the viewer does not need to wait for the next cue to resolve grammar or meaning.

## Core rule

> 짧게 자르지 말고, 의미가 닫히는 지점에서 자른다.

Equivalent operating order:

```text
meaning closure
→ grammar/protected phrase preservation
→ spoken rhythm
→ on-screen dwell time
→ character count
```

Character count is a safety rail, not the primary split criterion. A slightly longer cue that preserves meaning is better than a short cue that strands a predicate tail.

## Protected phrase classes

### 1. Possibility / auxiliary constructions

Keep together:

```text
할 수 있다
할 수 있냐
할 수 있는
볼 수 있다
갈 수 있다
될 수 있다
```

Bad:

```text
할 수
있냐
```

### 2. Attributive + bound/dependent noun

Keep together where possible:

```text
만드는 걸
하는 것
가는 데
되는지
한다는 점
그런 의미
```

Bad:

```text
한다는
점이 있고
```

### 3. Predicate-completion chunks

Keep judgment/completion predicates intact:

```text
되었다고 볼 수 있고요
가능하다고 봅니다
중요하다고 생각합니다
나눠보도록 하겠습니다
평가받고 있기 때문에
진행되고 있습니다
```

If too long, split **before** the entire predicate chunk, not inside it.

### 4. Numbers, units, ranges, rank phrases

Normalize and keep together:

```text
4~5년 정도 뒤에는
10위 내에서
30조 원
1000만 명
100~300Mbps
```

### 5. Domain fixed expressions

Do not split terms that should be read at a glance:

```text
실리콘 포토닉스
광반도체
우주 데이터센터
달 착륙선
주가매출비율
시가총액
조정 EBITDA
차등 의결권
```

## Peer-review structure

For this user's TTimes/YouTube SRT work, run subagents as a short editorial peer-review meeting before final alignment.

Recommended roles:

1. **Text correction reviewer** — ASR errors, spelling/spacing, proper nouns, numbers, units, domain terms.
2. **Human readability reviewer** — cue boundaries, meaning closure, predicate chunks, protected phrases, visual rhythm.
3. **Omission/distortion reviewer** — compare ASR/captions against draft and flag missing or meaning-altered content.

The main agent integrates; subagents do not write final files. If reviewers disagree on a recurring segmentation pattern, ask/call the user and then patch the skill with the approved rule.

## Lint patterns worth running before final alignment

Flag cue-boundary splits matching:

```regex
할 수\s*\n\s*(있|없|있는|있냐|있고|있게|있습니다)
(하는|되는|만드는|보는|가는|있는|없는|했다는|하려는|받는|주는|쏘는|쓰는|먹는|드는|될)\s*\n\s*(것|걸|게|데|바|수|거|지|정도|점|의미|부분|구조|방식|때문)
(한다는|라는|다는|되었다고|됐다고|가능하다고|중요하다고|필요하다고|어렵다고|평가받고|진행되고|나눠보도록|다뤄보도록|살펴보도록)\s*\n\s*(점|의미|이유|볼 수|봅니다|생각합니다|하겠습니다|있기|있고|있습니다)
[0-9]+\s*\n\s*(원|달러|조|억|만|명|개|년|개월|배|%|Mbps|위)
실리콘\s*\n\s*포토닉스|광\s*\n\s*반도체|데이터\s*\n\s*센터|유리\s*\n\s*기판
```

Treat matches as strong review targets, not automatically-correct-in-place truth; context and audio still matter.

## Quality scoring frame

A useful review score is:

```text
meaning-unit preservation: 35
Korean grammar/protected phrases: 25
visual length/rhythm: 20
cue timing: 20
```

This prevents over-valuing short lines. The first question is always: **does this cue make sense to a human at the moment it appears?**

## Concrete integration lesson

When the user says “이거 해봐” for a YouTube TTimes SRT, do not stop after ASR + line wrapping. Use:

```text
metadata/captions/audio
→ MLX ASR
→ glossary + draft
→ peer review by text/readability/distortion
→ integrate user-style rules
→ lint protected phrase splits
→ realign from scratch
→ validate exact body match + no overlap
→ deliver ASCII *_srt.txt on Telegram
```
