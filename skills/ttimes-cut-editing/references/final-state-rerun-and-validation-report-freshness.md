# Final-State Rerun and Validation-Report Freshness

Use this audit after generation and after the validation JSON has received its final test/output/OOXML/runtime sections.

## Failure pattern

A tracked-DOCX pipeline may use one JSON file for both:

1. strict preflight integrity input, and
2. the cumulative validation report required by the plan.

Generation can pass against the early minimal shape, then the report gains fields such as `tests`, `dry_run`, `output`, `ooxml`, and `runtime`. If the generator uses exact-key validation, the final report can invalidate its own dry-run and generation commands. Stored `PASS` counts then describe a pre-report snapshot rather than the delivered state.

A second plan-compliance trap is testing a corrected CLI invocation rather than the exact command printed in the plan. A required flag added by implementation is still a spec mismatch when the plan omits it.

## Mandatory final-state audit

1. Run the plan's CLI command **verbatim** and record its real exit status.
2. Run the implementation's current/documented command against the final on-disk manifest and validation report.
3. Compare every exact-key schema validator with the final report shape, including nested integrity records.
4. Re-run the directly affected contract test after the report reaches its delivered form. Never treat a test result stored inside a subsequently modified input/report file as current evidence.
5. Independently audit the existing DOCX even if regeneration fails. Report separately:
   - artifact validity;
   - dry-run validity;
   - generator rerunnability;
   - plan-command compliance.
6. For a dry-run, verify complete in-memory application and expected counts, then prove no publication side effects. Practical probes include unchanged output hash and zero calls to `Document.save`, `tempfile.mkstemp`, and `os.replace`.
7. Run the final-state test before claiming the full suite still passes. A prior `Ran N tests ... PASS` record is stale if any fixture or input used by those tests changed afterward.

## Concurrent artifact mutation guard

Independent review can overlap a final fixer or publisher. A baseline may PASS, then a manifest or validator can change milliseconds later; mutation tests can also appear to fail for the wrong reason if their temporary baseline was copied during that transition.

1. Before validation, snapshot SHA-256 (or at minimum mtime + bytes) for the manifest, validator, tests, ledgers, and reports in scope.
2. Run the clean baseline first and require PASS before interpreting any adversarial mutation result.
3. Run each mutation in an isolated temporary copy and record the **specific intended rejection signal**, not only nonzero exit status or top-level `pass=false`. A pre-existing baseline defect must not count as proof that the mutation was detected.
4. Snapshot the tracked files again after tests. If any changed, discard the prior evidence, wait for a stable snapshot, and rerun the clean baseline, full suite, and every affected mutation.
5. Write the final report only from the stable rerun; then perform one post-report clean validator/test run. The report itself may be the only persistent file created by a read-only audit.
6. If a schema migration moves a field between namespaces (for example, `expected.ledger_rows` to source-level `ledger_rows`), update manifest and validator atomically or treat the intermediate state as non-reviewable.

A fail-closed claim therefore requires both: `clean baseline PASS` and `mutated copy FAIL for the intended reason`.

## Required-key plus optional-audit schemas

When one file must serve as both preflight input and cumulative report, preserve fail-closed behavior with two sets:

- required top-level keys that must always exist;
- an explicit allowlist of optional audit sections.

Accept a document only when `required ⊆ actual ⊆ required ∪ optional`. Continue using exact-key validation for nested integrity records such as `{path, sha256, bytes}`. Add one RED→GREEN test containing every declared optional section and a separate test proving an unknown top-level section is still rejected.

Boolean provenance flags do not belong inside an exact integrity record unless the schema explicitly includes them. Prefer `source: {path, sha256, bytes}` and place claims such as `source_unchanged` in an audit/output section.

## Pre-existing immutable output

A protected final DOCX may already exist when the suite runs. Tests that generate to custom temporary paths must not assert that the protected final is absent. Instead:

1. snapshot its SHA-256 and byte count before the test;
2. generate only to a temporary/custom output;
3. assert the protected final has the same hash and byte count afterward.

This makes the test valid both before and after publication while directly enforcing the real invariant. If a contract-only fix intentionally does not regenerate the final, distinguish current in-memory/dry-run checks from historical published-artifact audit values; never imply the existing final contains the new contract behavior.

## Integrity update order

After changing a manifest semantic field, recompute hash and byte count from the actual file bytes and update only the matching sidecar record. Then rerun the semantic fixture test, full suite, dry-run, and final source/output invariants. Do not copy a guessed size or stale digest into the report.

## Preferred designs

- Best: separate immutable preflight integrity input from the mutable cumulative audit report.
- Acceptable: define one explicit expanded report schema and test all plan-required sections.
- Keep plan commands and argparse requirements synchronized; do not silently rely on reviewers adding omitted flags.
- Treat stored audit results as historical once any fixture, manifest, validator, or report field they depend on changes; rerun before relabeling them current.

## Severity

A valid final DOCX with a dry-run/generator that cannot rerun is normally **Important**, not a clean pass. Missing direct assertions for optional diagnostics are **Minor** when independent execution proves the implementation correct.
