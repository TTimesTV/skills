# DOCX deletion-markup forensic audit for runtime mismatches

Use this reference when a DOCX-guided audio cut is materially longer than an editor's reported cut, or when Word appears to show more deletions than the extractor found.

## Forensic sequence

1. Hash-pin the DOCX and audio. Never modify either source during the audit.
2. Inventory every ZIP member and parse every `.xml`/`.rels` part, not only `word/document.xml`.
3. Count and classify all deletion-like or visibility-related constructs:
   - tracked deletion/move source: `w:del`, `w:delText`, `w:moveFrom`, move range markers
   - direct or inherited formatting: `w:strike`, `w:dstrike`
   - hidden content: `w:vanish`, `w:webHidden`, `w:specVanish`
   - non-deletion editorial channels: `w:color`, `w:highlight`, `w:shd`, comments, insertions
   - alternate text containers: headers, footers, text boxes, hyperlinks, `w:sdt`, `w:smartTag`, `w:customXml`
4. Inspect `word/styles.xml` and document defaults for inherited strike/hidden properties. Direct-run-only checks are insufficient until style inheritance is ruled out.
5. Inspect every run's parent tag. A parser that only reads direct `w:p > w:r` can miss runs nested in hyperlinks, content controls, smart tags, custom XML, or text boxes. If all runs are direct paragraph children, record that as evidence rather than assuming it.
6. Distinguish `w:pPr/w:rPr/w:strike` from text-run strike. This property formats the paragraph mark (¶) and newly typed text; it does not make all existing paragraph text an audio deletion. Existing text must still carry effective strike or revision markup.
7. Reconstruct contiguous marked groups independently, bridging only insignificant unmarked whitespace. Strip speaker/timestamp headers from audio queries even when the entire paragraph was struck. Compare the resulting `(paragraph identity, text)` ledger item-by-item with the production manifest—not merely by count.
8. Classify colored text from document-local evidence. Red text alone is not deletion. A note such as “put the red section here” plus a later red passage is a relocation instruction: only strike-marked spans inside it are deletions; relocating retained speech changes order, not duration.
9. Reconcile runtime with two ledgers:
   - markup shortfall before crossfades: `source - declared_cut_union - target`
   - delivered-output gap: `verified_output - target`
   Explain the difference using crossfade total and codec/container measurement tolerance.
10. Report exact OOXML paths and representative paragraph XPaths, plus a machine-readable appendix containing every reconstructed group.

## Interpretation rules

- Matching cut counts are not sufficient; require exact text and paragraph identity equality.
- Report whole-block counts at three levels instead of collapsing them into one number: literal fully deleted paragraphs, audio-bearing fully deleted paragraphs after metadata removal, and editorially meaningful blocks after explicitly named fragment exclusions. A claim such as “18 whole blocks” may be reproducible only by excluding a URL and selected orphan fragments; that is an editorial convention, not an OOXML fact.
- When adjacent fully deleted paragraphs or partial ranges overlap on the ASR timeline, report both node count and unioned interval count. Never infer join count directly from `w:del` count.
- A low-confidence or wrong occurrence assignment must be disclosed even when adjacent deletion coverage makes it runtime-neutral. Separate semantic correctness from duration sensitivity.
- A visual Word review is not a substitute for package inspection because Track Changes display settings can hide or restyle revisions.
- Color, comments, highlight, and insertion revisions are editorial signals, not deletion semantics unless the document explicitly defines a convention.
- Metadata such as title, recording details, participant names, timestamps, and editor notes may themselves be struck but are not audio cuts.
- If all known deletion channels are exhausted and the independent ledger exactly matches the production manifest, classify the runtime gap as **unmarked by this DOCX**. Do not invent missing cuts. The remaining hypotheses are extra editorial judgment outside the markup or a version/comparison mismatch.
- If the editor's target is approximate, label any exact-target arithmetic as an assumption. Distinguish “gap versus exactly 38:00” from “evidence of 5:28 omitted markup.”

## Worked-example pattern

A useful report should separate:

- total `w:strike` elements
- text-run strike properties versus paragraph-mark strike properties
- all contiguous groups versus speech-only groups
- red/colored text versus the subset also struck
- source duration, unioned declared cuts, expected pre-crossfade output, verified final output, and gap to the assumed target

This prevents three common false findings: counting hundreds of split runs as hundreds of cuts, treating a paragraph-mark property as whole-paragraph deletion, and treating a relocation color as duration-removing markup.
