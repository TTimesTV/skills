# Independent Plan-Compliance Review for Tracked DOCX Pipelines

Use this before regeneration when an implementation has changed after an independent artifact audit. It reviews the plan contract, not general code quality.

## Requirement-to-evidence trace

1. Extract every normative requirement from the relevant plan tasks, including exact CLI commands, named JSON fields, audit checkpoints, artifact checks, and sequencing constraints.
2. Trace each requirement through four layers:
   - plan line;
   - implementation line;
   - test assertion;
   - live execution or artifact evidence.
3. Review the negative space. A summary containing most required fields is still noncompliant if one named field is absent. Inspect returned dictionaries, printed JSON, validation records, and tests for every required field. In particular, distinguish revision-node counts from deleted-character counts; one does not prove the other.
4. A passing suite does not override a missing explicit output or audit contract.

## Staged state versus completion

Keep these states separate:

- **implementation ready**: code and contract tests are ready for regeneration;
- **pre-regeneration staged state**: the current final DOCX and cumulative audit are intentionally stale;
- **complete/deliverable**: the final was regenerated and every dependent audit section was refreshed and rerun.

A known stale final can be acceptable as a temporary review gate when it is explicitly identified and protected from delivery. It cannot prove final Task-level acceptance. After regeneration, refresh every affected section—including stored test counts—not only output, runtime, and narrative claims.

## Validation-discovered semantic corrections

A localized manifest correction may remain within plan scope without new editorial approval when all are true:

- it repairs an objective failure of a higher-level acceptance criterion, such as a retained sentence fragment or broken question/answer causality;
- it is the smallest possible range change;
- it does not add or remove a topic, change the number of edits, or alter overall editorial intensity;
- its reason remains consistent with the plan;
- it receives a focused regression test and is called out in the refreshed audit.

Treat broader editorial changes as plan changes requiring user approval. If a literal draft conflicts with explicit final narrative criteria, cite both and explain why the higher-level acceptance criterion controls.

## Semantic range versus physical deletion ledger

Keep the manifest range semantic and immutable. The physical OOXML deletion ledger may additionally consume only adjacent separator whitespace when needed to prevent leading, trailing, or doubled accepted text. Require all of the following:

- uniqueness and overlap checks use semantic ranges;
- the physical deletion contains the full semantic range;
- accepted text has clean boundaries;
- rejecting revisions reconstructs the source paragraph exactly;
- every real partial-cut fixture is checked, not just synthetic examples;
- punctuation and substantive characters are never consumed implicitly.

## Validation schema and official CLI

When one validation JSON serves as strict preflight input and a cumulative report:

- require the minimal generation keys;
- allow only explicitly planned optional audit sections;
- keep nested integrity records exact-schema;
- reject unknown top-level sections;
- do not treat stale optional PASS claims as current artifact evidence.

Run the plan's official CLI command verbatim. If it omits a companion validation argument, verify sibling-file inference, a clear missing-companion error, and a true no-write dry-run.

## Read-only independent verification

Under a no-file-modification review constraint:

- set `PYTHONDONTWRITEBYTECODE=1` for Python tests;
- use in-memory `compile(source, path, "exec")` instead of `py_compile`;
- apply DOCX changes in memory or generate only inside auto-cleaned temporary directories when allowed;
- compare source/final hashes and output size/mtime before and after dry-run;
- inspect the existing DOCX OOXML directly to prove whether it reflects the old or new manifest contract.

## Severity and verdict

- **Critical**: destructive behavior, source corruption, or unsafe publication.
- **Important**: an explicit plan contract is absent—for example, a required CLI JSON field or audit statistic. Blocks regeneration or the next stage.
- **Minor**: documentary drift or a safe, explicitly acknowledged staged condition.

Return `FAIL` whenever any Critical or Important item remains. Report `Critical`, `Important`, `Minor`, and `Verdict` separately, with plan/implementation/test/artifact line evidence for every finding.
