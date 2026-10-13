# TTimes Skills

티타임즈 제작 업무를 위한 팀 공유용 스킬 21개를 관리하는 저장소입니다. 각 스킬의 지침, 참고자료, 실행 스크립트, 템플릿, 예제와 기존 테스트를 함께 보관합니다.

## 스킬 목록

| 스킬 | 용도 |
| --- | --- |
| [ttimes-ai-video-direction](skills/ttimes-ai-video-direction/SKILL.md) | AI 영상 연출 |
| [ttimes-article-selection](skills/ttimes-article-selection/SKILL.md) | 기사와 헤드라인 선정 |
| [ttimes-audio-rough-cut-rendering](skills/ttimes-audio-rough-cut-rendering/SKILL.md) | 승인 컷 기반 음원 렌더 |
| [ttimes-cardnews-imagegen](skills/ttimes-cardnews-imagegen/SKILL.md) | 원고 기반 카드뉴스 |
| [ttimes-clip-library](skills/ttimes-clip-library/SKILL.md) | 편집 클립 보관 절차 |
| [ttimes-cut-editing](skills/ttimes-cut-editing/SKILL.md) | 인터뷰 컷 결정 |
| [ttimes-editorial-copy](skills/ttimes-editorial-copy/SKILL.md) | 화면 편집자막 |
| [ttimes-elevenlabs-dubbing-csv](skills/ttimes-elevenlabs-dubbing-csv/SKILL.md) | 영어 더빙 패키지 |
| [ttimes-explainer-graphics](skills/ttimes-explainer-graphics/SKILL.md) | 설명 그래픽 |
| [ttimes-factcheck-research](skills/ttimes-factcheck-research/SKILL.md) | 팩트체크 |
| [ttimes-guest-profile](skills/ttimes-guest-profile/SKILL.md) | 출연자 프로필 |
| [ttimes-original-cardnews](skills/ttimes-original-cardnews/SKILL.md) | 리서치 카드뉴스 |
| [ttimes-pd-material-planning-evaluation](skills/ttimes-pd-material-planning-evaluation/SKILL.md) | 영상 자료 기획 평가 |
| [ttimes-production-automation](skills/ttimes-production-automation/SKILL.md) | 제작 공정과 자동화 설계 |
| [ttimes-production-ledger](skills/ttimes-production-ledger/SKILL.md) | 제작 버전과 승인 원장 |
| [ttimes-screen-composition](skills/ttimes-screen-composition/SKILL.md) | 화면구성 |
| [ttimes-script-and-srt](skills/ttimes-script-and-srt/SKILL.md) | 싱크와 말자막 |
| [ttimes-shorts-rendering](skills/ttimes-shorts-rendering/SKILL.md) | 쇼츠 렌더 |
| [ttimes-square-carousel-cover](skills/ttimes-square-carousel-cover/SKILL.md) | 캐러셀 표지 |
| [ttimes-youtube-timestamps](skills/ttimes-youtube-timestamps/SKILL.md) | 유튜브 챕터 |
| [ttimes-youtube-upload-package](skills/ttimes-youtube-upload-package/SKILL.md) | 유튜브 업로드 패키지 |

## Codex에서 설치하기

Codex에 다음처럼 요청합니다. GitHub에 파일을 올리는 작업과 각 PC에 설치하는 작업은 별개입니다.

```text
$skill-installer
https://github.com/TTimesTV/skills 저장소의 skills/ 아래에 있는
ttimes-* 스킬을 모두 설치해줘. 이미 설치된 스킬은 변경 내역을 비교하고
기존 버전을 백업한 뒤 업데이트해줘.
```

하나만 설치하려면 해당 폴더를 지정합니다.

```text
$skill-installer https://github.com/TTimesTV/skills/tree/main/skills/ttimes-screen-composition
```

기본 설치 도구는 같은 이름의 설치 폴더가 이미 있으면 중단합니다. 위 업데이트 요청은 비교·백업을 포함한 별도 작업이며 자동 동기화를 의미하지 않습니다. 스킬 설치 후 다음 대화에서 확인하고, 보이지 않으면 앱을 다시 시작합니다.

## 사용 예시

```text
ttimes-script-and-srt 스킬로 이 영상의 한국어 원고와 SRT를 만들어줘.
ttimes-cut-editing 스킬로 이 인터뷰의 컷 편집안을 작성해줘.
ttimes-screen-composition 스킬로 이 최종 원고의 화면구성안을 만들어줘.
ttimes-youtube-upload-package 스킬로 이 영상의 업로드 패키지를 만들어줘.
```

