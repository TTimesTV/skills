---
name: ttimes-pd-material-planning-evaluation
description: Use for full-video TTimes PD material evaluations.
license: MIT
metadata:
  hermes:
    tags:
    - ttimes
    - pd
    - evaluation
    - materials
    - evidence
    - video-review
    related_skills:
    - ttimes-screen-composition
    - ttimes-article-selection
  author: Hermes Agent
  version: 1.0.0
---

# TTimes PD Material-Planning Evaluation

## Purpose

Produce a formal, evidence-based evaluation of a credited TTimes PD’s **material planning** across an entire video. Separate editorial ownership from design implementation, apply the correct credit-dependent scoring formula, cite real timecoded observations, and save a verified Markdown review.

This is an evaluation workflow, not a screen-composition drafting workflow and not a fact-check of every source shown in the video.

## Trigger

Use when asked to:

- formally evaluate a PD’s `자료 기획` or `자료·강조자막` work;
- review a complete TTimes episode with a rubric and score;
- audit material choice, speech synchronization, or evidence/explanation function;
- produce a saved review under a project’s `reviews/` directory.

## Evaluation Boundary

Evaluate only work attributable to the named PD by explicit credit.

### Material-planning dimensions

1. **자료 선택** — whether a visual was needed, whether the right source/object was selected, and whether staying on the speaker was the better choice.
2. **발화 싱크** — whether the visual matches the spoken actor, object, action, claim, timing, and meaning.
3. **증거·설명 기능** — whether the visual functions appropriately as evidence, explanation, context, comparison, or atmosphere and improves understanding.

Exclude unless separately and explicitly credited:

- speaker reasoning, factual choices, delivery, or persuasiveness;
- typography, color, crop, motion, layout, readability, and other designer implementation;
- filming, lighting, sound, ordinary speech captions;
- title, thumbnail, views, or audience performance.

## Credit Gate and Score Formula

Identify the exact credit string and evidence grade before scoring.

### Shared-credit gate

When the canonical credit names two or more people for the same role (for example, `글·자료: A, B`), evaluate the episode only as a **joint planning output** unless separate authorship evidence exists.

- Quote the complete shared credit string and label the evidence grade.
- State explicitly that no screen object, segment, strength, weakness, or score is attributed to one credited person alone.
- Phrase finding advice as `공동 기획 개선점` (or an equivalent joint label), not as an individual PD correction.
- Do not infer labor division from visual style, topic, edit pattern, or the fact that the review project centers on one named PD.
- The score formula still follows the credited role: shared `글·자료` remains the material-only route.

### Material-only credit

Examples: `자료`, `자료 : 이름`, `글·자료`.

Do **not** infer that `글` means emphasis-caption authorship. Include the exact phrase:

```text
자료 전용 범위 확인
```

Mark both emphasis-caption dimensions:

```text
확인 불가·총점 제외
```

Score only the three material dimensions and renormalize the 65-point base to 100:

```text
(material_selection × 25 + speech_sync × 20 + evidence_explanation × 20) ÷ 65
```

### Caption-and-material credit

Examples: `자막, 자료`, or another explicit equivalent. Score all five rubric dimensions using the project’s official weights. Never apply this route merely because large on-screen copy is visible.

Round only the final total according to the project rubric. Use a calculation tool rather than mental arithmetic.

## Full-Episode Review Workflow

### Timeout and interrupted-review recovery

When a prior full-episode review timed out or was interrupted, recover completed work before repeating expensive inspection:

1. Read the prior append-only/live task log from start to end and inventory its successful outputs, generated montages, media probes, decode checks, transcript extracts, and unfinished tool calls.
2. Inspect the on-disk review package and audit-montage directory before generating replacements. Reuse valid chronological composites and create only missing sheet groups or decisive timestamp frames.
3. Distinguish a **loaded image** from a **completed visual finding**. A vision-tool log that only says the image was attached/loaded does not preserve the agent’s actual analysis; re-inspect that image unless a textual finding was recorded afterward.
4. Establish a coverage ledger (`regular sheets`, `scene sheets`, `CC`, `decisive ranges`) and resume from the first genuinely unverified item. Do not restart at 00:00 merely because the previous agent failed to write the report.
5. If image loading hits a file-descriptor/resource limit, stop parallel fan-out, wait briefly, and continue sequentially or in pairs with existing composites. The durable lesson is bounded batching, not that the vision tool is unavailable.
6. After recovery, run the same deterministic validator and full-decode/path/UTF-8 checks required for a fresh review. A recovered review has no reduced completion standard.

