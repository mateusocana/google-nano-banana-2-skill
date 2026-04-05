#!/usr/bin/env python3
import argparse
import base64
import json
import mimetypes
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime

DEFAULT_MODEL = os.environ.get('GOOGLE_NANO_BANANA_MODEL', 'gemini-3.1-flash-image-preview')
API_KEY = os.environ.get('GEMINI_API_KEY')
API_BASE = os.environ.get('GOOGLE_GEMINI_API_BASE', 'https://generativelanguage.googleapis.com')


class ApiError(RuntimeError):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def guess_mime(path):
    mt, _ = mimetypes.guess_type(path)
    return mt or 'application/octet-stream'


def inline_part(path):
    p = pathlib.Path(path)
    if not p.exists():
        raise FileNotFoundError(f'Image not found: {path}')
    if not p.is_file():
        raise IsADirectoryError(f'Image path is not a file: {path}')
    data = p.read_bytes()
    if len(data) == 0:
        raise ValueError(f'Image file is empty: {path}')
    return {
        'inlineData': {
            'mimeType': guess_mime(path),
            'data': base64.b64encode(data).decode('ascii')
        }
    }


def text_part(text):
    text = (text or '').strip()
    if not text:
        raise ValueError('Prompt cannot be empty')
    return {'text': text}


def make_request_url(model):
    return f'{API_BASE}/v1beta/models/{model}:generateContent?key={API_KEY}'


def parse_error_body(exc):
    body = getattr(exc, 'read', None)
    if body is None:
        return None
    try:
        raw = body().decode('utf-8', errors='replace')
        data = json.loads(raw)
        return data.get('error', {}).get('message') or raw
    except Exception:
        try:
            return body().decode('utf-8', errors='replace')
        except Exception:
            return None


def request_json(url, payload, timeout=180):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST',
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        message = parse_error_body(e) or f'HTTP {e.code}'
        raise ApiError(e.code, message) from e
    except Exception as e:
        raise ApiError(None, str(e)) from e


def should_retry(status):
    return status in {429, 500, 502, 503, 504}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prompt', required=True)
    ap.add_argument('--image', action='append', default=[])
    ap.add_argument('--outdir', default='/srv/obsidian-sync/openclaw/generated/google-nano-banana-2')
    ap.add_argument('--model', default=DEFAULT_MODEL)
    ap.add_argument('--retries', type=int, default=3)
    ap.add_argument('--retry-delay', type=float, default=2.5)
    args = ap.parse_args()

    if not API_KEY:
        print('Missing GEMINI_API_KEY', file=sys.stderr)
        sys.exit(2)

    if len(args.image) > 4:
        print('At most 4 input images are supported by this script.', file=sys.stderr)
        sys.exit(2)

    parts = [text_part(args.prompt)]
    for img in args.image:
        parts.append(inline_part(img))

    payload = {
        'contents': [{'role': 'user', 'parts': parts}],
        'generationConfig': {'responseModalities': ['TEXT', 'IMAGE']}
    }

    url = make_request_url(args.model)
    last_error = None
    for attempt in range(args.retries + 1):
        try:
            body = request_json(url, payload)
            break
        except ApiError as e:
            last_error = e
            if e.status == 429 and attempt < args.retries:
                sleep_for = args.retry_delay * (attempt + 1)
                print(f'Rate limited, retrying in {sleep_for:.1f}s...', file=sys.stderr)
                time.sleep(sleep_for)
                continue
            if e.status is not None and should_retry(e.status) and attempt < args.retries:
                sleep_for = args.retry_delay * (attempt + 1)
                print(f'API error {e.status}, retrying in {sleep_for:.1f}s...', file=sys.stderr)
                time.sleep(sleep_for)
                continue
            print(f'API request failed: {e.message}', file=sys.stderr)
            sys.exit(1)
    else:
        print(f'API request failed: {last_error.message if last_error else "unknown error"}', file=sys.stderr)
        sys.exit(1)

    outdir = pathlib.Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
    saved = []

    candidates = body.get('candidates', [])
    for cand in candidates:
        content = cand.get('content', {})
        for idx, part in enumerate(content.get('parts', []), start=1):
            inline = part.get('inlineData')
            if inline and inline.get('data'):
                mime = inline.get('mimeType', 'image/png')
                ext = mimetypes.guess_extension(mime) or '.bin'
                path = outdir / f'{stamp}-{idx}{ext}'
                path.write_bytes(base64.b64decode(inline['data']))
                saved.append(str(path))
            elif part.get('text'):
                print(part['text'])

    if not saved:
        print(json.dumps(body, ensure_ascii=False, indent=2))
        print('No image output returned', file=sys.stderr)
        sys.exit(1)

    for p in saved:
        print(p)


if __name__ == '__main__':
    main()
