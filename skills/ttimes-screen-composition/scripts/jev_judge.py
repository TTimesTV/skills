"""Cached JEV choice judgments; never logs credentials or HTTP response bodies."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

ENDPOINT = 'https://api.typesafe.ai/v1/systemone'
ENV = Path(os.environ.get('JEV_ENV_FILE', '.env'))

def key():
    value = os.environ.get('TYPESAFE_API_KEY', '')
    if not value and ENV.exists():
        for line in ENV.read_text(encoding='utf-8-sig').splitlines():
            name, sep, content = line.strip().partition('=')
            if sep and name.strip() == 'TYPESAFE_API_KEY':
                value = content.strip().strip('\"').strip("'")
                break
    if not value:
        raise RuntimeError('TYPESAFE_API_KEY missing')
    return value

def call(payload):
    request = urllib.request.Request(ENDPOINT,
        data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
        headers={'Authorization': 'Bearer ' + key(), 'Content-Type': 'application/json'}, method='POST')
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                result = json.load(response)
            if not isinstance(result.get('answers'), dict) or set(payload['questions']) - set(result['answers']):
                raise RuntimeError('JEV response missing requested answers')
            return result
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise RuntimeError('JEV HTTP ' + str(error.code)) from None
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise RuntimeError('JEV connection/timeout failure') from None
        time.sleep(2 ** attempt)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    requests = json.loads(args.input.read_text(encoding='utf-8-sig'))
    assert isinstance(requests, list) and requests, 'Input must be a nonempty payload list'
    args.output_dir.mkdir(parents=True, exist_ok=True)
    log = {'status': 'running', 'calls': 0, 'cache_hits': 0, 'usage_new_calls': {}, 'batches': []}
    try:
        for i, payload in enumerate(requests):
            assert payload.get('model') and payload.get('state') and payload.get('questions')
            digest = hashlib.sha256(json.dumps([ENDPOINT, payload], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
            path = args.output_dir / (digest + '.json')
            cached = path.exists()
            result = json.loads(path.read_text(encoding='utf-8')) if cached else call(payload)
            if set(payload['questions']) - set(result.get('answers', {})):
                raise RuntimeError('Cached response missing requested answers')
            if not cached:
                path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
                log['calls'] += 1
                for name, value in result.get('usage', {}).items():
                    if isinstance(value, (int, float)):
                        log['usage_new_calls'][name] = log['usage_new_calls'].get(name, 0) + value
            else:
                log['cache_hits'] += 1
            log['batches'].append({'index': i, 'sha256': digest, 'cached': cached, 'model': result.get('model'), 'usage': result.get('usage')})
            (args.output_dir / 'run.json').write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding='utf-8')
            print('batch', i + 1, 'cache' if cached else 'pass', flush=True)
        log['status'] = 'pass'
    except Exception as error:
        log['status'] = 'fail'
        log['error'] = str(error) if isinstance(error, (RuntimeError, AssertionError)) else type(error).__name__
        raise
    finally:
        (args.output_dir / 'run.json').write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in log.items() if k != 'batches'}, ensure_ascii=False))

if __name__ == '__main__':
    main()
