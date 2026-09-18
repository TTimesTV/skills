# Nissan Ao-Solar Extender scene and search analysis

## Why this reference exists

Use this as a calibrated example when a PD asks why a specific company video was chosen, what exact scene best matches an abstract energy claim, and how to distinguish practical footage sourcing from strategic brand meaning.

## Source inspected

- Working asset: `09. (차 위에 태양광)_Nissan.mp4`
- Duration: about 5:28
- Frame size: 1920×1080
- Local review copy SHA-256: `0bd4e42bdeddac0df7d0c915f8f3e8276dd4d89139790e0ac8ecc90cecbc86b3`
- The video identifies the concept as Nissan `Ao-Solar Extender`.

Do not treat the filename or company name as proof of exact frame content. The conclusions below came from direct frame inspection.

## Scene map

| Source time | Observed content | Best editorial use |
|---|---|---|
| 2:24–2:28 | Interview plus `Car Umbrella` concept diagram | Explain the inspiration/concept; not the actual deployment shot |
| 2:42–2:50 | Overhead view of a parked EV; roof-mounted solar surface extends/slides longitudinally | Best mechanism shot for vehicle-integrated solar and point-of-demand generation |
| 3:19–3:23 | Close-up of solar-cell/panel surfaces | Texture/technology detail; weak vehicle context |
| 3:24–3:27 | Interview wide shot with the physical vehicle and extended roof structure visible behind speakers | Establish real prototype and vehicle integration |
| 3:44–3:50 | Side profile of the parked vehicle with extended roof panel | Clear supplementary view of body-to-panel integration |
| 4:21–4:26 | Design sketches of vehicle and roof mechanism | Design-process or concept-development explanation |

Important correction pattern: a user or filename may say `2:24부터 슬라이딩 장면`. Inspect the actual sequence before repeating that timing. In this case 2:24 is the concept diagram; the observed physical deployment begins around 2:42.

## Recommended composition for an abstract EV-electricity-demand line

Example speech anchor:

```text
앞으로 전기자동차에 대한 전기 수요
```

Recommended visual:

```text
2:42–2:50 overhead deployment shot
+ spoken captions
+ short object label with arrow
```

Why it works:

- A generic EV insert shows only the electricity-consuming object.
- This shot shows the EV and an onboard generation mechanism in one frame.
- The expanding surface gives an observable action that suggests adding generation area at the point of demand.
- It visualizes `new load + one possible local supply response`; it does not prove demand magnitude or sufficiency.

Story function:

```text
ILLUSTRATE_MECHANISM
```

not:

```text
PROVE_DEMAND_SCALE
PROVE_SOLAR_CAN_FULLY_SUPPLY_EV_LOAD
```

## Arrow-label placement

In the 2:42–2:50 overhead shot, the car sits near the center/left while comparatively open lawn remains on the right.

Preferred treatment:

- Put the label in the right-side negative space.
- Point a leftward arrow to the roof panel.
- Keep the arrow tip on the extending solar surface, not the windshield or generic roof edge.
- Enter after the vehicle/panel geometry is readable; hold through the visible extension; remove before the next composition.
- Prefer a concise object label such as `차 지붕 위 태양광` over a long explanatory sentence when spoken captions are also present.

This is a `C7 object label` supporting a material insert, not a standalone thesis caption.

## Why the Nissan source may have been chosen

The strongest default interpretation is practical sourcing convenience:

- The official/company-style video contains an explicit vehicle-integrated solar concept.
- It offers multiple clean, broadcast-friendly angles: overhead deployment, panel close-up, prototype wide shot, and side profile.
- The sliding motion is more legible than a static solar-roof still.
- Search and rejection criteria are straightforward.

Useful search terms:

```text
Nissan Ao-Solar Extender
Nissan sliding solar panel EV
Nissan solar roof extender
日産 Ao-Solar Extender
car roof sliding solar panel Nissan
```

Do not infer without additional evidence that Nissan was selected because it represents the solar industry, endorses a broader claim, or carries strategic brand symbolism. Company choice can be a production-quality and asset-discovery shortcut.

## Search-practice workflow

1. Translate the speech beat into an observable object/action (`EV load` → `electric car`; `local generation` → `roof solar surface extending`).
2. Search for a mechanism, not just a noun (`sliding solar roof EV`, not only `electric car`).
3. Inspect the full candidate sequence and create a coarse contact sheet.
4. Refine promising intervals at 0.5–1.0 second spacing.
5. Record exact observed in/out points and separate concept diagrams from physical demonstrations.
6. Choose frames with negative space appropriate for labels and spoken-caption safe areas.
7. State the visual's claim boundary: illustrative mechanism, not statistical evidence.
8. Explain company selection first as a sourcing/production decision unless placement or user confirmation supports deeper meaning.

## Cloud-file practical note

On macOS File Provider volumes, a nonzero logical file size with zero allocated blocks indicates an unhydrated placeholder. Materialize the file before hashing, probing, or frame extraction. Opening the source through the owning application/Finder can trigger hydration; then re-check allocated blocks and work from a hashed local copy. Treat read errors before hydration as a state to resolve, not evidence that the media is corrupt.
