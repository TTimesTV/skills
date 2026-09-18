# 2026-07-09 — 60~85분 ASR → TTimes cue-body-only delivery

## Context

User asked: `승인된 샘플 스타일로 60~85분 ASR을 TTimes 말자막 cue body로 분절하고 파일로 저장하라.`

This was a fast existing-ASR chunk conversion task, not a full SRT/timing rebuild. Existing ASR chunks were already present under the project workspace:

- `redraft/asr_parts/part_60_70_asr.txt`
- `redraft/asr_parts/part_70_80_asr.txt`
- `redraft/asr_parts/part_80_85_asr.txt`

Final cue-body file was saved at:

- `redraft/parts/part_60_85_caption_body.txt`

## Practical pattern that worked

1. Read all requested ASR chunk files together.
2. Create one plain text output with **one cue body per line** only:
   - no timestamps
   - no indices
   - no markdown
   - no blank lines
   - no sentence-final periods
3. Apply Gem1-style minimal correction first:
   - obvious ASR term fixes: `채찔 pt` → `챗GPT`, `클로우드` → `Claude`, `엔스트로픽` → `Anthropic`, `젠슨왕/젠슨항` → `젠슨 황`, `DLM/디렘` → `D램`, `HMAM` → `HBM`, `MPU` in AI-chip context → `NPU`, `사이마리` → `SMR`, `그리기에` → `그리드`
   - preserve transcript-close spoken wording; do not summarize or rewrite into article prose.
4. Apply Gem2-style line breaking:
   - meaning-closed cue bodies, usually 12~20 visible chars
   - practical hard max: 27 chars including spaces
   - short Q/A reactions may stand alone if meaningful; otherwise merge tiny discourse fragments into the adjacent cue.
5. Validate mechanically and patch only the flagged lines.

## Useful validation snippet

```bash
python3 - <<'PY'
from pathlib import Path
import re
p=Path('redraft/parts/part_60_85_caption_body.txt')
lines=p.read_text().splitlines()
non=[l for l in lines if l.strip()]
lengths=[len(l) for l in non]
print('lines_total',len(lines),'nonempty',len(non),'blank',len(lines)-len(non))
print('max_len',max(lengths),'avg_len',round(sum(lengths)/len(lengths),2))
print('over27',sum(1 for l in non if len(l)>27))
print('over25',sum(1 for l in non if len(l)>25))
print('timestamps',sum(1 for l in non if re.search(r'\[\d|\d{1,2}:\d{2}',l)))
print('markdown_index_like',sum(1 for l in non if re.fullmatch(r'\d+[.)]?',l)))

exact_bad={'근데','그런데','그리고','그래서','그러니까','다만','하지만','그럼','왜?','뭐가?','심지어','따지고 보면','오늘 한번','사인','드릴게요'}
orphan=[]
for i,l in enumerate(non,1):
    if l in exact_bad:
        orphan.append((i,len(l),l))
    if re.fullmatch(r'(그리고|그런데|근데|그러면|그다음에|하지만|다만|그래서|또|네|아),?', l):
        orphan.append((i,len(l),l))
print('orphan_heuristic',len(orphan))
for x in orphan[:50]: print('ORPHAN',*x)

bad_terms=['젠슨왕','젠슨항','엔스트로픽','클로우드','지퓨','하이니스','하이넥스','마이크로미','HMAM','MPU','DLM','채찔','디렘','사이마리','그리기에','제버스']
text='\n'.join(non)
print('bad_terms',[t for t in bad_terms if t in text])
PY
```

## Final validation profile from this session

- non-empty cue bodies: 784
- max length: 27 chars including spaces
- average length: 14.17 chars
- over 27: 0
- timestamps / indices / markdown: 0
- blank lines: 0
- orphan heuristic hits after patching: 0
- bad term scan hits: 0

## Pitfalls and fixes observed

- Tiny discourse fragments such as `따지고 보면`, `사인`, `뭐가?`, `심지어`, `오늘 한번`, or standalone `그렇죠/맞아요` can look mechanically valid but feel orphaned. Merge them into the neighboring cue when the combined line stays within 27 chars and does not blur a sentence boundary.
- A few generated lines may still be ≤4 chars and acceptable if they are true reactions (`맞습니다`, `똑같아요`, `89조?`, `두 개나`). Do not blindly merge all short lines; inspect meaning.
- For numbered/list explanation, avoid orphaning labels like `2차적인 건`, `4차적인 건`, or predicate tails like `드릴게요`; merge with the quoted/action phrase if length allows.
- If no project brief is found, default to the already-approved Park/Jongcheon-like style: transcript-close, minimal correction, no heavy paraphrase, no long report, deliver the cue-body file path plus a compact validation summary.
