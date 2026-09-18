# TTimes YouTube Description Timestamps / Chapters

Use this reference when the user asks for a TTimes YouTube `타임스탬프`, `챕터`, or shows the mobile YouTube description/chapter UI.

## Meaning

For this user, **YouTube timestamp** means the clickable chapter list written in the video description:

```text
MM:SS chapter title
```

It does **not** mean:

- SRT cue timestamps;
- sentence-by-sentence transcript timecodes;
- subtitle synchronization;
- a full timestamped script.

YouTube turns the description list into the visual `챕터` strip and shows the active chapter title over the player.

## TTimes example observed from the channel UI

```text
00:00 20강으로 완성하는 실습형 AI 레버리지 강좌 소개
00:16 하이라이트
02:06 AI칩이란?
06:58 주요 AI칩 메이커는?
16:34 빅테크 진영의 AI칩 전략
25:31 AI칩 스타트업의 고객은?
30:59 세레브라스 주가 폭락
36:59 리벨리온의 경쟁력
43:21 메타가 눈독들인 퓨리오사AI
47:56 엔비디아에 타격줄까?
```

At playback `53:26`, the player displayed the active chapter `엔비디아에 타격줄까?`, matching the final chapter that begins at `47:56`.

## Output rules

1. Start with `00:00`.
2. Use ascending `MM:SS` or `H:MM:SS` times.
3. Use one concise editorial topic title per major subject shift.
4. Keep chapter titles scannable; do not turn them into sentence summaries.
5. Default delivery is plain text lines only—no bullets, numbering, table, or explanatory prose unless requested.
6. Confirm every timestamp is inside the final video duration and corresponds to the actual cut, not the pre-cut transcript.
7. If the user says only `타임스탬프` in a TTimes YouTube context, default to this chapter-list format. Route to SRT only when they explicitly ask for 자막, SRT, 말자막, 싱크, or cue timing.

## Workflow

1. Identify the exact final-cut video or supplied final media.
2. Use the final transcript/ASR with timing as the substrate.
3. Mark only major topic transitions, intro/highlight, and final segment boundaries.
4. Write concise TTimes-style chapter titles.
5. Verify ascending times, `00:00` start, no duplicate or near-duplicate chapters, and last timestamp before video end.
6. Return the chapter list as a copy-paste-ready description block.

## Pitfall

Do not answer a request for `유튜브 타임스탬프` with an SRT, a `[시작 → 종료] 발화` transcript, or an explanation of timestamp syntax. The expected artifact is usually the copy-paste-ready YouTube description chapter block itself.
