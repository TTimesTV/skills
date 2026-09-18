---
name: ttimes-cut-editing
description: Use when a TTimes PD must decide what to keep, cut, retake-select, or move in an interview and deliver the editor-facing cut-editing DOCX. Includes editorial judgment plus Track Changes/red move-instruction authoring; excludes actual MP3/timeline rendering.
license: MIT
metadata:
  hermes:
    tags:
    - ttimes
    - cut-editing
    - pd-editing
    - interview
    - paper-edit
    - docx
    related_skills:
    - ttimes-audio-rough-cut-rendering
  author: Hermes Agent
  version: 1.5.3
---

# TTimes Cut Editing

## Overview

`컷편집` is the **PD decision stage**. It decides what viewers should hear and in what order. It is not the act of cutting waveforms and it is not merely applying strikethroughs.

Persona:

> 나는 오디오 오퍼레이터나 Word 기술자가 아니라 티타임즈 편집 PD다. 방송 발화와 제작 현장 발화를 구분하고, 질문–주장–근거–사례–결론의 기능을 판단한다. 길이를 맞추기 위해 자르지 않고 정보 밀도와 방송 가능성을 높이기 위해 자른다.

Core boundary:

- **컷편집:** PD가 `KEEP / CUT / MOVE / RETAKE_SELECT / REVIEW`를 판단하고, 그 승인 판단을 변경추적 삭제·빨간 이동 지시가 있는 편집자용 DOCX로 완성한다.
- **러프 컷편집:** 편집자가 승인된 컷편집 DOCX를 원본 음원·영상 타임라인에 구현한다. 신규 내용 판단은 하지 않는다.

## When to Use

Use when the user asks:

- 어디를 자를지 판단해 달라.
- 방송 가능한 흐름으로 컷편집해 달라.
- 제작 발화, 재시작, 중복 설명을 골라 달라.
- 기존 편집자 컷처럼 내용 구성을 압축해 달라.
- 원본·싱크·취소선본·컷편집본 사이의 편집 의미를 비교해 달라.
- 기존 컷을 버리고 처음부터 다시 판단해 달라.

Do not use this skill merely to render an approved cut plan to MP3. Use `ttimes-audio-rough-cut-rendering` for that.

## Inputs and Authority

Possible inputs:

- complete source-close timecoded transcript
- source audio when transcript semantics or take boundaries are unclear
- the user's narrative priority
- prior PD cut DOCX, final editor artifact, EDL, or comparison cut
- runtime only as a post-edit sanity signal

Before judgment:

1. Search same-project files for `원본`, `싱크`, `컷편집`, `수정`, approved, EDL, and final audio variants.
2. Reconstruct genealogy by comparing the full restored transcript, not filenames alone.
3. Treat final approved EDL/audio as strongest evidence, then approved cut DOCX, then review/strike DOCX, then clean transcript.
4. Never merge materially different cut plans silently.
5. Freeze one canonical source and label other plans as references.

Completion criterion: the canonical source and reference plan are named, their relationship is known, and the decision stage is not operating on an accidental review version.

## Pass 1 — Broadcast Gate and Production Speech

This is a cut-editing judgment even when no deletion mark exists.

Inspect the head and tail independently. Remove:

- `준비됐습니다`, `시작하겠습니다`, `들어가 볼게요`
- mic/camera/recording checks
- crew/editor-directed speech
- post-close room conversation
- failed count-in or abandoned opening

Semantic test:

- CUT: `이제 촬영 시작하겠습니다`
- KEEP: `태양전지 연구를 시작한 것은 1997년입니다`
- CUT: `다시 갈게요` when a clean replacement follows
- KEEP: `태양전지가 다시 각광받고 있습니다`

A segment is production speech when it addresses production rather than viewers, sits outside the intended on-air gate, adds no subject-matter proposition, or is replaced by a clean take. Explicit production commands can be cut directly; borderline cases require two signals.

Completion criterion: the accepted transcript begins on the intended viewer-facing sentence and ends on the intended close, while valuable content recorded after the nominal close is either moved before the close or explicitly rejected.

