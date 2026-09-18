# TTimes caption/SRT working method + examples (2026-07-08)

## Trigger

During a long user-provided MP3 → Korean TTimes 말자막 → SRT job, the user corrected both workflow and segmentation style repeatedly. This reference captures the durable class-level method and examples to avoid repeating the same mistakes.

## Core working method

This task is not “ASR cleanup” or “character packing.” It is an editorial subtitle workflow:

```text
MP3/video
→ MLX Whisper ASR + word timestamps
→ transcript-close stable caption script
→ minimal Gem1-style correction
→ Gem2-style human-readable segmentation
→ subagent review as reviewers only
→ Main Hermes integration
→ line-preserving SRT alignment
→ deliver *_srt.txt only by default
```

## Main vs subagents

Mandatory: use subagents for this class of task.

Correct role split:

- Main Hermes writes and owns the whole script rhythm from start to finish.
- Subagents review: proper nouns, numbers, ASR errors, small-sentence readability, 접착어, omissions/distortions.
- Main Hermes integrates only high-confidence fixes and validates final files.

Failure mode:

```text
part1 subagent writes final captions
part2 subagent writes final captions
part3 subagent writes final captions
Main concatenates
```

Why it fails: the tone and rhythm split by part; the result stops feeling like one broadcast subtitle script.

## Do not over-explain delivery

Default delivery after a completed job is one attachment:

```text
*_srt.txt
```

If the user asks, also provide timecode-free script text. Do not attach JSON, meeting minutes, internal reports, or verbose explanations unless explicitly requested. Use clean user-facing filenames, not internal labels like `Gem1Gem2`, `park_style`, or experiment/version jargon.

## Segmentation priority

```text
1. 작은 문장성: noun/target + verb/judgment/predicate where possible
2. meaning closure / human readability
3. 접착어 protection
4. spoken rhythm
5. 25-char target / 27-char max
```

25 visible chars is the target; 27 is the practical max; 28+ should not be delivered.

## Good vs bad examples

### Small-sentence readability

Good:

```text
소프트웨어나 이런 것 쪽으로 많이 다뤘었는데
주위 친구들도 너무나 전문가예요
확실히 구분이 잘 안되는 느낌이 들고
```

Bad:

```text
소프트웨어나 이런 것 쪽으로 많이
다뤘었는데

주위 친구들도 너무나
전문가예요

확실히
구분이 잘 안되는 느낌이 들고
```

Why: the bad forms strand a predicate, degree adverb, or judgment and force the viewer to wait for the next cue.

### 뭔가 / 뭐랄까

Good:

```text
그게 요새 조금 꺾이면서
뭔가 이제 한 사이클이 좀 변해가고 있는 느낌이 드는데
```

Bad:

```text
그게 요새 조금 꺾이면서 뭔가 이제 한 사이클이 좀 변해가고 있는
느낌이 드는데
```

When `뭔가`, `좀 뭔가`, or `뭐랄까` appears mid-thought, often split before it so the previous semantic unit closes and the filler opens the next unit. This is a tendency, not an absolute rule.

### Person / affiliation / title intro

Good:

```text
오늘 또 바이라인네트워크 심재석 대표님
그리고 최용식 아웃스탠딩 창업자님 모셨습니다
안녕하십니까?
```

Bad:

```text
오늘 또 바이라인 네트워크의 심재석 대표님 그리고 최용식
아웃스탠딩 창업자님 모셨습니다. 안녕하십니까?
```

Why: the bad version breaks the second person’s title/affiliation structure and includes sentence-final periods.

### Connectors and discourse markers

Good:

```text
또 지금 어떻게 보면 빅테크나 이런 데서도
근데 AI 칩 같은 경우는
```

Bad:

```text
또
지금 어떻게 보면 빅테크나 이런 데서도

근데
AI 칩 같은 경우는
```

Do not strand `또`, `그리고`, `그래서`, `그러면`, `근데`, `그런데`, `일단`, `어쨌든`, `결국`, `사실`, `아무래도`, `실제로`, `대표적으로`.

