# Session lesson: `/plan` + predicate attachment for TTimes spoken captions

Use this note when regenerating Korean spoken-dialogue SRTs after quality failures or rule changes.

## What improved quality

The successful workflow was not just better line wrapping. Quality improved after the task was forced through a `/plan`-style sequence before file generation:

1. Decide what to reuse vs discard.
   - Reuse: MP3/downloaded source, MLX Whisper/ASR word timings, confirmed term corrections, high-confidence prior review findings.
   - Discard: bad script segmentation and SRT cue bodies when readability fails.
2. Rebuild transcript/cues under a single ordered rule set.
3. Run subagents only after the brief encodes the true failure mode.
4. Main Hermes integrates suggestions; subagents do not author final copy.
5. Re-align line-preserving SRT and verify body equality.

## Critical segmentation rule

The winning top-level rule was:

> 문장 끝에서 끊되, 목적어/부사어/시간어를 서술어 없이 고립시키지 않는다.

Bad:

```text
지난주 금요일에 집을 다
그렇게 꾸며놨어요 일하기 적합하게
```

Good:

```text
지난주 금요일에 이사 갔거든요
집을 다 일하기 적합하게 꾸며놨어요
```

The issue is not cue length; it is predicate attachment. A cue like `집을 다` has no small-sentence readability.

## Subagent review brief must include

Ask reviewers to read each cue standalone and flag:

- object/adverbial/time phrase stranded without predicate
- predicate tail split into the next cue
- degree/discourse marker isolated without the phrase it modifies
- sentence ending plus unrelated next sentence packed together
- high-confidence ASR/term/numeral/unit errors

Tell reviewers not to over-flag deliberately short cues that are greetings, responses, or topic headers.

## Verification beyond machine lint

Mechanical checks are necessary but insufficient:

- script lines == SRT cues
- SRT body exact match
- max visible <= 27
- no periods in cue body
- no overlaps/nonpositive durations

Also inspect for the known human-failure class:

- stranded 목적어/부사어/시간어
- stranded 정도부사 or 접속어
- broken 보조용언 / 의존명사 chunks
- term residuals such as wrong speaker names or product names
