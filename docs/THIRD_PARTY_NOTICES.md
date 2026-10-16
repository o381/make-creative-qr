**English** | [简体中文](THIRD_PARTY_NOTICES.zh-CN.md)

# Third-party dependencies and assets

The optional code implementation uses the dependencies below. Licenses were checked against installed package license files and metadata on 2026-10-13. This repository does not distribute dependency source, binaries, models or system runtimes. Full package licenses and bundled-component notices still apply; the project's MIT License does not replace them.

| Dependency / reviewed version | Upstream | License |
| --- | --- | --- |
| opencv-contrib-python-headless 5.0.0.93 | https://github.com/opencv/opencv-python | Python wrapper: MIT; OpenCV / contrib: Apache-2.0; bundled components: package LICENSE-3RD-PARTY.txt |
| zxing-cpp 3.1.1 | https://github.com/zxing-cpp/zxing-cpp | Apache-2.0 |
| Segno 1.6.6 | https://github.com/heuer/segno | BSD-3-Clause |
| NumPy 2.4.6 | https://github.com/numpy/numpy | Core: BSD-3-Clause; combined package metadata: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0; bundled notices: package licenses directory |
| Pillow 12.3.0 | https://github.com/python-pillow/Pillow | MIT-CMU; bundled binary components retain their notices |
| sharp 0.34.5 | https://github.com/lovell/sharp | Apache-2.0; prebuilt libvips and other components retain their licenses |

The English and Chinese SVG panels in `docs/assets` are typographic project illustrations, not QR codes or experimental artworks. Outlined glyphs use Noto Serif, Noto Serif SC, Noto Sans and Noto Sans SC under SIL Open Font License 1.1; the [font license](licenses/Noto-OFL.txt) is included. Font files are not distributed.

`particle-locators.json` contains payload-independent, seven-unit geometry for three functional regions, assembled for this workflow as technical guidance. It contains no complete data matrix. Unreviewed private icons are not distributed. Historical reference images, private artworks and private encoding data are outside this repository.
