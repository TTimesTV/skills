# 이주환 1·2편 컷편집 표준화

## 목적

같은 장편 기술 인터뷰의 1·2편 Track Changes를 전수 복원해, 컷 비율이 아니라 **삭제 기능–retained 대체–정보 보호–accepted 연결성**을 표준화한 사례다. 실제 PD 컷을 무조건 gold로 보지 않고 `GOLD / VALID_BUT_CASE_SPECIFIC / DEFECT / UNRESOLVED`로 감사한다.

## Source 기준선

| 편 | nonempty deletion | insertion | accepted 문자 유지율 |
|---|---:|---:|---:|
| 1편 | 79 | 2 | 86.7% |
| 2편 | 109 | 7 | 82.3% |

두 편 모두 MOVE·형광·직접 취소선 없이 Track Changes 삭제와 소수 삽입으로 편집됐다. 유지율은 다음 작업의 목표가 아니라 결과다.

## 공통 편집 모드

```text
원래 강의 spine 유지
→ 방송 전후 제작 발화 제거
→ failed take·즉시 중복 정리
→ 진행자 우회·책/브랜드 홍보 축소
→ 첫 정의·수치·메커니즘·대표 비유 보호
→ 편별 질문을 기능적으로 분리
```

- 1편: 기존 AX가 왜 실패하고 월드 모델이 왜 필요한가
- 2편: 세계를 어떻게 명세하며 인간이 왜 설계 주체여야 하는가

## 범용화할 규칙

1. **Head/tail gate는 표시와 독립 심사한다.** 표시된 포스트롤을 지워도 바로 뒤 미표시 제작 발화가 남을 수 있다.
2. **Clean retake 하나를 선택한다.** 숫자·고유명·기술명이 다르면 자동 선택하지 않는다.
3. **진행자 발화는 화자가 아니라 기능으로 본다.** 질문 호출·개념 번역·결론 회수면 보호하고, 반복·예고·사적 농담이면 줄인다.
4. **기술 설명은 길이가 아니라 기능 중복으로 판단한다.** 첫 정의·고유 수치·인과·실행 조건은 보호한다.
5. **자기홍보와 논증 권위를 분리한다.** 책·강연·브랜드는 줄여도 고객 수·실패율·대표 프로젝트는 근거가 될 수 있다.
6. **사례는 원칙–사례–결론 묶음으로 심사한다.** 사례를 남기면서 호출 원칙을 없애지 않는다.
7. **Accepted state 전체를 연속독해한다.** 로컬 join이 깨끗해도 역참조·문장 파편·편 tail이 깨질 수 있다.

## Large-block subsumption gate

`앞에서 비슷한 사례가 나왔다`는 이유만으로 장문 Q&A를 통째로 자르지 않는다. 블록 컷 전에 문장별 unique proposition inventory를 만든다.

| 문장 기능 | 이미 retained에 있음 | 처리 |
|---|---:|---|
| 반복 사례 | Yes | CUT 가능 |
| 새 인과 브리지 | No | 압축 보호 |
| 새 상태·책임 정의 | No | 보호 |
| 세 번째 추상 요약 | Yes | CUT 가능 |

이주환 2편 1:08~1:12는 환불 사례 반복을 줄이는 과정에서 다음 고유 명제까지 사라졌다.

- 외부 시스템 write는 단순 rollback이 어렵다.
- 실패를 없던 일로 지우지 말고 반대 실행으로 보상한다.
- 카드사·기업·고객은 서로 다른 책임과 상태를 가진다.
- `컨텍스트는 상태가 아니다.`

전체 복원은 불필요할 수 있지만, `외부 실행은 비가역적이므로 context가 아니라 state와 책임을 명세해야 한다`는 압축 문장은 보호해야 한다.

## Tracked correction audit

삽입·교정도 별도 편집 판단이다.

- 단순 번역 gloss: 채택 가능
- 도메인 상태·고유명·숫자·단위 확정: source audio 또는 권위 정의 확인 전 `NEEDS_REVIEW`
- 유창해졌다는 이유만으로 정확하다고 판정하지 않는다.

사례:

- `Predictable → 예측 가능`, `Fully Autonomous → 완전자동화`: 의미 동일 가능성이 높음
- `Shipped/Shipping → 배송완료/배송중`: 회사 상태 정의에 따라 의미가 달라질 수 있어 unresolved
- `ROAS 120`: 지표명은 복원 가능하지만 120의 단위는 별도 확인

## Anti-gold 회귀검사

### 1편

- `에이전트를 판매한 게 벌써 4년째` 삭제 후 `4년째 하고 계신다고` 유지: backward-reference 단절
- 실행 위험·실패 허용 임계점 삭제 후 의료 사례 유지: principle→example 브리지 손실
- `서랍 안이 근데 그 서랍의 잠금 규칙을 모르고`: partial cut 문장 파편
- 자기홍보 문장 삭제 뒤 `.` 문단 잔존: punctuation ownership 실패
- `네, 지금 그러면 이대로`: 미표시 part-boundary tail

### 2편

- 1:08~1:12 장문 블록: 반복 사례와 고유 실행 원칙을 함께 제거
- partial deletion 후 `, 그 전에도…`로 시작: 문두 쉼표 파편
- 배송 상태 삽입: 용어 교정을 도메인 상태 확정으로 처리할 위험

## Revision 수와 semantic decision 수

Raw revision 행수를 오류 개수로 보고하지 않는다.

- 2편 `DEFECT 37행`은 semantic 결함 2개다: 과잉컷 블록 36행 + 문두 쉼표 1행
- `UNRESOLVED 7행`은 배송상태 교정 1개 semantic group이다.

인접 revision은 source anchor·동일 기능·동일 결과로 semantic group화하고 raw/semantic 계수를 별도 보고한다.

