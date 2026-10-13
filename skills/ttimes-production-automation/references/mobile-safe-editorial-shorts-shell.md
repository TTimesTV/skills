# Mobile-safe editorial Shorts shell

Use when the user approves a portrait screenshot or mood reference and wants a branded 9:16 wrapper around an already edited 16:9 highlight. This is a **design-implementation variant** of deterministic derivative rendering, not evidence that highlight selection itself is automated.

## Composition pattern

```text
mobile-safe top hook
→ full-width 16:9 highlight
→ branded lower panel with official logo
```

A reliable 1080×1920 starting geometry is:

- reserve roughly `y<140` for app chrome; place essential top copy below it
- keep the central 16:9 highlight near the middle (`1080×608` when full width)
- assume the right-side reaction rail may cover approximately `x>900` through the middle/lower screen
- keep persistent logo/essential brand copy centered and above roughly `y=1700`; bottom metadata/navigation may obscure the rest

These are review heuristics, not universal YouTube constants. Generate a review-only safe-guide image when the platform UI or client version matters; never burn the guides into the deliverable.

## Reference-image interpretation

Separate actual template design from player chrome. Play, volume, CC, cast, progress, and menu icons visible in a screenshot are app/player UI and must not be recreated.

Extract the reference's class-level grammar rather than tracing every decoration:

- background material: paper, newspaper, collage, grain, grid, or flat brand field
- title hierarchy: kicker, main hook, speaker/episode label
- center transition: clean edge, border, torn paper, tape, or mask
- lower brand lockup: official logo, channel name, slogan, CTA
- alignment and safe margins

When a user prefers the screenshot's *feel*, preserve its hierarchy and material language while applying TTimes brand assets. Do not force the earlier reference Short's shell after the user has chosen a new direction.

## Hook writing

The upper panel must work as the thumbnail-like promise throughout playback.

1. Start from the source title and the actual selected speech.
2. Put the concrete object in a small kicker when useful.
3. Use a short question or reversal as the large hook.
4. Avoid strengthening a claim merely for visual impact.

Session calibration:

```text
kicker: 중국 AI ‘키미 K3’
main: 미중 AI 수준차,
      정말 사라졌나?
speaker: 강정수 박사
```

This was supported by the source title. A stronger line such as `키미가 격차를 끝냈다` would overstate the evidence.

## Official logo acquisition

Prefer delivered brand assets. If a cloud logo path is a File Provider placeholder, verify byte readability/allocated blocks before using it. Do not fabricate a wordmark from memory.

For a YouTube-owned brand surface, an official channel avatar is a defensible fallback:

```bash
python3 -m yt_dlp --playlist-end 1 --flat-playlist --dump-single-json \
  'https://www.youtube.com/@TTimesTV' > channel.json
```

Inspect `thumbnails` and download the highest-resolution channel avatar. Record that it came from the official channel. Preserve its proportions and colors; a rounded-corner square is acceptable only as a layout treatment around the intact avatar.

## Deterministic implementation

For exact Korean copy, logo fidelity, and repeatable geometry, use a transparent Pillow overlay rather than relying on generated text inside an image model.

Recommended layer order:

```text
textured 1080×1920 brand background
+ transparent 16:9 viewport
+ optional torn-paper masks overlapping the viewport edges
+ exact source-grounded top copy
+ official logo in lower safe zone
+ original highlight audio
```

Use a fixed random seed for procedural grain/tear edges so rerenders are reproducible. Keep torn edges shallow enough that they do not cover burned-in captions. Preserve the landscape highlight's aspect ratio; no face-tracking crop unless explicitly requested.

## Lower-panel discipline

- The logo is the primary persistent element.
- Keep the area around it quiet enough for recognition.
- Do not add huge decorative words behind or below the logo merely to fill space; Shorts metadata already creates visual density at the bottom.
- A slogan may sit below the logo if it remains above the bottom UI zone.
- Prefer a CTA only in the last 2–3 seconds rather than a large persistent subscribe button, unless the reference explicitly requires a permanent CTA.

## QA

Run the standard codec/hash/decode gates, then inspect a contact sheet and start/middle/end frames for:

- top hook legibility at phone size
- title inside the safe horizontal region
- right-rail collision with important central details
- bottom metadata collision with the logo/slogan
- torn edge covering subtitles or faces
- logo proportion/color fidelity
- decorative texture competing with the headline
- unintended player UI copied from the screenshot

A valid iteration sequence is: render overlay → inspect natively → fix contrast/quiet-zone issues → render MP4 → contact-sheet QA → decode/hash → deliver. In one calibration, a low-opacity white speaker pill made white text nearly disappear, and oversized decorative lower text competed with the logo; the durable fix was dark text on an opaque light pill and a quiet lower margin.
