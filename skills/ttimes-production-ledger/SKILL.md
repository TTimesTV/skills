---
name: ttimes-production-ledger
description: Curate and qualify TTimes versions overnight.
license: MIT
metadata:
  hermes:
    tags:
    - TTimes
    - Obsidian
    - Ledger
    - Production
    - Reconciliation
    related_skills:
    - ttimes-production-automation
    - session-librarian
  version: 0.2.0
  platforms:
  - macos
---

# TTimes Overnight Qualification Ledger

## 공유 환경에서의 실행 조건

이 스킬은 제작·보관 절차를 포함하지만 개인 보관함, 세션 DB, 외부 실행기는 배포하지 않는다. 현재 사용자가 제공한 프로젝트·승인 기록과 명시적으로 지정한 보관 위치만 사용한다. 클라우드 쓰기·예약 작업은 현재 사용자가 해당 작업을 요청하고 연결이 검증된 범위에서 실행한다. 아래 과거 경로·시간표는 설정 예시이며 자동 등록이나 업로드 권한을 뜻하지 않는다.


사용자가 자는 동안 당일 TTimes 산출물을 프로젝트별로 모아 **초안·후보·최종본의 계보를 정리하고 퀄리피케이션하는 스킬**이다. 제작 중 매 턴 기록하지 않고, 야간 배치에서 권위본·승인 근거·품질 격차·병목·다음 실험을 정리한다.

## When to Use

- 매일 야간 배치에서 당일 TTimes 세션과 산출물을 정리할 때
- 같은 프로젝트에 `draft`, `v2`, `final`, QA본이 섞여 권위본 계보가 필요할 때
- 사용자 승인·거절·수정 지시를 다음 제작의 품질 기준으로 승격할 때
- 전날 최종본과 당일 후보를 비교해 퀄리피케이션 결과를 남길 때

다음에는 사용하지 않는다.

- 제작 중간의 매 메시지·매 파일 생성 직후
- 대화만 있었고 프로젝트 상태·결정·산출물이 바뀌지 않았을 때
- 원시 채팅 전체를 Obsidian에 복제할 때
- 파일명에 `final`이 있다는 이유만으로 완료를 추정할 때

## Canonical Locations

- Vault: `PROJECT_VAULT`
- Master: `PROJECT_VAULT/50_TTimes/제작 레저.md`
- Formats: `PROJECT_VAULT/50_TTimes/01_대담`~`07_업로드·채널`
- Operations: `PROJECT_VAULT/50_TTimes/90_운영`
- Sync state: `PROJECT_VAULT/50_TTimes/90_운영/TTimes 레저 동기화 상태.md`
- Working roots: `LOCAL_REFERENCE_NOT_DISTRIBUTED`, `LOCAL_REFERENCE_NOT_DISTRIBUTED`, `LOCAL_REFERENCE_NOT_DISTRIBUTED`

## Evidence Hierarchy

강한 근거부터 적용한다.

1. 사용자의 명시적 승인·거절·수정 지시
2. 외부 시스템의 실제 읽기 검증
3. 통합 QA의 명시적 `PASS`·`FAIL`
4. 개별 QA·manifest·SHA-256
5. 산출물 파일 존재
6. 세션의 계획·설명

상위 근거와 하위 근거가 충돌하면 상위 근거를 따른다. `QA PASS`, `사용자 승인`, `납품`, `게시`, `표출 확인`은 서로 다른 상태다.

## Qualification Levels

- `unqualified_draft` — 제작 중 초안; 비교·학습용
- `candidate` — 완성 후보이나 통합 QA 또는 사용자 판단 전
- `provisional` — 기계적 QA 통과, 사용자 승인 전
- `qualified` — 사용자 승인과 요구된 QA를 모두 충족
- `disqualified` — 사용자 거절 또는 치명적 QA 실패
- `superseded` — 더 최신의 qualified 권위본으로 대체됨

파일명 `final`은 퀄리피케이션 근거가 아니다. **사용자 승인 + 필요한 QA**가 있어야 `qualified`, 그중 현재 권위본만 `final`로 기록한다.

야간 기록에는 프로젝트마다 다음을 남긴다.

1. 버전 계보: 초안 → 수정안 → 후보 → 잠정 통과 → 승인 최종본
2. 현재 권위본과 근거 파일
3. 이전 버전보다 좋아진 점
4. 아직 미달한 점과 주 병목
5. 다음 제작에서 유지·폐기·재시험할 규칙

## Bottleneck Field

모든 활성 프로젝트에는 현재 진행을 막는 **단 하나의 주 병목**을 기록한다.

