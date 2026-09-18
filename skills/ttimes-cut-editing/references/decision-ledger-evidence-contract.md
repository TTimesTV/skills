# Decision Ledger Evidence Contract

## 목적

Track Changes 전수감사에서 `읽기 좋은 분석 문자열`과 `원본에 대한 추적 가능성`을 동시에 지키는 fail-closed 계약이다. 특정 인터뷰가 아니라 OOXML 기반 컷편집 감사 전반에 적용한다.

## Canonical state extraction

두 상태를 같은 원본에서 재현한다.

- `accepted`: `w:del`·`w:moveFrom` 제외, `w:ins`·`w:moveTo` 포함
- `restored`: `w:del`·`w:moveFrom` 포함, `w:ins`·`w:moveTo` 제외

원본 DOCX SHA-256이 manifest와 다르면 추출·감사를 중단한다. 원본은 읽기 전용으로 유지한다.

## Raw와 semantic text를 분리한다

한 필드로 두 목적을 해결하지 않는다.

- `deleted_or_inserted_text`: 앞뒤 공백을 제거한 판단용 semantic text
- `raw_ooxml_text`: `w:delText`/`w:t`의 literal text. 경계 공백·문장부호 포함

문자수도 두 개로 보고한다.

- semantic chars: 비교·분류 편의용
- raw OOXML chars: source fidelity 검증용

공백을 trim한 합계로 raw 삭제량을 대체하지 않는다.

## ID를 분리한다

- `revision_id`: 원시 OOXML `w:id`
- `analysis_id`: `EP2-R001` 같은 안정 합성 ID
- `semantic_group_id`: 인접 raw revision을 하나의 편집 판단으로 묶는 ID

합성 ID를 `revision_id`에 넣으면 XML로 직접 역추적할 수 없다. raw revision 수와 semantic defect 수를 별도 집계한다.

## Boolean과 설명을 분리한다

다음 필드는 엄격한 lowercase `true/false`만 허용한다.

- `unique_fact_lost`
- `number_or_entity_touched`
- `epistemic_qualifier_touched`

근거·고유명·숫자 목록은 각각 `*_detail`에 둔다. `없음`, `4년`, `YES: ...` 같은 설명 문자열을 boolean 필드에 넣지 않는다.

## Local join과 global story defect를 분리한다

`accepted_join_status`는 국소 splice 상태다.

- `CLEAN`: 문법·화자·구두점 경계가 정상
- `FRAGMENT`: 미완성 술어·문장 파편
- `ORPHAN`: 고아 화자·반응·지시어
- `AMBIGUOUS`: 오디오 없이는 경계 확정 불가

긴 블록을 잘라 로컬 문장은 매끈하지만 고유 논증이 사라진 경우:

- `accepted_join_status=CLEAN`
- `pd_choice_assessment=DEFECT`
- lost proposition과 dependency를 detail/Main resolution에 기록

글로벌 논증 gap을 무조건 `ORPHAN`으로 표시하지 않는다.

## Validator 최소 조건

최종 PASS는 적어도 다음을 검사한다.

1. source SHA-256
2. semantic deletion/insertion 수
3. raw deleted character 수
4. ledger exact row count
5. 필수 필드와 빈 셀
6. operation/unit/join/assessment enum
7. strict boolean 형식
8. `revision_id`가 원시 ID 형식이고 `analysis_id`가 별도 존재
9. `raw_ooxml_text` 비어 있지 않음
10. 원장 문서순 text와 raw revisions의 1:1 대조

## Review sequencing pitfall

정규화·enrichment 중인 원장을 reviewer가 동시에 읽게 하지 않는다. 그렇지 않으면 reviewer가 pre-normalization enum과 post-normalization join을 섞어 stale FAIL을 보고할 수 있다.

권장 순서:

```text
extract → ledger 작성 → normalize/enrich → validator PASS
→ artifacts freeze → independent spec review
→ 수정 → validator/test 재실행 → fresh re-review
```

검증 보고서의 분포도 ledger 변경 뒤 반드시 재산출한다. 코드가 PASS해도 보고서가 legacy reason/unit/join 분포를 담으면 documentary evidence는 stale하다.

## Manifest-driven 검증

Validator가 source path·hash·expected count를 코드에 다시 하드코딩하면 manifest가 stale하거나 변조돼도 발견하지 못한다.

- source path, SHA-256, raw markup 회계, semantic/raw revision 통계, ledger scope·행수는 manifest에서만 읽는다.
- validator는 실제 DOCX의 `w:del/w:ins/moveFrom/moveTo/strike/highlight`를 다시 세어 manifest와 대조한다.
- manifest에는 제목, runtime, 편 구간, restored/accepted 추출 계약을 포함한다.
- 녹음일이 source에 없으면 OOXML 생성일을 녹음일로 추정하지 말고 `null + UNKNOWN_NOT_IN_SOURCE`로 기록한다.
- extractor가 검사하는 `expected` 통계와 ledger 전용 `ledger_rows`를 분리한다. ledger metadata를 extractor 통계 namespace에 넣으면 재추출이 실패한다.

## Adversarial validator test

정상 artifacts PASS만으로 validator 품질을 증명하지 않는다. 임시 복사본에 다음 변조를 넣고 각각 FAIL하는지 확인한다.

- 빈 `*_detail`
- 빈·중복·패턴 불일치 `analysis_id`
- 실제 raw에 없는 `revision_id`
- `raw_ooxml_text="FABRICATED"`
- semantic text·paragraph index·operation의 raw revision 불일치
- manifest의 hash·raw markup·expected count 변조

원장 각 행은 문서순 raw revision과 `w:id`, semantic text, raw text, paragraph index, operation까지 1:1로 비교한다. 단순히 숫자형 ID·비어 있지 않은 raw text만 검사하면 fabricated evidence를 통과시킨다.

## 회귀 테스트

- raw boundary space가 있는 deletion fixture
- invalid enum 거부
- 설명 문자열이 들어간 boolean 거부
- exact row mismatch 거부
- raw `w:id` 누락/합성 ID 오용 거부
- raw deleted chars mismatch 거부
- fabricated raw text·가짜 revision ID·빈 detail의 동시 변조 거부
- manifest v2 필수 계약과 실제 DOCX raw markup 대조
- manifest 기반 extractor 재실행과 validator 동시 PASS

환경 설치 실패 같은 일시적 문제는 이 계약에 기록하지 않는다. 재사용할 것은 source-fidelity와 fail-closed 검증 방식이다.