## Pass 2 — Retakes and Local Cleanup

Cut or select among:

- abandoned starts followed by complete restarts
- duplicate opening/question takes
- word-search that is replaced by a clean term definition
- isolated third-party acknowledgements
- orphan `네네`, `맞습니다`, or `그래서` created by an adjacent cut
- immediate repetitions that add no rhythm or meaning
- English terminology followed by a semantically duplicate Korean retake, when one complete version is sufficient
- part-boundary production talk such as where to stop, what to ask next, or what the editor should insert

Do not remove all natural hesitations or host reactions. A reaction can frame the next answer or preserve human rhythm. Do not delete all English/Korean pairs either: keep the English term once when the name itself matters and retain the Korean explanation when it adds meaning.

After every local cut, check dependent cleanup: if an interruption is removed, its reply may also need removal. After a part-boundary block is removed, verify the last accepted line is a complete viewer-facing sentence; remove or escalate orphan speaker labels, `네`, `그럼`, `이대로`, and half-started next-part speech.

## Pass 3 — Explicit Markup and Moves

Read all relevant forms:

- Track Changes deletion (`w:del`, `w:moveFrom`)
- direct strikethrough
- comments and natural-language edit notes
- red insertion/relocation instructions
- `w:highlight` or paragraph shading used to pair a pickup/source block with a natural-language destination note

Classify each as:

- `CUT`
- `MOVE`
- `KEEP`
- `NON_AUDIO`
- `NEEDS_REVIEW`

Moves are not deletions. Record source span, destination, ordering, and transition. Net runtime should remain approximately unchanged.

A strike-review document may encode a move without `w:moveFrom`/`w:moveTo`: a highlighted pickup after the formal close can be the source, while a highlighted note such as `뒤에 형광색 부분 여기에 넣기` marks the destination. Reconstruct this relationship before simulating the accepted state. Apply CUT, remove NON_AUDIO instructions, remove the MOVE source from its original location, insert it at the destination, then clean failed starts and speaker-boundary errors inside the moved block. Never assume that every highlighted token is approved speech.

See `references/direct-strike-highlight-move-forensics.md` for the reconstruction and validation procedure.

Explicit markup is evidence, not infallible ground truth. A known PD-approved tracked plan outranks a partial review strike plan. A cut plan may still miss production speech or leave a broken connector; audit it rather than worship it.

### OOXML deletion accounting

When the task asks for a revision-by-revision ledger, do not equate raw `w:del` count with spoken deletion count.

1. Count every `w:del`, then classify it by parent and payload.
2. Treat a `w:del` under `w:rPr` as a formatting/paragraph-property revision marker unless it actually contains deletion text; do not create a semantic ledger row from it.
3. Use text-bearing direct-`w:p` deletions as the initial revision ledger, then preserve their exact revision IDs and paragraph identities.
4. Report both counts, e.g. `128 total w:del = 79 text-bearing cuts + 49 rPr property markers`, instead of silently collapsing them.
5. Label character metrics precisely. The authoritative literal metric is the sum of exact `w:delText` Unicode code points, including spaces and speaker/timecode text. A whitespace-normalized or metadata-stripped count is a separate derived metric and must not replace the literal count.
6. For whole-paragraph cuts, empty left/right anchors are structural facts; serialize them explicitly as `<PARAGRAPH_START>` and `<PARAGRAPH_END>` when a tabular contract requires nonempty fields.

See `references/lee-juhwan-ep1-cut-editing-calibration.md` for a worked 128-container/79-text-revision example. For strict raw/semantic text separation, original `w:id` traceability, boolean/detail fields, local-vs-global defect semantics, validator gates, and safe review sequencing, see `references/decision-ledger-evidence-contract.md`.

## Pass 4 — Content and Narrative Editing

Map each section:

```text
question → answer thesis → mechanism/evidence → representative example → implication/transition
```

Protect the thesis and all unique information needed to understand the conclusion.

### Safe high-confidence cut classes

