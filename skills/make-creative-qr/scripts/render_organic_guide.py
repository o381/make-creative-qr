#!/usr/bin/env python3
"""Make a varied exact-information SVG guide, not final bitmap artwork."""
import argparse
import json
import math
from pathlib import Path
import random
import re
import secrets


def color(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
        raise argparse.ArgumentTypeError('Use six-digit hex colors')
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--matrix', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--shape', choices=['shards', 'cavities'], default='shards')
    p.add_argument('--seed', type=int)
    p.add_argument('--group-probability', type=float, default=.5)
    p.add_argument('--density', type=float, default=.2)
    p.add_argument('--invert', action='store_true')
    p.add_argument('--background', type=color)
    p.add_argument('--palette', type=color, nargs='+')
    args = p.parse_args()
    if not 0 <= args.density <= .5 or not 0 <= args.group_probability <= 1:
        raise ValueError('density must be 0..0.5; group probability must be 0..1')
    matrix = json.loads(Path(args.matrix).read_text(encoding='utf8'))['matrix']
    n = len(matrix)
    if n < 21 or n > 177 or (n-21) % 4 or any(len(row) != n for row in matrix):
        raise ValueError('Invalid standard QR matrix dimensions')
    if any(v not in (0, 1) for row in matrix for v in row):
        raise ValueError('Matrix must contain binary modules')
    seed = args.seed if args.seed is not None else secrets.randbits(32)
    rng = random.Random(seed)
    bg = args.background or ('#261249' if args.invert else '#fff8e6')
    palette = args.palette or (['#fff5a1', '#ffecc9', '#e5fff3', '#e8f3ff']
                              if args.invert else ['#971b6e', '#3747b0', '#0c6872', '#ab284d'])
    unit, pad = 24, 240
    size = n*unit+2*pad
    template = Path(__file__).resolve().parent.parent/'assets/particle-locators.json'
    finders = json.loads(template.read_text(encoding='utf8'))['finders']

    def finder(r, c):
        return (r < 7 and c < 7) or (r < 7 and c >= n-7) or (r >= n-7 and c < 7)

    def path(points):
        return 'M'+'L'.join(f'{x:.5f},{y:.5f}' for x, y in points)+'Z'

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
           f'viewBox="0 0 {size} {size}">',
           '<metadata>Information guide; material rendering and full-file verification required.</metadata>',
           '<defs><filter id="carrier"><feGaussianBlur stdDeviation="3"/></filter></defs>',
           f'<rect width="{size}" height="{size}" fill="{bg}"/>']
    carrier = [f'<circle cx="{pad+(c+.5)*unit}" cy="{pad+(r+.5)*unit}" r="14.4"/>'
               for r in range(n) for c in range(n) if matrix[r][c] and not finder(r, c)]
    svg.append(f'<g fill="{palette[0]}" opacity="{args.density}" '
               f'filter="url(#carrier)">{"".join(carrier)}</g>')
    cells = [(r, c) for r in range(n) for c in range(n) if matrix[r][c] and not finder(r, c)]
    rng.shuffle(cells)
    used, groups = set(), 0
    for r, c in cells:
        if (r, c) in used:
            continue
        w = h = 1
        sizes = [(2, 1), (1, 2), (2, 2), (3, 1), (1, 3)]
        rng.shuffle(sizes)
        if rng.random() < args.group_probability:
            for ww, hh in sizes:
                if r+hh <= n and c+ww <= n and all(
                        matrix[rr][cc] and not finder(rr, cc) and (rr, cc) not in used
                        for rr in range(r, r+hh) for cc in range(c, c+ww)):
                    w, h = ww, hh
                    break
        used.update((rr, cc) for rr in range(r, r+h) for cc in range(c, c+w))
        groups += int(w*h > 1)
        cx, cy = pad+(c+w/2)*unit, pad+(r+h/2)*unit
        if w == h == 1:
            rx = unit*(.13+rng.random()*.32)
            ry = rx*(.65+rng.random()*.5)
            cx += (rng.random()-.5)*unit/12
            cy += (rng.random()-.5)*unit/12
        else:
            rx = unit*(w*.5-(.12 if h == 1 else .03))
            ry = unit*(h*.5-(.12 if w == 1 else .03))
        ink = rng.choice(palette)
        if args.shape == 'cavities':
            svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{ink}"/>')
        else:
            points = []
            for k in range(19):
                theta = k*2*math.pi/19
                radius = .92+rng.random()*.13
                points.append((cx+rx*radius*math.cos(theta), cy+ry*radius*math.sin(theta)))
            svg.append(f'<path d="{path(points)}" fill="{ink}"/>')
        for rr in range(r, r+h):
            for cc in range(c, c+w):
                for _ in range(rng.randrange(9, 27)):
                    x, y = pad+(cc+rng.random())*unit, pad+(rr+rng.random())*unit
                    radius = .35+rng.random()*1.6
                    svg.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{rng.choice(palette)}"/>')
    # Keep these calibrated function contours upright. Randomizing them impaired detection.
    for (r, c), layers in zip([(0, 0), (0, n-7), (n-7, 0)], finders):
        for layer in layers:
            opacity = min(1, max(0, (220-layer['level'])/150))
            if not opacity:
                continue
            alpha = (255-math.floor(255*(1-opacity)+116*opacity+.5))/139
            d = ' '.join(path([(pad+(c+x)*unit, pad+(r+y)*unit) for x, y in poly])
                         for poly in layer['polygons'])
            svg.append(f'<path d="{d}" fill="{bg}" fill-rule="evenodd"/>')
            svg.append(f'<path d="{d}" fill="{palette[0]}" opacity="{alpha:.8f}" fill-rule="evenodd"/>')
    svg.append('</svg>')
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(''.join(svg), encoding='utf8')
    print(json.dumps({'file': str(out), 'seed': seed, 'modules': n, 'merged_groups': groups,
                      'status': 'guide-only-requires-material-rendering-and-verification'}))


if __name__ == '__main__':
    main()
