---
name: make-creative-qr
description: Use when creating or repairing artistic QR codes from QR images or explicitly supplied content, including hidden QR images and codes integrated into scenes or abstract compositions.
---

**English** | [简体中文](SKILL.zh-CN.md)

# Make Creative QR

Let viewers see a coherent scene, material relationships and an idea first; scanning must recover the original content. Creativity belongs in the details carrying information. A background alone cannot replace the design of the encoding itself.

Use this file as a platform-independent creation protocol. Work with tools, nodes, layers, plugins or APIs actually available in the current host, following their formats and applicable rules. The core workflow is self-contained; use references and bundled scripts only when accessible and appropriate. Communicate in the user's language unless they request another language.

## Automatic entry and input routing

When asked to use this Skill through a repository or directory link, read the actual `skills/make-creative-qr/SKILL.md`, or its Chinese edition, rather than just the homepage. A supplied single-file edition contains the core workflow; load accessible references when the relevant step needs them. Reading a link supplies instructions for the current task; persistent installation and discovery depend on the host. The Skill's location is not the content to encode.

Once this Skill is selected or a creative-QR task is established, an uploaded QR image alone starts one artwork. The user need not repeat tool checks, preservation, creative review, decoding or delivery instructions. Follow the actual request when the user only asks to read a code, install the Skill or explain its use; those requests do not start image generation.

| Input or follow-up | Action |
| --- | --- |
| QR image, including one uploaded without text in an active creation task | Inspect and decode the actual image, lock its content, then create using established preferences or defaults |
| Exact URL or text explicitly supplied for QR creation | Lock that content and build a verified source code; no QR upload is required |
| Style or scene reference | Use it for appearance with the current locked content; if no target content exists, ask for the QR or exact content rather than borrowing a reference image's encoding |
| “Continue” or “another idea” | Resume unfinished work; after a delivered candidate, continue the creation task with a distinct composition. Retain the locked content unless the user changes it |
| “Cannot scan” | Diagnose and repair the corresponding failed version, keeping the locked content. Record the reported scanning method; leave it unknown if unspecified |

## Delivery conditions

- **Correct content and real decoding:** decode the actual complete file and every predefined resized or compressed variant. Recovered bytes must exactly match the source, without conflicting content. A readable guide, crop or single size cannot qualify the artwork.
- **Natural composition:** a scene needs an event that makes sense independently; an abstract work needs its own compositional rule. The information area must not look like a dedicated scanning panel or square texture. Three corners must not become unique symbols, isolated clusters or specially cleared areas.
- **Bound evidence:** bind results to the actual file or immutable asset version. Reverify after editing, exporting again or changing versions; do not inherit an old report.
- **Separate status:** record appearance, software decoding and phone scans separately. “Keep it” or “more natural” does not mean the user scanned it. A failed phone scan sends it back for revision. Without phone evidence, say “software checks passed; phone scan not confirmed.”

Tools can change; these conditions remain. Missing capabilities or evidence leave a candidate, not a completed verified scannable artwork.

## 0. Map the host's capabilities

Inspect the actual tool inventory, invocation rules and output fields. Choose available implementations for the following capabilities. Do not copy another platform's tool names, commands, paths, image numbers or parameters, or invent an interface.

A documented, configured relay or third-party plugin can supply a capability. Inspect available integration paths before declaring a tool missing; the absence of an official provider entry is not evidence that image generation is unavailable.

Confirm decoder operation on a known readable control when starting or changing the environment. A missing engine, import failure or invocation error is a capability failure, not evidence that the artwork is unreadable; restore or replace that capability before diagnosing the image.

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

## 1. Resolve the brief and use defaults

Reuse the user's style, elements, palette, intended use and feedback from this task. When these are absent, choose a coherent new concept and palette, produce one artwork, and use the default phone-sharing test profile in step 5. Briefly state the chosen direction and proceed; missing aesthetic preferences and “you decide” do not require a questionnaire or another confirmation. Do not impose a single photographic style, material or layout on every user.

Ask only when missing information prevents correct execution, such as no recoverable target content, several codes without a clear target, or an unresolved output requirement essential to the stated use. Ask for the missing item together and continue independent source or tool checks while waiting. Explicit user instructions take precedence over defaults. Creation does not itself authorize public posting or unrelated operations.

Styles may include colorful cartoons, anime, abstract geometry, material macro photography and collage. Adapt suggestions to the user. Do not assume games or science fiction mean cyberpunk, neon circuits or fantasy magic. Natural integration does not require realism, landscapes or food.

