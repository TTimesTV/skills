# Exhaustive front-half segmentation final regression audit

Use when an immutable final candidate assigns a bounded front section such as cue 1~983 plus the 983-984 seam, especially after a predecessor regression pass and later source/term edits.

## Durable lesson

A post-merge regression audit must not restrict itself to the previously changed windows or to classic protected-phrase regex hits. A candidate can preserve all earlier repairs yet still contain many residual readability defects in untouched boundaries: short topic/subject cues detached from a predicate, adverbial or reason clauses detached from their completion, and two completed question/answer beats packed inside one cue.

## Required candidate-generation passes

After the independent all-cue/all-boundary read, run all of these as candidate generators:

1. Protected-phrase adjacency audit.
2. **Adjacent-fit enumeration:** for every adjacent pair in scope, compute `len(left + " " + right)`. Manually inspect every pair that fits within the current maximum (normally 27). A fit is not automatically a finding, but it exposes avoidable fragmentary splits missed by protected-phrase regexes.
3. **Intra-cue completed-thought scan:** search each cue for a question mark followed by additional text. Distinguish indirect quotation/reporting (`"...?"라고`) from packed question→answer or echo→answer (`eSSD? eSSD에다...`, `뭐예요? 중국 거예요`).
4. Re-read all predecessor-fix windows and all later source/term-modification windows with one boundary on either side.
5. Inspect the requested outer seam and state whether it is normal or defective.

## Finding discipline

- Count an adjacent-fit candidate only when merging or redistributing materially improves small-sentence readability or protects a real grammatical relation.
- Do not merge two intentionally separate completed thoughts merely because they fit.
- Do not report a long-name or bilingual-term split when every token-preserving ≤27 alternative merely strands another connector, modifier, or predicate. Record it as a non-finding tradeoff instead.
- Default to token-preserving boundary changes. Verify unique exact match, whitespace-normalized token preservation, and all proposed cue lengths ≤27.
- Keep source fidelity, terminology, and factual accuracy outside a segmentation-only verdict, even when their already-applied edits are rechecked for segmentation regressions.

## Scope arithmetic

For cue 1~N plus seam N-(N+1):

- assigned cues inspected: `N`
- internal boundaries: `N-1`
- outer seam: `1`
- total boundaries inspected: `N`
- cue `N+1` is context only and findings should remain scoped to the assigned range unless the brief says otherwise.

## Reporting

Report one PASS/FAIL headline, category subtotals that sum to the finding total, exact current multiline strings, token-preserving proposals with measured lengths, source/term edit-window recheck notes, opening and closing hashes, and `no_candidate_edits: true`.

This workflow complements `post-merge-segmentation-regression-audit.md`: predecessor diffs locate regressions, while adjacent-fit and intra-cue scans prevent the final audit from inheriting omissions in earlier reports.
