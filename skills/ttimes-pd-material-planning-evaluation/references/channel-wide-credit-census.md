# Channel-Wide Credit Census and Resumable Evaluation

Use this reference when the request expands from one credited episode to every episode in a channel.

## Freeze the population first

- Freeze one authoritative channel tab/export as the population before searching credits.
- Keep excluded tabs (for example Shorts or Streams) in separate files and never merge them into official completeness counts.
- Gate every downstream metadata, credit, and evaluation script against the frozen ID set; cached metadata can contain out-of-scope IDs.
- Prove completeness with an explicit equation:
  `metadata available + explicitly classified inaccessible = frozen population`.
- Keep unresolved access failures separate until individually retried and classified. Do not call the census complete while `unresolved > 0`.

## Credit evidence hierarchy

1. Explicit role and person in the description.
2. Explicit role and person in an opening credit.
3. Explicit role and person in an ending credit.
4. Other on-screen role labeling.

Name-only hits, adjacent-but-unlinked OCR words, stylistic similarity, repeated guests, and job-title inference stay in a hold ledger. `RA` must not be converted to `PD`. Shared credits remain shared; never infer object-level authorship.

## Screen-credit scans

- Description-unconfirmed videos require both opening and ending inspection when the project demands it.
- OCR only proposes candidates. Human adjudication must verify that role and name belong to the same credit item/frame before promotion.
- Preserve candidate frames and OCR text as evidence; record no-hit, candidate, hold, inaccessible, and retry-exhausted states distinctly.
- A 403 from a section-download URL is not proof that the video is inaccessible. Retry metadata/direct access separately and leave screen-scan failure in a hold state.

## Resumable batch architecture

- Persist one JSONL/CSV record per video immediately after processing.
- Build the queue as `frozen population − terminal states`; do not depend on one long-lived process.
- Process small bounded batches, then recompute progress. This survives gateway/background-process lifetime limits and avoids file-descriptor pressure from thousands of frames.
- **Transient failures never become completed scan states merely because a retry count was reached.** Keep them out of completeness totals, rotate them behind never-attempted items so the census can advance, and retry later with a fresh URL/process. If the project must stop, report them as explicit holds; do not relabel them `no credit` or let the driver count them as done.
- Distinguish access classification from segment-download mechanics. A successful metadata/direct-video probe does not prove that an FFmpeg section download will work, while a section-download 403 or missing `.part` file does not prove the source video is inaccessible.
- For unattended mechanical scans, a script-only local cron tick can process one small batch without sending user notifications. Verify the first tick actually increases the ledger, and remove/pause the job after completion.
- Cron script paths under Hermes must be relative to `~/.hermes/scripts/`, not absolute.

### Concurrency lock and resource scheduling

- Put an atomic lock around each cron tick (for example, creating a lock directory and removing it in `finally`). If the lock already exists, return `LOCKED_SKIP`; never let a manual run and scheduled run write the same output or `.part` file concurrently.
- Treat `No such file ... .part` during otherwise successful transcoding as a likely concurrent-writer race before classifying it as access failure.
- Do not run high-fan-out full-video vision evaluation and large opening/ending OCR scans at the same time on a low file-descriptor limit. Pause one lane, finish the bounded batch, verify descriptors are available again, then resume the other lane.
- A cron/tool process can fail before the script starts when the parent process has exhausted descriptors. That failure must not append a per-video scan result.
- After changing lock/retry logic, run one tick and verify: the job reports success, the unique terminal-state count increases, no duplicate `.part` race appears, and OCR candidates/no-hit counts remain auditable.

## File and CLI edge cases

- Video IDs can begin with `-`. Pass them as `--id=<value>` or after `--`; never as a separate positional-looking value that argparse may treat as an option.
- Load contact sheets sequentially or in small groups. If file descriptors are exhausted, stop launching work, let active workers close files, then retry narrowly.

## Caption recovery and transcript provenance

