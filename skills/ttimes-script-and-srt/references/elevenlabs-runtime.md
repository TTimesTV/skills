# 공유 환경의 전사 실행 경로

말자막, SRT, 싱크, 워딩, 화자 구분, 부분 재전사는 **ElevenLabs Scribe v2 API**로 수행한다. 이 규칙은 과거 전사 사례보다 우선한다. 기존에 같은 음원으로 받은 ElevenLabs JSON이 있으면 재사용한다.

## 인증

- 인증 파일은 사용자가 지정한 위치에서 읽으며 작업 산출물이나 Git 저장소로 복사하지 않는다.

- `ELEVENLABS_API_KEY` 환경변수를 우선 사용한다. 파일이 필요하면 `ELEVENLABS_ENV_FILE` 또는 `--env`로 경로를 지정한다.
- 변수명: `ELEVENLABS_API_KEY`
- 환경변수에 키가 없으면 `--env`로 지정한 파일을 읽는다.
- 키 값은 로그·대화·문서·명령행에 출력하거나 복사하지 않는다. API key ID가 아닌 실제 `sk_` 형식 키인지 출력 없이 확인한다.
- 키가 없거나 인증·잔액·네트워크 오류가 나면 구체적인 실패 원인을 보고한다. 별도 전사 엔진을 설치하거나 실행하지 않는다.

## 실행

```powershell
python "skills/ttimes-script-and-srt/scripts/elevenlabs_transcribe.py" --check
python "skills/ttimes-script-and-srt/scripts/elevenlabs_transcribe.py" --audio "C:/absolute/path/source.mp3" --output "C:/absolute/path/work/scribe_v2_raw.json"
```

`POST https://api.elevenlabs.io/v1/speech-to-text` 요청은 `model_id=scribe_v2`, 원음 언어(한국어 `ko`), `diarize=true`, `timestamps_granularity=word`, `tag_audio_events=false`, `no_verbatim=false`를 사용한다. 화자 수는 직접 확인한 경우에만 고정한다.

원본 MP3는 바로 업로드한다. FFmpeg는 필요한 음원 추출·짧은 구간 추출에만 쓴다. 장편이라는 이유로 선제적으로 전체를 여러 청크로 쪼개 반복 요청하지 않는다. 서비스 제한이나 확인된 누락이 있을 때만 필요한 범위를 나누고 절대 시간 오프셋을 보존한다.

## 완료 확인

성공 응답만으로 완료 처리하지 않는다. JSON의 `text`와 `type=word` 항목, 유한한 시작·종료 시간, 실제 발화 끝부분 도달 여부를 확인한다. `spacing`은 단어 수에서 제외한다. 원본 JSON은 보존하고 편집본은 별도로 만든다.

불명확한 이름·숫자·문장은 주변 문맥을 포함한 12~25초만 추출해 같은 API로 확인한다. 같은 결과가 반복돼도 불명확하면 추측으로 확정하지 않는다. 이 환경에서는 Scribe v2를 유지하며, 미확정 사항은 표시한다.

자막 본문을 먼저 검수·고정한 뒤 단어 타이밍에 맞춘다. 워드의 대략적인 문단 시간을 실제 단어 종료보다 우선해 자막을 자르지 않는다. 본문 일치·겹침·표시 길이·음성 공백은 별도로 검증한다.
