## Subtitle segmentation core rule: small-sentence readability

User-approved operating rule (2026-07-08): Before character-count packing, check whether each cue reads like a **small sentence**. A good cue usually contains a noun/target axis plus a verb/judgment/predicate axis, so it can be understood on screen without waiting for the next cue.

Priority order for segmentation:

```text
1. sentence-ending boundary: when a sentence/thought ends, usually move the next sentence/thought to the next cue; do not merge separate sentences just because they fit under 27 chars
2. small-sentence readability: noun/target + verb/judgment/predicate where possible
3. predicate attachment: never strand an object/adverbial/time phrase without its predicate when the predicate can fit nearby. Bad: `지난주 금요일에 집을 다 / 그렇게 꾸며놨어요 일하기 적합하게`. Better: `지난주 금요일에 이사 갔거든요 / 집을 다 일하기 적합하게 꾸며놨어요` or `집을 다 그렇게 꾸며놨어요 / 일하기 적합하게`.
4. meaning closure / human readability
5. adhesive-word protection (접착어: discourse markers, degree adverbs, demonstratives, auxiliaries, connective endings)
6. spoken rhythm
7. 25-char target / 27-char max
```

Pitfall: do not combine two completed sentences/questions into one cue merely because the combined text is under 27 chars. Prefer `아직 버전 아니에요? / 아, 끝난 거 아니에요?` as separate cues unless a very short reply/greeting clearly reads better compacted.

Examples:

```text
GOOD:
소프트웨어나 이런 것 쪽으로 많이 다뤘었는데
주위 친구들도 너무나 전문가예요
그게 요새 조금 꺾이면서
뭔가 이제 한 사이클이 좀 변해가고 있는 느낌이 드는데

BAD:
소프트웨어나 이런 것 쪽으로 많이 / 다뤘었는데
주위 친구들도 너무나 / 전문가예요
확실히 / 구분이 잘 안되는 느낌이 들고
계시지만 / 일반적으로는 대충 들어는 봤어도
```

Exceptions: topic-setting fragments can stand alone when they intentionally open the next cue, e.g. `첫 번째 모티베이션은 / 독점 체제에 대한 불안감이에요`. Short replies/greetings such as `안녕하세요`, `그렇죠`, `아니요` can also stand alone.

User style calibration note (2026-07-08): The user identified `250708_박종천_AI데이터센터_인지부채_srt.txt` as the best/most accurate feeling output. Its measurable profile was roughly 830 cues, avg visible chars ~17.1, max 33, 133 cues over 25, 67 over 28, and 72 cues <=7. This means the user's preferred 'accurate' feel is not strict mechanical packing; it prioritizes transcript-close wording, natural speech rhythm, meaning-complete cues, and light Gem1/Gem2-style cleanup over aggressive packing or subagent-written rewrites. However, the user later clarified that for future work 25 visible Korean chars should still be the normal target and **27 chars is the practical max**. Apply the combined rule: meaning closure first, 25 target/27 max second. For similar jobs, use the Park Jongcheon file as a style reference: stable transcript-first, Main Hermes owns the full editorial pass, subagents review only, and never let subagents author final caption chunks by part. See `references/2026-07-08-park-jongcheon-reference-style-and-human-readability.md`.

### Long source MP3 chunked-ASR recovery

If a long source MP3/video full-file MLX run collapses into repeated filler such as `네` in the latter half while the audio still contains real speech, stop using that full-file ASR as the timing/text substrate. Re-run MLX in short chunks, usually 5-minute mono 16 kHz WAV chunks, merge word timestamps by adding each chunk offset, and build the script/SRT from the merged chunked JSON. This is especially important around 45+ minute Korean interview files where previous-text conditioning can drag the model into repeated acknowledgements. See `references/2026-07-09-drive-mp3-chunked-mlx-recovery.md`.

Visible-length pitfall: for this user's TTimes bottom caption box, count spaces too when enforcing the 25 target / 27 max. Non-space-only counts can produce cues that pass mechanically but look too wide. If term patches make cue bodies exceed 27 chars, split only the body cue and renumber; never apply broad range regexes to whole SRT text because they can corrupt `-->` timecode lines.

For TTimes 말자막, use an explicit 100-point score before delivery. Start at 100 and subtract **1 point per visible subtitle error** found in final review. Do not deliver unless the score is **≥95**. If the task is explicitly a **분절 업무**, the final score must be dominated by segmentation quality: do **not** average it upward with mechanical format/timing/term scores. If segmentation/readability is 45점, the overall deliverable is about 45점 even when timecodes, 27-char limit, and terminology checks pass. If the user later finds **5 or more errors** after Hermes claimed ≥95, treat the delivery as failed/out and redo; do not defend the score.

**Critical scoring rule for 분절 업무:** if the user frames the task as subtitle segmentation / 분절 work, the final score is dominated by segmentation quality, not by mechanical SRT validity. Do **not** average a high timing/format score with a low segmentation score to inflate the result. If segmentation/readability/small-sentence quality is 45, the whole deliverable is about 45 even if timecodes, 27-char max, and term scans pass. Mechanical checks are only prerequisites; they are not the score.

Count as -1 each:
- Broken Korean grammar/phrase split: 관형어+명사, 서술부, 의존명사, 보조용언, 조사/어미 split (`어떤/전쟁`, `설명해주셨던/게`, `할 수/있다`).
- Bad list split or missing comma in lists (`워크 에이전트, 코딩 에이전트`, `애저, AWS, GCP, 콜로서스`).
- ASR/proper-noun/number/unit/case error (`ai` not `AI`, `지신`, `계획이 세우는`).
- Overlength cue beyond the agreed threshold, unless explicitly justified.
- Over-polishing, omission, summarization, or meaning drift.
- Timing/body mismatch, overlap, nonpositive cue, low-match cue not manually checked, or any unreviewed cue gap containing ASR speech. Multi-second speech without a visible subtitle is a delivery-blocking failure even when structural SRT checks pass.

Mandatory before claiming ≥95:
1. Run mechanical validation.
2. Run ASR speech-coverage validation: coverage percentage, spoken-gap threshold counts, and longest spoken gap; adjudicate every material hit.
3. Inspect all automated lint hits.
4. Spot-check at least the first 3 minutes, one middle 3-minute block, one late 3-minute block, and all term-dense/quote/list sections.
5. Record the score and the remaining known caveats. If score <95, keep editing instead of sending.

ASR-failure stop rule:
- If subagent audits find dozens of ASR/proper-noun/number errors after two correction rounds, stop treating the transcript as an editable near-final draft. Declare the current draft failed, do not keep global-patching it, and switch to a sample-first/manual-pass workflow: rebuild a short 2–3 minute section from audio/clip ASR, submit that sample for user style approval, then proceed chunk-by-chunk. Do not promise a 95-point full-length deliverable from a heavily corrupted 60+ minute ASR in one pass.

## If blocked

- If source discovery from title is ambiguous, ask for link.
- If YouTube download fails but captions are accessible, report the limitation and ask whether script-only from captions is acceptable.
- If MLX fails, try another transcription path only if available; otherwise deliver the blocker honestly.
