# Independent final rough-cut audit

Use this after generation when the verifier must not trust the apply summary or generation code as the sole authority.

## 1. Freeze and reopen

- Recompute SHA-256 and bytes for final DOCX, source DOCX, transcript JSON, manifest, validation ledger, and apply summary.
- Run ZIP integrity and parse every `.xml`/`.rels` member.
- Reopen with `python-docx`; on macOS also run `textutil -convert txt` and require exit code 0 plus nonempty output.
- Treat native readback as a smoke test only; OOXML remains authoritative.

## 2. Map source paragraphs into the final document

1. Derive exact source block header/body paragraph indexes from transcript data.
2. Identify tracked instruction paragraphs by exact declared text and required red/bold `w:ins` shape.
3. Exclude only those inserted paragraphs from the final direct-`w:p` sequence.
4. Pair the remaining final paragraphs positionally with every source paragraph.
5. Record piecewise source→final index offsets caused by inserted sibling paragraphs.

For every mapped pair verify:

- rejected text equals source text exactly
- paragraph order and attributes are unchanged
- `w:pPr` is canonical-XML equivalent
- source-character `w:rPr` signatures equal rejected-character signatures

For paragraphs not targeted by cuts or speaker corrections, require full paragraph C14N equality and no revisions. This catches silent rewrites that text-only checks miss.

## 3. Independent revision ledger

Resolve manifest ranges independently rather than importing the mutation helper as proof. Distinguish two ranges:

- **semantic anchor range**: exact manifest-matched characters used for uniqueness and editorial overlap checks;
- **physical deletion-ledger range**: semantic characters plus only the boundary separator whitespace needed to prevent leading, trailing, or doubled accepted whitespace.

A reusable physical-range policy is:

- semantic start is offset `0`: consume following whitespace;
- semantic end is `len(text)`: consume preceding whitespace;
- retained text exists on both sides and both immediate boundaries are whitespace: consume following whitespace;
- otherwise do not expand.

Keep semantic matching unchanged, and preflight the expanded physical ranges independently for overlap before OOXML mutation. For each partial-cut paragraph, concatenate accepted `w:t` and deleted `w:delText` nodes in document order and require exact reconstruction of the original source text.

For each cut:

- report cut ID, block, mode, semantic half-open range, physical deletion range, deleted character count, exact deletion preview, and revision ID(s)
- partial cut: require one exact `w:delText` at the mapped body paragraph
- whole block: require exact header and body deletions separately
- multiple cuts in one paragraph: compare a multiset of expected `(type, text)` revisions and preserve source order

Then compare all source-paragraph revisions against the complete expected multiset. Report both unexpected and missing revisions; both must be empty.

Globally verify `w:trackRevisions` once, expected `w:del`/`w:ins` counts, unique contiguous IDs, one author, parseable shared UTC dates, direct paragraph placement, legal deletion/insertion shapes, no nested revisions, and correct `xml:space="preserve"` on boundary whitespace.

## 4. Speaker correction audit

For each move, verify four nodes independently:

1. source-body deletion, including exactly one separator space when required
2. target-body insertion, including exactly one trailing separator before existing text
3. old-header deletion
4. corrected-header insertion

Compare accepted source/target body text and accepted/rejected headers with the pure expected values. Check `pPr` preservation and exact `rPr` cloning for all four affected run classes.

## 5. Accepted and rejected simulations

Construct expected accepted paragraphs directly from source + manifest:

- apply all cut ranges
- apply speaker corrections
- insert editor notes at declared sibling positions

Construct expected rejected paragraphs as the untouched source sequence plus empty inserted-note paragraphs. Compare both simulations paragraph by paragraph, not as one global concatenated string.

Search accepted text for advertisement phrases, placeholder speakers, and unexpected red text. Verify every retained header and speaker transition.

## 6. Runtime estimates

Use at least two explicitly labeled estimates:

### Timestamp/character hybrid

- source duration = maximum transcript `end`
- whole-block cut seconds = `end - start`
- partial-cut seconds = `(deleted chars / block chars) × block duration`
- accepted estimate = source duration − whole seconds − partial estimates

### Global character-ratio cross-check

Use a consistent character metric in numerator and denominator. If transcript metadata reports `clean_chars`, it may exclude whitespace; reproduce that metric by counting non-whitespace characters. Also report the Python range-index metric including spaces/punctuation when useful.

Present the two accepted estimates as a range and compare both endpoints with the target tolerance. A manifest can be structurally perfect yet fail delivery because it overcuts. If whole cuts alone make the target impossible, call that out.

## 7. Narrative and whitespace audit

Inspect 80–120 accepted characters on each side of every cut. For every cut classify:

- grammar/sentence-fragment continuity
- topic continuity
- speaker/header flow
- dangling references to deleted explanations
- advertisement or placeholder-speaker residue
- whitespace join quality

Explicitly detect:

- leading space when a start-of-paragraph deletion leaves a spaced suffix
- double space when both retained sides carry separators
- trailing space when a deletion-to-end leaves the preceding separator
- Korean morpheme/particle concatenation when neither side has a valid separator

Do not let an exact accepted-vs-manifest comparison hide manifest-authored whitespace defects. Native `textutil` readback is useful for proving those defects are visually exposed.

## 8. Reporting

Give two verdicts when needed:

- **technical/manifest verdict** for OOXML and ledger correctness
- **overall delivery verdict** including runtime and editorial continuity

Report Critical, Important, and Minor findings separately. Include hashes and state whether any protected input or persistent output was modified. Remove all temporary audit scripts/readbacks before finishing.
