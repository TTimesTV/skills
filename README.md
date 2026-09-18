# TTimes Skills

티타임즈 제작 업무를 위한 팀 공유용 스킬 16개를 관리하는 저장소입니다. 각 스킬의 지침, 참고자료, 실행 스크립트, 템플릿, 예제와 기존 테스트를 함께 보관합니다.

## 스킬 목록

| 스킬 | 용도 |
| --- | --- |
| [ttimes-article-selection](skills/ttimes-article-selection/SKILL.md) | 발언을 직접 뒷받침하는 기사·헤드라인 선정 |
| [ttimes-audio-rough-cut-rendering](skills/ttimes-audio-rough-cut-rendering/SKILL.md) | 승인된 컷 결정에 따른 오디오 가편집 |
| [ttimes-cardnews-imagegen](skills/ttimes-cardnews-imagegen/SKILL.md) | 원고 기반 카드뉴스 제작과 이미지 생성 |
| [ttimes-cut-editing](skills/ttimes-cut-editing/SKILL.md) | 인터뷰 컷 결정과 편집 지시 DOCX 작성 |
| [ttimes-editorial-copy](skills/ttimes-editorial-copy/SKILL.md) | 강조·설명·질문 등 화면 편집자막 작성 |
| [ttimes-elevenlabs-dubbing-csv](skills/ttimes-elevenlabs-dubbing-csv/SKILL.md) | 영어 더빙·믹싱·자막·썸네일 패키지 |
| [ttimes-factcheck-research](skills/ttimes-factcheck-research/SKILL.md) | 수치·인용·기술 주장 팩트체크 |
| [ttimes-original-cardnews](skills/ttimes-original-cardnews/SKILL.md) | 취재·리서치 기반 오리지널 카드뉴스 |
| [ttimes-pd-material-planning-evaluation](skills/ttimes-pd-material-planning-evaluation/SKILL.md) | 영상 전체의 PD 자료 기획 평가 |
| [ttimes-production-automation](skills/ttimes-production-automation/SKILL.md) | 제작 단계·역할·자동화 범위 설계 |
| [ttimes-screen-composition](skills/ttimes-screen-composition/SKILL.md) | 최종 컷에 맞춘 자막·자료 화면구성 |
| [ttimes-script-and-srt](skills/ttimes-script-and-srt/SKILL.md) | 영상·음성·YouTube 기반 한국어 원고와 SRT |
| [ttimes-shorts-rendering](skills/ttimes-shorts-rendering/SKILL.md) | 가로 영상 하이라이트를 세로 쇼츠로 렌더링 |
| [ttimes-square-carousel-cover](skills/ttimes-square-carousel-cover/SKILL.md) | 티타임즈 스타일 정사각형 캐러셀 표지 |
| [ttimes-youtube-timestamps](skills/ttimes-youtube-timestamps/SKILL.md) | YouTube CC 기반 설명란 타임스탬프 |
| [ttimes-youtube-upload-package](skills/ttimes-youtube-upload-package/SKILL.md) | 해시태그·타임스탬프·고정댓글 업로드 패키지 |

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

## 팀 공유 범위와 의존성

- 개인 보관함 연동 전용 `ttimes-clip-library`, `ttimes-production-ledger`는 제외했습니다.
- 개인 Google Drive·OneDrive·Obsidian 연결, 자동 업로드, 개인 대화 DB, 개인 저장 경로와 브라우저 인증정보 재사용 지시는 제외했습니다.
- 현재 작업에서 팀원이 제공한 파일과 지정한 프로젝트 폴더를 사용합니다. 필요한 외부 서비스는 각 팀원이 자기 환경에서 별도로 준비합니다.
- 기존 Hermes/Mac 제작 환경에서 축적한 지침을 포함합니다. MLX, ffmpeg, ElevenLabs, 이미지 도구, 글꼴 및 외부 실행기는 사용 환경에 맞게 준비해야 합니다. 설치만으로 이 의존성이 구성되지는 않습니다.
- `PROJECT_ROOT/`, `PROJECT_OUTPUT/`는 해당 작업의 폴더를 뜻하는 예시 표기입니다. `LOCAL_REFERENCE_NOT_DISTRIBUTED`는 배포하지 않은 과거 개인 산출물 경로를 제거한 표시입니다. 파일 존재를 가정하지 말고 포함된 기준 자료를 사용하거나 팀원이 기준본을 제공하도록 합니다.
- 스킬 폴더에 포함된 기준 이미지·문서와 편집 교정 사례는 보존했습니다. 원본 영상·음성, 계정 설정과 인증 파일은 포함하지 않습니다.

## 수정·배포

이 저장소에서 수정 → 변경 검토·검증 → Git 커밋·푸시 → 사용 PC에 업데이트 순서로 관리합니다. 변경은 별도 브랜치와 PR로 검토할 수 있으며, 이미 공유한 커밋의 수정은 `git revert`로 되돌릴 수 있습니다.

초기 가져오기 범위와 검증 결과는 [IMPORT-REPORT.md](IMPORT-REPORT.md), 파일별 해시는 [manifest.json](manifest.json)에 있습니다. 외부 API를 호출하는 실제 제작 작업 전체를 검증한 배포는 아닙니다.

## 공개 범위와 권리

이 저장소에는 제작 지침과 교정 사례, 기준 이미지 및 문서가 포함됩니다. API 키·인증 파일·원본 영상·음성·대화 DB는 배포 대상이 아닙니다. 기존 파일에 명시된 라이선스는 보존하며, 저장소 전체에 새 라이선스를 임의로 부여하지 않았습니다. 포함된 이미지·문서와 상표의 이용 권리는 각 권리자에게 있습니다.
