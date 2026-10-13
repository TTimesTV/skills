---
name: ttimes-clip-library
description: Archive cut video clips to Drive and Obsidian.
license: MIT
metadata:
  hermes:
    tags:
    - video
    - clips
    - youtube
    - google-drive
    - obsidian
    - provenance
    related_skills:
    - obsidian
    - google-workspace
    - artifact-delivery-verification
  version: 0.1.0
---

# TTimes Clip Library

## 공유 환경에서의 실행 조건

이 스킬은 제작·보관 절차를 포함하지만 개인 보관함, 세션 DB, 외부 실행기는 배포하지 않는다. 현재 사용자가 제공한 프로젝트·승인 기록과 명시적으로 지정한 보관 위치만 사용한다. 클라우드 쓰기·예약 작업은 현재 사용자가 해당 작업을 요청하고 연결이 검증된 범위에서 실행한다. 아래 과거 경로·시간표는 설정 예시이며 자동 등록이나 업로드 권한을 뜻하지 않는다.


유튜브 원본은 링크로 보존하고, 사용자가 실제로 요청해 Hermes가 절단한 편집 클립만 Google Drive와 Obsidian에 축적한다. 전체 원본 MP4를 영구 보관하거나 검증되지 않은 파일을 업로드하지 않는다.

## When to Use

- 사용자가 유튜브 영상의 특정 구간을 잘라 달라고 요청할 때
- 제작용으로 전달한 짧은 MP4를 나중에 재사용할 수 있게 등록할 때
- 기존 클립의 원본 URL·타임코드·사용 이력·Drive 위치를 찾을 때
- 클립 라이브러리의 누락·중복·무결성을 검사할 때

다음에는 사용하지 않는다.

- 전체 유튜브 영상을 영구 보관하는 아카이브
- 승인되지 않은 저작물의 대량 다운로드
- 원본 발언 아카이브 정본 구축
- 최종 편집 타임라인 자동 조립

## Prerequisites

- 로컬 프로젝트: `LOCAL_REFERENCE_NOT_DISTRIBUTED`
- Obsidian vault: `PROJECT_VAULT`
- TTimes 전용 루트: `PROJECT_VAULT/50_TTimes`
- 전역 클립 인덱스: `50_TTimes/클립 라이브러리.md`
- Google OAuth scope: `https://www.googleapis.com/auth/drive.file`
- Drive 루트: `TTimes Clip Library`
- 실행기:
  - `clip_library.py`: 로컬 검증·원장·Obsidian 반영
  - `drive_connector.py`: 좁은 권한의 Drive 업로드·읽기검증

Google Drive 커넥터에는 삭제 명령이 없다. `drive.file` 범위 밖의 기존 Drive 파일에는 접근하지 않는다.

## Procedure

### 1. 원본 계보 확정

유튜브 URL, 영상 ID, 공식 제목·채널, 원본 IN·OUT을 확정한다. 원본 타임코드가 불명확하면 추측하지 말고 `미확인` 상태로 등록한다.

완료 조건: URL에서 추출한 영상 ID와 기록할 영상 ID가 일치한다.

### 2. 클립 생성·검증

사용자가 지정한 구간을 절단하되 편집용 핸들은 요청 범위와 프로젝트 필요에 맞춘다. 완성 클립에 `ffprobe`를 실행해 재생 가능한 영상·음성 스트림, 양수 길이, 파일 크기를 확인하고 SHA-256을 계산한다.

완료 조건: `ffprobe` 성공, 길이 양수, 재생 스트림 존재. OneDrive placeholder나 0으로 채워진 파일은 실패다.

### 3. 로컬 원장과 Obsidian 등록

`terminal`로 다음 형태를 실행한다.

