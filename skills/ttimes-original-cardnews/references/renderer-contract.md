# Renderer contract — original-editorial-4x5-v1

실행 확인 환경: `PROJECT_ROOT/python` (Pillow 설치), macOS 시스템 한글·영문 폰트.

```bash
PROJECT_ROOT/python PROJECT_ROOT/render_editorial_cards.py /absolute/path/cards.json /absolute/path/new_output
```

## 실제 최초 에피소드

- 원고·출처: `PROJECT_ROOT/cards.json`
- 실제 사진·공식 로고: 같은 작업의 `assets/`
- 렌더러: 이 스킬의 `scripts/render_editorial_cards.py`
- 형식 상태: 사용자에게 제시할 후보. 승인 정본 아님.

## 입력

JSON top-level: `title`, `format`, `size: [1080,1350]`, `status`, `date`, `photo`, `logo`, `pages`, `sources`.
`pages`는 `id`가 1부터 연속되고 중복이 없어야 한다. 각 페이지는 `layout`, `kicker`, 줄 배열 `title`, `source_ids`를 갖는다. 출처표는 키별 URL/DOI/범위/권리 상태를 보존한다.

레이아웃별 필드:
- cover: deck, byline, photo_credit, photo_note. top-level photo/logo 사용.
- policy: stat, stat_label, scope, rows[[label,body]], note, source.
- contrast: context, metrics[{value,label,color}], note, source. 두 지표용이며 비교 대상/단위는 명시해야 한다.
- compare: panels[{label,headline,body}], conclusion, note, source. 두 패널.
- number: value, metric, body, note, source.
- limits: rows[[label,body]], conclusion, source. 세 범위.
- steps: intro, steps[[number,title,body]], note, source. 세 단계.
- workplace: question 줄 배열, body, note, source. 이 레이아웃 이름이 직장 이야기를 모든 뉴스에 강제하지 않는다.
- discussion: intro, options[[label,text]], closing, source. 세 선택지이며 자유 응답을 포함한다.

현재 렌더러의 행·패널 수와 좌표는 위 사례에 맞춘 제한된 시작점이다. 더 많은 행/패널, 다른 화면비, 추가 시각물을 자동 수용한다고 주장하지 않는다. 새 설계에는 별도 레이아웃을 구현·검증한다. 고정된 9장 수가 아니라 각 페이지의 독립 논점으로 페이지 수를 정한다.

## 출력

연속 번호 PNG, 다중 페이지 PDF, 전체 미리보기 JPG, `render_manifest.json`(페이지별 해시·텍스트 박스·출처 ID).

PDF 파일명은 JSON의 `output_basename`으로 지정한다(미지정 시 `cardnews.pdf`). 정확한 조판은 2배 해상도에서 계산 후 1080×1350으로 축소한다. 글자 넘침은 실패 처리한다. 텍스트 박스 검사는 시각·사실 검수를 대체하지 않는다.

## 사용 제한

사진 원본과 로고의 권리를 별도로 확인한다. AFP 크레딧은 AFP가 실제 원출처일 때만 적용한다. 시스템 폰트 파일은 재배포하지 않는다. 배포 패키지와 사용자 계정으로의 공개 게시를 혼동하지 않는다.
