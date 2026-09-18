# ASR speech-coverage gap audit and repair

## Failure class

A structurally valid SRT can still contain long visual holes while speech continues. Checks such as sequential indices, no overlap, no non-positive duration, and maximum cue duration do **not** detect this.

Typical cause:

- Final body is corrected, compressed, or paraphrased relative to ASR.
- Fuzzy alignment anchors cue starts/ends only to matched words.
- Repetitions, fillers, restatements, or unmatched spoken phrases between anchors are assigned to no cue.
- A readability extender only targets text-length display duration and therefore may leave multi-second spoken gaps untouched.

## Mandatory pre-delivery gate

After final SRT timing and readability adjustment:

1. Parse every cue interval.
2. Load ASR word timestamps.
3. Compute ASR-word coverage: a word is covered when its midpoint falls inside a cue interval.
4. Enumerate every adjacent-cue gap containing one or more ASR words.
5. Report counts at thresholds `>=0.8s`, `>=1s`, `>=2s`, `>=3s`, and the longest spoken gap.
6. Do not deliver while any material spoken gap remains unreviewed.

A result like `overlaps=0` is only a structural prerequisite. It is not a speech-coverage pass.

## Repair classification

For every spoken gap, compare its ASR words with the neighboring cue bodies and the source context:

- **Repeated/restated neighboring meaning:** do not invent a duplicate subtitle. Extend the previous cue, next cue, or both across the spoken interval.
- **Filler/disfluency with no new meaning:** cover it by extending an adjacent cue; do not add ugly filler text merely to increase coverage.
- **Meaningful source content absent from both neighbors:** insert one or more transcript-close cues using ASR word start/end times. Keep normal segmentation and <=27 visible characters.
- **True silence/no ASR words:** preserve the gap.

After insertion or extension:

- Renumber cues.
- Assert every original cue body remains an ordered subsequence unless the user explicitly requested text edits.
- Recheck indices, overlaps, non-positive durations, added-cue length, quote balance, and ASR-word coverage.
- Re-run the spoken-gap scan; target zero unreviewed gaps containing ASR words.

## Reporting rule

When the user asks to fix only the holes:

- Deliver a corrected SRT as a separate artifact; preserve a backup of the prior delivery.
- Report only changed intervals.
- Distinguish `새 cue 추가` from `기존 cue 타이밍 보완`.
- Do not resend or narrate the entire subtitle body.

## Acceptance warning

If ASR-word coverage is materially low or there are multi-second gaps containing speech, the SRT is not a usable final delivery even if all conventional SRT hard gates pass. State this plainly and repair before claiming completion.
