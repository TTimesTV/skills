# Immutable Full-Candidate Final Audit

Use this mode when the user asks for `전 구간 최종 통합 검수`, `fresh review`, or a final audit of a named immutable 말자막 candidate.

## Scope contract

1. Recompute and record the candidate SHA-256 before review; do not edit the candidate.
2. Read every cue and manually adjudicate every adjacent cue pair. If the body has `N` non-empty cues, the claimed scope is `N` cues plus `N-1` boundaries.
3. Read the approved transcript, glossary, correction ledger, and available ASR words/segments. Treat the approved transcript as wording authority while using actual cut audio/ASR to resolve omissions, malformed accepted text, and source-order disputes.
4. Run mechanical body and protected-phrase audits only as candidate generators. Regex hits are not findings until manually confirmed, and regex zero is not a pass.
5. Verify the candidate hash again after writing the report.

## Four independent axes

- **Source fidelity / omission / distortion:** compare normalized approved speech and candidate order, then confirm material replacements, deletions, and insertions with ASR/audio. A grammatically unnecessary paraphrase is a fidelity finding even when the gist survives. Treat deleted quantifiers and scope markers (`대부분의`, `일부`, `약`, `한`, `이상/이하`, negation, modality) as high-risk even when the remaining sentence sounds fluent; compression can silently universalize or strengthen a claim.
- **Segmentation / small-sentence readability:** inspect all boundaries for adnominal+noun, dependent-noun+predicate, object/adverbial+predicate, auxiliary predicate, quote, list, number/unit, and proper-name splits. Count only confirmed failures, not every continuation across a cue. Pay special attention to late source-restoration edits: restoring one token can push a previously valid cue over the visual maximum and induce a new `데 / 있어서`, object/predicate, quoted-adnominal/noun, or nominal-clause/predicate split.
- **Intra-cue grammar:** separately detect malformed particles, duplicated subjects/topics, impossible collocations, stacked connective endings, and ASR-shaped non-sentences. A clean boundary does not certify the cue itself.
- **Terms / names / numbers:** enforce the current glossary and correction ledger globally, including state-label spacing and repeated occurrences in one local explanation.

## Regression-aware freshness pass

A heavily corrected candidate needs a fresh full audit, but predecessor comparison can still be useful **after** that independent read:

1. Complete the all-cue/all-boundary review without using prior findings as the verdict.
2. If an immediate predecessor exists, diff predecessor → current candidate as a regression locator only.
3. Re-read every changed hunk in the current candidate and check both axes together: did a source-fidelity restoration create a protected-phrase split, or did a segmentation repair delete a quantifier/scope token?
4. Confirm each suspected defect against the current exact string and source hierarchy. Do not copy old line numbers or count a diff hunk automatically.
5. Design a minimum correction that passes the visual limit. Label it honestly as `boundary-only` only if no lexical token changes; if a 27-character constraint requires source-backed deletion or substitution, label it `minimal lexical/boundary repair` and cite the ASR/approved-source basis.

This catches the common trade-off regression where one review pass fixes source fidelity by restoring a word, while another pass creates a broken adjacent boundary to keep every cue within 27 characters—or vice versa.

### Concrete regression families to scan

- A segmentation repair can silently delete scope: `이 에이전트의 일반성을 갖고 있는 대부분의 지능들은요` must not become `이 에이전트의 일반성을 갖춘 지능들은요`; losing `대부분의` universalizes the claim.
- Do not convert a source-backed attributive relation into an unsupported conjunction merely to avoid a modifier/name split. For example, `LLM 지능의 1등을 달렸던 / 오픈AI의 최고 과학자였던 …` must not become `LLM 지능 1등을 달렸고 / 오픈AI 최고 과학자였던 …` without direct source support.
- One local repartition can contain several atomic defects. A span that independently splits `수행하는 데 / 있어서`, `일을 / 할 수 있게 되는 건`, and `걸 / 깨달으면서부터잖아요` counts as three confirmed boundaries, although the report may provide one shared correction block if the section arithmetic remains explicit.
- A glossary-complete pass can still miss a transliteration typo. Compare suspicious Korean loanwords with ASR and the underlying English term even when no glossary row exists, e.g. source-backed `엑시큐션` versus candidate `익스큐션`.
- After drafting every minimal correction, measure each proposed cue against the visual maximum. If fitting requires deleting a repeated token, require direct ASR support and label the change `minimal lexical/boundary repair`, never `boundary-only`.

## Segmentation-only immutable audits

When the user assigns a narrower role such as `분절 검수만` and supplies only the immutable cue body, keep the verdict strictly inside that role instead of implying source/audio verification. This also covers a bounded exhaustive assignment such as `후반 1001~1999 cue 분절 전수검수`: “full” means every cue and boundary inside the assigned range, not necessarily the whole file.