- `REDUNDANCY`: a weaker statement duplicates a clearer retained statement
- `HOST_RESTATE`: the host repeats what the guest already established
- `FAILED_SUMMARY`: the host summary mixes standards or misstates the answer
- `SUPERSEDED_EXPLANATION`: a harder version repeats a clearer definition/result
- `FACT_RISK`: uncertain or false aside that is not required by the core argument
- `WEAK_EXAMPLE`: several examples serve the same function and a stronger, evidenced example remains
- `UNRECOVERED_TANGENT`: history or application idea never returns to the thesis
- `BLOCK_SUBSUMED`: an entire Q/A block is fully replaced elsewhere

### Two-key rule

An unmarked content cut requires at least two:

- no unique proposition, number, definition, caveat, or causal bridge is lost
- a clearer complete retained segment performs the same function
- the segment is off-axis from the current question
- the segment is one of several examples and a stronger one remains
- deletion leaves grammatical and logical continuity
- the segment adds fact-check risk without supporting the conclusion

A whole Q/A block requires at least three and an over-cut review.

### Protected content

Never auto-cut:

- first clean answer to a question
- first occurrence of a key number or definition
- causal/contrast bridge
- limitation or counterargument that changes interpretation
- commercialization, cost, stability, yield, competition, policy, or strategy conclusion
- a sentence needed to resolve `그래서`, `그렇기 때문에`, `이것`, or another referent
- a moved block that supplies the ending or execution condition

## Editorial Pattern Learned from the Park Nam-gyu Calibration

The editor was not simply shortening. The retained axis was:

```text
AI-era power problem
→ perovskite technical advantage
→ commercialization bottleneck
→ China versus Korea's differentiated route
→ solar + intelligent ESS + industrial electrification
→ K-energy export system
→ industrial ecosystem required to execute it
```

Observed choices:

- preserve the scientist's discovery story because it establishes authority and causality
- remove mineral-name history because it has no later payoff
- keep intuitive physical result and representative numbers; remove a second, harder lecture of the same point
- keep satellite light-weight evidence; remove speculative smartphone/space-data-center accumulation
- keep strategy-driving China scale; remove repeated amazement and risky instant conversions
- move the industrial-ecosystem conclusion before the formal close

Do not generalize these as `all history`, `all technical detail`, `all politics`, or `all lifestyle examples` must be cut. Their narrative function decides.

See `references/park-namgyu-cut-editing-calibration.md`.

## Cross-Case Rules Strengthened by the Lee Ju-hwan Calibration

The Lee Ju-hwan Episode 1 plan showed a different edit mode: preserve the lecture spine and perform dense local cleanup of production speech, retakes, host detours, self-promotion, and immediate duplication. Together with the Park Nam-gyu case, it strengthens four general rules.

### 1. Audit backward references, not only forward connectors

Before deleting a fact or phrase, search later accepted speech for explicit references to it:

- `아까 말씀하신`
- `앞서 말한`
- `두 번째 이유`
- `4년째라고 하셨는데`
- `그 사례/그 수치/그 책`

If the antecedent is cut, either preserve it, remove/rewrite the later reference, or retain a different complete antecedent. A clean local join can still be globally incoherent.

### 2. Preserve principle → example → conclusion chains

A representative example must not survive without the principle that explains why it appears. For each retained case, verify:

```text
what principle or risk calls the example
→ what the example demonstrates
→ what conclusion is drawn
```

If abstract setup is long, compress it to one sentence rather than deleting the entire bridge and dropping straight into a medical, legal, financial, or technical case.

### 3. Separate self-promotion from argumentative authority

Cut or compress awards, bestseller/lecture boasts, sales motive talk, and biography that does not change the argument. Preserve credentials, customer counts, failure rates, costs, or representative numbers when they establish evidence, scale, or why the speaker is qualified to make the claim.

### 4. Validate the accepted document structurally

In addition to semantic reading, detect:

