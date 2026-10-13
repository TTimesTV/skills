# Long-form → Shorts reverse engineering

Use when the user supplies both a full YouTube video and a derivative Short and asks how it was made or whether the process can be automated.

## Evidence-first workflow

1. **Download both actual YouTube files.** Do not infer production structure from thumbnails, screenshots, or transcripts alone when the URLs are available.
2. Record duration, resolution, FPS, upload order, hashes, and caption availability.
3. Fetch timed transcripts for both and locate repeated phrases in the full video's body.
4. Inspect the full video's opening separately. A Short may reuse a pre-edited cold open rather than being cut directly from the body.
5. Compare audio:
   - resample both to mono PCM;
   - cross-correlate the Short against the first 1–2 minutes of the full master;
   - report the best offset and normalized correlation;
   - treat a very high match as evidence of derivative reuse, not merely similar speech.
6. Build 1-second contact sheets and scene-change frames for the Short. Separate:
   - true source/shot cuts;
   - graphic-state changes;
   - caption animation;
   - motion inside one shot.
7. Map body speech to Short time using exact phrase matches and adjacent context. Record reordered segments explicitly and label transcript-derived boundaries as approximate unless verified against audio/EDL.
8. Decompose the vertical output into persistent template layers: eyebrow, headline, central landscape viewport, bottom hook, CTA/source, labels, and any new captions.

## Core classification

Always distinguish two materially different automation problems:

### A. Derivative wrapper automation

```text
approved/pre-edited landscape highlight
→ extract
→ place inside 9:16 template
→ insert approved top/bottom copy
→ render and QA
```

If the Short simply nests an existing 16:9 cold open with burned-in B-roll, graphics, and captions, this path is deterministic and should be the first MVP. Face tracking, autonomous B-roll selection, and new caption timing may be unnecessary.

### B. Editorial highlight generation

```text
full body
→ select claims
→ reorder/compress
→ add evidence/B-roll/graphics/captions
→ approve
→ vertical derivative
```

AI may draft candidates, but the PD must approve the story axis, context-preserving reorder, claim strength, materials, and final copy. Do not describe A's high automation rate as proof that B can run unattended.

## Recommended story-function map

Map selected speech by function rather than transcript order alone:

```text
specific proof or vivid case
→ reversal/tension
→ provocative question
→ mechanism/evidence
→ strategic conclusion
```

A reorder can strengthen retention while still creating context risk. Preserve source genealogy for every segment.

## Minimum persistent manifest

```text
source path/URL/hash/duration/resolution
short path/URL/hash/duration/resolution
verified cold-open offset and correlation method
source body ranges → short ranges
story function per range
reorder flag
vertical template fields
fact-risk state
PD approval state
render/QA state
```

## Build order

1. Fixed-template wrapper from an approved cold open.
2. Candidate extraction and PD selection from full transcripts.
3. Approved rough-cut assembly with genealogy.
4. Caption/material drafts and fact-risk gates.
5. Optional NLE adapter after the actual platform and project template are known.
6. Upload and live-player QA.

For a flattened output MVP, FFmpeg plus a pre-approved static/animated template is usually simpler and more reliable than starting with autonomous NLE control. Use an NLE bridge only when editable timelines are required.

## Publication-risk gate

Block automatic finalization for claims containing percentages, universals, causal conclusions, sanctions/effectiveness judgments, market share, performance superiority, or similarly strong assertions. Preserve the exact source range, evidence basis, qualifier, and PD approval.

## Pitfalls

- Assuming the Short was cut directly from the body when it actually reused the full video's opening highlight.
- Treating every scene-detector hit as an editorial cut; graphic highlights and caption entrances also trigger differences.
- Calling a body mapping exact when it was derived only from auto-captions.
- Rebuilding B-roll/captions that are already burned into the approved landscape highlight.
- Promising editable Premiere/Resolve/FCP automation before the NLE and template are identified.
- Using YouTube's delivery encode as the production master. YouTube downloads are valid for forensic analysis; internal high-resolution masters are preferable for final production.

## Verification

- Both actual videos were downloaded and hashed.
- Short/full relationship was tested with audio or frame evidence, not assumed.
- Cold-open reuse and body-source genealogy were analyzed separately.
- Reordered body segments are visible in the map.
- Template-only work and editorial work have separate automation claims.
- Risky headline claims remain blocked until fact and PD approval.