```bash
python3 'LOCAL_REFERENCE_NOT_DISTRIBUTED' register \
  --source-url 'YOUTUBE_URL' \
  --source-title 'SOURCE_TITLE' \
  --channel 'CHANNEL' \
  --clip-path '/absolute/path/clip.mp4' \
  --clip-title 'CLIP_TITLE' \
  --source-in 'HH:MM:SS' \
  --source-out 'HH:MM:SS' \
  --source-note '/absolute/path/existing_source_note.md' \
  --description 'SCENE_DESCRIPTION' \
  --project 'PROJECT' \
  --tags 'TAG1,TAG2,TAG3'
```

기존 canonical source note를 우선 사용한다. 새 임의 폴더를 만들지 않는다. 같은 clip ID는 새 항목을 추가하지 않고 갱신한다.

완료 조건: JSON 원장과 source note의 자동관리 블록, `클립 라이브러리.md` 인덱스가 모두 같은 clip ID를 가진다.

### 4. Drive 승격

미디어가 검증됐고 사용자가 제작용 클립 전달을 요청한 작업이면, 설정된 라이브러리로 자동 승격한다.

```bash
'LOCAL_REFERENCE_NOT_DISTRIBUTED' \
  'LOCAL_REFERENCE_NOT_DISTRIBUTED' upload 'CLIP_ID'
```

업로드기는 영상 ID 하위 폴더를 생성하고 파일을 올린 뒤 Drive의 size와 MD5를 로컬 파일과 비교한다. 일치할 때만 원장과 Obsidian에 Drive 링크를 기록한다.

완료 조건: 상태 `uploaded_and_verified`, 로컬·Drive size 일치, MD5 일치, `webViewLink` 읽기 성공.

### 5. 최종 검증

```bash
python3 'LOCAL_REFERENCE_NOT_DISTRIBUTED' verify
```

완료 조건: `pass: true`, 중복 clip ID 0, 영상 ID 불일치 0, source note 누락 0. 사용자에게는 클립 전달 결과와 등록·Drive 상태만 간결히 알린다.

## Pending Media Handling

OneDrive placeholder, 손상 MP4, 미확인 타임코드는 `--allow-invalid`로 메타데이터만 등록할 수 있다. 이 상태는 반드시 `pending_media_recovery`로 남기며 Drive에 업로드하지 않는다. 복구 후 동일 항목을 유효 파일과 정확한 IN·OUT으로 다시 등록한다.

## Safety Rules

- 전체 원본 영상은 임시 처리 후 삭제하고, 실제 선택 클립만 보존한다.
- Drive 파일 삭제·영구삭제·공유권한 변경을 실행하지 않는다.
- OAuth 토큰·인증 코드·클라이언트 비밀을 채팅이나 결과물에 출력하지 않는다.
- 원본 URL·원본 시각·프로젝트 사용 이력·해시를 보존한다.
- 검증되지 않은 MP4는 업로드하지 않는다.
- Drive 업로드 성공 응답만 믿지 말고 size·MD5·webViewLink를 읽어 검증한다.

## Pitfalls

- OneDrive `.noindex` 경로의 파일은 크기가 있어도 실제 내용이 0으로 채워진 placeholder일 수 있다.
- 영상 ID가 같은 원본에서 여러 클립이 나올 수 있으므로 원본 노트는 하나, clip ID는 구간별로 분리한다.
- Drive 로컬 경로는 기기마다 달라지므로 Obsidian에는 `webViewLink`와 파일 ID를 기록한다.
- 원본 시간이 불명확한데 클립 길이만 보고 타임코드를 역추정하지 않는다.

## Verification Checklist

- [ ] YouTube URL·영상 ID 일치
- [ ] source IN < source OUT
- [ ] ffprobe 성공·양수 길이·스트림 존재
- [ ] SHA-256 기록
- [ ] JSON 원장·source note·전역 인덱스 clip ID 일치
- [ ] Drive size·MD5 일치
- [ ] Drive 링크 읽기 성공
- [ ] 삭제·공유·공개 설정 변경 없음
