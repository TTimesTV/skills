# 2026-07-08 long YouTube → TTimes script/SRT delivery lessons

## Context

User supplied YouTube URL `https://www.youtube.com/watch?v=-hAr7RzkeOU&t=5s` for a 54-minute TTimesTV video: `아르테미스, 위성 통신, 우주 데이터센터...'우주산업'을 당장 공부해야 하는 이유`.

Pipeline used:

1. `yt-dlp --dump-single-json` for metadata and chapters.
2. `yt-dlp --write-auto-subs --write-subs --sub-langs 'ko,ko-orig,ko.*,en'` for captions; English subtitle download may hit 429, but Korean captions were available.
3. `yt-dlp -x --audio-format mp3` for source audio.
4. `ffprobe` verified duration about 3263s.
5. Chunked MLX Whisper (`chunk_mlx_whisper_merge.py`, 300s chunks) produced word timestamps.
6. Generated a TTimes-style script, then a line-preserving SRT with cue timing refinement.

## Technique that worked

For 95점 cue sync, the successful refinement pattern was:

- Generate script lines first.
- Build a normalized script character stream from all final script lines.
- Build a normalized ASR character stream from MLX word timestamps, with char→word index mapping.
- Use sequence/fuzzy matching to map each script line span to first/last ASR word indices.
- Set cue `start` from first matched word and `end` from last matched word.
- Apply light Korean 말자막 padding (`start` about -0.055s, `end` about +0.13~0.19s).
- Resolve overlaps by midpoint/gap rules.
- Enforce min/max duration; then validate exact body match and no overlaps.

This is the same pattern that upgraded the earlier K-startup test from roughly 80점 to the user's “너무 너무 잘 맞는다” response.

## Major workflow correction from user

The user explicitly corrected that for this class of TTimes/YouTube → script → SRT work, **subagents must always be used**. This is not optional even if YouTube captions exist, MLX ASR looks good, or sequence/cue matching scores are high.

The user defined the quality score for this task class as mainly:

1. **Text correction quality** — spelling/spacing, ASR errors, proper nouns, people/company names, numbers, units.
2. **Readable segmentation** — short, natural, speech-rhythm-based spoken captions.
3. **Cue timing quality** — starts/ends actually match speech after word-range refinement.

For early/calibration-stage work, run it like a small review meeting: split the video into chunks, have subagents inspect, compare disagreements, then Main Hermes integrates and normalizes style before redoing cue matching from scratch. It is okay if this takes longer.

Recommended subagent roles:

- A: term/proper-noun/number/unit correction review.
- B: line-length/readability/segmentation review.
- C: omission/distortion review against YouTube captions + MLX ASR.

For 40–50+ minute dialogue videos, use at least A+B; C is strongly recommended.

## Segmentation lessons from the user's examples

Do not split only by mechanical character count. Use speech rhythm, meaning, and the way the questioner builds the sentence.

Preferred:

```text
이렇게 우주에 많은 분들, 많은 나라들
그다음에 기업들까지 관심을 갖는 이유
```

Not:

```text
이렇게 우주에 많은 분들, 많은 나라들, 기업들까지
관심을 갖는 이유
```

Reason: the last list item `기업들까지` naturally attaches to the predicate `관심을 갖는 이유`.

Preferred:

```text
다른 행성을 어떤 개척을 해서 자원이나
뭐 이런 것들까지
```

Not:

```text
다른 행성을 어떤 개척을 해서 자원이나 뭐 이런
것들까지 ...
```

Reason: `뭐 이런 것들까지` is a spoken supplement and should stay together.

Preferred for question-building structures:

```text
지금 요새 등장하고 있는 단어가
뉴 스페이스라는 단어가 등장을 하는 것 같은데
이게 스페이스 우주니까
새로운 우주 시대인 것 같은데
```

Reason: preserve the staged build-up: topic → term → explanation → question.

## Pitfalls

- Do not rely on coarse segment-level alignment after generating a cleaned script; it feels close but not 95점. Always run the cue word-range refinement pass for this user.
- Long TTimes videos amplify proper-noun issues. Build a metadata glossary before generating/line-breaking: e.g. SpaceX, Starlink, Artemis, NASA, Apollo, Lockheed Martin, Northrop Grumman, Blue Origin, Blue Moon, Gwynne Shotwell, Kalshi, PDR, IR deck.
- Avoid broad/global replacements that create new errors. Example pitfall: replacing `스페이스 X` after another correction created `스스페이스X`. Use guarded regex or post-scan for doubled tokens.
- Avoid generic replacements that change meaning. Example pitfall: globally replacing `AI에` → `AI에게` made `AI에 적응` wrong. Prefer context-specific corrections.
- A high ASR/cue sequence score does **not** prove the spoken-caption segmentation is good. Readability review is a separate quality gate.
- Keep validation/debug JSON local; user does not want it attached.

## Delivery preference learned

The user strongly prefers separate deliverables, and ZIP is annoying on mobile:

1. Primary SRT delivery for Telegram should be an ASCII `.txt` file containing exact SRT content, e.g. `basename_srt.txt`.
2. Tell the user they can rename `.txt` → `.srt` if needed.
3. Use ZIP only if `.txt` delivery also fails or the user explicitly asks. If zipped, include only the requested SRT/TXT, not validation JSON.

Do not repeatedly resend the same `.srt` path after the user says the attachment did not appear.

## Space-industry correction bank from the rework

High-risk corrections discovered by the subagent review and final integration:

```text
8컷 라인 / 파이콘나인 / 팔콘 라인 → 팰컨9
조정 앱이 다 → 조정 EBITDA
XAI → xAI
인계점 → 임계점
흑자전 → 흑자 전환
스페이스에서는 → 스페이스X는
고무가 절반도 → 공모가의 절반도 인정해 줄 수 없다
시청 → 시총
히트니 켈슨 → 휘트니 틸슨
자산 응용사 → 자산운용사
완전 성형화 → 완전 상용화
하이퍼로프 → 하이퍼루프
마일스톨 → 마일스톤
로프트 한자그룹 → 루프트한자그룹
아이에이지 → IAG
지구의 그 돈 궤도 → 궤도를 잘 조정하면
달이 다치 / 다리를 한 대 → 달이 대체 / 달에 한 번
안 볼 이유 → 안보 이유
하늘에 탁 튀어야 → 하늘이 탁 트여야
100만 개 때우겠다 → 100만 개 띄우겠다
게임 체인지기 → 게임 체인저
뉴스페이스 담당 여행 → 뉴 스페이스 담당 영역
10총 → 시총
이걸 필드로 → 이걸 필두로
```

Numbers/units to normalize:

```text
100에서 300Mbps → 100~300Mbps
10만 명 / 51000만 명 → 1000만 명 / 5000만 명
30조원 → 30조 원
시가총액는 → 시가총액은
```

The final rework after subagent integration had roughly: `script lines = 1324`, `srt cues = 1324`, exact body match, zero overlaps/non-positive durations, median cue duration about 2.21s, max about 3.8s, average match score about 0.982. The key lesson is the order, not the exact numbers: text correction and readable segmentation must be fixed before final cue matching/refinement.

## Verification checklist for future reruns

Before final delivery:

- `script non-empty lines == SRT cues`
- `SRT bodies == script lines`
- sequential cue indices
- no overlaps
- no non-positive durations
- scan short cues and long holds
- inspect user-called-out ranges manually
- report concise validation summary and attach only the requested deliverable
