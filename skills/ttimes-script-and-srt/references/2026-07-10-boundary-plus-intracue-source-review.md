# Long-form Korean caption review: boundary audit is not enough

## Durable lesson

A protected-phrase adjacency audit can pass while many **intra-cue** errors remain. Long spoken Korean needs two independent review layers before timing:

1. **Boundary layer** — every adjacent cue pair: adnominal+noun, object/adverbial+predicate, dependent noun, auxiliary predicate, number+unit, fixed chunks.
2. **Intra-cue/source layer** — every cue against ASR/audio: malformed particles, duplicated objects/topics, broken quotations, spoken false starts that become ungrammatical captions, proper nouns, units, and meaning-changing omissions.

Do not infer quality from candidate count alone. Broad regex candidates need manual adjudication, but zero confirmed boundary failures does not certify the body.

## High-value intra-cue error classes

- Wrong collocation: `박사 과정을 받은` → `박사 학위를 받은`
- Duplicated noun/unit: `문제가 1만 문제` → `문제 1만 개`
- Duplicated case marking: `칩을 발표를 했다`, `양산을 하려고` → `칩을 발표했다`, `양산하려고`
- Topic/subject collision: `제품이 아마존은`, `이게 공통점은` → remove the stray topic
- Broken indirect question/quotation: `어떻게 쓰냐 보면` → `어떻게 쓰는지 보면`; `된다라는` → `된다는`
- Missing unit or particle: `1조 3000억 받았고` → `1조 3000억 원을 받았고`
- Meaning reversal by omission: `두 명한테 팔고 끝나잖아요` vs source `끝나면 안 되잖아요`
- Malformed source disfluency: preserve tone, but minimally repair unreadable spoken grammar instead of keeping it verbatim

## Reviewer protocol

For long-form work, assign reviewers by line/time range and require both:

- all adjacent boundaries inspected;
- every cue checked for intra-cue grammar and source fidelity against merged word timestamps/audio.

Reviewer output format:

```text
line(s) | current text/pair | minimal source-close correction | error class/evidence
```

Main must:

1. Record candidate body hash and line count in every brief.
2. Treat stale-review line numbers as hints only; search quoted current strings before applying.
3. Apply only findings still present in the current body.
4. Generalize each confirmed issue to an error-family scan over the whole body.
5. Re-run length, punctuation, quote balance, rejected-name, number/unit, adjacency, and intra-cue pattern checks.
6. Regenerate SRT from the body; never patch timed bodies directly.
7. Re-run exact-body, index, overlap, nonpositive-duration, max-duration, and low-match spot checks.

## Anti-pattern

Do not repeatedly compress the body while reviewers are running. Heavy Main rewrites make reviews stale, lower ASR match, and can introduce new grammar errors. Prefer local exact-string corrections after a transcript-close baseline is established.

## Acceptance gate

Before final delivery, require:

- approved sample prefix unchanged;
- no unreviewed adjacency candidates;
- no unreviewed intra-cue/source findings;
- no ordinary cue over 27 chars except documented approved exceptions;
- SRT bodies exactly equal frozen body lines;
- no overlap, nonpositive duration, or uninspected low-match cue.
