# TTimes Korean→English Dubbing: English Thumbnail Workflow

This reference is part of the dubbing deliverable. Use it after the final English dub and English SRT are frozen when the user requests an English YouTube package.

## Definition of done

The English package is not complete until all requested assets exist and are verified:

1. final English voice master;
2. final English voice + preserved background/SFX mix;
3. forced-aligned US English SRT based on the final clean voice;
4. 1280×720 English thumbnail;
5. manifests, QA, duration/loudness checks, and hashes as applicable.

Do not stop at the MP3 or SRT if an English thumbnail is part of the request.

## Production model: generate the visual, typeset deterministically

Use two layers:

```text
image generation → text-free core visual
Pillow/Figma-equivalent composition → exact headline, comparison line, and official logos
```

Do not ask image generation to render final technical terms, capitalization, or logos. It commonly corrupts `zHBM`, `HBF`, `tHBM`, company names, and TTimes branding.

When the user explicitly requests image generation, a manual inpainting-only result does not satisfy the request. The core technical visual must be newly generated; deterministic composition is only for exact typography and real brand assets.

## Default canvas and hierarchy

- 1280×720, 16:9, sRGB JPEG at high quality.
- Matte black or near-black background.
- Large high-contrast headline in the lower third.
- One smaller comparison line below it.
- TTimes logo at the same size and coordinates as the supplied/original TTimes reference thumbnail when one exists.
- Company/institution logos near the relevant structures, with enough black negative space for legibility.
- Mobile thumbnail readability takes priority over fine technical decoration.

## TTimes + Figma visual language

The result should look like a modern editorial vector graphic built in Figma, not generic AI semiconductor art.

Required tendencies:

- fixed three-quarter camera across related technical objects;
- clean geometric forms and precise spacing;
- restrained semi-transparent technical cutaways;
- crisp vector-like outlines;
- limited palette and controlled glow;
- black background and strong white typography;
- copper/salmon regular grids for DRAM/HBM;
- cold cyan/blue translucent logic with irregular internal wiring;
- blue cooling effects without invented hoses, tubes, or fans unless the source requires them.

Avoid:

- photoreal CGI chips;
- glossy metal and cinematic reflections;
- cyberpunk neon overload;
- busy circuit-board wallpaper;
- clip art, cards, borders, and PowerPoint styling;
- humans, faces, hands, or silhouettes unless explicitly requested;
- generated words, letters, numbers, logos, or watermarks in the core visual.

## Architecture-comparison thumbnails

When several technologies are compared:

- show each architecture as a distinct object, not three color-swapped copies;
- preserve one coherent camera and substrate baseline;
- make structural differences legible before color differences;
- use a secondary color distinction when two stacks otherwise look too similar;
- do not give HBM and HBF identical warm colors when that obscures the comparison.

Practical palette example:

- HBM/DRAM stack: copper or salmon;
- HBF/flash stack: related but distinct gold or amber;
- GPU/logic: cold cyan or cobalt;
- cooling: restrained blue;
- headline emphasis: teal, yellow, or orange selected to match the visual.

## Typography contract

- Preserve user-approved wording and capitalization exactly.
- Typeset headline and comparison text after image generation.
- Use bold condensed or heavy sans-serif typography suitable for mobile.
- Do not silently rewrite a phrase because another version sounds more marketable.
- Run an exact string comparison against the approved copy before delivery.
- Do not duplicate `zHBM`, `HBF`, or `tHBM` beneath company logos when the comparison line already contains them unless the user explicitly requests per-object labels.

## Logo contract

- Use official transparent PNG/SVG assets whenever possible.
- Do not reconstruct logos with image generation.
- Do not crop a logo from a compressed JPEG and threshold it unless no clean asset exists; JPEG noise creates dirty halos and blocks.
- If a reference TTimes thumbnail exists, measure and match the TTimes logo's visual bounding box and coordinates. Use a clean transparent master at that measured size/position.
- Preserve brand colors where useful; white wordmarks may be used on black if that matches the reference treatment.
- Company logos must not overlap dense chip linework. Move the logo or lower the architecture rather than accepting low contrast.
- Align each company logo to the visual center of its corresponding architecture unless the user specifies another relationship.

## Coordinate-language discipline

Track every revision with explicit `(center_x, top_y)` values.

Interpret directional edits literally:

- `왼쪽/오른쪽` changes x;
- `올려/내려` changes y;
- when `가운데쪽` follows `내려` or `올려`, it normally refers to the vertical center, not horizontal centering;
- when `가운데정렬` refers to a chip/object, align the logo's horizontal center to that object's center.

Do not change both axes when the user requests one-axis movement. Preserve all unmentioned elements.

## Core generation prompt checklist

A good prompt specifies:

1. exact 16:9 canvas and empty typography zones;
2. no people;
3. matte black background;
4. TTimes editorial energy plus Figma vector execution;
5. each architecture's physical arrangement;
6. fixed camera and common baseline;
7. material/color grammar;
8. negative list: no photorealism, generic neon, text, logos, labels, watermarks.

The prompt should describe the mechanism, not merely say “three AI chips.”

## Deterministic composition checklist

Before exporting:

- resize/crop the generated core to exactly 1280×720;
- add readability gradients only where needed;
- place official company/institution logos;
- place the clean TTimes logo at the measured reference size/position;
- typeset the exact headline and comparison line;
- ensure each comparison term uses the approved case;
- use separate output filenames for revisions;
- retain the source core, logos, composition script, and final output.

## Visual QA gates

Inspect the actual exported JPEG, not only the script:

- dimensions are exactly 1280×720;
- no misspelled or duplicated technical terms;
- TTimes logo is clean, correctly sized, and correctly positioned;
- no dirty halo, black extraction box, or JPEG residue around logos;
- company logos are centered over the intended architecture and do not overlap linework;
- HBM and HBF remain distinguishable in structure and color;
- headline remains readable at mobile scale;
- no people or forbidden visual elements appear;
- the final file opens successfully and is the file actually delivered.

## Failure lessons from production

- A generic image-generated chip poster can be technically polished yet fail TTimes style.
- A manually inpainted source with replacement text does not satisfy an explicit image-generation request.
- Image generation should not be trusted for exact English copy or logos.
- Matching a logo by extracting it from a JPEG can preserve size but import compression dirt; measure from the JPEG, then place a clean transparent master.
- Moving a logo “toward the center” on the wrong axis creates avoidable revision loops. Record x/y explicitly.
- If a logo overlaps a tall stack, raise the logo or lower the stack; do not leave it partially hidden.
- If two compared memory architectures share the same copper color, selectively recolor one related technology to a distinct but harmonious hue.