- punctuation-only paragraphs such as `.`
- orphan speaker/timecode lines after a deleted block
- incomplete head/tail fragments
- episode endings that do not close on a viewer-facing complete thought
- repeated greeting or immediate duplicate left outside tracked deletions
- partial-example boundaries that end on a hanging conjunction or unfinished predicate

See `references/lee-juhwan-ep1-cut-editing-calibration.md`.

## Series-Level Rules from the Lee Ju-hwan Episodes 1–2 Standardization

The two-episode comparison adds two safeguards without changing the established workflow.

### Inventory unique propositions before a large block cut

`BLOCK_SUBSUMED` is a hypothesis, not proof that a whole Q/A block is redundant. Before deleting a long block:

1. List each proposition in the block.
2. Point to the exact retained sentence that replaces it.
3. Separate repeated examples from new causal bridges, state definitions, responsibility boundaries, or execution mechanisms.
4. If a unique principle can be compressed, preserve one complete sentence rather than deleting it with the repetitive case.

A local join can be clean while the argument loses a global bridge. Count raw revisions and semantic edit groups separately; dozens of `w:del` rows may belong to one block-level defect.

### Audit tracked corrections as editorial decisions

An insertion or terminology correction is not automatically harmless. If it fixes or introduces a domain state, proper name, number, unit, or certainty level, mark it `NEEDS_REVIEW` until the source audio or an authoritative domain definition confirms it. Fluency and familiar wording do not prove semantic fidelity.

### Run an accepted-state correction pass outside Track Changes

A revision ledger does not cover every defect. Read the full accepted transcript and flag unmarked:

- hanging predicates and incomplete host turns
- ASR entity errors or accidental numbers
- enumeration promises such as `두 가지` when only one item follows
- retained numeric contradictions across axis count, exponent, percentage, multiplier, or unit
- conflicting state names or transition order

Track Changes may be internally consistent while the accepted transcript remains wrong.

### Salvage unique definitions without restoring production audio

If the only full name or definition of a body term appears in post-roll production talk, keep the production block cut. Recover the definition at the first viewer-facing mention through a caption, pickup, or verified narration. Do not restore room conversation merely because it contains a useful definition.

See `references/lee-juhwan-series-cut-editing-standardization.md` for the two-episode comparison, large-block over-cut example, tracked-correction audit, accepted-state correction findings, and Gold/Anti-Gold regression cases.

## Format and Entity Rules from the Monthly-Tech Calibration

Before deciding cut intensity, classify the source form:

- **Interview:** question/answer, authority, counterargument, and story restructuring may require macro cuts.
- **Prepared single-speaker briefing:** preserve the prepared item spine by default and prioritize micro cleanup of false starts, immediate duplication, external interruption, and terminology slips.
- **Panel or meeting:** speaker turn, overlap, and role-dependent value require a separate turn-level pass.

Do not infer that every source needs the retention ratio or block-cut style of a prior calibration.

### Proper-name and number collision gate

A cleaner take is not automatically the correct take. If competing versions differ in:

- company/person/product/event name
- model or technology label
- date, percentage, price, capacity, or other number

then mark `NEEDS_REVIEW`, re-listen to the audio, check an authoritative source when appropriate, and run a global accepted-state entity consistency scan. Never choose the most frequent spelling as truth merely because ASR repeated it.

### Interruption-sandwich audit

For an external alarm, announcement, phone call, crew interruption, or technical stop, inspect the whole sandwich:

```text
hanging phrase before interruption
→ external/production audio
→ crew response or runtime discussion
→ abandoned restart
→ final clean restart
```

Keep the last complete pre-interruption thought and the clean restart; remove the contaminated middle only after verifying punctuation ownership and join continuity.

### Cross-paragraph micro-edit audit

Immediate duplication can cross paragraph/timecode boundaries. Compare the tail of each accepted block with the head of the next block instead of limiting duplicate detection to one paragraph.

See `references/monthly-tech-june-cut-editing-calibration.md`.

## Adversarial Rules from the Park Young-sun–Lee Sang-gi Calibration

This direct-strike plan was audited rather than treated as gold. It adds safeguards for aggressive partial deletions and highlighted relocation blocks.

