"""Transcribe exact source media using the configured ElevenLabs env file."""
import argparse
import os
import hashlib
import json
import math
import mimetypes
from pathlib import Path

DEFAULT_ENV = Path(os.environ.get('ELEVENLABS_ENV_FILE', '.env'))

def load_key(path):
    configured = os.environ.get("ELEVENLABS_API_KEY", "")
    if configured:
        return configured
    if not path.exists():
        raise ValueError("Set ELEVENLABS_API_KEY or provide --env")
    for raw in path.read_text(encoding='utf-8-sig').splitlines():
        line = raw.strip()
        if line.startswith('ELEVENLABS_API_KEY='):
            value = line.split('=', 1)[1].strip().strip('\"\'')
            if value.startswith('sk_') and len(value) > 10:
                return value
            raise ValueError('ELEVENLABS_API_KEY must contain an actual API key, not a key ID')
    raise ValueError('ELEVENLABS_API_KEY is missing from the selected env file')

def validate(payload):
    words = [w for w in payload.get('words', []) if w.get('type') == 'word']
    if not payload.get('text') or not words:
        raise ValueError('Response has no transcript or word timestamps')
    for w in words:
        a, b = w.get('start'), w.get('end')
        if not all(isinstance(t, (int, float)) and math.isfinite(t) for t in (a, b)) or a < 0 or b < a:
            raise ValueError('Invalid word timestamps in response')
    return {'words': len(words), 'speech_tail': max(w['end'] for w in words), 'speakers': len({w.get('speaker_id') for w in words if w.get('speaker_id')})}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--env', type=Path, default=DEFAULT_ENV)
    p.add_argument('--audio', type=Path)
    p.add_argument('--output', type=Path)
    p.add_argument('--language', default='ko')
    p.add_argument('--model', choices=['scribe_v2', 'scribe_v1'], default='scribe_v2')
    p.add_argument('--check', action='store_true', help='Check configuration without an API call')
    p.add_argument('--validate-json', type=Path, help='Validate an existing response without an API call')
    args = p.parse_args()
    if args.validate_json:
        print(json.dumps(validate(json.loads(args.validate_json.read_text(encoding='utf-8')))))
        return
    key = load_key(args.env)
    import httpx
    if args.check:
        print(json.dumps({'status': 'pass', 'env_key_present': True, 'key_format_valid': True, 'httpx_available': True, 'api_called': False}))
        return
    if not args.audio or not args.output:
        p.error('--audio and --output are required')
    if args.output.exists():
        p.error('Output already exists; reuse it or select a new output path')
    with args.audio.open('rb') as stream, httpx.Client(timeout=httpx.Timeout(connect=30, read=1800, write=1800, pool=30)) as client:
        response = client.post('https://api.elevenlabs.io/v1/speech-to-text', headers={'xi-api-key': key}, files={'file': (args.audio.name, stream, mimetypes.guess_type(args.audio.name)[0] or 'application/octet-stream')}, data={'model_id': args.model, 'language_code': args.language, 'diarize': 'true', 'timestamps_granularity': 'word', 'tag_audio_events': 'false', 'no_verbatim': 'false'})
    if response.status_code != 200:
        raise RuntimeError(f'ElevenLabs HTTP {response.status_code}: {response.text.replace(key, "[REDACTED]")[:800]}')
    payload = response.json()
    summary = validate(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_suffix(args.output.suffix + '.tmp')
    temp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    temp.replace(args.output)
    summary.update(status='pass', model=args.model, output_sha256=hashlib.sha256(args.output.read_bytes()).hexdigest())
    print(json.dumps(summary))

if __name__ == '__main__':
    main()
