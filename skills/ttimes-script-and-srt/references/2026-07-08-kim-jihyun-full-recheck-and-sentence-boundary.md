# Kim Jihyun AI leadership SRT — full-recheck lessons (2026-07-08)

## Trigger

During a long user-provided MP3 → Korean TTimes-style SRT job, the user rejected the delivered `김지현 AI리더십` subtitle as still carrying ASR/term errors and poor cue joining. The session produced durable workflow/style corrections for this user's subtitle class.

## Speed / workflow lesson

For this user, do not let rule documentation or long explanations block the deliverable. After ASR finishes, stay on the fast practical path:

```text
ASR
→ Main Hermes transcript-close script pass
→ subagents as reviewers only
→ integrate high-confidence fixes
→ term/lint scan
→ line-preserving SRT align
→ deliver *_srt.txt
```

If the user asks for notes/rules during a subtitle job, treat documentation as secondary. Continue the subtitle pipeline unless they explicitly say to stop generation and discuss rules.

## Sentence-boundary rule added after user correction

The user clarified that when a sentence/thought ends, the next sentence should usually move to the next cue even if the combined line fits under 27 chars.

Priority order should be:

```text
1. sentence/thought boundary: if a sentence ends, prefer next cue
2. small-sentence readability: noun/target + predicate/judgment
3. meaning closure
4. adhesive-word protection
5. spoken rhythm
6. 25-char target / 27-char max
```

Do **not** pack two completed sentences into one cue just because they fit. Bad pattern:

```text
아직 버전 아니에요? 아, 끝난 거 아니에요?
안녕하십니까 안녕하십니까
```

Prefer:

```text
아직 버전 아니에요?
아, 끝난 거 아니에요?

안녕하십니까?
안녕하십니까
```

Short replies/greetings can still be compact when it improves rhythm, but the default is: sentence ends → next cue.

## Product-name spelling correction

The user objected to converting Korean spoken product names to English spelling. For Korean 말자막, keep the Korean spoken form unless the user explicitly asks for English brand spelling.

```text
재미나이 / 재미나 / Gemini  → 제미나이
```

Do not normalize `제미나이` to `Gemini` by default.

Preferred Korean-subtitle product forms from this job:

```text
챗GPT
제미나이
클로드
퍼플렉시티
NotebookLM
젠스파크
에이닷
오픈AI
앤트로픽
```

Acronyms remain acronyms:

```text
AI, GPU, NPU, HBM, LPDDR, D램, SMR, AWS, TSMC
```

## Full-recheck terms caught late

These were high-confidence errors caught only after the user demanded a full txt recheck. Include similar variants in future term scans:

```text
김지연 / 김지원 → 김지현
홍재희 → 홍재의
TTIM → 티타임즈
퍼블릭시티 / 퍼플레시티 / 퍼플렉스티 → 퍼플렉시티
재미나 / 재미나이 / Gemini → 제미나이
첫째 패티 / 체치패티 / 챗집 PT / HHPT → 챗GPT
오픈클로 → 오픈AI
마이크로미 → 마이크론
젠슨 왕 / 젠슨항 / 제니스 왕 → 젠슨 황
엔트로픽 / 엔스트로픽 → 앤트로픽
DLM / 디렘 → D램
HMAM / HB → HBM
펜리스 → 팹리스
스마트클라스 → 스마트글라스
사이마리 → SMR
그리기 → 그리드
가격설 → 제번스 역설
```

## High-value idiom / ASR fixes from the job

```text
섬머슴이 사람 잡는다 → 선무당이 사람 잡는다
도깨비 방문처럼 → 도깨비 방망이처럼
수박 겉탈기 → 수박 겉핥기
땅 짓고 헤엄치기 → 땅 짚고 헤엄치기
확증 편하게 → 확증 편향
웹도독 → 웩더독
```

## Review pattern that worked

When the user says to recheck the whole txt, do not defend previous validation. Re-dispatch subagents over the full line range with high-confidence-only instructions, then run Main Hermes's own term/lint scan before realigning.

Useful subagent split:

```text
A: lines 1–550
B: lines 551–1100
C: lines 1101–end
```

Subagents should return:

```text
cue/line number | current text | proposed correction | reason
```

Main Hermes should integrate only high-confidence items, rerun:

```text
- bad term scan
- sentence-final period scan
- 27-char max scan
- adhesive/orphan scan
- dependent noun / auxiliary split scan
- number+unit split scan
- body exact match / overlap / nonpositive timing validation
```

## Delivery lesson

After corrections, deliver the revised `*_srt.txt` only. Keep explanation short unless asked. Avoid internal file names such as `Gem1Gem2`, `park_style`, or experiment names in user-visible deliverables.