### Preserve speaker labels atomically

If a partial cut removes the speaker/timecode at the start of a paragraph but leaves spoken text, preserve or reconstruct that label separately. A semantically reasonable cut that creates an unlabeled utterance is not editor-ready.

### Treat highlighted move spans as candidate bundles

Highlight plus a move instruction establishes relocation intent, not clean-take boundaries. Rejudge the highlighted span internally for failed starts, host interruptions, questionable numerical reactions, diarization errors, and source-position residue. Move only the selected clean take, remove it from the source position, and delete the instruction as `NON_AUDIO`.

### Verify derived numerical reactions

When a host converts a guest's number into `one third`, `N times`, or `N people for a month`, verify that denominator, unit, and time basis support the conversion. If it cannot be derived from the recorded premise, mark it `NEEDS_REVIEW` or cut the reaction; fluency does not validate arithmetic.

### Audit predicate ownership across speaker boundaries

ASR can split one predicate across speakers, such as `말씀드 / 드릴 수 있습니다`, then attach only a trailing acknowledgment to the second speaker. Use grammar plus audio to assign the sentence completion and separate the reaction. Without audio, keep it unresolved rather than accepting diarization literally.

### Preserve epistemic qualifiers

Before deleting `조심스럽게`, `제가 알기로`, `정확한 규모는 모르지만`, `추정하면`, or similar phrasing, test whether the retained claim changes from uncertain inference to factual assertion. If certainty changes, the qualifier is meaning-bearing and protected.

### Keep an executable minimum in policy conclusions

Do not reduce policy logic to `지원이 필요하다` when the deleted material contains the only actor, target, mechanism, or execution structure. Preserve at least one sentence answering who should do what, through which institution or infrastructure, and why it resolves the bottleneck.

See `references/park-youngsun-lee-sanggi-cut-editing-calibration.md`.

## Calibration Governance

Preserve a workflow the user has already approved. A positive reaction such as `좋다`, `이 자세가 마음에 든다`, or praise for one result is evidence that the **current** workflow worked; it is not by itself an instruction to redesign that workflow.

When a new cut plan or correction arrives:

1. Keep the established sequence: canonical-source inspection → independent reason/story/adversarial reviews → Main evidence-based synthesis.
2. Store case-specific observations in `references/` first.
3. Promote a rule into the core SKILL.md only when it is an explicit workflow correction, a verified defect that would recur, or a pattern supported across multiple cases.
4. For a material change to role structure, output contract, or decision threshold, state the proposed change and confirm intent before replacing an approved workflow.
5. Do not freeze known errors: small verified fixes and missing validation checks should still be patched promptly.

This is a stability rule, not a ban on learning. Prefer additive references and narrow safeguards over rewriting successful core behavior from one conversational remark.

## Three Reviews

Use three independent lenses on the same canonical source and ledger.

### Under-cut review

Find remaining production chatter, failed takes, duplicated propositions, repeated examples, and weak host preambles.

### Over-cut review

Find lost unique facts, mechanisms, numbers, caveats, strategic logic, or human rhythm.

### Continuity review

Read the complete accepted transcript. Check Q/A pairing, referents, connectors, chronology, speaker rhythm, and moved blocks.

A local boundary sounding clean is not enough. The whole accepted transcript must make sense.

## Runtime

Runtime is an outcome and anomaly detector, not a quota.

- A much longer result can signal wrong document authority, missed production speech, or under-cut repetition.
- A much shorter result can signal over-cutting or a move treated as deletion.
- Never delete the final seconds merely to enter a target band.

For the Park Nam-gyu case, literal strike execution produced about 43:28 while the approved editorial plan projects about 38:14–38:20. This calibrates the difference between a review-mark execution and cut editing; it is not a universal retention ratio.

## Output: Editor-Facing Cut-Editing DOCX

The user-facing output is the completed `*_컷편집.docx` that the PD hands to the editor.

Internally maintain an approved decision ledger. Each operation contains:

- stable ID
- source block/time range/text anchors
- `KEEP`, `CUT`, `MOVE`, `RETAKE_SELECT`, or `NEEDS_REVIEW`
- reason class and short editorial rationale
- retained replacement or explicit statement that the story axis excludes the topic
- left/right retained context
- move destination and order when applicable
- review status

The final DOCX must:

- preserve the source file unchanged at its original path
- encode deletions as real Word Track Changes (`w:del`/`w:delText`)
- encode relocation, transition, and insertion instructions as tracked red text
- preserve speaker labels and timecodes
- use globally unique revision IDs with author/date metadata
- pass Accept All and Reject All simulations
- pass ZIP/XML/openability checks and source-hash verification
- remain faithful to the approved ledger; OOXML difficulty may not change the editorial decision

Also keep internally:

- accepted transcript
- unresolved decisions
- expected runtime calculated after the ledger is stable
- source/ledger/output hashes and revision accounting

Handoff:

- completed and approved cut-editing DOCX → `ttimes-audio-rough-cut-rendering`
- unresolved editorial judgment → remain in this skill; do not render

Detailed OOXML and validation procedures are preserved under this skill's `references/` directory, especially `ooxml-validation.md`, `integrated-application-ledger.md`, and `tracked-instruction-paragraphs.md`.

## Common Pitfalls

1. **Literal-cut tunnel vision:** marked phrases disappear but production speech and editorial redundancy remain.
2. **Keyword deletion:** `시작` can be production or substantive content.
3. **Wrong-ground-truth consensus:** reviewers agree on an accidental document version.
4. **Quota cutting:** runtime becomes a reason to sacrifice information.
5. **Long-means-bad:** unique technical or historical information is removed merely because it is long.
6. **Reaction-means-noise:** useful host rhythm is erased.
7. **Connector orphaning:** a cut leaves `그래서` or `그렇기 때문에` without its premise.
8. **Move-as-delete:** the source is removed but the destination insertion is omitted.
9. **Block-only editing:** whole paragraphs are judged, but short duplicate phrases, failed wording, and repeated terminology remain inside retained paragraphs.
10. **Raw revision counting:** empty/split `w:del` containers are treated as semantic cut groups; rebuild accepted/restored transcripts and group nonempty deletions by context.
11. **Part-boundary residue:** production discussion is removed but a final speaker label, `네`, or half-started next-part sentence remains.
12. **Speakerless partial deletion:** a cut removes the paragraph's speaker/timecode but leaves accepted speech with no owner.
13. **Highlight-as-clean-take:** every highlighted run is moved even though the span contains failed starts, interruptions, or diarization errors.
14. **Fluent arithmetic acceptance:** an intuitive host conversion is kept without checking its denominator, unit, and time basis.
15. **Tracked-only blind spot:** the revision ledger passes while unmarked ASR entities, enumeration promises, hanging predicates, or retained-number conflicts remain in accepted speech.
16. **Evidence-field collapse:** trimmed semantic text replaces raw OOXML text, synthetic analysis IDs replace `w:id`, or explanatory prose is stored in boolean fields.
17. **Stale concurrent review:** reviewers inspect ledgers during normalization/enrichment and report mixed pre/post-mutation evidence. Freeze artifacts before independent review and rerun reviewers after fixes.
18. **Production-definition restoration:** room conversation is restored wholesale merely because it contains the only full name; salvage the definition into viewer-facing text instead.
19. **Happy-path validator:** current artifacts pass, but empty detail fields, fabricated raw text, fake `w:id`, or duplicate analysis IDs also pass. Run adversarial mutation tests and cross-check every ledger row against raw revisions.
20. **Manifest shadow constants:** source paths, hashes, or expected counts are duplicated in validator code, allowing the manifest and validator to disagree silently. Make the manifest authoritative and keep extractor statistics separate from ledger-only metadata.
21. **False mutation-proof:** a mutated copy fails only because the clean baseline was already invalid or changed concurrently. Require a clean baseline PASS, the intended mutation-specific rejection signal, stable before/after fingerprints, and a final rerun after report creation. See `references/final-state-rerun-and-validation-report-freshness.md`.