- `approval` — 사용자 선택·승인 대기
- `source` — 원본·인용·팩트 근거 미확정
- `speaker_or_transcript` — 화자·전사·싱크 불확실
- `production` — 생성·편집·렌더 미완료
- `qa` — 기계적 QA 실패 또는 미실행
- `delivery` — 납품 대상·최종 패키지 미확정
- `publish_verification` — 게시됐으나 외부 표출 미확인
- `external_dependency` — 로그인·권한·서비스·사람 의존
- `none` — 다음 단계가 막히지 않음

병목에는 `종류 / 증거 / 해소 조건 / 담당`을 함께 쓴다. 여러 문제가 있더라도 다음 상태 전이를 가장 먼저 막는 하나만 주 병목으로 선택한다.

## Procedure

1. **야간 인벤토리.** 당일 자정 전후 변경된 세션과 제작 파일을 프로젝트 ID·영상 ID·canonical path로 묶는다. 완료 조건: 새 파일과 수정 파일이 프로젝트별로 전부 귀속됨.
2. **버전 계보 작성.** 파일명·mtime만 믿지 말고 manifest·hash·handoff·세션 결정으로 초안, 수정안, 후보, 이전 권위본을 배열한다. 완료 조건: 버전마다 역할과 근거가 있음.
3. **근거 확인.** QA JSON, 사용자 승인·거절, 외부 표출을 직접 읽는다. 완료 조건: 각 qualification 판정에 근거 경로 또는 세션이 있음.
4. **퀄리피케이션.** `unqualified_draft`~`superseded` 중 하나를 지정하고 현재 final을 최대 1개만 둔다. 완료 조건: `final`과 `qualified`를 혼동하지 않음.
5. **품질 비교.** 이전 후보와 현재 후보의 개선·퇴행·미검증 항목을 사용자 기준과 QA 항목으로 비교한다. 디자인을 임의 평가하지 않고 PD가 보는 자료 선택·발화 싱크·강조자막과 명시된 제작 요구를 우선한다.
6. **학습 규칙 추출.** 명시 승인된 변화는 `유지`, 거절된 변화는 `폐기`, 근거가 약한 변화는 `재시험`으로 기록한다. 한 프로젝트의 우연한 성공을 전역 스킬 규칙으로 승격하지 않는다.
7. **레저 갱신.** 형식 레저·마스터·그날의 `야간 퀄리피케이션` 노트를 갱신한다. 교차 공정에는 링크만 두고 정본을 복제하지 않는다.
8. **커서 갱신.** 모든 파일·wikilink·근거 검증이 끝난 뒤에만 `last_success_at`을 전진시킨다. 실패 시 전진시키지 않는다.
9. **보고.** Obsidian 기록이 본체다. 실질 변경이 없으면 `[SILENT]`; 있으면 로컬 출력에 승격·탈락·병목만 남긴다.

## Periodic Reconciliation

- 매일 02:40 KST에 no-agent snapshot으로 당일 세션·제작 파일 변경을 고정한다
- 매일 03:20 KST에 변경이 있을 때만 이 스킬로 버전 정리와 퀄리피케이션을 수행한다
- 낮에는 제작과 QA에 집중하고 레저는 원칙적으로 야간에 한 번 정리한다
- 사용자가 명시적으로 지금 기록하라고 한 경우에만 주간 즉시 갱신한다
- 원시 대화와 대용량 산출물은 vault에 복사하지 않는다

## Pitfalls

- 긴 Telegram 세션 하나에 여러 제작 유형이 섞인다. 세션 전체를 단일 프로젝트로 간주하지 않는다
- CLI subagent 수는 작업량과 같지 않다. 세션 수를 성과 지표로 쓰지 않는다
- `final`, `approved`, `pass`가 파일명에 포함돼도 파일 본문이나 사용자 결정으로 재확인한다
- 최신 수정 후보가 기존 QA PASS보다 새롭더라도 검증 전에는 권위본으로 승격하지 않는다
- API 키·봇 토큰·Authorization 헤더·자격 증명을 기록하지 않는다

## Verification

- 수정한 Markdown의 frontmatter와 H1이 유효함
- 새 `[[wikilink]]`가 모두 기존 노트로 해석됨
- canonical path와 QA path가 실제로 존재함
- 상태 변화마다 근거 세션 또는 근거 파일이 있음
- 활성 프로젝트마다 주 병목이 정확히 하나 있음
- 선언한 프로젝트 수·세션 수는 프로그램 재집계값과 일치함
- 외부 상태 변경은 실제 대상을 읽어 확인함
