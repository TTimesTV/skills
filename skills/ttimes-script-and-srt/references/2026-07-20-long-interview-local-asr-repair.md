# 긴 무자막 기술 인터뷰: 국소 ASR 환각 복구와 초안 신선도

## 적용 상황

- 20분 이상 한국어 기술 인터뷰
- YouTube 자막 비활성화
- 5분 청크 MLX를 사용했지만 특정 청크 내부에서 10~30초 반복 토큰·단어 루프·의미 붕괴가 발생
- 승인 샘플 이후 전체 본문을 만들고 있는 단계

## 검증된 흐름

1. **소스 고정**
   - YouTube 페이지가 재생되는데 CLI가 `No video formats found`를 내면 실행 파일과 `python3 -m yt_dlp` 버전을 비교한다.
   - 더 최신인 호출 경로로 포맷 조회·오디오 다운로드를 재시도하고 `ffprobe`로 길이·비트레이트를 검증한다.

2. **샘플 승인 동결**
   - 0~3분을 기계적으로 180초에서 자르지 않는다. 3분 직전 새 질문이 시작되면 직전 완결 생각에서 끝낸다.
   - Turbo ASR + Large-v3 비교 + 짧은 targeted ASR로 이름·제목·숫자·명백한 비문을 판정한다.
   - 사용자 승인 후 cue body의 줄 수·SHA256을 기록하고 전체 본문의 exact prefix로 고정한다.

3. **전체 ASR**
   - 5분 mono 16kHz 청크, Korean, word timestamps, `condition_on_previous_text=False`.
   - 각 청크의 첫 문장·마지막 문장, 최종 실제 발화 도달 여부, 동일 세그먼트 반복을 확인한다.

4. **국소 환각 탐지**
   - 정확히 같은 세그먼트가 여러 번 반복되는 경우뿐 아니라 `캔디디디…`처럼 한 토큰이 수십 초 늘어지는 경우도 탐지한다.
   - 청크 프로세스가 정상 종료됐거나 최종 tail이 존재해도 중간 20~30초가 붕괴할 수 있다.

5. **국소 재전사**
   - 붕괴 전후 5~10초 문맥을 포함한 좁은 WAV 클립을 만든다.
   - 다른 MLX 모델(예: `whisper-large-v3-mlx`)과 좁은 용어 prompt를 사용한다.
   - 다중 clip 필터를 사용할 때는 반환 세그먼트의 실제 시작·종료 범위를 반드시 확인한다. 범위가 예상보다 넓으면 전역 대체에 쓰지 말고 필요한 구간만 선택한다.

6. **전역 타임라인 보수**
   - 원본 merged JSON에서 repair interval과 겹치는 `segments`와 `words`를 모두 제거한다.
   - repair JSON의 local timestamps에 clip offset을 더한다.
   - 복구 segments/words를 삽입하고 정렬한다.
   - `segments`, `words`, timecoded baseline, 영향을 받은 range 파일을 함께 다시 생성한다.
   - repair interval/source를 manifest에 기록한다.
   - word timestamps 단조 증가와 최종 발화 시각을 재검증한다.

7. **stale 초안 무효화**
   - 본문 작업자나 reviewer가 repair 이전 range 파일을 읽었다면 그 구간의 결과는 stale이다.
   - 줄 번호만 보고 패치하지 않는다. 환각 구간을 repaired baseline에서 다시 작성하고, 연결 문장까지 Main이 재검수한다.
   - 최종 후보 hash를 바꾼 뒤 omission/source review를 다시 실행한다.

## 사용자 제공 부분 원고 활용

사용자가 인터뷰 일부를 붙여줬다면 그 텍스트는 해당 범위의 강한 lexical reference다. 다만 원고 타임코드가 현재 컷 영상과 다를 수 있다.

- 양쪽에서 고유한 긴 문장 2개 이상을 anchor로 잡는다.
- source time과 pasted time의 offset이 일정한지 확인한다.
- offset이 확인된 범위에서만 용어·누락·문장 복구에 사용한다.
- 타이밍은 여전히 현재 링크의 실제 오디오와 MLX word timestamps가 권위다.

## 리뷰 권한

- Source reviewer: 실제 어휘·반복·범위어·조사 누락을 판정
- Segmentation reviewer: token-preserving 경계·문장부호 제안만 수행
- Terminology reviewer: 공식 표기·숫자·약어 판정
- Main: 충돌 판정과 전체 리듬 통합

Segmentation reviewer가 `도입하다`, `핵심`, `방식` 같은 미발화 어휘를 넣거나 반복을 삭제하면 source evidence 없이는 기각한다. 문법이 어색해도 먼저 실제 발화를 복원하고, 명백한 비문만 최소 교정한다.

## 최종 게이트

- 승인 샘플 exact prefix·hash 유지
- repaired interval의 환각 문자열 0
- body 모든 줄 ≤27자 또는 승인된 예외
- 끝 마침표 0
- 모든 인접 cue와 모든 cue 내부 문법·source fidelity 검사
- SRT body == frozen body lines
- overlap/nonpositive 0
- ASR speech-containing gap 전수 판정
