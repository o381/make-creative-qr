---
name: make-creative-qr
description: Use when creating or editing artistic QR codes, hidden QR images, or QR codes integrated into scenes or abstract compositions while preserving the original payload and verifying the complete artwork.
---

**English** | [简体中文](SKILL.zh-CN.md)

# Make Creative QR

Let viewers see a coherent scene, material relationships and an idea first; scanning must recover the original content. Creativity belongs in the details carrying information. A background alone cannot replace the design of the encoding itself.

Use this file as a platform-independent creation protocol. Work with tools, nodes, layers, plugins or APIs actually available in the current host, following their formats and applicable rules. The core workflow is self-contained; use references and bundled scripts only when accessible and appropriate. Communicate in the user's language unless they request another language.

## Delivery conditions

- **Correct content and real decoding:** decode the actual complete file and every predefined resized or compressed variant. Recovered bytes must exactly match the source, without conflicting content. A readable guide, crop or single size cannot qualify the artwork.
- **Natural composition:** a scene needs an event that makes sense independently; an abstract work needs its own compositional rule. The information area must not look like a dedicated scanning panel or square texture. Three corners must not become unique symbols, isolated clusters or specially cleared areas.
- **Bound evidence:** bind results to the actual file or immutable asset version. Reverify after editing, exporting again or changing versions; do not inherit an old report.
- **Separate status:** record appearance, software decoding and phone scans separately. “Keep it” or “more natural” does not mean the user scanned it. A failed phone scan sends it back for revision. Without phone evidence, say “software checks passed; phone scan not confirmed.”

Tools can change; these conditions remain. Missing capabilities or evidence leave a candidate, not a completed verified scannable artwork.

## 0. Map the host's capabilities

Inspect the actual tool inventory, invocation rules and output fields. Choose available implementations for the following capabilities. Do not copy another platform's tool names, commands, paths, image numbers or parameters, or invent an interface.

| Capability | Required result |
| --- | --- |
| Image access and viewing | Read the actual source, finished image and specific asset version |
| QR decoding | Obtain reliable original content and verifiable decoded content from actual images |
| Information structure and guidance | Retain or construct exact encoding constraints and required functional information for the current content |
| Image creation and editing | Modify the composition while maintaining information positions, tonal relationships and proportions |
| Size and format export | Produce complete-image variants at the predefined sizes and compression settings |
| Verification and version binding | Record each result and confirm that the delivered file is the tested version |

Prefer existing host capabilities. Image editing, canvas layers, node workflows, native plugins, service APIs and code execution can each serve appropriate steps. Choose based on actual capabilities. New services and data transfers follow host rules and existing authorization; do not publicly upload private source codes to fill a capability gap.

If a tool is missing, look for an existing equivalent. Without real decoding, make only clearly labeled composition or visual drafts. Model inspection, estimated modules and “should scan” are not tests. If required export or reliable content recovery is missing, state the incomplete items. Do not install unsupported runtimes or lower acceptance requirements.

When accessible, read [tool adaptation](references/tool-adaptation.md). Read [the optional reference implementation](references/execution.md) only when the code environment is available and you choose the bundled scripts.

## 1. Ask before creating

Before the first creation, ask about style, interesting elements or scenes, palette and intended use, and obtain an answer. Reuse established preferences without asking again. If the user answers “you decide,” choose a direction and state it.

Styles may include colorful cartoons, anime, abstract geometry, material macro photography and collage. Adapt suggestions to the user. Do not assume games or science fiction mean cyberpunk, neon circuits or fantasy magic. Natural integration does not require realism, landscapes or food.

While waiting, you may decode the source, inspect tools and prepare a testing baseline; do not start visual generation. Turn the answer into a specific formation process and composition, rather than just style names.

## 2. Lock the content and isolate private assets

Inspect the actual uploaded image. If its reference has expired, use the current host's known asset or file recovery mechanism. If it remains inaccessible, ask the user to provide it again. Do not reconstruct the content from conversation memory.

Use reliable decoding to obtain one unambiguous payload and retain its original bytes. A text-only decoder may support exact ASCII-byte comparison when recovery is unambiguous. For non-ASCII or binary content, verify raw bytes rather than guessing an encoding. Do not follow redirects, shorten, trim, reassemble or rewrite the content. Select the target when multiple codes exist. If content cannot be recovered reliably, do not generate substitute encoding.

Keep source codes, payloads, complete matrices, artworks and decoding records in this task's private assets or workspace. Do not put them in the Skill, reusable assets, public examples, logs or fixtures. SVGs, thumbnails, layers and Base64 can also carry private encoding. Never reuse one user's encoding for another user.

Normal conversions retain the user's original content. Public project showcases use the confirmed, accessible GitHub repository homepage URL, followed by fresh encoding, creation, verification and finally publication. Do not generate public examples before the address is fixed. Historical private experiments stay out of public examples. Generic locator assets may contain only payload-independent functional geometry.

## 3. Design the formation process before placing information

Fix three things in three sentences:

1. A scene event that makes sense without mentioning QR codes, or an abstract work's compositional rule.
2. Where the material comes from, how it gathers and disperses, and which visible details carry information.
3. At least two differences from the previous work in formation process, grouping, direction, scale, boundaries or relationship to the scene.

