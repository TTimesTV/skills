# Bounded 20-minute raw-ASR → 말자막 body 초벌

## Trigger

Use when the user names a bounded range such as `00:00~20:00` in an existing merged raw ASR and asks for an `원문 밀착 말자막 body 초벌`, with an existing transcript-close baseline, glossary, and correction ledger.

## Durable workflow

1. Read the raw ASR through the exact end boundary and inspect the crossing segment. Stop at the latest complete thought before the boundary rather than dragging in a new, unfinished turn merely because its segment starts just before the cutoff.
2. Read the transcript-close baseline for the same source and use it as the drafting substrate only after confirming its range correspondence with the raw ASR.
3. Read `glossary.txt` and `correction_ledger.tsv` before drafting:
   - apply `confirmed` forms everywhere;
   - treat `likely` and unresolved entries conservatively;
   - do not turn a likely guess into an authoritative correction merely because the baseline already contains it.
4. Create only the requested output file. Do not modify the baseline, raw ASR, glossary, ledger, or unrelated project files.
5. Output one non-empty cue body per line, with no timecodes, speakers, indices, markdown, blank separators, or sentence-final periods.
6. Preserve order, modality, repetition, reactions, and colloquial tone. Use only local grammar repair when the ASR is visibly broken; do not summarize or broadly rewrite.
7. Segment for small-sentence readability with a 25-character target and 27-character hard maximum, counting spaces and Latin characters.

## Automation lesson

A whole-stream dynamic-programming wrapper can be useful as a rough first pass, but it is unsafe as the final draft:

- If every baseline line is segmented independently, it preserves arbitrary ASR chunk seams and creates protected-phrase splits.
- If all baseline lines are joined into one stream, it can over-merge speaker turns, reactions, discourse pivots, and multiple completed thoughts when punctuation is sparse.
- Multiword technical names may be split unless explicitly protected (`Human in the Loop`, `State Tracking`, `Query Fan-Out`, `Answer Fusion`, `Response Fusion`, `Vera Rubin`, `Claude Code`).

Therefore, automation is scaffolding only. Protect confirmed multiword terms before segmentation, then manually inspect every generated cue and every adjacent boundary. Repartition boundaries before considering lexical changes.

## Review and validation

Run both bundled audits:

```bash
python3 scripts/audit_caption_body.py BODY.txt
python3 scripts/audit_protected_phrase_splits.py BODY.txt
```

Then manually adjudicate every candidate. Regex hits are prompts, not automatic failures: topic-setting fragments, conditional clauses, and comparison clauses may be acceptable, but true adnominal–noun, dependent-noun, object/adverbial–predicate, auxiliary, fixed-name, and number–unit splits must be repaired.

After every terminology or spacing patch, rerun the length audit; a one-character correction can create a 28-character cue.

Final mechanical gate:

- UTF-8 text
- no blank lines
- no timestamps or speaker labels
- no markdown
- no sentence-final periods
- maximum 27 characters
- confirmed ledger variants absent
- line count, character count excluding newlines, maximum/average length, and SHA-256 reported

## Handoff style

For this bounded first-draft task, return only a terse completion summary: saved path, line count, character count, maximum/average length, validation result, SHA-256, and one short caveat if uncertain ledger forms were intentionally retained. Do not attach unrelated reports unless requested.
