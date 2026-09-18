# TTimes 승인 표지 2종 — 전 포맷 공통 비교 기준

## 승인 자산

### 이중학–윤명훈

- Asset: `assets/approved-lee-junghak-ai-slop-cover.png`
- SHA-256: `2e8c1ab7cf5a1eadb1f2905f7e368bc53f19f46d344fdc61350f05b1965c717d`
- Historical typography: 79px, white + periwinkle
- Historical logo position: upper-left

### 박영선–박철민

- Asset: `assets/approved-park-tech-talk-mlcc-fcbga-cover.png`
- SHA-256: `70551267b29eb731490c1eb056bb5ca4f06e6f2ebf6a8cfc913380b5d27e1d07`
- Historical typography: 68/61px, white + teal
- Logo position: upper-right

과거 픽셀값과 이중학 표지의 좌측 로고는 승인 당시 기록이다. 신규·재제작에서는 사용자가 확정한 전역 타이포 80px과 우측 상단 로고를 적용한다.

## 두 승인본의 공통 표지 문법

```text
exact article `_list_`
→ center square crop
→ 얼굴·핵심 오브젝트 보호
→ 필요한 만큼의 restrained dark lower gradient
→ 하단 대형 제목
→ 공식 TTimes 로고 우측 상단
```

### 반드시 공통으로 적용

1. 실제 `_list_`를 그대로 사용한다. ImageGen 재해석 금지.
2. 제목은 하단의 큰 로어서드로 구성한다. 빈 공간을 찾았다는 이유로 상단 구석에 작은 카피를 띄우지 않는다.
3. 제목 배경은 가독성을 위한 절제된 암색 그라데이션만 허용한다.
4. 형광펜, 불투명 색상판, 빨간 직물판, 둥근 박스, 경고 박스, 시리즈 배지를 표지에 임의로 추가하지 않는다.
5. 제목의 강조는 글자색으로만 처리한다.
6. 제목은 표지 80px 고정이며 행 수·색·정렬만 실제 문구와 이미지에 맞게 바꾼다.
7. 공식 TTimes 로고는 우측 상단에 둔다.
8. 게스트 프로필, 직함, 출처, 날짜, 타임코드를 넣지 않는다.
9. 얼굴뿐 아니라 로봇 손·제품·기술 오브젝트처럼 제목의 근거가 되는 핵심 물체도 보호한다.

## 시리즈·형식별로 달라질 수 있는 것

- 제목 행 수
- 제목 정렬과 x/y
- 흰색 이외의 한 가지 강조색
- 그라데이션 방향과 강도
- 정사각 크롭 초점
- 인물·제품·로봇·기술 오브젝트의 상대적 비중

## Blocking comparison gate

새 표지를 만들기 전에 두 승인 이미지를 실제로 불러와 타깃 표지와 연락판으로 비교한다. 다음 중 하나면 차단한다.

- 타깃만 상단 작은 제목
- 타깃만 불투명 컬러 하단판
- 타깃만 둥근 제목 박스·형광펜
- 타깃만 임의 시리즈명·프로필·출처
- `_list_` 핵심 오브젝트를 그래픽 판으로 소실
- 승인본보다 제목 위계가 현저히 약함

기술 QA가 PASS여도 이 승인본 비교가 없으면 표지를 완료 처리하지 않는다.
