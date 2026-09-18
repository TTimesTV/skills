# 2026-07 TTimes 역할·자동화 캘리브레이션

## 사용자 요청에서 확정된 구분

```text
PD = 무엇을, 왜, 언제 보여줄지 결정
영상편집디자이너 = 어떻게 보이게 만들지 구현
자동화 = 반복 실행, 후보 생성, 기계적 검수
```

## 당시 확인된 제작 스킬 상태

### Operational artifact workflows

- `media-localization-workflows`: MLX ASR, 화자분리, 컷 전 싱크 DOCX
- `ttimes-cut-editing`: KEEP/CUT/MOVE/리테이크 판단과 컷편집 DOCX
- `ttimes-audio-rough-cut-rendering`: 승인 컷 기반 오디오 러프컷
- `ttimes-script-and-srt`: 최종 컷 말자막·SRT
- `ttimes-article-selection`: 주장 입증형 기사·헤드라인 선정
- `ttimes-youtube-timestamps`: 챕터
- `ttimes-youtube-upload-package`: 해시태그·타임스탬프·고정댓글

### Partial/specification workflows

- `caption-layering-workflow`: 강조·설명자막 작성은 가능하나 전체 원고 자동 탐지→승인→NLE 전달 시스템은 없음
- `ttimes-screen-composition`: 화면구성·자료-완료 DOCX 설계는 가능하나 NLE 자동 변환은 없음
- `youtube-editorial-strategy`: 제목·썸네일·오프닝 전략은 가능하나 자동 디자인·성과연동은 없음

### Concept-only items at calibration time

- persistent `SEG/CAP/ART/ASSET` manifest
- `DRAFT → PD_APPROVED → LOCKED → DESIGN_IMPLEMENTED → QA_PASS` state engine
- 촬영 카드 인제스트·프록시·멀티캠 NLE 자동화
- 설명자막 일괄 탐지·근거 검색·PD 승인 파이프라인
- Premiere/Resolve/Final Cut marker/template automation
- 자료 권리 DB, integrated master QA, CMS publishing, analytics feedback loop

Do not treat this dated snapshot as permanent. Re-inspect live skills, scripts, NLE plugins, and project artifacts before each new audit.

## High-value user correction

The user wrote `오픈라우터 -> 설명자막` intending a direct explainer-caption request. It was incorrectly expanded into an OpenRouter automation pipeline. Correct routing:

```text
OpenRouter : OpenAI, 앤트로픽, 구글 등 여러 회사의 AI 모델을 하나의 API로 연결해, 비용·성능·용도에 따라 원하는 모델을 선택해 사용할 수 있게 해주는 AI 모델 중개 플랫폼
```

Likewise:

```text
라우팅(Routing) : 사용자의 요청을 목적·비용·속도·성능 등의 조건에 맞는 AI 모델로 보내는 과정

라우터(Router) : 요청의 내용과 조건을 판단해 가장 적합한 AI 모델이나 처리 경로를 선택·연결하는 시스템
```

Lesson: in active caption work, `X → 설명자막` is a deliverable arrow, not a systems diagram.
