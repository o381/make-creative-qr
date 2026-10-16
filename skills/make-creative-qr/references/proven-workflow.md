**English** | [简体中文](proven-workflow.zh-CN.md)

# Information guides and material editing

Implement the main workflow with available host tools. Information guides may use layers, masks, nodes, rasters or vectors. The scripts, assets and parameters here form an optional reference route; other agents need not install or invoke them. The main workflow's results and acceptance conditions remain the same.

## Technical starting point and limits

Generate an exact matrix for the current original content, then design its visible materials. `assets/particle-locators.json` contains normalized geometry and tones for three functional regions only, without any user's data matrix or link. The default particle method uses M error correction, at least version 5, 24-pixel module units, a six-module quiet margin and carrier density 0.2. A 0.15–0.3 range can be explored; it neither guarantees decoding nor provides a natural-composition recipe.

Fixed traversal grouping in `render_guide.py` suits a single baseline, not the final layout of an entire collection. New works may use a new mask/version and valid randomized horizontal/vertical grouping in `render_organic_guide.py`. Material behavior and scene relationships must still create compositional differences. Dark-particle and light-cavity guides have passed software tests in some cases; this does not qualify final artwork, inversions or arbitrary viewpoints.

Use material to express required locator tones rather than mechanically deleting them. Default soft contours may turn into three distinctive gray blobs or cleared regions. Matching material alone does not guarantee integration. Review the overall distribution using the [main workflow](../SKILL.md); a scannable locator template does not establish visual acceptance.

Changing grayscale contours, breaking dark cores into fragments, adding particles or connecting shapes are experiments requiring retesting. Similar average grayscale does not prove fidelity. Do not introduce arbitrary data errors to camouflage locators. Higher error correction cannot guarantee detection with missing functional information.

## Scene editing prompt

Define the event, material formation and composition through the main workflow first. The current guide must already use the scale and position needed for that composition. Do not invent prompt justifications for an unsuitable fixed grid. Identify the information guide and visual reference using host-supported references; any style reference supplies aesthetics only. Do not assume fixed image numbering or order.

```text
Create [EVENT OR VISUAL RULE] in [STYLE AND PALETTE].
Show how [MATERIAL] forms, gathers and disperses through [PROCESS].
A viewer unaware of the hidden code should understand the composition.
The information-guide input fixes the marks within this full scene.
Preserve their footprint, tonal gaps, relative scale and framing.
Render them as the same material produced by the event, with coherent
cluster sizes, surface behavior and density changes inside and outside.
The surrounding details must participate in this process, not decorate
a separate rectangular pattern. Do not add arbitrary matching blobs
as camouflage or make three regions receive unique visual treatment.
Keep the necessary light gaps and safe exterior separation intact.
No pasted code, display panel, square backing or three replacement icons.
The style-reference input, if present, supplies style only, not encoded content.
```

This template does not require all encoded marks to connect or require extra noise. The goal is plausible material behavior without exposing a dedicated code surface. Powder, continuous liquid, fragments and negative space each need a credible distribution.

## Abstract or material-led artwork prompt

Use only when the user chooses this direction; do not impose a code-dominated subject on a scene-based request. Define an abstract rule rather than substituting element count or texture complexity for composition.

```text
Create an abstract artwork governed by [COMPOSITIONAL RULE], using
[MATERIAL OR SHAPE VOCABULARY] in [PALETTE].
The information-guide input constrains information positions and light gaps.
Translate these marks into meaningful groups, varied scales and edges
consistent with the rule, without exposing a rectangular code panel.
Apply the same visual vocabulary throughout; avoid three unique corner
symbols, cleared islands, nested targets or decorative locator rings.
Preserve all encoded centers, proportions, framing and tonal separation.
Control highlights and shadows inside the existing dark footprints.
No random replacement code, conventional QR overlay or decorative
background doing all the creative work. No unwanted text or watermark.
```

## Revision order

Keep the qualified file and report as a technical fallback. Revisions do not inherit its qualification.

1. If the whole looks forced, redesign material distribution and scene relationships. Do not just add texture, outer dots or tails to the fixed grid.
2. For local material mismatches, unify thickness, gloss, particle-size range and edges across the boundary. Keep highlights and micro-shadows within existing dark contours and protect light gaps.
3. If three regions look special, inspect shape, grayscale, sharpness and surrounding gaps. Do not add replacement icons or unexplained camouflage clusters, or simply remove functional information.
4. For decoding failures, diagnose density and tonal drift against the guide and repair the specific problem. If a size passes but the original fails, export a new candidate and fully test the actual new file and all required variants. Use `qualify` when choosing the bundled scripts.
5. After every information, visual or export change, retest and review the whole image. Consistent material, a readable skeleton or one successful size cannot replace both final acceptance checks.