각 스킬의 SKILL.md에 있는 입력 조건과 검증 절차를 따릅니다.

## 저장소 구조

```text
skills/<skill-name>/SKILL.md
skills/<skill-name>/references/
skills/<skill-name>/scripts/
skills/<skill-name>/templates/
skills/<skill-name>/assets/
skills/<skill-name>/tests/
```

하위 폴더는 해당 스킬에 있는 경우에만 포함됩니다. 참고자료의 상대 경로를 유지하도록 개별 파일 대신 스킬 폴더 전체를 설치합니다.

## Gemini와 다른 AI에서 읽기

[GEMINI.md](GEMINI.md)를 먼저 읽고 해당 작업의 SKILL.md와 연결된 references를 사용합니다. GitHub의 Code → Download ZIP으로 전체 폴더를 받을 수 있습니다. 문서를 제공하는 것은 작업 지침으로 사용하는 것이며 모델 가중치의 영구 학습을 뜻하지 않습니다.

## 팀 공유 범위와 의존성

- 2026-10-14 사용자 요청으로 현재 티타임즈 스킬 21개 전체를 포함했습니다. 기존 배포에서 제외했던 클립 보관·제작 원장·자동화 설계도 절차 참고용으로 포함합니다.
- API 키, 인증 파일, 개인 대화 DB, 브라우저 프로필, 원본 음성·영상은 포함하지 않습니다. 개인 절대 경로는 공유용 표시로 바꿨으며 설치된 로컬 원본은 수정하지 않았습니다.
- PROJECT_ROOT, PROJECT_OUTPUT, PROJECT_VAULT는 사용자가 지정할 위치입니다. LOCAL_REFERENCE_NOT_DISTRIBUTED는 저장소에 없는 과거 파일·실행기를 뜻합니다. 존재하거나 실행된 것으로 간주하지 마세요.
- 전사 기본 경로는 ElevenLabs Scribe v2입니다. ELEVENLABS_API_KEY 환경변수 또는 --env 파일을 사용합니다. 공통 env 경로는 ELEVENLABS_ENV_FILE로 지정할 수 있습니다. 과거 문서의 로컬 전사 엔진 지침은 최신 기본 경로보다 우선하지 않습니다.
- JEV는 TYPESAFE_API_KEY 환경변수 또는 JEV_ENV_FILE로 지정한 env 파일이 필요합니다. 호출·캐시·사용량을 기록하고 결과를 직접 검토합니다. Gemini에서 키·도구가 없으면 미실행으로 표시하며 실행한 척하지 않습니다.
- ffmpeg, Word, 폰트, 이미지 생성, 브라우저, 클라우드 및 외부 실행기는 각각의 환경에서 준비해야 합니다. 파일 동기화가 전체 제작 자동화의 실행 성공을 보장하지 않습니다.
- Drive·OneDrive·Obsidian과 야간 예약은 별도 설정이 필요한 선택 기능입니다. 이 저장소를 읽었다는 이유로 업로드나 예약을 실행하지 않습니다.
- 기준 이미지·문서 및 편집 사례는 포함된 범위에서 보존했습니다. 보고서 외부 경로가 있다고 실제 회차 원본까지 배포된 것은 아닙니다.

## 수정·배포

이 저장소에서 수정 → 변경 검토·검증 → Git 커밋·푸시 → 사용 PC에 업데이트 순서로 관리합니다. 변경은 별도 브랜치와 PR로 검토할 수 있으며, 이미 공유한 커밋의 수정은 `git revert`로 되돌릴 수 있습니다.

초기 가져오기 범위와 검증 결과는 [IMPORT-REPORT.md](IMPORT-REPORT.md), 최신 동기화 내역은 [SYNC-REPORT-20261014.md](SYNC-REPORT-20261014.md), 파일별 해시는 [manifest.json](manifest.json)에 있습니다. 외부 API를 호출하는 실제 제작 작업 전체를 검증한 배포는 아닙니다.

## 공개 범위와 권리

이 저장소에는 제작 지침과 교정 사례, 기준 이미지 및 문서가 포함됩니다. API 키·인증 파일·원본 영상·음성·대화 DB는 배포 대상이 아닙니다. 기존 파일에 명시된 라이선스는 보존하며, 저장소 전체에 새 라이선스를 임의로 부여하지 않았습니다. 포함된 이미지·문서와 상표의 이용 권리는 각 권리자에게 있습니다.
