**English** | [简体中文](execution.zh-CN.md)

# Optional Python/Node reference implementation

Use this reference only when the host has suitable code execution and you choose the bundled scripts. The main workflow does not require these libraries or commands. Other tools must achieve equivalent acceptance under SKILL.md and tool-adaptation.md. Without a code environment, choose available native tools rather than copying unusable shell commands. Dependency preparation follows the host's runtime and permission rules.

Set `SKILL_DIR` to the actual Skill directory and `TASK_DIR` to a separate workspace for this task. Directory names may change after installation.

Check Python for `cv2`, `zxingcpp`, `segno`, `numpy`, `PIL` and `cv2.wechat_qrcode_WeChatQRCode`. Standard OpenCV does not include contrib modules. If needed, the assistant can install into the task directory without asking the user to install software manually:

```bash
python3 -m pip install --target "$TASK_DIR/python-deps" -r "$SKILL_DIR/scripts/requirements.txt"
export PYTHONPATH="$TASK_DIR/python-deps${PYTHONPATH:+:$PYTHONPATH}"
```

Use Node and an available `sharp`. If absent, install within the task directory and point `CREATIVE_QR_NODE_MODULES` at its `node_modules`. Avoid global installation or changes to the user's project environment. State missing capabilities honestly; do not claim unperformed checks.

| Command | Output and meaning |
| --- | --- |
| `capture` | Private payload.bin, current matrix.json and source-report.json without plaintext content |
| `render_guide.py` | Exact information-skeleton SVG; not qualified artwork |
| `rasterize.cjs` | Skeleton PNG or explicitly sized scan PNG; must be retested after writing |
| `verify` | Quick complete-file check; exit 0 means all supplied files decode to the original content, not that resize/compression acceptance is complete |
| `probe` | Original and in-memory variant diagnostics; exit 0 means at least one diagnostic succeeded and cannot qualify delivery |
| `export` | Mechanical PNG export using the same Pillow Lanczos as diagnostics; requires a new path and no upscaling; output is not yet qualified |
| `qualify` | Exit 0 only when the actual file and all required PNG/JPEG variants match without conflicts; failure is 2 and exception is 1 |
| `check_delivery.py` | Read-only review of an existing report against current actual files before saving/display; hash, complete-pixel-read or required-evidence mismatch returns 2. Does not replace qualification, visual review or phone evidence. |

`usable` requires at least one engine to recover the original payload with no conflicting content. Detection alone or `matching_engines` alone is insufficient.

ZXing uses PIL RGB images; if using ndarray, follow its BGR convention. OpenCV explicitly converts RGB to BGR. Incorrect channel order can wrongly reject colored codes.

WeChatCV returns text rather than general raw bytes; the scripts use it as a fallback only for ASCII. Verify non-ASCII or binary content with ZXing raw bytes rather than guessing unknown encodings.

Do not supply corners, known boundaries, pure-code mode or crops to the final decoder. Distinguish original images from resized variants during diagnostics.

During iteration, prioritize particle density, light gaps, highlights, dark shadows, particle sizes and image dimensions. Bright colors may still contain dark shadows. Higher resolution is not necessarily better than a suitable display size.

If only a smaller version passes, export that size and retest the actual file against its predefined profile. Print work must be verified at its intended size and format. Report camera or print tests only after actually performing them.

## Software acceptance and phone evidence

The default phone-sharing profile is `qualify --widths 480 640 800 --qualities 85`, with the actual file at least 800 pixels wide. PNG and quality-85 JPEG at every size must pass. “At least one size passed” is insufficient. Define other use profiles before generation; do not remove tests after failure.

Read `all_qualified` and each image's `software_gate_passed` in `qualification.json`. Reports retain the actual file SHA-256, complete-file results, every variant, conflicts and failures. Keep reports in the private task directory. A batch returns 2 if any image fails. Individually qualified files may be selected, but failed group members cannot be delivered with them.

The scripts always set `physical_phone_test_performed` to false and `phone_scan_status` to `unverified`. These define the boundary of software evidence; do not manually change them to claim a phone test. Keep phone feedback in separate private records bound to the exact file and method. A user's failed scan has veto power.

Internal variants are mechanically resized/compressed complete-image diagnostics, not saved delivery files. If a smaller diagnostic passes, write an actual scan PNG with `export` and run `qualify` again. Do not assume Sharp and Pillow produce identical output; two consecutive resizes may alter particle contours. Editing, exporting again or re-encoding invalidates the old report.

Additional smaller sizes or stronger compression may aid diagnostics, but partial success cannot qualify delivery:

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" probe \
  --payload "$TASK_DIR/source/payload.bin" --image "$CANDIDATE_PNG" \
  --widths 320 480 640 800 --qualities 85 70 \
  --report "$TASK_DIR/probe-report.json"
```

When mechanical export is needed, use a new path, then run the full required `qualify` profile on the actual output:

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" export \
  --image "$CANDIDATE_PNG" --out "$FINAL_PNG" --width 800
```

Before actual delivery, run integrity review with the same sizes and qualities defined before generation:

```bash
python3 "$SKILL_DIR/scripts/check_delivery.py" \
  --payload "$TASK_DIR/source/payload.bin" --report "$TASK_DIR/qualification.json" \
  --images "$FINAL_PNG" --widths 480 640 800 --qualities 85
```

Check each tool's return code before its dependent step. After a nonzero result, do not upload, overwrite a saved version or display it as finished. Integrity review cannot approve damaged files or borrow a report for a different path; a new delivery path needs fresh `qualify`. If a saved local file can still change, recheck before display.

Resolve the creative direction from established preferences or the Skill's defaults before generation, and lock the current user's content. Never reuse one user's QR for another user.

## Reference command sequence

Use only after choosing this implementation and preparing dependencies. Paths and filenames are conventions for this route and can be adapted to the task.

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" capture \
  --source "$SOURCE_IMAGE" --out "$TASK_DIR/source"
python3 "$SKILL_DIR/scripts/render_guide.py" \
  --matrix "$TASK_DIR/source/matrix.json" --out "$TASK_DIR/guide.svg" --shape grains
node "$SKILL_DIR/scripts/rasterize.cjs" \
  "$TASK_DIR/guide.svg" "$TASK_DIR/guide.png" 1000
```

Check success after each step. These guides provide technical constraints only. Continue with the host's creative capabilities to produce the actual artwork.

For a new arrangement of the same content, re-encode original bytes. Choose parameters for the content and composition; the values below only illustrate the interface:

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" reencode \
  --payload "$TASK_DIR/source/payload.bin" --out "$TASK_DIR/variant-matrix.json" \
  --mask 6 --min-version 5
python3 "$SKILL_DIR/scripts/render_organic_guide.py" \
  --matrix "$TASK_DIR/variant-matrix.json" --out "$TASK_DIR/variant.svg" \
  --shape shards --group-probability .5
```

Run the default seven tests on the actual complete artwork, then perform delivery review:

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" qualify \
  --payload "$TASK_DIR/source/payload.bin" --images "$FINAL_PNG" \
  --widths 480 640 800 --qualities 85 --report "$TASK_DIR/qualification.json"
```

This implementation's software gate passes only with exit 0 and `software_gate_passed` true for the current file. Then run `check_delivery.py` as described above. Record visual acceptance and phone status independently.
