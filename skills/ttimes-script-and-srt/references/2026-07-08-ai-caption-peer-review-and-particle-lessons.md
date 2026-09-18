# 2026-07-08 AI/TTimes Caption Peer Review Lessons

Session class: YouTube interview → Korean TTimes-style 말자막 SRT for AI/tech dialogue videos.

## Durable user corrections

### 1. Human readability is meaning-closure, not shortness

User strongly corrected mechanical short segmentation. The governing rule is:

> 짧게 자르지 말고, 의미가 닫히는 지점에서 자른다.

Bad splits the user called out or implied:

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

4 5년 정도
```

Preferred:

```text
한다는 점이 있고
나눠보도록 하겠습니다
되었다고 볼 수 있고요
할 수 있냐
10위 내에서
4~5년 정도 뒤에는
```

If a protected phrase makes a cue longer, keep the phrase intact and split earlier in the sentence.

### 2. Add `서술부 완성구` to protected phrases

Previous protected phrases covered 의존명사/숫자/고정표현, but the user pointed out that predicate-complement chunks also must stay together.

Protect examples:

```text
한다는 점이 있고
라는 의미가 있고
되었다고 볼 수 있고요
가능하다고 봅니다
중요하다고 생각합니다
나눠보도록 하겠습니다
평가받고 있기 때문에
진행되고 있습니다
```

Do not leave these at cue end:

```text
한다는
라는
되었다고
가능하다고
나눠보도록
평가받고
진행되고
```

### 3. `AI에` vs `AI의` matters

The user specifically corrected that `의` and `에` must be distinguished carefully. This is not cosmetic; it changes meaning.

Use syntax, not sound:

```text
AI에 어떤 일을 시킬지        # AI에게 / AI에다 — target/direction
AI에 적용하다                # target/location/adverbial
AI의 리서치와 보고서 초안     # AI's/of AI — noun modifier
AI의 중요성 / AI의 제2막      # noun modifier
AI의 도움을 받아             # of/from AI
```

Flag ambiguous `에/의` cases during peer review.

## Peer review workflow refinement

For this user, peer review is not optional for TTimes/YouTube script+SRT work. Run subagents with explicit axes:

1. **Text correction** — ASR errors, proper nouns, numbers, units, particles (`에/의`).
2. **Human readability** — cue boundaries close meaning; protected phrase/predicate chunks preserved.
3. **Meaning preservation** — no omissions, no over-polishing, no ASR hallucination carried forward.
4. **Timing** — final main-agent responsibility after integration.

If subagent results arrive after an initial delivery, do not ignore them. Integrate high-confidence fixes, rerun alignment/validation, and resend updated SRT.

## Common AI/tech transcript correction patterns from this session

These are not universal replacements; use as high-risk review candidates in AI/cloud/coding videos:

| ASR-ish / bad | Likely correction |
|---|---|
| 쪽과 있거든요 | 조크가 있거든요 |
| 각계격파 | 각개격파 |
| 책 모델 | 챗 모델 |
| 해포탄 | 핵폭탄 |
| 추출금지 | 수출 금지 |
| 가드레이 | 가드레일 |
| 세이블 | 페이블 |
| 미토트 | 미토스 |
| 쏘넷 / 손에 | 소넷 |
| 오포스 | 오퍼스 |
| 기더부 | 깃허브 |
| 컬서 | 커서 |
| 7GPT 프로 | 챗GPT 프로 |
| 배드락 | 베드록 |
| 세라브레스 | 세레브라스 |
| 트레이닝/트레이니엄 confusion | 트레이니움 |
| 인퍼런스야 | 인퍼런시아 |
| 해결모니 | 헤게모니 |
| 안목지 | 암묵지 |
| AI 짱코드 | AI가 짠 코드 |
| 복사 부채는 엔터 | 복사 붙여넣고 엔터 |
| 꼬다는 보리자로 | 꿔다 놓은 보릿자루로 |
| 구독이 무서워서 | 구더기 무서워서 |

## Delivery/validation pattern reinforced

Telegram delivery should still be ASCII `*_srt.txt` containing exact SRT text. Validate before delivery:

```text
script_lines == srt_cues
SRT bodies == script lines
overlap == 0
nonpositive == 0
phrase_lint_count == 0
low_match_count ideally 0
```

When late corrections are integrated, regenerate from the final script, do not patch SRT bodies directly.
