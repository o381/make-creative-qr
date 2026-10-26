<p align="right"><sub><strong>English</strong> · <a href="README.zh-CN.md">简体中文</a></sub></p>

<h1 align="center">Make Creative QR</h1>

<p align="center"><em>Make the code part of the picture.</em></p>

<p align="center">
  An agent Skill for creative QR artwork.<br>
  Turn real QR content into a scene. Verify the complete image.
</p>

<p align="center">
  <a href="#light-takes-shape">Selected work</a> ·
  <a href="#make-your-own">Use the Skill</a> ·
  <a href="examples/README.md">Full collection</a>
</p>

<br>

<h3 align="center"><a name="light-takes-shape"></a>Light takes shape</h3>

<p align="center"><em>A glass, a pencil, and a different way of seeing.</em></p>

<p align="center">
  <a href="examples/README.md#caustic-jelly"><img src="docs/assets/showcase/caustic-jelly.webp" width="560" alt="Refracted light becomes a jellyfish on the tabletop."></a><br>
  <sub>Jellyfish of light</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.md#pencil-whale"><img src="docs/assets/showcase/pencil-whale.jpg" width="560" alt="A pencil&#x27;s shadow takes the shape of a swimming whale."></a><br>
  <sub>A whale&#x27;s shadow</sub>
</p>

<br>

<h3 align="center">Small things, other worlds</h3>

<p align="center"><em>An everyday detail opens onto somewhere else.</em></p>

<p align="center">
  <a href="examples/README.md#zipper-city"><img src="docs/assets/showcase/zipper-city.webp" width="560" alt="An open zipper reveals a city glowing in the lining."></a><br>
  <sub>Zipper city</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.md#stamp-sea"><img src="docs/assets/showcase/stamp-sea.jpg" width="560" alt="A snail draws the sea out of a postage stamp."></a><br>
  <sub>A sea in a stamp</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.md#shaved-night"><img src="docs/assets/showcase/shaved-night.jpg" width="560" alt="Blue pencil shavings scatter into a piece of night."></a><br>
  <sub>Shavings of night</sub>
</p>

<br>

<h3 align="center">Nothing stays still</h3>

<p align="center"><em>Spots take wing. Notes take flight. Rain writes back.</em></p>

<p align="center">
  <a href="examples/README.md#jaguar-butterfly"><img src="docs/assets/showcase/jaguar-butterfly.jpg" width="560" alt="Spots pass from a sleeping jaguar into a butterfly&#x27;s wings."></a><br>
  <sub>Jaguar butterfly</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.md#flying-score"><img src="docs/assets/showcase/flying-score.webp" width="560" alt="A piano score breaks into a flock of birds."></a><br>
  <sub>The score takes flight</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.md#rain-letter"><img src="docs/assets/showcase/rain-letter.jpg" width="560" alt="Rain rings unfold around a paper boat in indigo print."></a><br>
  <sub>Rain writes back</sub>
</p>

<br>

<p align="center"><a href="examples/README.md">Explore all 14 works →</a></p>

<p align="center"><sub><a href="examples/verification.json">Decoding &amp; phone-scan records</a><br>Phone scans remain pending where unconfirmed. Public works point to this repository.</sub></p>

<br>

<h3 align="center"><a name="make-your-own"></a>Make your own</h3>

Import the [Skill directory](skills/make-creative-qr/) into an agent that supports directory-based Skills, or provide the [Skill instructions](skills/make-creative-qr/SKILL.md). Upload a real QR image, then ask:

```text
Use make-creative-qr to create an artwork with a naturally integrated QR code.
First confirm my style, elements and intended use. Preserve the original
scanned content. Check the complete artwork and sharing sizes.
```

Documentation defaults to English, with a complete [Chinese edition](skills/make-creative-qr/SKILL.zh-CN.md). Creation and delivery follow the user's language.

<details>
<summary>Creative approach, verification and privacy</summary>

The scene should stand on its own: materials have an origin, density follows an idea, and the visual language continues through the encoded area. Preserve the original scanned bytes without replacing, shortening or rewriting them. Verify the complete artwork and sharing variants; a failed phone scan requires revision.

The Skill defines capabilities and acceptance criteria; the agent uses tools available in its host. The bundled Python/Node scripts are one optional implementation. Creation requires image viewing and generation, reliable decoding, export and file-integrity checks. Without real decoding or required exports, outputs remain design candidates.

The default software profile has seven checks: the actual complete file, plus PNG and quality-85 JPEG variants at widths of 480, 640 and 800 pixels. Each must recover the original content without conflicts. Crops, supplied corner coordinates and pure-code mode cannot replace complete-image verification. Bind evidence to a content digest or file hash and recheck after editing or export. Software success cannot establish a phone app scan.

Confirm style, elements and use before creation; build information guidance and revise using visual and decoding feedback. Photography, illustration, anime, geometry and collage can all carry information. Non-ASCII or binary content needs reliable original-byte evidence; do not generate replacement encoding when the input cannot be confirmed.

Private source codes, payload data, artworks and recognition records stay out of public examples, reusable assets and test fixtures. Decoding runs in the host environment; generation and storage depend on the chosen services. This project does not promise an entirely offline workflow.

[Tool adaptation](skills/make-creative-qr/references/tool-adaptation.md) · [Optional reference implementation](skills/make-creative-qr/references/execution.md)

</details>

<br>

<p align="center"><sub>
  <a href="CONTRIBUTING.md">Contribute</a> ·
  <a href="SECURITY.md">Privacy &amp; security</a> ·
  <a href="docs/THIRD_PARTY_NOTICES.md">Third-party notices</a> ·
  <a href="LICENSE">MIT License</a>
</sub><br><sub>MIT covers code and documentation; artwork and third-party assets have separate terms.</sub></p>
