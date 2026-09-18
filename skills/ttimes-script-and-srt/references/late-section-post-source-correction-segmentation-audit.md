# Late-section post-source-correction segmentation audit

Use when an immutable candidate has already passed a source/term correction generation after a bulk segmentation merge, and the user assigns a bounded late-section final regression audit.

## Scope arithmetic

For inclusive cue range `[A, B]`:

- inspect `B-A+1` cues;
- inspect all `B-A` internal boundaries;
- include seam `(A-1)-A` when the range begins at a section boundary;
- state internal and seam counts separately.

Hash the candidate before and after report generation. Never edit it during the audit.

## Two-layer freshness check

1. Read every current cue and adjacent boundary independently. Do not begin from old findings.
2. Recheck prior-generation fixes against the current hash:
   - exact-search every prior token-preserving proposal;
   - if a later source correction changed one lexical token, verify the **structurally analogous current split** rather than marking the old proposal missing;
   - distinguish “prior fix retained” from “new current-hash regression nearby.”
3. Diff the immediate predecessor only as a locator for source-corrected windows. Re-read each changed window plus both outer seams.

Typical source-correction regressions include:

- a corrected attributive form creating `SAP 같은 / 회계 시스템`;
- a corrected year or possessor leaving `SK하이닉스의 / 매출 성장률`;
- grammar restoration creating a split inside a fixed compound such as `데이터센터 / 건설 속도`;
- a corrected head noun preserving the intended prior boundary even though the old exact proposal no longer matches.

## Full-read findings commonly missed by prior regression reports

A report that validated only changed windows can miss older residual defects elsewhere. During the independent full read, also catch:

- short object/adverbial cues whose predicate can be merged within 27 characters;
- isolated transition or location cues (`그런데`, `Meta에서`, `여러분, 그러면`) when a complete small sentence fits;
- question plus answer/reason packed in one cue (`왜요? 주민들이 …`);
- subject/value judgments that fit in one cue (`마진율 / 10%도 안 돼요`);
- long noun compounds split at an avoidable boundary.

Count a finding only when a materially better token-preserving redistribution exists and every proposed cue is `<=27` characters. Do not replace one protected split with another.

## Deterministic report gate

Build findings as structured records containing category, exact current multiline string, proposal, and rationale. Before delivery assert:

- finding heading count = current/proposal pair count = headline total;
- category subtotals sum to the headline total;
- every current block occurs exactly once in the immutable candidate;
- removing only whitespace/cue boundaries yields identical current/proposal token streams;
- every proposed cue is within the visual maximum;
- candidate opening and closing SHA-256 match.

Report prior-generation verification separately from newly confirmed current-hash findings. Keep source fidelity, terminology, and factual accuracy outside a segmentation-only verdict.
