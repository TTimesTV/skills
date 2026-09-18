# Numbered asset intent audit

Use when the user asks to reverse-engineer why an existing `01`, `02`, … material and nearby caption were chosen.

## 1. Establish the actual package topology

Do not assume every file named `(자료) ...docx` is already an inline `자료-완료` document. Classify the package first:

1. **Inline-complete:** DOCX contains `//NN`, `//자막`, colors/highlights, source notes, and placement instructions.
2. **Split working package:** DOCX is a clean cut transcript while numbered media files, 말자막 TXT/SRT, cut audio, and article/graphic files live beside it.
3. **Reference corpus:** only extracted observations or a prior completed example remain.

Inspect the DOCX OOXML, not only plain-text extraction, before declaring callouts absent. Check body, text boxes, comments, tracked revisions, headers/footers, and related XML parts.

Completion criterion: state which topology is present and which artifact carries placement/caption authority.

## 2. Freeze an evidence bundle per asset ID

For each requested ID collect:

- exact asset filename, source label, size, and media type
- actual playable media frames or still pixels when available
- duration and relevant source time range
- nearest transcript and spoken-caption anchors
- previous and next numbered assets
- inline `//자막`, if actually present
- source, fact, and rights status

A filename such as `(태양광 전지)_Tesla.mp4` establishes the labeled subject and source family, not the exact shot content. Do not describe unseen footage as fact.

For cloud-hosted material, verify byte readability before media analysis. Work from a local immutable copy and record its hash. If only metadata are available, keep pixel-dependent findings unresolved rather than upgrading them from the filename.

## 3. Analyze intent on four levels

### Placement

Which exact speech beat is the best match? Compare candidate anchors instead of choosing the first matching noun.

### Story function

Classify the material's primary role:

- illustrate
- prove
- identify
- explain
- compare
- quantify
- process
- establish place/person/time
- cover an edit
- reset rhythm
- create mood or brand recognition

Do not call official or branded footage `PROVE` unless its actual pixels and context support the claim.

### Caption relationship

Check three distinct possibilities:

1. an explicit editorial caption exists
2. only spoken captions coexist with the material
3. no text is intended because the material or speaker face carries the beat

The absence of `//자막` may be an intentional `material + spoken caption` composition. Never invent an editorial caption and report it as the PD's original choice. A hypothetical alternative must be labeled as a proposal.

### Selection motive

Separate why this specific source may have been chosen from what the footage literally shows. Possible motives include visual quality, modernity, recognizability, product concreteness, sequence continuity, source reliability, rights availability, or contrast with neighboring assets. Keep motives as inference until the PD confirms them.

## 4. Evidence labels

Every finding must use one of:

- **Confirmed:** directly visible in the source package or media
- **Strong inference:** supported by ordering, transcript anchor, filename/source, and neighboring assets
- **Weak inference:** plausible but not uniquely supported
- **Unresolved:** requires actual media, missing callout, or PD confirmation

This protects the learning process: a user correction can promote or reject an inference without contaminating confirmed facts.

## 5. Three-review meeting

Use three independent lenses for important calibration:

1. **Story/placement:** why this beat needed a visual and where it belongs
2. **Footage/source:** what the actual scene contributes and why this source was selected
3. **Caption/adversarial:** whether editorial text exists, whether no caption is intentional, and what misleading interpretation the combination could create

Main integrates by evidence quality, not majority vote.

## 6. User-review output

For each asset ID return:

```text
Asset ID and filename
Confirmed placement candidates
Actual material description
Primary/secondary function
Caption relationship
Why the PD likely chose it
Why this source rather than a generic alternative
Simultaneous screen composition
Risks and alternative interpretations
Evidence confidence by claim
Questions for PD correction
```

Analyze one asset or a small coherent sequence first when calibrating a new standard. Apply the user's correction to the whole error class before moving to the next batch.

## Pitfalls

- treating a clean `(자료)` DOCX as a completed inline plan
- inferring exact video content from filename alone
- ignoring numbered files stored beside the transcript
- searching the transcript for `//01` and concluding the asset has no role
- inventing a missing editorial caption
- calling branded B-roll factual evidence
- analyzing an asset without its neighboring IDs
- presenting the agent's suggested caption as the user's original caption
