# Workflow Scaling and Clean Recut

Use this reference to keep a rough-cut task proportional and editorially grounded.

## Default content-first checklist

For a trusted local source and an already-working generator:

1. Read the complete original transcript without looking at prior cut IDs.
2. Map each block's editorial function; do not cut yet.
3. Compare repetitions and draft a fresh ledger with content-based reasons.
4. Simulate and continuously read the complete accepted transcript.
5. Restore anything whose removal breaks meaning, evidence, caveats, questions, referents, or conversational rhythm.
6. Freeze the manifest only after the accepted transcript is coherent.
7. Calculate runtime from timestamps as a **post-edit result**, not as a quota.
8. Run one no-write validation, generate one new-version DOCX, audit once, and deliver only the requested artifact.

Do not insert another approval checkpoint after the user has already asked to execute unless the read-through reveals a genuinely new narrative trade-off.

## Editorial-function map

Before selecting cuts, label each block with one or more functions:

| Function | Default treatment |
|---|---|
| Question / framing | Preserve when the answer depends on it |
| Core claim | Preserve |
| Mechanism / explanation | Preserve even when long |
| Evidence / concrete example | Preserve unless a stronger duplicate exists |
| Limitation / counterargument | Preserve; it prevents overclaiming |
| Transition / conversational completion | Preserve when it carries the next beat |
| Repetition | Compare variants; cut only the weaker one |
| Topic drift | Cut when it does not return to the thesis |
| Advertisement / post-roll | Cut unless explicitly requested |

A line's duration is not an editorial function. Short does not mean disposable and long does not mean bloated.

## Repetition comparison

When two passages cover the same subject:

1. Put them side by side.
2. Identify which version contains more mechanism, evidence, qualification, or narrative context.
3. Preserve the stronger version.
4. If the earlier passage is a cold-open teaser and the later passage is the full answer, usually keep the full answer and add an editor bridge if removing the teaser makes the opening abrupt.
5. Do not remove both the framing question and the detailed answer merely because they share keywords.

Every manifest reason should name the editorial redundancy or drift. Reasons such as “needed to hit 12 minutes” are invalid unless the user supplied a hard runtime requirement.

## Accepted-transcript gate

Local boundary checks are necessary but insufficient. Read the full accepted transcript from beginning to end and verify:

- each question still has the intended answer
- pronouns, demonstratives, and phrases such as “그 위”, “그런데”, and “그러니까” retain a referent
- causal links and technical caveats survive
- removing an example has not made the conclusion unsupported
- the speaker's thesis is not made stronger or weaker than the source
- dialogue still sounds human rather than reduced to bullet points

Only after this gate may the manifest be treated as final and runtime be calculated.

## One-off audit ceiling

The audit should prove:

- source hash unchanged
- each declared cut appears exactly once
- speaker corrections and editor notes match the new manifest
- Track Changes is enabled and revision IDs are unique
- DOCX ZIP/XML and a Word-compatible readback open successfully
- accepted text has no broken grammar or boundary whitespace
- the complete accepted transcript matches the content-approved simulation
- retained runtime is reported as the post-edit result

Once these pass, deliver. Do not add another reviewer merely to review the audit.

## Escalate to engineering mode only when

- no existing generator can express the requested edit
- the generated artifact is actually malformed or loses source text/formatting
- inputs are automated, external, or adversarial rather than trusted local files
- the user explicitly requests a reusable pipeline, CLI feature, or security hardening
- a repeatable defect requires a production-code fix

Potential hardening findings that do not affect the trusted current artifact should be listed separately and deferred. Examples include swap-and-restore TOCTOU defenses, parsing every optional package part, generalized validation schemas, and exhaustive adversarial fixtures.

## Clean recut procedure

A request such as “change the plan and redo it from the beginning” is a reset signal:

- preserve prior files for comparison but mark them non-authoritative
- re-read the original transcript and timestamps
- discard old target duration, target cut count, and cut-strength quota
- ask about narrative priority only if multiple materially different stories are plausible
- assign new cut IDs and use new manifest/validation/output filenames
- independently reconsider every prior cut; do not retain it because it was already tested
- factual source repairs, such as an unmistakable speaker-boundary correction, may be rediscovered and retained
- calculate runtime only after the new accepted transcript passes continuous reading

For a conservative recut, “remove only obvious waste” is still a content judgment, not a duration band. Preserve conversational reactions when they support rhythm; if removing a duplicate teaser makes the new opening syntactically abrupt, add one explicit editor bridge note rather than deleting more substance.

## Stop conditions

Stop and simplify if any of these occurs:

- more implementation/review time than editorial decision time
- cuts are being added or restored primarily to hit a round runtime number
- a second serial spec or quality review for the same one-off artifact
- creation of new CLI/schema/test infrastructure not required by the requested DOCX
- reviewing hypothetical hostile inputs while the pinned local source already passes package/openability checks

The recovery action is: freeze code, return to the original transcript, rebuild the content-function map, finish a fresh manifest, read the accepted transcript, generate once, audit once, and deliver.
