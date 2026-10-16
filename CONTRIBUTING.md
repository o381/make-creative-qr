**English** | [简体中文](CONTRIBUTING.zh-CN.md)

# Contributing

Improvements to composition, scanning reliability, failure diagnosis and documentation are welcome. Describe the concrete problem and expected behavior before submitting a focused pull request.

## Contributing assets

Use the project's confirmed GitHub homepage URL for public reproductions. Create fresh reproduction images and verify their decoded content; do not submit private source codes or derived artworks. Exclude private payloads, complete matrices, task directories, original reports and service credentials. State the source and redistribution license of external images, models or templates.

## Creative contributions

Explain the event or compositional rule that works independently of the QR code, which details carry information, and how formation and distribution differ from existing approaches. Inspect complete images and thumbnails for square boundaries, three special corners and dedicated code panels. Changing only color, material or background is not a complete new approach.

## Verification contributions

Use real host decoding on actual complete files and recheck the delivered version. If using bundled code, run `qualify` and `check_delivery.py`. Default tests cover the original file, 480/640/800-pixel PNGs and quality-85 JPEGs at each size. Report matching engines, failures and phone status. Crops or supplied-corner decoding cannot substitute for full-image checks.

Keep phone evidence separate; do not manually edit software reports to claim phone tests. Decoder changes need public-content reproductions and relevant regression checks. Reverify after generation or edits; reports for different files or old versions do not apply.

For translations, keep English at the canonical paths and Chinese in `.zh-CN.md` siblings. Update reciprocal language links and both versions when changing workflow requirements. Preserve image hashes, payloads and the distinction between software and phone evidence.

## Discussion

Describe defects and evidence concretely, and respect different styles. Report private or security-sensitive data through [SECURITY.md](SECURITY.md).
