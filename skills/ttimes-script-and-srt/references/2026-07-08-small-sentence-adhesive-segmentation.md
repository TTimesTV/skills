# Small-sentence + adhesive-word subtitle segmentation rules (2026-07-08)

## Trigger

During a long Korean MP3 → TTimes-style SRT workflow, the user rejected mechanical line packing and clarified the preferred segmentation logic. The user wanted rules established before more file generation.

## Core rule: 작은 문장성 first

Before character-count packing, check whether each cue reads like a small sentence:

```text
noun/target axis + verb/judgment/predicate axis
```

If a cue can be understood on screen without waiting for the next cue, it can usually stand alone. This sits above adhesive-word rules and character-count rules.

Priority order:

```text
1. 작은 문장성: 명사/대상 + 동사/판단/서술어
2. 의미 완결 / human readability
3. 접착어 보호
4. 말 리듬
5. 25자 목표 / 27자 max
```

## User-approved examples

Good because the cue contains a target and predicate/action:

```text
소프트웨어나 이런 것 쪽으로 많이 다뤘었는데
주위 친구들도 너무나 전문가예요
```

Bad because it strands a predicate/adverb:

```text
소프트웨어나 이런 것 쪽으로 많이
다뤘었는데

주위 친구들도 너무나
전문가예요
```

Good with a mid-thought filler/transition split:

```text
그게 요새 조금 꺾이면서
뭔가 이제 한 사이클이 좀 변해가고 있는 느낌이 드는데
```

## Adhesive-word classes

These are not absolute split/no-split commands. They are signals to avoid leaving weak words stranded. Use them under the small-sentence rule.

### 1. Discourse / transition markers — usually attach to following phrase

```text
또
그리고
그래서
그러면
근데
그런데
일단
어쨌든
결국
사실
아무래도
실제로
대표적으로
```

Avoid:

```text
또
지금 어떻게 보면
```

Prefer:

```text
또 지금 어떻게 보면
```

### 2. Filler / hesitation markers — often split before them when mid-thought

```text
뭔가
좀 뭔가
뭐랄까
그 뭐랄까
이제 뭐랄까
```

Example:

```text
그게 요새 조금 꺾이면서
뭔가 이제 한 사이클이 좀 변해가고 있는 느낌이 드는데
```

### 3. Demonstrative + dependent noun/postposition phrases

```text
이런 것 / 이런 거 / 이런 게 / 이런 데 / 이런 식 / 이런 느낌 / 이런 상황 / 이런 측면 / 이런 부분 / 이런 정도
그런 것 / 그런 거 / 그런 게 / 그런 데 / 그런 식 / 그런 느낌 / 그런 상황 / 그런 측면 / 그런 부분 / 그런 정도
```

Important: this is flexible, not an absolute “always keep with prior word” rule. If the whole small sentence fits, keep it together:

```text
소프트웨어나 이런 것 쪽으로 많이 다뤘었는데
```

If too long, split at a meaning-complete boundary, not between the demonstrative and what it depends on.

### 4. Degree / emphasis adverbs — attach to the following predicate/adjective

```text
너무나
굉장히
정말
아주
되게
꽤
상당히
엄청
엄청나게
너무
많이
워낙
확실히
대충
당연히
분명히
```

Avoid:

```text
주위 친구들도 너무나
전문가예요

확실히
구분이 잘 안되는 느낌이 들고
```

Prefer:

```text
주위 친구들도 너무나 전문가예요
확실히 구분이 잘 안되는 느낌이 들고
```

### 5. Modal/evaluative adverbs — attach to judgment phrase

```text
확실히
아마
분명히
당연히
대체로
일반적으로
일반적으로는
결과적으로
실질적으로
상대적으로
냉정하게
어떻게 보면
```

### 6. Connective endings — attach to preceding clause

Avoid starting a cue with these tails unless there is a strong spoken pause:

```text
~지만
~는데
~고
~고요
~거든요
~잖아요
~때문에
~라서
~면서
~니까
~더라도
~라고
~다고
~는지
~듯이
```

Prefer:

```text
전문가분들은 워낙 잘 알고 계시지만
일반적으로는 대충 들어는 봤어도
```

### 7. Auxiliary / possibility expressions — keep together

```text
할 수 있다 / 할 수 있는 / 할 수가 있다
볼 수 있다
될 수 있다
갈 수 있다
쓸 수 있다
만들 수 있다
선택할 수 있다
비교할 수 있다
```

### 8. Topic-setting fragment exception

Fragments can stand alone when they intentionally open the next cue:

```text
첫 번째 모티베이션은
독점 체제에 대한 불안감이에요
```

Short replies/greetings can also stand alone:

```text
안녕하세요
그렇죠
아니요
```

## Punctuation preference

For this user's 말자막 body, remove sentence-final periods/full stops. Keep only necessary decimal points/abbreviations.

```text
합니다. -> 합니다
거예요. -> 거예요
```

Question marks can remain for real questions unless the user says otherwise.

## Practical review checklist

Before final SRT delivery, scan or lint for:

- Cues with only an adverb/connector (`너무나`, `확실히`, `그리고`, `근데`).
- Cues ending with weak lead-ins (`... 많이`) followed by a lone predicate (`다뤘었는데`).
- Connective endings stranded at the start of the next cue.
- `뭔가/뭐랄까` appearing mid-cue where a split before it would improve readability.
- Sentence-final `.` in body lines.
- 28+ visible chars.

Subagents should be briefed with this reference and should review as advisers only; Main Hermes integrates final text and SRT timing.
