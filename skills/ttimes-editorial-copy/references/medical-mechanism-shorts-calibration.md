# Medical-mechanism Shorts calibration

Use for cancer immunotherapy, vaccines, cell therapy, and other biomedical Shorts where the viewer must understand who recognizes what, who acts, and why the prior treatment fails.

## Script spine

```text
fresh event or contradiction
→ first-generation direct cell damage
→ molecular-target blockade
→ immune-checkpoint release
→ recognition failure
→ personalized target teaching
→ clinical proof level
→ remaining production/survival caveat
→ opening thesis return
```

Generation labels are explanatory shorthand, not a universal official taxonomy. State that once if the format allows; do not let the caveat derail the opening.

## Explain by actor, signal, action, failure

For each treatment answer:

```text
actor: who actually kills or blocks?
target/signal: what does it detect or bind?
action: what physically changes?
failure: why can it still fail?
```

Cancer-immunotherapy calibration:

- Cytotoxic chemotherapy: drug damages DNA replication or division machinery; fast-dividing normal tissue is collateral.
- Targeted therapy: drug blocks a cancer-driving mutant protein or pathway; requires the target and can face resistance.
- Checkpoint inhibitor: T cell is the killer; tumor PD-L1 engages T-cell PD-1 to suppress attack; pembrolizumab blocks PD-1. This releases an existing response but does not teach a new tumor target.
- Personalized neoantigen vaccine: tumor and normal sequences are compared; candidate mutation-derived peptides are ranked; mRNA encodes selected targets; antigen-presenting cells display the peptides and expand tumor-specific T-cell responses.

## Definitions at the causal beat

Do not front-load a glossary. Define the noun exactly when it becomes necessary:

```text
T cell: an immune cell that inspects displayed peptide fragments and can kill abnormal cells.
Antigen, in this T-cell context: a protein-derived peptide fragment the immune system can recognize.
MHC: the cell-surface display platform carrying peptide fragments.
Neoantigen: a mutation-derived peptide absent from normal cells and newly present in the tumor.
```

Compact viewer-facing sequence:

```text
cell cuts internal proteins
→ displays peptide fragments on MHC
→ T-cell receptor inspects the peptide–MHC display
→ abnormal target can trigger killing
```

## Essential checkpoint-inhibitor limit

`브레이크를 푼다` alone is too abstract. Preserve both prerequisites:

1. a T-cell population must already recognize a tumor antigen;
2. those T cells must reach or engage the tumor.

If recognition is absent, checkpoint blockade cannot create it from nothing. Releasing immune brakes can also cause immune attack on normal organs.

Useful analogy, used only after the mechanism is stated:

```text
T cell = police
antigen = suspect identity
PD-1 = stop-order receiver
checkpoint inhibitor = blocks the false stop order
personalized vaccine = distributes the suspect profile
```

Do not let the analogy replace PD-1/PD-L1 or antigen recognition.

## Length and narration authority

- The user may allow any Short under three minutes and control speed in edit. Do not force a 60- or 75-second target from rough character counts.
- Preserve the definitions required for comprehension, then synthesize the approved voice/tempo and measure the real audio.
- For Typecast 필재 `1.1배`, use the established 필재 voice with `normal`, consistent seed/pitch/intensity, and `audio_tempo: 1.1` unless post-render speed is explicitly requested.
- Generate in 4–6 semantic sections, add short natural pauses, normalize, and verify measured duration, peak, loudness, codec, and abnormal silence.

## Current-result wording

For an interim/topline Phase 3 announcement, distinguish:

```text
endpoints met
≠ detailed hazard ratio disclosed
≠ overall-survival benefit proven
≠ approval completed
```

Never import Phase 2 risk-reduction percentages into Phase 3 wording unless the company separately reports them.

## User-correction pitfalls

- Do not alternate between a tiny 60-second stub and an unbounded lecture. Keep one coherent script within the user-named ceiling.
- After a partial correction, return the full integrated script when the PD says `전체원고`.
- Do not estimate a precise duration before TTS and then defend it. Generate the audio and report the measured duration.
