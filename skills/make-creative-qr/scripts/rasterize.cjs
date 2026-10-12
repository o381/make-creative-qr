#!/usr/bin/env node
// Rasterize exact information guides or export a verified-size scan PNG.
const fs = require('fs'), path = require('path');
let sharp;
const candidates = ['sharp'];
for (const envName of ['CODEX_PRIMARY_RUNTIME_NODE_MODULES', 'CREATIVE_QR_NODE_MODULES'])
  if (process.env[envName]) candidates.push(path.join(process.env[envName], 'sharp'));
for (const name of candidates) {
  try { sharp = require(name); break; } catch (err) {
    if (err.code !== 'MODULE_NOT_FOUND') throw err;
  }
}
if (!sharp) throw new Error('Install sharp in a task-local directory and set CREATIVE_QR_NODE_MODULES');
(async () => {
  const [input, output, rawWidth] = process.argv.slice(2);
  if (!input || !output) throw new Error('Usage: rasterize.cjs INPUT OUTPUT.png [WIDTH]');
  if (path.resolve(input) === path.resolve(output)) throw new Error('Use a separate output path');
  let image = sharp(input);
  if (rawWidth) {
    const width = Number(rawWidth);
    if (!Number.isInteger(width) || width < 64) throw new Error('WIDTH must be an integer >=64');
    image = image.resize({width, kernel: 'lanczos3'});
  }
  fs.mkdirSync(path.dirname(path.resolve(output)), {recursive: true});
  fs.writeFileSync(output, await image.png().toBuffer());
  console.log(JSON.stringify({file: path.resolve(output), status: 'written-requires-scan-verification'}));
})().catch(err => { console.error(err.message); process.exit(1); });
