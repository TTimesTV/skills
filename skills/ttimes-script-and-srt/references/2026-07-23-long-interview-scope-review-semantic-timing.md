# 긴 기술 인터뷰: 범위 격리·리뷰 수렴·semantic timing repair

## 적용 상황

40~60분대 무자막 기술 인터뷰를 `MLX ASR → bounded 초벌 → Main 통합 → immutable review → SRT`로 처리할 때 사용한다.

## 1. Bounded draft의 입력 격리

- 긴 영상은 5~10분 timestamped source slice를 물리적으로 생성하고 SHA-256을 고정한다.
- drafter에는 **해당 slice 하나 + glossary/ledger만** 준다.
- 전체 raw transcript나 timecode-free baseline을 함께 주면 요청 범위를 무시하고 뒤까지 계속 작성하면서도 잘못된 범위를 보고할 수 있다.
- 결과의 첫/마지막 내용과 source first/last timestamp를 Main이 직접 대조한다.
- 범위를 넘은 산출물은 `obsolete/`로 격리하고 splice하지 않는다.

## 2. Immutable review를 시간·cue 범위로 나누기

- 50분대 전체 source/term reviewer는 10분 timeout에 걸릴 수 있다. 같은 immutable hash를 유지한 채 `00~30분`, `30분~끝`처럼 나눈다.
- 분절 reviewer도 cue 전반/후반으로 나누고 seam을 양쪽 범위에 포함한다.
- 한 generation의 모든 reviewer가 끝나기 전 body를 수정하지 않는다.
- source·term review와 segmentation review를 분리한다. 어휘 reviewer는 source/audio evidence가 있는 lexical fix만 제안하고, segmentation reviewer는 token-preserving boundary move만 제안한다.

## 3. 분절 수렴의 anti-overmerge 기준

반복 검수는 0건까지 하되, 다음을 prompt에 명시한다.

- `합치면 27자 이하`라는 이유만으로 finding을 만들지 않는다.
- 현재 cue가 자체 문장성·화제 제시·열거·반응·말맛 리듬을 가지면 유지한다.
- finding은 실제 보호구 분리, 고아 조각, 질문/답변 혼합, 직접인용 파손으로 제한한다.
- 모든 current block은 immutable candidate에서 unique exact-match여야 한다.
- 제안은 token order/content를 보존하고 각 cue가 27자 이하여야 한다.

보고서 적용은 exact current→proposal replacement로 자동화할 수 있다. 적용 전 candidate hash를 확인하고, 적용 후 blank/over-27/token-drift를 즉시 검사한다. 어순이 부자연스러운 token-preserving 제안은 Main이 source 의미를 보존하면서 별도 정상화한다.

## 4. Aligner 선택

sequence ratio 자체보다 다음을 우선한다.

1. ASR word-midpoint coverage
2. 0.8/1/2/3초 spoken-gap count
3. max spoken gap
4. unmatched cue의 성격
5. overlap/nonpositive timing

실전 비교에서는 sequence 정렬이 약 99.15% coverage·2초 이상 gap 0건, token 정렬이 약 93.82%·2초 이상 gap 9건이어서 sequence를 선택했다.

## 5. Semantic gap repair

교정된 영문 용어가 ASR의 한글 음차와 lexical match되지 않으면 실제 발화 단어가 cue 사이 gap으로 남는다. 예: `Antigravity/앤티그래비티`, `OpenRouter/오픈…`, `Evaluation/이벨류에이션`, `SAP/삽`.

- gap의 ASR words와 좌우 body를 읽고 해당 의미 cue를 판정한다.
- 좌측 cue 소유면 left end를 right start까지 확장한다.
- 우측 cue 소유면 right start를 left end까지 당긴다.
- blind midpoint나 침묵만 보고 cue를 새로 만들지 않는다.
- repair log에 gap, 방향, 좌우 body를 기록한다.

이 방식으로 0.8초 이상 semantic gap을 0건으로 줄이고 word-midpoint coverage를 약 99.44%까지 높였다.

## 6. 짧은 cue timing-only 보정

body가 최신 해시에서 source/segmentation PASS한 뒤에는 본문을 다시 바꾸지 않는다.

- 0.7초 미만 cue를 모두 나열한다.
- `왜요?`, `그렇죠`, 인사, 짧은 답변처럼 독립 turn은 유지한다.
- 의미상 읽기 시간이 필요한 fragment/term cue만 수동 선정한다.
- 먼저 인접 무음을 사용하고, 부족하면 긴 이웃 cue가 최소 0.5초 이상 남는 범위에서 수백 ms를 빌린다.
- cue 수·본문·순서는 그대로 두고 timing-only log를 남긴다.
- 최종 validator로 body/SRT count, overlap, nonpositive, max visible length를 재검증한다.