1. **Inspect the canonical inputs**
   - rubric;
   - video manifest and decode status;
   - exact credit string/evidence grade;
   - CC transcript;
   - regular-interval and scene-change contact sheets;
   - nearby completed reviews for house format only, not for copying judgments.

2. **Confirm media integrity**
   - duration, codecs, dimensions, hash, and full-decode status;
   - report these in the review.

3. **Read the entire CC in chronological order**
   - use it as timing and semantic support;
   - do not treat ASR spelling as authoritative for names or quoted screen text;
   - run a transcript-quality gate before using ASR semantically: check lexical diversity, repeated-token/phrase dominance, empty-segment rate, and whether timestamps span the runtime. Timestamp coverage alone does not prove semantic usability; a transcript may span the whole video while repeating one junk label in nearly every segment.
   - if ASR fails that gate, read it through only to document the failure and coverage; do **not** describe it as a usable semantic transcript. Derive findings and high-confidence timecodes from the original video, burned-in ordinary subtitles, and visible screen objects, and state this fallback explicitly in the review’s method and limitations.
   - if a non-empty `transcript.tsv` is misclassified as binary by a generic file reader, inspect its leading bytes and NUL count before choosing an encoding. A verified fallback is Python `Path(path).read_text(encoding="utf-8-sig")`, followed by normalization of both `\r` and `\n` line endings. Do not infer UTF-16 merely from the reader refusal: decoding UTF-8 bytes as UTF-16 can produce plausible-looking but unusable garbage.

4. **Inspect the entire video visually**
   - review all regular-interval contact sheets from start to end;
   - review all scene-transition sheets;
   - inspect decisive moments more closely when needed;
   - do not claim “full review” from a few sampled screenshots;
   - when the task explicitly requires **single sequential review / no parallel image calls**, make exactly one vision call per sheet, write a durable textual finding for that sheet, let the call return and release its image handle, and only then load the next sheet. Do not use parallel wrappers, pre-load the next image, or treat a successful image attachment as completed inspection;
   - when loading many contact sheets through vision tools without that stricter requirement, process them sequentially or in small batches rather than one large parallel fan-out; this keeps the review auditable and avoids exhausting local file descriptors. A transient load failure should be retried after narrowing the batch, not treated as evidence that the sheet was reviewed;
   - for long episodes with dozens of sheets, a verified efficiency pattern is to preserve each sheet’s width, normalize dimensions, and vertically concatenate **4–5 consecutive sheets** into numbered temporary composites (for example, `R_001–R_005`, then `R_006–R_010`). Inspect every composite in order, repeat separately for scene-transition sheets, and retain the manifest’s original sheet/frame counts in the review. Do not shrink sheets into an unreadable single mega-grid, skip originals that failed to load, or report the temporary composite count as the canonical sheet count.
   - create composites in an explicitly temporary subdirectory inside the review package. Delete that directory only after the saved review passes deterministic validation, so canonical packages do not retain unneeded derivative grids.

5. **Build a chronological material ledger**
   - divide the whole runtime into meaningful sections;
   - note visible objects, source type, concurrent speech, and function;
   - distinguish absent evidence from synchronization errors: a well-timed but weak source is not a sync failure;
   - separate **experience/appearance claims** from **causal/economic claims**: venue photos and social posts may explain layout, atmosphere, or visitor experience, but they do not establish why a business closed, whether renovation caused failure, or whether an investment was profitable;
   - when decisive claims are spread across long talking-head sections, derive a claim-driven timestamp list from the complete CC and extract a temporary one-shot montage from the original video. Use it to confirm exactly where evidence appears or remains absent, then remove the temporary montage after the review is verified.

6. **Select findings**
   - at least 3 strengths and 2 weaknesses;
   - each finding must include `타임코드 / 화면 객체 / 동시 발화 기능 / 판정 / PD 개선점`;
   - for shared-role credits, replace the last field with `공동 기획 개선점` and keep every judgment collective;
   - prefer findings that reveal repeatable planning behavior, not isolated decorative frames.

7. **Score conservatively**
   - calibrate scores against the complete episode, not only highlights;
   - explain each deduction using observed patterns;
   - keep material selection, synchronization, and evidence function analytically separate.

