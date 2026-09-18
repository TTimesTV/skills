# 2026-07-09 김지현 1편 컷 — chunked ASR, Main 선납품본, late subagent integration

## Context

YouTube: `https://youtu.be/k29tnwrTHq0` (`김지현 1편_컷편`, 41:57). User requested `/plan` then execution for TTimes 말자막 SRT.

## Durable lessons

1. **No-caption long YouTube videos can make full-file MLX Whisper collapse even when it exits 0.**
   - In this case full-file MLX produced timestamp disorder and a hallucinated repeated phrase loop around `챕터가 챕터...`.
   - Treat this as ASR substrate failure, not as text to patch.
   - Switch to 5-minute chunked MLX with `--condition-on-previous-text False`, then merge word timestamps.

2. **Validate ASR substrate before caption work.**
   - Check `words > 0`, last word timestamp ≈ source duration, no backward timestamps, no repeated filler/phrase loops.
   - Example good chunked metrics: duration ≈ 2517s, `words=5654`, `segments=1051`, backward=0, last word≈duration.

3. **Subagents are mandatory reviewers, but do not block all progress blindly.**
   - Dispatch term/readability/omission reviewers early.
   - Main can continue building and validating the SRT while they run.
   - If they have not returned after reasonable waiting, deliver only as `Main 검증 선납품본` and explicitly promise a `v2` if high-confidence subagent findings arrive.
   - Do **not** mark the review task completed until summaries actually return and are integrated.

4. **Common ASR traps from this video class.**
   - `김지연` → `김지현`
   - `TTIMG` → `티타임즈`
   - `홍재희` may need host-name verification; avoid overclaiming if uncertain.
   - `AX 무쇠` → `AX무새`
   - `섬머슴/섬모샘` → `선무당`
   - `채찍 PT/체치PT/채취패티` → `챗GPT`
   - `퍼플레시티/퍼블릭시티` → `퍼플렉시티`
   - `클로우드/크로드` → `클로드`
   - `코팔롯/코팔` → `코파일럿`
   - `노트북의 램/노트북 에렉` → `노트북LM`
   - `캐즈머/캐즘로` → `캐즘/캐즘으로`
   - `치사점` → `시사점`
   - `빨래빵망이` → `빨래방망이`
   - `팔당량` → `할당량`
   - `확증 편하게` → `확증 편향에`

5. **Segmentation fixes found during Main review.**
   - Remove dead sentence-final periods, but preserve real `?` for questions.
   - Watch for short orphan cues that are not reactions: `때문에`, `게`, `하더라도`, `보고`, `있어야` should be merged/split around the predicate.
   - Short reactions like `될까요?`, `있잖아요`, `알았어요`, `같은데`, `건가?` can remain short if they match the spoken beat.

## Recommended validation snippet shape

After alignment, verify:

```text
cue count == body line count
body_match == true
overlap == 0
nonpositive == 0
over27 == 0
final_periods == 0
known_bad_hits == {}
low fuzzy match == 0
long_over_5 == 0
```

If the only remaining issue is pending background subagents, label the file as `Main 검증 선납품본`, not final integrated review.
