# Protected-Phrase Adjacency Audit for Korean TTimes Captions

Use this reference whenever a Korean 말자막 body is created, resegmented, or corrected after the user points out an awkward cue boundary.

## Core lesson

A user correction is usually an **error-class signal**, not a request to patch one literal string.

If the user points out:

```text
될 수가
있는데
```

do **not** conclude that `수가` is a filler and globally rewrite it to `수`. The source wording may legitimately contain `-(으)ㄹ 수가 있다/없다`. The actual error is that a protected grammatical construction was split across cue boundaries.

Preserve the spoken particle unless the user explicitly asks for prose normalization. Fix the segmentation:

```text
될 수가 있는데
```

## Required protected classes

Audit every adjacent cue pair for all of these classes, not just `수`.

1. **관형어·관형형 + 일반 명사**
   - `차지하는 / 시장 점유율`
   - `많은 / 돈`
   - `납품하는 / 비즈니스`
   - `따라갈 / 롤모델`
2. **관형형 + 의존명사**
   - `하는 / 것`
   - `만드는 / 걸`
   - `가는 / 데`
   - `될 / 수`
   - `같은 / 게`
   - `한 / 만큼`
3. **의존명사 + 조사·서술부**
   - `수 / 있는데`
   - `것 / 같아요`
   - `걸 / 사용하는`
   - `줄 / 알았습니다`
4. **목적어·부사어 + 서술어**
   - `보드에 바로 / 끼울 수 있다`
   - `트레이니엄을 / 사용하거든요`
5. **보조용언·복합서술어**
   - `하고 / 있다`
   - `하게 / 되다`
   - `해 / 보다`
6. **수량·단위·범위 결합구**
   - `한두 개 / 정도`
   - `한 / 10~20배`
   - `500만 / 개`
7. **고정 결합명사구**
   - `늘린다는 / 측면`
   - `다변화되는 / 과정`
   - `고평가받고 있는 / 상황`

## Mandatory workflow

1. Edit the **body-only TXT** first. Do not edit SRT body text directly.
2. Run `scripts/audit_protected_phrase_splits.py BODY.txt` to generate broad candidates.
3. Read **every adjacent cue pair manually**, even when the script reports zero candidates.
4. For each candidate, inspect at least the previous cue, current pair, and next cue.
5. Repartition the whole local sentence, not just the two offending strings.
6. Re-run length, number/unit, punctuation, and protected-phrase gates after every change.
7. Freeze the body with line count and SHA256 before timing alignment.
8. If the body changes after reviewer feedback, invalidate stale reviews and re-run the relevant audit on the new hash.

## Why automation is not sufficient

In a real 0–3 minute sample, the deterministic script returned `candidates=0`, but Main manual review still found:

```text
앤트로픽 같은 회사가
트레이니엄을 어마어마하게 사용하거든요
```

and a subject/predicate break around the GPU explanation. Regex is a candidate generator, never a quality certificate.

The required acceptance statement is not merely:

```text
automatic candidates: 0
```

It is:

```text
automatic candidates reviewed
all adjacent cue pairs manually read
confirmed protected-phrase breaks: 0
unresolved candidates: 0
```

## Character-limit rule

The 25/27-character target is subordinate to grammatical integrity.

- Never solve an overlength cue by splitting a protected construction.
- First remove non-meaningful repetition or use a source-faithful compact wording.
- Do not compress concrete numbers, contract direction, or technical qualifiers.
- If the user supplied authoritative text that must be preserved exactly, allow the longer line rather than rewriting it.

## Sample-first gate

For this user's TTimes/SRT workflow:

1. Build only the first 0–3 minute body sample.
2. Run the full protected-phrase audit.
3. Deliver the clean TXT for rhythm approval.
4. Do not proceed to the full body until the user approves the sample.

## Reviewer brief

A reviewer must receive:

- exact body path
- current line count
- current SHA256
- assigned line range
- explicit protected classes above
- instruction to return exact line numbers, current pair, minimal correction, and reason

Subagents are reviewers. Main owns final wording and performs the final sequential read.
