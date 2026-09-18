# 긴 인터뷰 SRT 정렬기 선택과 승인 본문 순서 보존

## 적용 상황

- 20분 이상 한국어 인터뷰
- 승인된 timecode-free cue body를 MLX word timestamps에 정렬
- cue body는 사용자 승인으로 동결되어 있으나 일부 어순이 실제 발화와 조금 다름
- `overlaps=0`, `exact_body_match=true`만으로 타이밍 품질을 판단할 수 없는 경우

## 핵심 교훈

같은 37분 38초·약 1,000 cue 본문을 두 정렬기로 비교했을 때:

| 정렬 방식 | 본문 일치 | 문자/토큰 일치율 | ASR word midpoint coverage | 발화 포함 공백 |
|---|---:|---:|---:|---:|
| 문자 dense-window + 5.5초 cap | true | 0.976 | 69.54% | 683곳 |
| 토큰 전역 SequenceMatcher | true | 0.936 | 99.66% | 7곳 |

문자 일치율이 더 높아도 정렬기가 cue를 핵심 단어 주변으로 과도하게 자르고 duration을 cap하면 실제 발화가 자막 없이 남을 수 있다. 정렬기 선택은 sequence ratio가 아니라 다음 순서로 판정한다.

1. exact body match
2. monotonic/non-overlap/nonpositive
3. ASR word midpoint coverage
4. speech-containing gap count와 최장 공백
5. low-match·고유명사·반복 문구 구간의 실제 타임코드

## 실행 절차

1. 최종 body TXT를 동결하고 hash·line count를 기록한다.
2. 최소 2개 정렬 전략을 진단 SRT로 실행할 수 있으면 비교한다.
3. 각 진단본에 대해 다음을 계산한다.
   - cue count == body lines
   - exact body equality
   - overlap/nonpositive
   - min/median/max duration
   - ASR word midpoint coverage
   - 0.25초 이상 cue gap 중 ASR word가 있는 구간
   - `>=0.8s`, `>=1s`, `>=2s`, `>=3s`, longest spoken gap
4. coverage가 높은 기질을 선택하되, 2초 이상 spoken gap은 모두 수동 판정한다.
5. 최종 body가 바뀌면 정렬·coverage 검증을 처음부터 다시 한다.

## 승인 본문 어순이 실제 발화와 다를 때

승인 샘플에서 사용자가 이미 body 순서를 승인했는데 실제 음성은 같은 단어를 다른 순서로 말할 수 있다. 예:

```text
승인 body:
AI를 도입하기 전에
우리의 비즈니스, 우리의 도메인을
에이전트 친화적으로 전환하는 것

실제 발화:
우리의 비즈니스, 우리의 도메인을
AI를 도입하기 전에
에이전트 친화적으로 전환하는 것
```

이 경우 alignment score를 높이려고 승인 body를 되돌리거나 cue 순서를 바꾸지 않는다.

1. 승인 prefix hash와 exact body를 유지한다.
2. 반복 문구가 앞선 위치로 매핑돼 생긴 gap인지 확인한다.
3. 이미 인접 cue가 의미를 담고 있다면 새 자막을 만들지 않는다.
4. semantically matching한 이전 cue를 다음 cue 실제 시작 직전까지 연장해 spoken gap을 덮을 수 있다.
5. 연장 후 반드시 확인한다.
   - `early_next_exposure == false`
   - `previous_cue_lingers_into_next_idea == false`
   - cue duration이 과도하지 않음
6. 실제 새 의미가 빠졌다면 timing extension이 아니라 body에 source-close cue를 추가하고 전체 재정렬한다.

일괄 midpoint bridge는 금지한다. ASR word가 있는 gap만, 최대 허용 폭을 제한하고, 다음 cue 시작보다 작은 guard를 남겨 이전 cue end를 확장한다.

## Local ASR repair와 정렬

- 20~30초 반복 환각은 좁은 clip + second model로 재전사한다.
- merged `segments`뿐 아니라 `words`도 교체한다.
- baseline/range derivatives를 다시 만든다.
- 복구 전 range를 읽은 subagent 초안은 해당 interval에서 stale이다.
- Main이 repaired transcript로 누락 구간을 복원한 후 current hash에서 omission review를 다시 한다.

## Subagent 초벌의 역할

승인 샘플 이후 긴 본문을 범위별로 초벌 작성시키는 것은 허용되지만, subagent는 final-script author가 아니다.

- worker 입력: 승인 sample, source range, correction contract
- worker 출력: bounded draft + path/hash/line/max length
- Main 필수 작업:
  - 실제 파일·hash 검증
  - 5분/범위 경계 연결
  - local ASR repair interval 재작성
  - terminology ledger 적용
  - whole-body source/segmentation/term review
  - frozen sample prefix equality

초벌 self-report만으로 전체 본문 검증 완료라고 말하지 않는다.
