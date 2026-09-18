# 21분 무자막 기술 인터뷰: body 리뷰와 타이밍 보정 교훈 (2026-07-23)

## 적용 범위

YouTube 수동/자동 CC가 없는 20분 안팎의 한국어 기술 인터뷰를 티타임즈 말자막 SRT로 만드는 경우.

## 안정적으로 작동한 본문 경로

1. 실제 컷편 오디오를 16 kHz mono WAV로 동결하고 MP4/WAV 해시를 기록한다.
2. 5분 청크 MLX Whisper(`condition_on_previous_text=False`)로 전사하고, segment/word timestamp를 절대 시각으로 병합한다.
3. raw ASR baseline의 줄·문자·단어·마지막 발화 시각을 기록한다.
4. 7분 안팎의 bounded range 초벌을 병렬 작성할 수 있지만, Main이 실제 파일·해시를 검증하고 범위 경계·용어·문법을 전 구간 통합한다.
5. candidate를 content-addressed snapshot으로 동결한 뒤 용어/숫자, 모든 인접 경계, 누락·왜곡을 독립 리뷰한다.
6. 리뷰어가 시간 초과해도 보고서 파일이 남았을 수 있다. headline만 보지 말고 파일 존재·완결 범위·해시를 직접 확인한다.
7. 1차 리뷰를 한 배치로 반영하고 fresh combined verifier를 한 번만 돌린다. verifier가 exact one-line restoration만 요구하면 그대로 반영하고 deterministic audit로 종료한다.

## 출처 판정과 중복 문장 함정

- 충돌 계층: 실제 컷 오디오 → targeted clip ASR → raw ASR → verified term ledger → reviewer 제안.
- 모델/회사/숫자는 10~20초 targeted clip으로 재확인한다. 이 세션에서 `Mythos`, `GPT-6`, `마이크론`, `앤트로픽이 아니라 하이퍼스케일러`가 이렇게 확정됐다.
- 화자의 사실상 자기수정이나 모순(`3분의 1 가격` 뒤 `3분의 2 가격`)은 말자막에서 임의 사실교정하지 않고 실제 발화를 보존한다.
- 비슷한 문장이 두 번 보여도 자동 중복 삭제하지 않는다. 예: 앞의 `고성능 NVIDIA GPU도 없이 만들었다`는 개발 조건이고, 뒤의 `HBM과 GPU가 많이 필요한데 / 고성능 NVIDIA GPU도 부족하다`는 운영 병목이다. 어휘가 겹쳐도 논증 역할이 다르면 둘 다 남긴다.
- 리뷰어가 익숙한 단위나 대상을 보완하라고 해도 원음이 `폰트 8`, `10만 개`, `5만 개`라면 말자막에는 들린 표현을 유지한다. 사실자막이 아닌 spoken caption이기 때문이다.

## 타이밍 보정에서 얻은 교훈

초기 character→word alignment는 body를 정확히 보존해도 기술용어 정상화 때문에 `Mixture of Experts`, `NVIDIA GPU`, `OpenRouter`, `FriendliAI` 같은 cue가 낮게 매칭될 수 있다.

필수 순서:

1. ASR word-midpoint coverage와 spoken-gap 목록을 계산한다.
2. 각 gap을 `앞 cue 소유`, `뒤 cue 소유`, `실제 누락`, `의도적 침묵`으로 판정한다.
3. 고유명사/영문 표기 차이 때문에 매칭이 끊겼다면 새 텍스트를 만들지 말고 해당 의미를 가진 cue의 start/end만 실제 단어 구간으로 확장한다.
4. `100% coverage`는 연속 interval을 억지로 만들면 쉽게 조작된다. coverage=100, overlaps=0만으로 합격시키지 않는다.
5. 특히 **짧은 gap에도 blind midpoint fallback을 쓰지 않는다.** 모든 speech-containing gap에는 semantic owner를 기록한다.
6. 최소 표시시간(예: 0.75초)을 강제할 때 다음 cue의 start를 뒤로 밀면 coverage는 유지돼도 next cue가 늦거나 previous cue가 다음 발화에 남을 수 있다. 보정 후 반드시 `early_next_exposure`, `previous_cue_lingers`, `late_next_start`, spoken order를 재검사한다.
7. 최소 표시시간 확보는 먼저 실제 무음 여백을 사용하고, 부족할 때만 의미상 같은 인접 cue의 경계를 제한적으로 이동한다.

## 완료 게이트

- final body와 SRT body가 정확히 일치
- 최대 27자, 문장 끝 마침표 0, 빈 줄 0
- sequential index, overlap 0, nonpositive 0
- 모든 speech-containing gap이 의미상 판정됨
- 최소 표시시간 보정 후 semantic timing 재검사
- FFmpeg/WebVTT 변환으로 SRT 파서 통과
- Telegram 전달본은 `PROJECT_OUTPUT/`의 ASCII `.txt`, source/destination SHA-256 일치
