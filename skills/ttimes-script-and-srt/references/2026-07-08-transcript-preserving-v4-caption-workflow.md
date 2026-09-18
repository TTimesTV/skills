# 2026-07-08 TTimes transcript-preserving v4 workflow lessons

## Context

During a long YouTube → TTimes 말자막/SRT task, the user rejected two failure modes:

1. **Over-polished rewrite**: subagent cue candidates were integrated too aggressively, causing 윤문/요약/생략 and loss of spoken detail.
2. **Over-segmentation / metric chasing**: forcing 28/25-char compliance by extracting or auto-merging cue candidates produced unnatural rhythm despite good-looking length metrics.

The accepted direction was to return to the stable transcript-like base and apply only local, evidence-backed edits.

## Durable user standard

Use this as the default standard for TTimes spoken captions:

```text
원문을 다시 쓰지 말고, 원문을 망치지 않는 선에서 방송 자막으로 정리한다.
```

Practical meaning:

- Preserve actual spoken wording, order, examples, repetitions, and colloquial rhythm.
- Do not summarize, compress, or rephrase into polished prose.
- Fix only clear ASR/proper-noun/number/case-particle errors, obvious 비문, and visual overlength.
- Lightly trim fillers only when they clearly damage readability; do not erase speaker texture.
- If a correction would remove spoken content, mark it `확인 필요` or leave the stable base unchanged.

## Length target after this session

- Target: **≤25 visible Korean characters** per cue.
- 26–28: warning/exception if preserving a phrase is more important.
- 29+: must fix by minimal split, not deletion or rewrite.
- Average should stay roughly **15–18 visible chars**.
- Too-short cues are also a failure: avoid many <=7-char fragments unless they are natural reactions/emphasis.

## Subagent usage rule

Subagents are reviewers, not final writers.

Ask them for line-numbered proposals only:

```text
line / OLD / NEW / reason / confidence / risk
```

Do **not** ask or allow them to produce the final full cue list as a replacement transcript. Their `cue 후보` blocks are review material only. Main Hermes must integrate local edits into the stable transcript base.

## Safe v4 sequence

1. Start from stable transcript-like base (`stable_transcript_base.txt`), not from polished peer cue candidates.
2. Create line-numbered file with visible char counts.
3. Dispatch subagents:
   - A: 원문보존/ASR/고유명사/숫자/조사 오류, line-based only.
   - B: 가독성/25자 제한, line-based split/merge suggestions only.
   - C: moderator/checklist, conflicts and spot-check ranges.
4. Apply high-confidence local edits only.
5. Split overlength lines by minimal semantic break; preserve all content.
6. Re-align from final script and validate.
7. Spot-check final SRT text in the chat/file before claiming done.

## Mandatory red flags

Do not deliver if any of these happen:

- `low_match_count` spikes after broad rewrite.
- avg match score drops materially without a known reason.
- line count changes drastically because content was rewritten/condensed rather than split.
- The output reads like an article summary instead of spoken subtitles.
- Subagent suggestions have been pasted directly into the final script.

## Formatting / delivery lesson

When the user says `여기다가 달라`, `텍스트로 줘`, or `코드블록으로 달라`, do not only attach a file or paste tool output. Provide the requested text in the assistant reply as a fenced code block, splitting into multiple messages/parts if necessary.

For normal Telegram SRT delivery, still attach the `.txt` SRT file named:

```text
YYMMDD_인물_핵심주제1_핵심주제2_srt.txt
```

But if the user explicitly asks for clipboard-style chat text, satisfy that format directly.

## Concrete correction examples

- `ai`, `에이아이`, `에이아` → `AI`; preserve `xAI`.
- `워크 에이전트 코딩 에이전트` → `워크 에이전트, 코딩 에이전트`.
- `에이전틱 한` → `에이전틱한`.
- `디버깅 할` → `디버깅할`.
- `계획이 세우는` → `계획을 세우는`.
- `받은 모든 지신 무시하고` → `받은 모든 지시를 무시하고`.
- `인지 부채가 안 쓰인다` → `인지 부채가 안 쌓인다`.
- Use quotes for embedded prompt text, but do not split quote markers awkwardly.

## Spot-check ranges pattern

For long AI/tech talk videos, spot-check:

- opening hook/repeated metaphor sections;
- company/model mapping sections with many proper nouns;
- quoted prompt-injection examples;
- numeric reasoning sections;
- dense product-list sections (`워크 에이전트, 코딩 에이전트`, `AI5/AI6`, `TPU/GPU`, etc.).