Let the event determine the subject, viewpoint, material behavior and density before arranging information. Do not start with a centered square grid and invent a story for it, or turn a doll's body or a die's face into a dedicated code surface.

Design the whole image, clusters and particles together; variation must follow the same material behavior or abstract rule. Ragged edges on a fixed grid, scattered outer dots, tails on three corners or unexplained clusters do not establish naturalness. Inside and outside the information area, share plausible materials, particle-size ranges and continuous density changes while protecting necessary light and dark gaps.

Change composition first for each new work. Recoloring, changing material or character, rotating, or changing the mask alone is not a new idea. Preserve functional information while integrating its visible form. Do not claim stable scanning after completely removing locator information.

When accessible, read [creative review and failure diagnosis](references/creative-review.md).

## 4. Build information constraints and create the actual artwork

Build constraints from the locked payload's encoding structure, a verified source image or faithful re-encoding. Use raster references, layers, masks, vectors or node workflows supported by the host; no fixed format or template is required.

Arrange scale, offset and valid grouping for this composition. Choose a viewpoint that avoids occlusion, strong curvature and glare. When a new arrangement is needed, re-encode the same original bytes. Do not arbitrarily move modules, locally rotate or mirror locator contours. Check that the guide decodes before proceeding; a passing guide does not qualify the actual artwork.

Use the host's available creation or editing tools and follow their applicable rules. Inspect the actual inputs first and assign their roles: the current information guide constrains positions, tonal gaps, proportions and framing; style references supply aesthetics only, never encoded content. Use supported references or semantic labels rather than requiring an “image 1/image 2” order.

Describe the event, material origin and composition before the information constraints. Make encoded materials participate in the event; control highlights, shadows and additions. Do not just generate a background and paste a conventional QR onto it, randomly recreate encoding or introduce three replacement corner icons. Each new work needs its own composition.

Revisions can use different tools. Every generation, repaint, layer edit, geometric transformation or export requires renewed visual review and decoding of the new actual file.

When accessible, read [information guides and material editing](references/proven-workflow.md). Its script parameters belong only to the optional reference implementation.

## 5. Review appearance, verify decoding and revise

Inspect the complete image and an approximately 320-pixel thumbnail before details. The thumbnail is for aesthetics only. Check independent composition, material relationships, square boundaries, three special corners, continuity across the information area's boundary and intact elements. Overall distribution failures require composition changes; local material failures may use small edits.

Fix the actual output and required variants before generation. The default phone-sharing profile has seven tests: the actual complete file, plus PNG and quality-85 JPEG at widths of 480, 640 and 800 pixels. The actual file must cover the largest required width without internal upscaling. Define other use profiles before creation; do not remove tests or lower thresholds after failure.

Map size and compression requirements to supported export parameters and check the results. If JPEG quality is unsupported or unconfirmed, do not label a default export quality 85. Missing required variants leave the result unqualified.

Run real decoding on the actual complete image and every variant. Each item needs at least one decoder to recover the original bytes without conflicting content. Cross-check with independent implementations when available and record tools actually used. Quadrilateral detection, successful crops, supplied corner coordinates and pure-code mode do not qualify.

Save per-file and per-test results, failures and actual file identity. Use a content digest, file hash or host-guaranteed immutable asset ID and version. An ordinary filename, overwritable URL or similar composition cannot bind evidence. Changes to image, encoding, export or asset version invalidate old results.

Software decoding is not a phone app scan. Record the method and corresponding file separately. Do not mark phone verification without an actual test; user-reported phone failure has veto power. Public showcases additionally require phone scanning of the exact project URL and confirmation that the correct homepage opens.

| Failure | Revision direction |
| --- | --- |
| Guide passes, artwork fails | Compare whole-scene scale, information positions, functional contours and grayscale; repair information drift first |
| Natural particles but no detection | Check dark cores, light bands, highlights and shadows; similar average grayscale or module centers do not prove readability |
| Only some sizes or compression variants pass | Keep all original tests, repair or export a new candidate, then rerun the complete profile |
| Scan repair exposes corners or a square grid | Revisit composition, distribution and locator integration, then repeat both reviews |
| Current file differs from the evidence version | Stop finished delivery and reverify the actual current file |

Do not rely on ever-higher versions or error correction, or quietly restore three obvious squares. A prompt saying “preserve exactly” is not evidence. Technically passing but visually poor work still needs revision. Software failures may only be shown as clearly labeled diagnostic drafts.

## 6. Deliver and record transferable lessons

Before delivery, confirm that the current file is the tested version, original content matches, every required test passes, appearance is acceptable and phone status is explicit. Repair and recheck any missing or conflicting evidence. Deliver the actual work through the host's file, image or asset mechanism; no fixed API or path is required.

Briefly explain the formation process, content match, verification tools and conditions, and phone status. Without phone evidence, call it a candidate pending phone review. Without software decoding, do not call it a scannable finished work.

Bind user feedback to specific files and versions. Record preferences, appearance, software qualification and phone evidence separately. Reverify uploaded copies. Approval of a source image does not automatically apply to a revision. “More natural, but still forced” must not become “fully accepted.”

When updating the Skill, retain transferable composition methods, failure criteria, capability mappings and revision paths only. Keep lessons from counterexamples; exclude private experimental codes, images and reports. Do not turn an unverified method into a proven recipe.