### Connective endings

Good:

```text
전문가분들은 워낙 잘 알고 계시지만
일반적으로는 대충 들어는 봤어도
```

Bad:

```text
전문가분들은 워낙 잘 알고
계시지만 일반적으로는
대충 들어는 봤어도
```

Keep connective endings such as `~지만`, `~는데`, `~고`, `~고요`, `~거든요`, `~잖아요`, `~때문에`, `~라서`, `~면서`, `~니까`, `~더라도`, `~라고`, `~다고`, `~는지`, `~듯이` attached to the preceding clause unless the speech pause strongly justifies otherwise.

### Dependent nouns / auxiliaries

Good:

```text
전문적으로 할 수 있는 칩이
스타트업도 나올 수가 있는 거예요
이 정도면 된 것인가를
판단할 수 있어요
```

Bad:

```text
전문적으로 할 수
있는 칩이

스타트업도 나올 수가 있는
거예요

이 정도면 된
것인가를 판단할 수 있어요
```

Keep together forms like `할 수 있는`, `볼 수 있다`, `될 수 있다`, `있는 거예요`, `된 것인가`.

### Numbers and units

Good:

```text
TPU 50만 개가 판매되면
구글에 18조 원 매출을
새로 갖다 준다고 합니다
80~90% 정도라고 볼 수 있습니다
```

Bad:

```text
TPU 50만
개가 판매되면
18조
원 매출을
80~90
% 정도라고 볼 수 있습니다
```

Number+unit/range must stay together.

### Proper nouns / ASR traps from this session

High-priority corrections included:

```text
TTIM / 티티엠류 → 티타임즈
홍재희 → 홍재의
김지연 / 김지원 → 김지현
챗집 PT / 체치패티 / HHPT → 챗GPT
퍼플레시티 / 퍼플렉스티 → 퍼플렉시티
노트북 LM / 노트북의 램 → NotebookLM
재미나이 → 제미나이
크로드 / 클로우드 → 클로드
앤스트로픽 / 엔트로픽 → 앤트로픽
젠슨 왕 / 젠슨항 → 젠슨 황
하이니스 / 하이넥스 → 하이닉스
마이크로미 → 마이크론
DLM / 디렘 → D램
LP DDR → LPDDR
HMAM / HB → HBM
펜리스 → 팹리스
스마트클라스 → 스마트글라스
사이마리 → SMR
그리기 → 그리드
```

Use these as examples of correction class, not as a universal glossary for unrelated videos.

### Idioms / colloquial ASR traps

Good:

```text
선무당이 사람 잡는다
도깨비 방망이처럼 쓰는 거
수박 겉핥기로 아는
벽에 못을 박는 데
망치가 필요하지
톱이 필요한 거 아니잖아요
```

Bad:

```text
섬머슴이 사람 잡는다
도깨비 방문처럼 쓰는 거
수박 겉탈기로 아는
벽에 못을 막는데 망치가 필요하지 못하고
```

### Over-polishing failure

Good transcript-close subtitle:

```text
근데 이걸 AI한테 자꾸 맡겨
내가 뭘 잘하고 못하는지를 구분해야 되잖아요
```

Bad over-written summary:

```text
AI 활용 시 자신의 역량을 구분하는 것이 중요합니다
```

Why: the second is a summary/article sentence, not spoken-caption text.

## Validation checklist

Before final delivery:

- `script lines == srt cues`
- SRT bodies exactly match script lines
- 27-char overflow = 0
- sentence-final periods in caption bodies = 0
- overlaps = 0
- nonpositive durations = 0
- lint for `할 수\n있는`, dependent noun splits, number+unit splits
- spot-check first/middle/late sections and term-dense sections
- confirm user-corrected names remain corrected

## Progress reporting

If user asks “몇 %?” give a practical whole-pipeline percent, not just ASR percent. ASR completion is only an early stage; after ASR, main script, subagent review, integration, alignment, and validation remain.
