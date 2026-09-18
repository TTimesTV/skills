# Inline DOCX instruction examples

These are the **visible editor-facing examples** for the user's current TTimes grammar.

- base transcript: black/default
- exact speech range governed by the preceding object: blue/cyan without highlight
- production object: yellow highlight + cyan/blue bold
- black resumption after a blue run: OUT
- local editor-only correction or warning: red
- `@@`: correction locator only

Do not print internal IDs, function/render/status codes, search queries, rights states, repeated default speech-caption states, or long IN/OUT anchors in the visible Word body.

## 1. Selected video + editorial caption

```text
//12. (데이터센터 공식 투어)_기업 공식 영상_(01:12~)_서버랙 사이 점검 장면

//자막
전력 인프라가 AI 확장의 병목

[exact governed speech run in blue]
[black transcript resumes at OUT]
```

Both yellow objects share the following blue sync. That adjacency encodes simultaneous use; do not add `자료 //12와 함께` or a separate simultaneous-state block.

## 2. Process graphic with simultaneous lines

```text
//35. (태양전지→ESS 흐름 그래픽)_직접제작

//자막
태양전지에서 발전하고
ESS에 저장해 보완

※ 두 문장 처음부터 동시 표시. 태양전지→ESS 화살표.

[exact governed speech run in blue]
```

Use the exception note only because the arrow and simultaneous presentation change implementation.

## 3. Explicit build exception

```text
//자막
① 태양전지에서 발전
② ESS에 저장
③ 수요 시간대에 공급

※ 발화에 맞춰 ①→②→③ 누적. 앞 단계는 지우지 않음.

[exact governed speech run in blue]
```

Without this note, multiple approved lines display simultaneously.

## 4. Verified direct quote card

```text
//자막
“계면(Interface)이 곧 소자다”

//출처
박남규 교수 인터뷰

[exact governed speech run in blue]
```

If the wording is vulnerable to accidental paraphrase, add one local red line:

```text
※ 직접 인용. 따옴표 안 윤문 X
```

Detailed quote-verification evidence remains in the internal ledger.

## 5. Editor-discretion footage reuse

```text
//07. (해당 기업 해외사업 영상)_(재탕·기존과 다른 장면)

[exact governed speech run in blue]
```

`재탕`, `아무 장면`, `그냥 말하는 장면`, and `영상 끝?` are valid completed instructions when the permissible range is already clear.

## 6. No-material / one-man continuity

One-man continuity is the default absence of a production object. Usually write nothing.

Only when a local exception matters:

```text
//원맨 유지
※ 표정·리듬이 핵심. 일반 타이핑·악수 스톡 X
```

Do not emit a repeated state block such as `자료필요도=NONE` or `ONE_MAN_CONTINUITY`.

## 7. Article or photo

```text
//04. (관련 기사 캡쳐)_머니투데이
```

```text
//09. (최태원 사진)_뉴스1
```

The exact following blue run supplies timeline placement. Put source URL, publication date, fact basis, and rights status in the internal ledger unless one item directly changes the editor's action.

## Internal sidecar example — never paste into the final Word body

```yaml
asset_id: 12
use_id: 12-03
function: ILLUSTRATE
need: OPTIONAL
source_status: VERIFIED
asset_status: SELECTED
rights_status: PENDING
speech_mode: SUPPRESS
start_anchor: "전력 인프라"
end_anchor: "다음 수치 그래픽 직전"
search_query: "data center server aisle maintenance"
include:
  - 실제 점검 행동
  - 서버 랙 규모
exclude:
  - 홀로그램 AI
  - 코인 채굴장
```

This sidecar preserves auditability without turning the editor-facing timeline into a database ledger.
