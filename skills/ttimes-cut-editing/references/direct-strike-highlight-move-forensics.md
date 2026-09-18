# Direct-Strike + Highlight Move Forensics

## Trigger

Use when a cut-editing DOCX has:

- many direct `w:strike` runs but no `w:del`
- yellow-highlighted speech near the tail or after the formal close
- a highlighted note such as `뒤에 형광색 부분 여기에 넣기`
- separators that distinguish the on-air close from pickup takes

A plain “remove every strikethrough” simulation is insufficient because the document may encode both cuts and relocations without Word move revisions.

## Reconstruction procedure

1. Extract direct strike runs and group contiguous runs into semantic CUT operations.
2. Extract `w:highlight` and paragraph shading independently from font color.
3. Separate highlighted natural-language instructions from highlighted source speech.
4. Pair each destination instruction with the highlighted source block using:
   - explicit wording (`여기에 넣기`, `앞으로 이동`)
   - matching highlight style
   - source position, often after the formal close
   - semantic fit at the destination
5. Record a MOVE operation with source span, destination context, ordering, and expected net-zero runtime.
6. Build the final accepted state in this order:
   - apply CUT
   - remove NON_AUDIO instructions and separators
   - remove the MOVE source from its original location
   - insert the selected source at the destination
   - perform internal retake/speaker-boundary cleanup inside the moved block
7. Read the reconstructed accepted transcript continuously.

## Critical pitfalls

- A highlighted post-close block is not automatically post-close chatter; it may be a pickup intended for insertion.
- Highlighted source speech can still contain a failed start, host interjection, duplicated answer, or ASR speaker split. MOVE does not mean “keep every highlighted token.”
- A sentence split across two speaker labels can be one speaker’s continuous sentence; require audio or clear grammatical evidence before correcting attribution.
- Destination notes are NON_AUDIO and must not appear in the editor-facing accepted script.
- Do not count a MOVE as added runtime when the source is removed from its original position.
- Validate punctuation ownership after removing a strike region or destination note.

## Minimal ledger shape

```json
{
  "id": "M001",
  "decision": "MOVE",
  "source_time": "58:29-59:32",
  "destination_context": "efficiency explanation after 09:00",
  "instruction": "뒤에 형광색 부분 여기에 넣기",
  "internal_review": ["failed start", "speaker split"],
  "net_runtime_change": 0
}
```
