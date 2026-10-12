#!/usr/bin/env python3
"""Capture exact QR bytes; export scan files; qualify complete creative images.
Never print payload content. Probe transformations alone are not deliverables.
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import sys

import cv2
import numpy as np
from PIL import Image, ImageOps
import segno
import zxingcpp


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load_image(path):
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)
        if im.mode in ('RGBA', 'LA') or 'transparency' in im.info:
            rgba = im.convert('RGBA')
            base = Image.new('RGBA', rgba.size, 'white')
            base.alpha_composite(rgba)
            return base.convert('RGB')
        return im.convert('RGB')


def decode(im):
    records, errors = [], []
    try:
        # PIL is RGB-aware; ZXing ndarray input expects BGR, not RGB.
        for result in zxingcpp.read_barcodes(im):
            if result.format == zxingcpp.BarcodeFormat.QRCode and result.bytes:
                records.append(('ZXing-C++', bytes(result.bytes), 'raw-bytes'))
    except Exception as exc:
        errors.append({'engine': 'ZXing-C++', 'error_type': type(exc).__name__})
    try:
        bgr = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)
        texts, _ = cv2.wechat_qrcode_WeChatQRCode().detectAndDecode(bgr)
        for text in texts:
            if text and text.isascii():
                records.append(('WeChatCV', text.encode('ascii'), 'ascii-text'))
            elif text:
                errors.append({'engine': 'WeChatCV', 'error_type': 'non-ascii-text-only'})
    except Exception as exc:
        errors.append({'engine': 'WeChatCV', 'error_type': type(exc).__name__})
    return records, errors


def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf8')


def result_summary(im, expected, label, transformed=False):
    records, errors = decode(im)
    matches = sorted({engine for engine, payload, _ in records if payload == expected})
    conflicts = sorted({sha(payload) for _, payload, _ in records if payload != expected})
    return {'file': label, 'width': im.width, 'height': im.height, 'full_image': True,
            'diagnostic_transform': transformed, 'matches_original': bool(matches),
            'usable': bool(matches) and not conflicts, 'matching_engines': matches,
            'conflicting_payload_sha256': conflicts,
            'decoded_payload_sha256': sorted({sha(p) for _, p, _ in records}),
            'engine_errors': errors}


def capture(args):
    records, errors = decode(load_image(args.source))
    payloads = {data for _, data, _ in records}
    if len(payloads) != 1:
        print(json.dumps({'status': 'blocked', 'reason': 'multiple-payloads' if payloads else 'no-reliable-payload',
                          'distinct_payloads': len(payloads), 'engine_errors': errors}))
        return 2
    payload = payloads.pop()
    raw = any(kind == 'raw-bytes' for _, data, kind in records if data == payload)
    minimum = segno.make(payload, error=args.error, mode='byte', micro=False, boost_error=False)
    version = max(args.min_version, minimum.version)
    qr = segno.make(payload, error=args.error, mode='byte', version=version,
                    micro=False, boost_error=False)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    payload_path = out / 'payload.bin'
    fd = os.open(payload_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'wb') as handle:
        handle.write(payload)
    os.chmod(payload_path, 0o600)
    matrix = [list(row) for row in qr.matrix]
    write_json(out / 'matrix.json', {'version': version, 'error': qr.error, 'mask': qr.mask,
                                    'payload_sha256': sha(payload), 'matrix': matrix})
    report = {'status': 'captured', 'payload_bytes': len(payload), 'payload_sha256': sha(payload),
              'source_engines': sorted({e for e, _, _ in records}),
              'byte_evidence': 'raw-bytes' if raw else 'ascii-text', 'qr_version': version,
              'error': qr.error, 'modules': len(matrix), 'opencv_version': cv2.__version__}
    write_json(out / 'source-report.json', report)
    print(json.dumps(report, ensure_ascii=False))
    return 0


def verify(args):
    expected = Path(args.payload).read_bytes()
    if not expected:
        raise ValueError('Empty payload unsupported')
    results = [result_summary(load_image(p), expected, str(p)) for p in args.images]
    report = {'source_payload_sha256': sha(expected), 'opencv_version': cv2.__version__,
              'results': results, 'all_usable': all(r['usable'] for r in results)}
    if args.report:
        write_json(args.report, report)
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report['all_usable'] else 2


def reencode(args):
    payload = Path(args.payload).read_bytes()
    if not payload:
        raise ValueError('Empty payload unsupported')
    minimum = segno.make(payload, error=args.error, mode='byte', micro=False, boost_error=False)
    version = max(args.min_version, minimum.version)
    qr = segno.make(payload, error=args.error, mode='byte', version=version,
                    mask=args.mask, micro=False, boost_error=False)
    write_json(args.out, {'version': qr.version, 'error': qr.error, 'mask': qr.mask,
                         'payload_sha256': sha(payload), 'matrix': [list(row) for row in qr.matrix]})
    print(json.dumps({'status': 'reencoded', 'file': str(args.out), 'version': qr.version,
                      'error': qr.error, 'mask': qr.mask, 'payload_sha256': sha(payload)}))
    return 0


def probe(args):
    expected = Path(args.payload).read_bytes()
    if not expected:
        raise ValueError('Empty payload unsupported')
    im = load_image(args.image)
    results = [result_summary(im, expected, str(args.image))]
    for width in args.widths:
        if width < 64:
            raise ValueError('Probe width must be at least 64')
        height = max(1, round(im.height * width / im.width))
        scaled = im.resize((width, height), Image.Resampling.LANCZOS)
        results.append(result_summary(scaled, expected, f'{width}px PNG diagnostic', True))
        for quality in args.qualities:
            if not 1 <= quality <= 100:
                raise ValueError('JPEG quality must be 1..100')
            buffer = io.BytesIO()
            scaled.save(buffer, format='JPEG', quality=quality)
            buffer.seek(0)
            with Image.open(buffer) as jpeg:
                results.append(result_summary(jpeg.convert('RGB'), expected,
                                               f'{width}px JPEG q{quality} diagnostic', True))
    report = {'source_payload_sha256': sha(expected), 'opencv_version': cv2.__version__,
              'diagnostics_only': True, 'results': results,
              'passing_sizes': sorted({r['width'] for r in results if r['usable']})}
    if args.report:
        write_json(args.report, report)
    print(json.dumps(report, ensure_ascii=False))
    return 0 if any(r['usable'] for r in results) else 2


def export_scan(args):
    """Mechanically export with the same resampler used by probe/qualify."""
    source, output = Path(args.image), Path(args.out)
    if source.resolve() == output.resolve():
        raise ValueError('Use a separate output path')
    im = load_image(source)
    if args.width < 64 or args.width > im.width:
        raise ValueError('Scan export width must be >=64 and no greater than the source width')
    height = max(1, round(im.height * args.width / im.width))
    output.parent.mkdir(parents=True, exist_ok=True)
    im.resize((args.width, height), Image.Resampling.LANCZOS).save(output, format='PNG')
    print(json.dumps({'file': str(output), 'width': args.width, 'height': height,
                      'status': 'exported-requires-qualification'}, ensure_ascii=False))
    return 0


def qualify(args):
    """Require the actual file AND every preselected display variant to pass.

    This is a software gate, never evidence of a physical phone/app test.
    No transformed or cropped image can substitute for the actual file.
    """
    expected = Path(args.payload).read_bytes()
    if not expected:
        raise ValueError('Empty payload unsupported')
    widths = list(dict.fromkeys(args.widths))
    qualities = list(dict.fromkeys(args.qualities))
    if len(widths) < 2 or any(w < 64 for w in widths):
        raise ValueError('Select at least two display widths of 64px or more')
    if not qualities or any(not 1 <= q <= 100 for q in qualities):
        raise ValueError('Select at least one JPEG quality in 1..100')
    files = []
    for filename in args.images:
        path = Path(filename)
        im = load_image(path)
        actual = result_summary(im, expected, str(path))
        variants = []
        for width in widths:
            height = max(1, round(im.height * width / im.width))
            scaled = im.resize((width, height), Image.Resampling.LANCZOS)
            variants.append(result_summary(scaled, expected, f'{width}px PNG diagnostic', True))
            for quality in qualities:
                buffer = io.BytesIO()
                scaled.save(buffer, format='JPEG', quality=quality)
                buffer.seek(0)
                with Image.open(buffer) as jpeg:
                    variants.append(result_summary(jpeg.convert('RGB'), expected,
                                                   f'{width}px JPEG q{quality} diagnostic', True))
        failures = [r['file'] for r in [actual, *variants] if not r['usable']]
        if im.width < max(widths):
            failures.append('actual-file-smaller-than-required-display-width')
        accepted = not failures
        files.append({'file': str(path), 'file_sha256': sha(path.read_bytes()),
                      'software_gate_passed': accepted,
                      'qualification': 'software-verified' if accepted else 'draft',
                      'phone_scan_status': 'unverified', 'actual_file': actual,
                      'display_diagnostics': variants, 'failed_requirements': failures})
    report = {'source_payload_sha256': sha(expected), 'opencv_version': cv2.__version__,
              'gate': 'actual-file-and-all-selected-display-variants',
              'required_widths': widths, 'required_jpeg_qualities': qualities,
              'physical_phone_test_performed': False, 'results': files,
              'all_qualified': all(f['software_gate_passed'] for f in files)}
    write_json(args.report, report)
    print(json.dumps({'all_qualified': report['all_qualified'],
                      'physical_phone_test_performed': False,
                      'results': [{k: f[k] for k in ('file', 'qualification',
                                   'phone_scan_status', 'failed_requirements')} for f in files]},
                     ensure_ascii=False))
    return 0 if report['all_qualified'] else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    cap = sub.add_parser('capture')
    cap.add_argument('--source', required=True)
    cap.add_argument('--out', required=True)
    cap.add_argument('--error', choices=['L', 'M', 'Q', 'H'], default='M')
    cap.add_argument('--min-version', type=int, choices=range(1, 41), default=5)
    cap.set_defaults(run=capture)
    variant = sub.add_parser('reencode')
    variant.add_argument('--payload', required=True)
    variant.add_argument('--out', required=True)
    variant.add_argument('--error', choices=['L', 'M', 'Q', 'H'], default='M')
    variant.add_argument('--min-version', type=int, choices=range(1, 41), default=5)
    variant.add_argument('--mask', type=int, choices=range(8))
    variant.set_defaults(run=reencode)
    check = sub.add_parser('verify')
    check.add_argument('--payload', required=True)
    check.add_argument('--images', nargs='+', required=True)
    check.add_argument('--report')
    check.set_defaults(run=verify)
    diag = sub.add_parser('probe')
    diag.add_argument('--payload', required=True)
    diag.add_argument('--image', required=True)
    diag.add_argument('--widths', nargs='+', type=int, default=[320, 480, 640, 800])
    diag.add_argument('--qualities', nargs='+', type=int, default=[85, 70])
    diag.add_argument('--report')
    diag.set_defaults(run=probe)
    scan_export = sub.add_parser('export')
    scan_export.add_argument('--image', required=True)
    scan_export.add_argument('--out', required=True)
    scan_export.add_argument('--width', type=int, required=True)
    scan_export.set_defaults(run=export_scan)
    gate = sub.add_parser('qualify')
    gate.add_argument('--payload', required=True)
    gate.add_argument('--images', nargs='+', required=True)
    gate.add_argument('--widths', nargs='+', type=int, default=[480, 640, 800])
    gate.add_argument('--qualities', nargs='+', type=int, default=[85])
    gate.add_argument('--report', required=True)
    gate.set_defaults(run=qualify)
    args = parser.parse_args()
    try:
        return args.run(args)
    except Exception as exc:
        print(json.dumps({'status': 'error', 'error_type': type(exc).__name__}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