- If a cached automatic-caption URL returns HTTP 429, refresh the video page with `yt-dlp` and request current `ko-orig,ko` JSON3 captions before falling back.
- If refreshed captions remain rate-limited but the video is already downloaded, local ASR is a valid review aid. Preserve the raw ASR output separately and label the model and fallback reason.
- Inspect timestamp units before promoting an ASR TSV into the canonical transcript path. Some Whisper TSVs use milliseconds while project ledgers use seconds. Compare the final timestamp with media duration, normalize units, then verify the first and last rows.
- Treat local ASR as timing/semantic support, not authoritative screen text; cross-check actual video/contact sheets and use only high-confidence timestamps in findings.

## Progress communication and completion language

- Treat `batch finished`, `artifact saved`, `QA passed`, and `entire channel project complete` as four different states. Never summarize a successful batch with an unqualified “완료” when the census or review queue remains open.
- Every progress reply should lead with one explicit state label: `전체 미완료`, `이번 배치 완료`, or `최종 완료`. Then report reconciled counts such as `reviewed/confirmed`, `opening terminal/scan target`, and whether ending scans or human OCR adjudication have begun.
- When the user asks “다 한 거지?”, answer the overall project state first, not the latest batch state. Name the remaining work quantitatively and avoid burying it after local successes.
- Keep stale task-list counts synchronized immediately after score/QA merges so preserved context cannot later overstate or understate progress.

## Resource-exhaustion recovery

- Repeated `Errno 24` across unrelated file writes, state-database writes, vision loads, and tool startup is a process-level resource signal, not evidence that each artifact or tool is broken.
- First stop fan-out and pause mechanical scan cron jobs. Confirm disk space separately, then inspect the supervising gateway process’s **numeric file descriptors** rather than counting every `lsof` row (memory mappings inflate raw row counts).
- If the gateway is near its process FD limit and no child jobs remain, persist ledgers first, then use the platform’s supported external restart path. From Telegram, the user can send `/restart`; an in-process `hermes gateway restart` is intentionally blocked because it would kill its own command.
- After restart, verify a new gateway PID, a sharply reduced numeric-FD count, preserved reports/ledgers, and a successful read-write/QA smoke test before resuming work.
- Resume expensive work at concurrency 1. Only increase concurrency after several successful artifacts and stable descriptor counts. Do not resume screen OCR and full-video vision review simultaneously on a low-FD host.
- A subagent summary is not proof of a saved review. Verify the exact path, size/hash, merge into the canonical score ledger, and rerun project-wide QA. If session storage failed before a report was written, re-review unless the live log contains actual textual findings—not merely image-load calls.

## Evaluation pipeline

- Separate discovery completion from evaluation completion.
- Maintain independent ledgers for confirmed credits, held candidates, inaccessible videos, downloads/packages, reviews, scores, and QA.
- Merge scores using the canonical credit inventory—not free-form wording in individual reports—to choose the material-only versus caption-and-material formula.
- Mechanical QA proves schema and arithmetic, not that a human/agent reviewed the complete video.
- Do not publish intermediate rankings as final. Save provisional aggregates with an explicit machine-readable state such as `PROVISIONAL_NOT_FINAL`.
- A final aggregation must hard-fail until a human-adjudicated final confirmed inventory exists and every confirmed video has a score plus deterministic QA PASS. Reconcile `confirmed = reviewed = scored = QA-pass` before rankings, yearly/credit-type averages, top/bottom cases, and hashes are generated.

## Completion reconciliation

Before final reporting, verify:

- population equation balances;
- every description-unconfirmed accessible video has opening and ending terminal states or an explicit hold;
- every OCR candidate has human adjudication;
- confirmed and held lists are disjoint;
- every confirmed accessible video has a full review, score, and QA PASS;
- inaccessible confirmed videos are reported without invented scores;
- hashes cover the frozen population, ledgers, scores, QA, and final report.
