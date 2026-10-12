#!/usr/bin/env python3
"""Build an exact QR information guide as SVG, not final raster artwork."""
import argparse
import json
import math
from pathlib import Path
import re
from xml.sax.saxutils import escape


def color(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
        raise argparse.ArgumentTypeError('Use six-digit hex colors')
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--matrix', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--shape', choices=['grains', 'shards'], default='grains')
    p.add_argument('--background', type=color, default='#fff8de')
    p.add_argument('--palette', type=color, nargs='+', default=['#2834c8', '#a91bc4', '#d51781', '#7232c5'])
    p.add_argument('--density', type=float, default=.2)
    p.add_argument('--seed', type=int, default=45231)
    p.add_argument('--unit', type=float, default=24)
    args = p.parse_args()
    if args.unit < 4 or not 0 <= args.density <= .5:
        raise ValueError('unit must be >=4 and density must be 0..0.5')
    m = json.loads(Path(args.matrix).read_text(encoding='utf8'))['matrix']
    n = len(m)
    if n < 21 or n > 177 or (n-21) % 4 or any(len(row) != n for row in m):
        raise ValueError('Invalid standard QR matrix dimensions')
    if any(v not in (0, 1) for row in m for v in row):
        raise ValueError('Matrix must contain binary modules')
    template = Path(__file__).resolve().parent.parent/'assets/particle-locators.json'
    finders = json.loads(template.read_text(encoding='utf8'))['finders']
    u, pad = args.unit, args.unit*6
    size = n*u+pad*2
    state = args.seed & 0xffffffff

    def rand():
        nonlocal state
        state = (state*1664525+1013904223) & 0xffffffff
        return state/4294967296

    def finder(r, c):
        return (r < 7 and c < 7) or (r < 7 and c >= n-7) or (r >= n-7 and c < 7)

    def num(v):
        return f'{v:.5f}'

    def path(points):
        return 'M'+'L'.join(f'{num(x)},{num(y)}' for x, y in points)+'Z'

    stops = ''.join(f'<stop offset="{i/max(1,len(args.palette)-1):.6f}" stop-color="{c}"/>'
                    for i,c in enumerate(args.palette))
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{num(size)}" height="{num(size)}" '
           f'viewBox="0 0 {num(size)} {num(size)}">',
           '<metadata>Exact information guide; requires material rendering and full-image verification.</metadata>',
           f'<defs><linearGradient id="ink" gradientUnits="userSpaceOnUse" '
           f'x1="{num(pad+26*u/24)}" y1="{num(pad-14*u/24)}" '
           f'x2="{num(size-pad-52*u/24)}" y2="{num(size-pad-42*u/24)}">{stops}</linearGradient>'
           f'<filter id="carrier"><feGaussianBlur stdDeviation="{num(u/8)}"/></filter></defs>',
           f'<rect width="{num(size)}" height="{num(size)}" fill="{args.background}"/>']
    carrier = []
    for r in range(n):
        for c in range(n):
            if m[r][c] and not finder(r,c):
                carrier.append(f'<circle cx="{num(pad+(c+.5)*u)}" cy="{num(pad+(r+.5)*u)}" r="{num(u*.6)}"/>')
    svg.append(f'<g fill="url(#ink)" opacity="{args.density}" filter="url(#carrier)">{"".join(carrier)}</g>')
    svg.append('<g fill="url(#ink)">')
    used = set()
    for r in range(n):
        for c in range(n):
            if finder(r,c) or not m[r][c] or (r,c) in used:
                continue
            x,y = pad+c*u,pad+r*u
            merge = (r<n-1 and c<n-1 and r>8 and c>8 and
                     m[r+1][c] and m[r][c+1] and m[r+1][c+1] and
                     not finder(r+1,c+1) and
                     not any((r+a,c+b) in used for a in range(2) for b in range(2)))
            if merge:
                cx,cy,rad = x+u,y+u,u*.97
                points=[]
                for k in range(24):
                    a=k*math.pi/12
                    rr=rad*(.95+rand()*.08)
                    points.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
                svg.append(f'<path d="{path(points)}"/>')
                used.update((r+a,c+b) for a in range(2) for b in range(2))
            else:
                rr=u*(.12+rand()*.28)
                cx,cy=x+u/2+(rand()-.5)*2*u/24,y+u/2+(rand()-.5)*2*u/24
                ry=rr*(.7+rand()*.35)
                angle=rand()*180
                if args.shape == 'grains':
                    svg.append(f'<ellipse cx="{num(cx)}" cy="{num(cy)}" rx="{num(rr)}" ry="{num(ry)}" '
                               f'transform="rotate({num(angle)},{num(cx)},{num(cy)})"/>')
                else:
                    a=angle*math.pi/180
                    points=[(cx+rr*math.cos(a+k*math.pi/2),cy+ry*math.sin(a+k*math.pi/2)) for k in range(4)]
                    svg.append(f'<path d="{path(points)}"/>')
            for _ in range(12):
                px,py,rad=x+rand()*u,y+rand()*u,(.5+rand()*1.4)*u/24
                svg.append(f'<ellipse cx="{num(px)}" cy="{num(py)}" rx="{num(rad)}" ry="{num(rad*.8)}"/>')
    svg.append('</g>')
    for (r,c),layers in zip([(0,0),(0,n-7),(n-7,0)],finders):
        for layer in layers:
            a=min(1,max(0,(220-layer['level'])/150))
            if not a:
                continue
            alpha=(255-math.floor(255*(1-a)+116*a+.5))/139
            d=' '.join(path([(pad+(c+x)*u,pad+(r+y)*u) for x,y in poly]) for poly in layer['polygons'])
            svg.append(f'<path fill="{args.background}" fill-rule="evenodd" d="{escape(d)}"/>')
            svg.append(f'<path fill="url(#ink)" opacity="{alpha:.8f}" fill-rule="evenodd" d="{escape(d)}"/>')
    svg.append('</svg>')
    out=Path(args.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(''.join(svg),encoding='utf8')
    print(json.dumps({'file':str(out),'status':'guide-only-requires-material-rendering-and-verification',
                      'modules':n,'shape':args.shape,'native_size':size}))


if __name__ == '__main__':
    main()