8. **Write the formal Markdown review**
   - scope and credit gate;
   - review method and media facts;
   - score table and exact formula;
   - chronological full-episode summary;
   - strengths and weaknesses with timecodes;
   - dimension-level rationale;
   - final judgment and prioritized improvements;
   - evidence limitations.

9. **Verify the artifact**
   - inspect the actual validator source **before drafting** and mirror its literal schema; do not rely only on a nearby review or prose checklist. A material-review validator may require `총점: N/100`, circled finding headings such as `### ①`, literal `**강점.**` / `**약점.**` markers, and exact bold field labels even when the review is otherwise semantically complete;
   - exact output path exists and decodes as UTF-8;
   - required credit/scope phrase appears;
   - include the literal boundary nouns `출연자` and `영상디자이너` when the project-wide validator checks those tokens; semantically equivalent prose such as `디자인 구현` may still fail deterministic QA;
   - use a standardized strength section heading containing `잘된 지점` or `잘한 지점`, not only `강점`, when the project-wide validator requires it; separately satisfy any per-finding strength/weakness markers required by the material-review validator;
   - verify the two excluded caption dimensions as distinct score-table rows (do not rely only on a raw phrase count, which can be inflated by prose repetition);
   - recompute the formula from the three component scores and confirm both the formula prose and the validator's exact displayed-total token;
   - full-review counts/duration are present;
   - minimum findings and all required finding fields are present;
   - record an artifact checksum when the surrounding project uses hashes for auditability;
   - if a generic reader or targeted patcher misclassifies a confirmed UTF-8 Markdown/CSV file as binary despite zero NUL bytes, do not infer corruption or another encoding. Use a deterministic UTF-8 Python read/replace/write or full-file writer, then rerun both validators and UTF-8 checks.

### Project-wide ledger validator integration

Some review projects validate only IDs already present in a score ledger such as `scores.csv`; saving a Markdown review alone can therefore yield a misleading project-wide PASS that never inspected the new episode.

1. Inspect the project validator before running it and identify its authoritative input ledger and required columns.
2. Check whether the reviewed ID already exists in that ledger. If absent, add exactly one row with the final component scores, excluded-caption sentinels, total, review path, verification state, and material-only scope. If present, replace/update it rather than appending a duplicate.
3. Preserve the ledger's existing encoding and CSV quoting. A UTF-8 BOM file may be misclassified as binary by a generic reader despite containing zero NUL bytes; use Python `csv` with `encoding='utf-8-sig'` instead of inferring UTF-16.
4. Run the project-wide validator only after the ledger row is present, then require both `failed: 0` and explicit inclusion of the new ID in its generated validation output.
5. Run the material-review validator separately as the per-file schema/formula gate. Neither validator substitutes for the other.
6. Hash the review and any modified ledger/validation artifact after all validators pass.

Use `scripts/validate_material_review.py` for deterministic UTF-8, scope, score-row, formula, finding-schema, and coverage-count checks. Resolve the validator path before running it: first check for a project-local `scripts/validate_material_review.py`; if it is absent, run the copy linked from this skill directory (use the absolute skill path returned by `skill_view`) rather than assuming the project contains the script. This fallback has been verified on a completed review and produced `"pass": true` with no failures.

The review path is a **positional first argument** (do not pass `--review`). Pass the exact CLI fields `--credit`, `--selection`, `--sync`, `--function-score`, and `--total`; when coverage facts are available, use `--duration-label` (the exact human-readable duration string present in the review), `--regular-frames`, `--scene-frames`, and `--sheets`. A verified invocation shape is:

```bash
python3 scripts/validate_material_review.py reviews/<id>.md \
  --credit '글·자료: 이름' \
  --selection 82 --sync 92 --function-score 80 --total 84 \
  --duration-label '30:07.929' \
  --regular-frames 603 --scene-frames 299 --sheets 31
```

Run the validator as a standalone command (or connect later checks with `&&`), never as the first command in a semicolon-separated shell chain: a later successful command can mask a validator failure with an overall zero exit code. Treat completion as valid only when the validator itself prints `"pass": true` and `"failures": []`.

See `references/formal-review-checklist.md` for the document skeleton and compact manual checklist.

## Channel-Wide Census Mode

When the task is to find and evaluate every credited episode in a channel, treat discovery as a separate audited pipeline before final ranking:

- freeze the exact channel population and exclusions;
- reconcile available metadata plus explicitly inaccessible videos to that population;
- search descriptions, then inspect opening and ending credits for description-unconfirmed videos;
- use OCR only to nominate frames for human adjudication;
- persist per-video checkpoints in small resumable batches rather than relying on one long process;
- keep confirmed, held, inaccessible, review, score, and QA ledgers separate;
- do not present intermediate counts or rankings as final.

The detailed state model, retry rules, leading-hyphen video-ID pitfall, script-only checkpoint scheduling pattern, caption-recovery provenance requirements, resource-exhaustion recovery, progress-language rules, provisional/final report gates, and final reconciliation checklist are in `references/channel-wide-credit-census.md`.

## Quality Rules

- **Source genealogy:** identify the original source and any translated/repackaged page separately where visible.
- **Current fact vs future scenario:** penalize visuals that make a conditional forecast look like established fact.
- **Legal/status claims need state labels:** when a case involves a request, proposal, debate, pending outcome, current law, or completed result, label that state explicitly. A headline phrased as `~할까`, `~되나`, or `~돌아가나` is not evidence that the outcome occurred. For inheritance, marriage, personhood, regulation, and liability claims, distinguish the nominal beneficiary/object from the actual legal mechanism (for example, direct inheritance vs trust/caretaker administration).
- **Article screenshot limits:** a related headline may provide context but does not automatically prove the broader spoken causal claim. Prefer a compact `date / actor / action / legal or factual result` card when several national or case examples are compared.
- **Spatial claims need maps:** migrations, borders, routes, territorial fragmentation, and supply paths generally require spatial explanation.
- **Comparisons need common denominators:** normalize year, population, product scope, visit type, price basis, or measurement conditions.
- **Company/product screens have a narrow evidentiary role:** first-party app screens can explain workflow, interface states, and the benefit a user sees, but they do not independently prove market size, market share, adoption, clinical effectiveness, or competitive superiority. For company performance claims, require a consistent data card with source, as-of date, denominator, metric definition, and like-for-like competitor values; label company-provided figures explicitly.
- **AI prompting demos are executions, not general proof:** a same-session sequence of prompt → response → revised prompt is strong material for reproducibility, workflow, and speech synchronization, but one successful generation does not establish that a prompting method generally improves accuracy or eliminates hallucinations. For comparative claims, look for a fixed model/version, execution date, identical task, repeated trials, evaluation criterion, and baseline-vs-treatment results. For claims attributed to “research,” prefer a compact card naming the paper/authors/year, tested models or dataset, effect size, and limitations; distinguish `reduced` from `eliminated`.
- **Complex AI services need output genealogy plus a flow overview:** when a segment moves from source content through crawling/input, classification or function calls, generation, human review, and publication, inspect whether the episode shows both (a) the real input/output artifacts and (b) an overview such as `source → ingestion → model/function → safety/review → output`. Code and interface screens are useful node-level evidence but rarely explain the whole service alone. Score a missing overview under selection/explanation while preserving a high sync score when the code shown still matches the spoken object.
- **Platform operations need actor-and-flow diagrams:** when speech describes several parties, APIs, records, payments, prescriptions, logistics, or a before/after business-model change, long talking-head coverage is usually insufficient. Prefer an `actor → data/object → actor` flow, a current-vs-target network/map, or a payer/value/fee comparison. Evaluate missing structure under selection and explanation, not automatically under synchronization.
- **Strong-risk claims need stronger evidence:** nuclear control, war casualties, demographic collapse, regulation, and state fragmentation should use quantitative data or primary/authoritative reports where possible.
- **No designer leakage:** do not deduct for font size, animation, crop, color, or mobile readability in a PD material-planning score.

## Common Pitfalls

1. Treating `글·자료` as proof of emphasis-caption ownership.
2. Scoring visible emphasis copy despite absent caption credit.
3. Reviewing only highlight frames while claiming full-episode coverage.
4. Conflating missing material with bad synchronization.
5. Treating atmosphere footage, logos, or article headlines as full proof of a claim.
6. Fact-checking the speaker instead of evaluating how the PD selected and synchronized materials.
7. Omitting the exact 65-point renormalization formula.
8. Writing generic improvement advice without naming a specific replacement object, comparison, map, table, or authoritative source type.
9. Saving a polished review without mechanically verifying required phrases, score consistency, and finding counts.

## Completion Standard

The task is complete only when the full episode has been reviewed, the formula has been calculated, the Markdown artifact has been written, and deterministic checks confirm its scope language, score, findings, and path.
