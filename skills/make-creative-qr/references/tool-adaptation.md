**English** | [简体中文](tool-adaptation.zh-CN.md)

# Host tool adaptation

Choose tools by results. Bundled scripts, product names and model names are not required capabilities. Jimeng agents, canvas agents, Gemini and other hosts may be integration targets, but actual tools and permissions determine whether they can complete the workflow. Do not claim platform testing that has not happened.

## Map this task

Inspect the host's available tool inventory, node documentation, input/output contracts and file reference mechanism. For each required capability, record the actual implementation, parameter mapping, returned evidence and limitations. Do not invent calls.

| Workflow capability | Possible implementations | What to verify |
| --- | --- | --- |
| Inspect actual images | Image inputs, canvas previews, layers, asset access | Actual pixels, target version and accessible references |
| Recover and verify encoding | Native decoders, QR plugins, available decoding services, libraries, scan apps returning real results | Raw bytes or unambiguous ASCII, actual complete image and conflicting content |
| Build information guides | Verified source, encoder, vector/raster editing, nodes, masks, code | Fidelity to current original content, functional information and tonal relationships |
| Create and revise images | Image generation, inpainting, canvas layers, node editing, supported vector/image operations | Reference roles, composition and information constraints, new actual output |
| Export test variants | Canvas export, conversion tools, service APIs, code | Actual size, format, compression settings and full framing |
| Bind and deliver | File hashes, content digests, guaranteed immutable asset IDs and versions, native saving | Tested and delivered versions match |

One tool can serve several capabilities, and several tools can serve one. Make intermediate results, references and the next step's evidence explicit without imposing a universal calling format.

## Missing capabilities

- Editing and viewing without reliable decoding: create composition or visual candidates labeled unverified; do not deliver verified scannable artwork.
- Decoding and editing without code execution: use native guidance and export tools; Python/Node and bundled scripts are not required.
- Decoding without required format or quality export: continue supported design and diagnostics, but missing required tests remain unqualified. Relabeling cannot satisfy them.
- An input image without reliable content recovery: obtain decoding evidence first; do not guess text or generate a substitute link.
- A report for an old version: reverify the current actual asset. Similar appearance or the same filename cannot inherit qualification.
- Checks requiring supplied locations or crops: keep them as diagnostics, not full-image acceptance.

External services and new authorization follow host rules and current user authorization. Tool adaptation must not move private data into public demonstrations or reusable assets.

## Minimum record

Keep a private task record containing the original content baseline; actual file or immutable version identity; required sizes, formats and qualities; per-item real decoding results and conflicts; appearance review; separate phone feedback; and missing capabilities.

Use structured data, tables or asset-bound records the host can reliably preserve. JSON and SHA-256 are suitable where supported, but fields and algorithms need not match the bundled scripts. Evidence must retain the same meaning.

## Optional reference implementation

With a suitable code environment, the bundled Python/Node scripts provide one implementation. Their libraries, commands, filenames and output fields apply only to that route; interpret results according to its documentation.

Other routes must still recover the original content, decode complete images, test every variant and recheck delivery identity. Library detection alone, one phone scan or a model's self-score cannot establish full acceptance.

## Single file or complete directory

When only SKILL.md is supplied, follow its complete capability requirements, workflow and acceptance criteria. Missing references should not reduce every step to installing commands. The full directory adds creative diagnostics and optional implementations.

Product-specific files such as agents/openai.yaml are only for hosts that recognize them. Other hosts use their own Skill import or context mechanism; metadata invocation syntax is not a universal requirement.