Turn the established or chosen direction into a specific formation process and composition, rather than just style names. Resolve the target content before visual generation.

## 2. Lock the content and isolate private assets

For an uploaded source, inspect the actual image. If its reference has expired, use the current host's known asset or file recovery mechanism. If it remains inaccessible, ask the user to provide it again. Do not reconstruct the content from conversation memory.

Use reliable decoding to obtain one unambiguous payload and retain its original bytes. A text-only decoder may support exact ASCII-byte comparison when recovery is unambiguous. For non-ASCII or binary content, verify raw bytes rather than guessing an encoding. Do not follow redirects, shorten, trim, reassemble or rewrite the content. Select the target when multiple codes exist. If content cannot be recovered reliably, do not generate substitute encoding.

When the user explicitly supplies a URL or text to encode instead of a source image, retain the exact string as UTF-8 bytes unless they specify another encoding. Do not normalize the URL, follow it to replace its destination or borrow content from the Skill link or showcase. Create a plain source code and confirm that real decoding recovers these bytes before making artwork. This explicit-content route does not permit guessing an unreadable uploaded code's content.

Keep source codes, payloads, complete matrices, artworks and decoding records in this task's private assets or workspace. Do not put them in the Skill, reusable assets, public examples, logs or fixtures. SVGs, thumbnails, layers and Base64 can also carry private encoding. Never reuse one user's encoding for another user.

Normal conversions retain the user's original content. Public project showcases use the confirmed, accessible GitHub repository homepage URL, followed by fresh encoding, creation, verification and finally publication. Do not generate public examples before the address is fixed. Historical private experiments stay out of public examples. Generic locator assets may contain only payload-independent functional geometry.

## 3. Design the formation process before placing information

Read the latest task feedback and applicable Skill revisions before choosing the next composition. Carry unresolved defects forward as specific checks, not as a reason to repeat the same layout in another material.

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

Own the complete creation loop with the available tools: generate or edit, inspect the returned image, decode and diagnose, revise, then repeat both reviews. Do not stop after an idea, a prompt, a guide or the first failed image, or ask whether to continue between routine steps. Each retry needs a diagnosed defect and a changed approach; change the formation process when the same structural conflict recurs. Continue within existing authorization, tool limits and spending bounds until an acceptable software-qualified candidate is ready. If source recovery, a capability with no available substitute, authorization or a resource limit blocks further work, report the concrete blocker and current evidence without claiming completion. Respect a user-requested pause.

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

Before delivery, confirm that the current file is the tested version, original content matches, every required test passes, appearance is acceptable and phone status is explicit. Repair and recheck any missing or conflicting evidence. For a request to finish natural artwork, resolve known visual failures before requesting a phone retest; labeling an unattractive repair “diagnostic” does not bypass appearance review. Share such diagnostics when the user asks to inspect the investigation. Deliver the actual work through the host's file, image or asset mechanism; no fixed API or path is required.

Briefly explain the formation process, content match, verification tools and conditions, and phone status. Without phone evidence, call it a candidate pending phone review. Without software decoding, do not call it a scannable finished work.

Show or save the actual qualified candidate without waiting for another “continue.” If phone scanning is the remaining check, provide that exact file and request a scan in the user's intended app, such as WeChat, while retaining the unconfirmed status until evidence arrives. Do not make the user perform available software checks or repair known visual defects on the agent's behalf.

Bind user feedback to specific files and versions. Record preferences, appearance, software qualification and phone evidence separately. Reverify uploaded copies. Approval of a source image does not automatically apply to a revision. “More natural, but still forced” must not become “fully accepted.”

Close the learning loop within each creation round: bind observed defects and user feedback to the actual version, diagnose the cause, and update the relevant Skill guidance before the next attempt when a transferable lesson emerges. Maintain equivalent language editions together. If an existing rule already covers the failure, fix where and how it is applied rather than adding a synonymous prohibition. Record the changed decision and an evidence-based next check in the task; do not stop at a promise to improve. Use the [feedback loop](references/creative-review.md#turn-feedback-into-the-next-decision) for diagnosis and revision criteria.

Retain transferable composition methods, failure criteria, capability mappings and revision paths only. Keep lessons from counterexamples; exclude private experimental codes, images and reports. Keep individual preferences in task context unless they generalize. Do not turn an unverified method or a successful calibration coefficient into a proven recipe.