1. Verify the candidate hash, byte size, physical line count, non-empty cue count, and maximum visible length before review; re-hash after writing the sidecar report.
2. Convert an inclusive requested range `[A, B]` into explicit scope arithmetic: inspect `B-A+1` cues and all internal boundaries `A-(A+1)` through `(B-1)-B`, plus the preceding seam `(A-1)-A` when the user names a section boundary. State these counts. Do not count findings outside `[A, B]`; use the seam only to judge whether cue `A` opens badly.
3. Read every assigned cue and every assigned adjacent boundary. Run body/protected-phrase scripts only as candidate generators.
4. Audit the explicitly requested classes: adnominal+noun, dependent noun, object/adverbial+predicate, auxiliary predicate, number+unit, question/answer or speaker-turn packing, two completed sentences merged into one cue, small-sentence readability, and the 25-target/27-max rule.
5. Report each confirmed finding with the **exact current consecutive multiline string**, not merely line numbers. Require that string to occur uniquely in the immutable candidate, or include enough neighboring text to disambiguate it.
6. Give a token-preserving redistribution by default. Validate preservation after removing only cue-boundary whitespace—not with raw string equality, because moving a boundary necessarily moves a space/newline. Require source token order to remain unchanged and every proposed cue to remain within the agreed maximum.
7. Count only boundaries for which the proposed redistribution actually improves the protected construction. Do not “fix” one split by introducing another equally bad protected split or a meaningless tiny transition. If no clean token-preserving ≤27 redistribution exists, label it `lexical/source adjudication required` rather than presenting a defective boundary-only fix.
8. Keep separate arithmetic for segmentation/protected-phrase findings, question/answer or completed-thought packing, and over-limit cues. A 26–27-character cue is a warning, not automatically a finding when the maximum is 27. A cue containing three completed thoughts may be one cue-level packing finding, but state the internal defect count when atomic boundary arithmetic matters.
9. State that source fidelity, terminology, and factual accuracy were not audited unless the approved transcript, ledger, glossary, or audio/ASR was actually inspected.
10. Do not modify the immutable candidate. Write the report separately and verify: finding heading count == paired current/proposal block count == headline total; category subtotal sum == headline total; all current blocks exact-match; all redistributions preserve normalized tokens; all proposal lengths pass; candidate hash is unchanged.
11. Derive headline totals, category subtotals, cue lengths, and validation ratios from the final finding data structure. Never hard-code a report total separately: after adding or removing a finding, regenerate and assert that the top summary and final marker agree.

This narrower mode may legitimately report `0` findings in out-of-role axes, but it must not label those axes `PASS` without evidence.

## Evidence and reporting rules

- Earlier reports belong to their own candidate hashes. On a newer hash, treat their line numbers as stale and their findings as hypotheses: exact-search each quoted old string, then perform a fresh whole-body audit. Never derive the new verdict by subtracting already-fixed rows from an old total.
- Read the correction ledger before using the glossary as a surface-form mandate. A glossary identifies canonical terms but does not automatically require every parenthetical English expansion on screen. Require the full bilingual surface only when the ledger, approved transcript, direct source evidence, or established project convention makes it mandatory.
- Report exact current strings and exact adjacent pairs; line numbers may be included only as secondary locators.
- Separate confirmed findings from unresolved audio ambiguities. Exclude uncertain readings rather than padding the count.
- Count atomic defects consistently. If two different cues contain different grammar failures, they are two findings; a single repeated terminology inconsistency may be one explicitly labeled error family.
- When one span fails two independent axes (for example source distortion and a broken boundary), it may appear under both only when the report clearly explains the independent defects.
- For each correction, distinguish `boundary-only`, `punctuation-only`, `minimal lexical/particle repair`, and `source check required`. Never label a particle or lexical rewrite as token-preserving.
- If a parenthetical English gloss blocks a 27-character resegmentation, it may be omitted only when the evidence hierarchy does not make that surface form mandatory. If the ledger mandates it, report both the term failure and the need for broader resegmentation rather than silently dropping the gloss.
- State the inspected scope and do not claim a full review from samples.
- The normal artifact is `review/final_fresh_review.md`; do not modify the immutable body unless the user separately asks for fixes.

## Acceptance summary

Use a compact top block:

```text
PASS or FAIL
confirmed findings: N
- source fidelity: N
- segmentation/protected phrases: N
- intra-cue grammar: N
- terms/names/numbers: N
```

Before delivery, programmatically verify that section heading counts sum to the stated total, that the final marker agrees with the top block, and that the candidate hash and cue count remain unchanged.

## Pitfalls

- Do not confuse `all lint hits inspected` with `all boundaries inspected`.
- Do not silently accept broad cleanup merely because it improves grammar; compare it with the approved source and correction authority.
- Do not call an audio-ambiguous proper noun a confirmed error when multiple targeted ASR passes agree only on the same uncertain phonetics.
- Do not combine two unrelated cue defects into one finding merely to keep the report short; the arithmetic must be auditable.
