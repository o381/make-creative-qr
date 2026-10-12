#!/usr/bin/env python3
"""Check current file integrity against full software qualification evidence.

This read-only check does not decode again, approve appearance, or prove a
phone test. Run qualify first and check again immediately before delivery.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import sys

from PIL import Image, ImageOps


def digest(data):
    return hashlib.sha256(data).hexdigest()


def usable(record, expected, transformed):
    return (record.get('usable') is True
            and record.get('matches_original') is True
            and record.get('full_image') is True
            and record.get('diagnostic_transform') is transformed
            and bool(record.get('matching_engines'))
            and record.get('conflicting_payload_sha256') == []
            and record.get('decoded_payload_sha256') == [expected])


def check(report, path, expected, widths, qualities):
    if report.get('gate') != 'actual-file-and-all-selected-display-variants':
        raise ValueError('Not a full qualification report')
    if report.get('source_payload_sha256') != expected:
        raise ValueError('Report belongs to a different source payload')
    if not set(widths).issubset(report.get('required_widths', [])):
        raise ValueError('Required display widths were not tested')
    if not set(qualities).issubset(report.get('required_jpeg_qualities', [])):
        raise ValueError('Required JPEG qualities were not tested')
    entries = [r for r in report.get('results', [])
               if Path(r.get('file', '')).resolve() == path.resolve()]
    if len(entries) != 1:
        raise ValueError('Actual delivery path is absent or ambiguous')
    entry = entries[0]
    if entry.get('software_gate_passed') is not True or entry.get('failed_requirements') != []:
        raise ValueError('Actual file did not pass qualification')
    data = path.read_bytes()
    if digest(data) != entry.get('file_sha256'):
        raise ValueError('File changed after qualification')
    with Image.open(io.BytesIO(data)) as image:
        image.verify()
    with Image.open(io.BytesIO(data)) as image:
        image.load()
        image = ImageOps.exif_transpose(image)
        size = image.size
    actual = entry.get('actual_file', {})
    if not usable(actual, expected, False) or size != (actual.get('width'), actual.get('height')):
        raise ValueError('Missing or inconsistent actual-file evidence')
    if size[0] < max(widths):
        raise ValueError('Actual delivery file is too small')
    variants = entry.get('display_diagnostics', [])
    for width in widths:
        labels = [f'{width}px PNG diagnostic']
        labels += [f'{width}px JPEG q{quality} diagnostic' for quality in qualities]
        height = max(1, round(size[1] * width / size[0]))
        for label in labels:
            matches = [r for r in variants if r.get('file') == label]
            if len(matches) != 1 or not usable(matches[0], expected, True):
                raise ValueError('Missing or failed display evidence: ' + label)
            if (matches[0].get('width'), matches[0].get('height')) != (width, height):
                raise ValueError('Inconsistent display dimensions: ' + label)
    if path.read_bytes() != data:
        raise ValueError('File changed during integrity check')
    return {'file': str(path), 'status': 'software-evidence-current',
            'file_sha256': digest(data), 'appearance_approved': False,
            'physical_phone_test_performed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--payload', required=True)
    parser.add_argument('--report', required=True)
    parser.add_argument('--images', nargs='+', required=True)
    parser.add_argument('--widths', nargs='+', type=int, default=[480, 640, 800])
    parser.add_argument('--qualities', nargs='+', type=int, default=[85])
    args = parser.parse_args()
    try:
        if not args.widths or any(w < 64 for w in args.widths):
            raise ValueError('Invalid required widths')
        if not args.qualities or any(not 1 <= q <= 100 for q in args.qualities):
            raise ValueError('Invalid required qualities')
        payload = Path(args.payload).read_bytes()
        if not payload:
            raise ValueError('Empty payload')
        report = json.loads(Path(args.report).read_text(encoding='utf8'))
        results = [check(report, Path(p), digest(payload), args.widths, args.qualities)
                   for p in args.images]
        print(json.dumps({'all_current': True, 'results': results}, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({'all_current': False, 'reason': str(exc)}, ensure_ascii=False),
              file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