## Accepted-state correction pass

Track Changes 전수 원장만으로는 최종 accepted 오류를 모두 잡을 수 없다. 두 편의 연속독해에서 다음 미표시 후보가 추가로 나왔다.

- 1편 `도움이 되시는`에서 끝나는 hanging predicate
- 1편 `6개 축`과 `10의 5승`, `10만/100만 경우의 수`의 산술 충돌
- 2편 `그 개` → `걔가/AI가` ASR 후보
- 2편 `지능은 두 가지 종류` 뒤 두 번째 항목 부재
- 2편 `세개의 우리 도메인 명세` → `세계의` 등 ASR 후보
- 2편 도입의 `몇 억 번`과 후행 `1,500만 번` 충돌

따라서 final correction pass는 revision 밖 accepted text를 대상으로 미완성 술어, ASR 개체, 열거 약속, 숫자·단위·상태 전이 충돌을 검사한다.

## Production block의 정의 회수

1편 본문은 FDE를 사용하지만 풀네임이 없고, post-roll 제작 대화에만 `Forward Deployed Engineer`가 남는다. 이 경우 production block 전체를 복원하지 않는다.

- production/room conversation: CUT 유지
- 본문 첫 FDE 언급: `FDE(Forward Deployed Engineer·현장 배치 엔지니어)` 자막·픽업 후보
- 팔란티어 계보 등 부가 사실: 별도 검증 후 선택

유용한 정의가 production talk 안에 있다는 사실과 production audio를 방송에 복원해야 한다는 결론은 다르다.

## Local join과 global defect

2편 1:08~1:12 삭제 뒤 문법·화자 splice는 깨끗하다. 결함은 `ORPHAN`이 아니라 고유 논증의 글로벌 소실이다.

- `accepted_join_status=CLEAN`
- `pd_choice_assessment=DEFECT`
- lost proposition·retained replacement·story dependency로 과잉컷을 설명

국소 경계 상태와 전체 서사 평가는 같은 필드로 뭉개지 않는다.

## Decision ledger evidence 보강

이 사례의 spec review에서 다음 분리가 필요했다.

- semantic trimmed text 2,797/4,021자
- raw OOXML deleted text 2,815/4,033자
- `revision_id`는 원시 `w:id`, 합성 번호는 `analysis_id`
- 판단 boolean과 설명 detail 분리
- 정규화·enrichment 후 artifact를 freeze한 다음 reviewer 실행

자세한 계약은 `references/decision-ledger-evidence-contract.md`를 따른다.

## Decision ledger 최소 계약

각 판단은 다음을 가진다.

```text
source anchor와 timecode
operation과 reason
story function
retained replacement
unique fact/number/entity touch
forward/backward dependency
principle–example–conclusion dependency
accepted join status
GOLD / VALID_BUT_CASE_SPECIFIC / DEFECT / UNRESOLVED
독립 리뷰와 Main resolution
```

## Reviewer 이견의 Main 종결

- `4년째`는 두 해결이 모두 유효하다: 선행 사실을 복원하거나 후행 역참조 전제를 제거한다. 선행만 자르고 `4년째라고 하셨는데`를 남기는 상태만 결함이다.
- FDE는 production block CUT와 정의 보호가 충돌하지 않는다. production audio는 자르고 본문 첫 언급에서 정의를 회수한다.
- 국가 전략 재작성, 책 집필 동기, 어항·일론 머스크·아마겟돈 비유 압축은 사례별 선택이며 자동 규칙으로 승격하지 않는다.

## Calibration과 validator 결과

표준·schema·packet만 본 fresh reviewer가 24개 기본 문항(Q2 세부 포함 26섹션)을 모두 답했고 치명 문항 오류와 protected-content 오삭제가 0건이었다. 재현된 규칙은 production/definition 분리, retained replacement 없는 고유 명제 보호, 글로벌 dependency 검사, correction 불확실성, Track Changes 밖 accepted-state 검사다.

최종 validator는 정상 artifacts PASS뿐 아니라 adversarial mutation을 거부해야 했다. 실제 보강 항목:

- 빈 detail·analysis ID
- 중복/패턴 불일치 analysis ID
- 가짜 raw `w:id`
- fabricated `raw_ooxml_text`
- semantic text·paragraph index·operation 불일치
- manifest와 실제 DOCX raw markup 불일치

Manifest는 source authority이며 validator에 shadow constants를 두지 않는다. extractor 기대 통계와 ledger 전용 scope/row count는 별도 namespace로 둔다.

## 범용화하지 않을 것

- 이 화자가 의도적으로 영어 뒤 한국어를 반복했다는 이유로 모든 인터뷰에 `한국어 우선` 적용
- 이 시리즈의 책·3권 예고 허용량
- 신입직원·닥터스트레인지·게임·아마겟돈 같은 높은 비유 밀도
- 45분 편 길이 또는 82~87% retention

## 최종 검증 핸들

- 작업 루트: `PROJECT_ROOT/lee_juhwan_series`
- 1편 source SHA-256: `bc2806a004dccbf9276e5065b22b9916efb1327503a19b9e1d88c8c4c216c8ef`
- 2편 source SHA-256: `d4d30479c868ef444d64a42f2fea1b34c210baadb94f7515707dcea65a20fae6`
- pytest: `13 passed`
- 공식 artifact validator: `PASS`
- fresh calibration: 24/24 기본 문항, 치명 오류 0
- 최종 독립 재검증: 15개 adversarial mutation 전부 거부
- 검증 보고서: `validation/final_independent_review.md`
- artifact manifest: `validation/final_manifest.json`

검증 수치는 이 고정 source pair의 증거이며 다른 인터뷰의 retention·cut count 목표로 사용하지 않는다.
