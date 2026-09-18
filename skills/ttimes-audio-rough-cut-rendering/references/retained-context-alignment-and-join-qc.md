# Retained-Context Audio Alignment and Join QC

## Why deleted-text matching fails

A deletion transcript can contain:

- a duplicated word that was never separately spoken
- a typo or correction artifact
- wording different from ASR
- a short phrase repeated elsewhere

Matching the deleted string alone can cut the only retained occurrence. Use retained context as the boundary authority.

## Alignment method

For each approved cut:

1. Extract the retained suffix immediately before the cut.
2. Extract the retained prefix immediately after the cut.
3. Search within the operation's timecoded block.
4. Align the left suffix and right prefix independently.
5. Treat words between the retained anchors as the candidate deleted audio.
6. Confirm monotonic order against adjacent operations.
7. Use the approved deleted text only as supporting evidence.

If anchors are adjacent, classify the transcript deletion as `no_audio_noop`. Do not cut a similar word from retained context.

## Repeated phrase handling

When a phrase such as `그러니까` occurs several times:

- choose the occurrence nearest the approved block timestamp
- require the expected retained right context
- require the previous operation to end before it
- reject the match if it consumes a retained word

## Physical boundary selection

The semantic cut starts after the retained left word and ends before the retained right word. Select physical boundaries by:

- word start/end timestamps
- midpoint between adjacent retained/deleted words
- local low-energy point when it does not clip consonants
- short crossfade, normally only enough to prevent a click

Do not enlarge a semantic cut to solve a difficult join.

## Join QC

For each rendered join:

1. Extract roughly 4 seconds before and after.
2. Re-transcribe the clip.
3. Check expected retained left and right phrases.
4. Check that deleted text does not remain.
5. If short-clip ASR repeats or omits text, retry with 6 seconds on each side before calling it a bad join.
6. Independently verify full-file decode, expected duration, and operation accounting.

Short-clip Whisper hallucination is a review signal, not proof of a bad edit. Longer local context resolved several false alarms in the Park Nam-gyu case.

## Fail-closed cases

- missing retained anchor
- reversed anchors
- multiple equally plausible occurrences
- boundary would cut a retained word
- move destination is absent
- approved transcript and audio disagree materially

Return these to a human timecode check; never choose the nearest fuzzy match merely to finish rendering.