## Verification Checklist

- [ ] Canonical source and plan genealogy established
- [ ] Source form classified: interview, prepared briefing, panel, or other
- [ ] Head/tail broadcast gate reviewed
- [ ] Production speech and retakes judged even when unmarked
- [ ] External interruptions audited as complete interruption sandwiches
- [ ] Whole-block story pass and within-sentence micro-edit pass both completed
- [ ] Immediate duplication checked within and across paragraph/timecode boundaries
- [ ] Competing proper names and numbers resolved by audio/source verification or marked `NEEDS_REVIEW`
- [ ] Accepted-state entity spelling and numeric references are globally consistent
- [ ] Retained axis count/exponent, percentage/multiplier, and units are arithmetically consistent
- [ ] Enumeration promises (`두 가지`, `N개`) close with the stated number of items
- [ ] Unmarked ASR entities and hanging predicates were audited outside Track Changes
- [ ] Unique definitions found only in production talk were salvaged via verified caption/pickup without restoring the production block
- [ ] Part boundaries end on a complete viewer-facing sentence with no orphan label/acknowledgement
- [ ] Explicit cuts and moves accounted for
- [ ] Ledger preserves raw OOXML text separately from trimmed semantic text
- [ ] Raw `w:id`, synthetic `analysis_id`, and `semantic_group_id` are distinct
- [ ] Boolean judgment fields contain strict booleans and explanations live in detail fields
- [ ] Validator checks source hash, raw character totals, exact row counts, enum/boolean format, and raw-revision 1:1 order
- [ ] Validator reads source authority and expectations from the manifest rather than shadow constants
- [ ] Adversarial mutation tests reject empty detail/analysis IDs, duplicate IDs, fake `w:id`, fabricated raw text, and paragraph/operation mismatches
- [ ] Clean baseline passed before mutation tests, and each mutation failed for its intended rejection signal rather than an unrelated baseline defect
- [ ] Manifest/validator/tests/ledgers were fingerprinted before and after review; any concurrent change triggered a complete stable-state rerun
- [ ] Final validator and full suite were rerun after writing the report
- [ ] Extractor-only expected statistics are separated from ledger-only row/scope metadata in the manifest
- [ ] Artifacts were frozen before independent review; reports were regenerated after any normalization or enrichment
- [ ] Highlighted pickup/source blocks paired with destination notes; NON_AUDIO instructions removed
- [ ] Highlighted MOVE spans internally retake-selected rather than copied wholesale
- [ ] MOVE source removed from its original position and internal retake/speaker splits reviewed
- [ ] Partial deletions preserve a valid speaker/timecode for every retained utterance
- [ ] Cross-speaker predicate completions verified by grammar and audio, or marked `NEEDS_REVIEW`
- [ ] Derived host ratios/conversions are supported by denominator, unit, and time basis
- [ ] Epistemic qualifiers are preserved whenever deleting them would turn an estimate into a factual assertion
- [ ] Retained policy conclusions still name an actor, target, or execution mechanism rather than only requesting generic support
- [ ] Every unmarked content cut passes the two-key rule
- [ ] Unique facts, numbers, mechanisms, caveats, and strategic conclusions protected
- [ ] Accepted transcript read continuously
- [ ] Forward connectors and backward references both retain valid antecedents
- [ ] Every retained representative case still has its principle/mechanism bridge
- [ ] No punctuation-only paragraph, orphan speaker/timecode, hanging predicate, or incomplete episode tail remains
- [ ] Under-cut, over-cut, and continuity reviews complete
- [ ] Runtime calculated only after decisions stabilize
- [ ] Internal decision ledger is stable and has no unresolved judgment
- [ ] Final `*_컷편집.docx` uses valid Track Changes deletion and tracked red move instructions
- [ ] Accept All/Reject All simulation, ZIP/XML parsing, openability, and revision accounting pass
- [ ] Source DOCX hash remains unchanged
- [ ] Final DOCX is ready for editor handoff or `ttimes-audio-rough-cut-rendering`
