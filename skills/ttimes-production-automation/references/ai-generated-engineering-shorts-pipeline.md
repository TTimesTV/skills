# Physics-first AI engineering Shorts pipeline

## Use case

Use this workflow for short vertical explainers in which a limited number of generated clips must visualize an industrial or engineering mechanism. It is not the same class as wrapping an approved 16:9 highlight in a vertical shell.

The stable product shape is:

```text
physical paradox hook
→ one causal mechanism
→ generated motion footage
→ source-faithful narration and burned speech captions
→ restrained BGM
→ industrial meaning
```

Generated footage carries motion and atmosphere. Exact labels, arrows, numbers, units, and variant distinctions belong to post-production.

## Parameterized brief

Freeze these fields before scripting. Do not hard-code one pilot's values as universal defaults.

```yaml
topic:
target_duration:
generation_budget:
raw_clip_duration:
output_canvas: [1080, 1920]
frame_rate: 30
speed_candidates:
caption_character_limit:
caption_line_limit:
caption_min_duration:
optional_bgm_duration:
```

Manual Gemini generation is a valid human handoff when generation quota or API access is constrained. The skill prepares prompts and ingests returned clips; it must not describe unavailable API automation as implemented.

## Topic gate

Prefer topics that satisfy all four conditions:

1. **Paradox hook:** one sentence that sounds surprising but remains literally defensible.
2. **Visible physics:** fluid, heat, pressure, load, signal, rotation, or phase change can be shown as motion.
3. **Finite causal chain:** the mechanism fits the generation budget without collapsing several variants into one process.
4. **Industrial consequence:** the closing point explains why the mechanism matters to cost, reliability, capacity, maintenance, or infrastructure.

Reject or redesign topics that require dense logos, exact UI, extensive text, or invisible strategy diagrams to be intelligible.

## End-to-end gates

### 1. Fact and mechanism lock

- Verify the mechanism from primary or authoritative technical sources.
- Separate variants before writing; never merge distinct systems into one visual sequence.
- Freeze the exact claim strength, caveats, numbers, and screen-only notation.

Completion: one causal chain and its variant boundaries are explicit enough that every scene has one physical job.

### 2. Narration and shot manifest

Build narration and scenes together, but do not force one narration block to equal one generated clip. Record for each shot:

```text
story function | physical action | start state | end state | forbidden ambiguity | narration span
```

Prompts should specify motion, camera distance, material behavior, and continuity. Do not ask the generator to render authoritative Korean labels, precise numerical overlays, or stable component annotations.

Completion: the full causal chain fits the clip budget and the first seconds contain the hook rather than branding.

### 3. Asset ingest and causal reorder

Probe every returned clip and inspect beginning, middle, and end frames. Classify each clip by what is actually visible rather than its prompt or generation order. Reorder by physical causality. Trim misleading tails, such as vapor that reads as fire smoke, even when the prompt intended a correct phenomenon.

Completion: every used interval has a declared physical role and no clip is included merely because generation was expensive.

### 4. TTS completeness and rough cut

- Probe the real TTS duration.
- Inspect the ending for truncation before editing.
- Detect actual speech pauses; cut picture at acoustic and causal beats, not script-block boundaries.
- Label a source-truncated narration as incomplete and never invent the missing sentence.

Completion: the rough cut covers only audio that truly exists, and source incompleteness is explicit.

### 5. Speed lock before final captions

Create speed comparison previews if useful, but designate them as previews. Choose and freeze the final narration/picture speed before final SRT generation and burn-in.

A speed change from `a` to `b` transforms the whole synchronized timeline by `a/b`. It also shortens every caption exposure. Therefore a caption candidate validated at one speed is not automatically valid at another.

After any final-speed change:

1. transform or regenerate cue timing;
2. rerun minimum duration, character, line, overlap, silence-gap, and end-clamp checks;
3. re-render captions from the caption-free master;
4. inspect rendered frames again.

Completion: the delivery master, SRT, and caption QA all name the same final speed.

### 6. Source-faithful speech captions

Delegate lexical fidelity and timing to `spoken-caption-source-fidelity` and the short sped-TTS reference there. Preserve every spoken token in order; correct only approved recognition or orthographic errors. Prefer Korean grammatical cohesion over visual character balancing.

Completion: source→cue lexical equality, valid timings, project line limits, continuous-speech seams, and rendered safe-area checks all pass.

### 7. BGM only after picture and speed lock

Generate or acquire BGM after the approved duration is known. Do not select narration speed merely to match a music file.

Duration fit rule:

```text
absolute mismatch <= 5%  → subtle atempo adjustment
mismatch > 5%            → musical crossfade extension, loop, or regenerate to target duration
large structural mismatch → regenerate; do not distort narration to rescue the track
```

Use narration-first ducking and frame-preservation QA from `references/narration-first-shorts-bgm-mixing.md`.

Completion: the BGM has no abrupt boundary, speech remains dominant, and audio padding does not remove the final video frame.

### 8. Master QA and delivery

Require:

- expected canvas, frame rate, codecs, audio layout, and duration;
- full decode with zero errors;
- caption structure, source fidelity, first/last cue, and minimum exposure checks;
- representative contact sheet and disputed-frame inspection;
- narration-only, BGM-only, and final loudness/true-peak measurements;
- frame-count equality or decoded raw-frame hash equality when picture should be preserved;
- canonical filename and positive delivery receipt.

A compressed transport copy is distinct from the high-quality master. If upload times out, preserve the master and create a verified delivery encode rather than repeatedly resending the same oversized file.

## Editorial authority

```text
PD owns: topic, hook, claim strength, shot meaning, speed choice, BGM taste, publication approval
automation owns: probing, timing transforms, candidate assembly, caption alignment, rendering, deterministic QA
```

Automation may recommend an order from visible evidence but must not portray generated scenes as real corporate or facility footage.

## Common pitfalls

1. **One-clip/one-paragraph binding:** produces forced cuts and needless speed changes. Cut on real pauses and physical beats.
2. **Speed after captions:** silently invalidates minimum exposure and sync QA. Re-caption after final speed lock.
3. **BGM drives narration:** makes speech unnaturally fast. Fit or regenerate music instead.
4. **Prompt authority:** assuming a generated clip depicts what the prompt requested. Judge pixels, not intent.
5. **Text inside generation:** trusting generated labels, numbers, or arrows. Add them deterministically in post.
6. **Expensive-asset bias:** keeping a misleading clip because quota was consumed. Physical clarity outranks sunk cost.
7. **Incomplete source called final:** truncated TTS or missing clips must remain explicitly partial.
8. **Pilot constants become doctrine:** generation count, clip length, speed, caption limits, and mix values remain project parameters until reproduced across another topic.

## Reproducibility note

A single successful pilot validates the mechanical pipeline but not every editorial default. Run at least one second topic with a different physical chain before promoting pilot-specific constants to house-wide defaults. Preserve the first pilot as evidence, not as the universal template.
