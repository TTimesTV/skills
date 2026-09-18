from hashlib import sha256
from pathlib import Path

ASSETS=Path(__file__).resolve().parents[1] / 'references' / 'assets'


def digest(name):
    return sha256((ASSETS/name).read_bytes()).hexdigest()


def test_approved_lee_cover_is_locked():
    assert digest('approved-lee-junghak-ai-slop-cover.png') == '2e8c1ab7cf5a1eadb1f2905f7e368bc53f19f46d344fdc61350f05b1965c717d'


def test_approved_park_cover_is_locked():
    assert digest('approved-park-tech-talk-mlcc-fcbga-cover.png') == '70551267b29eb731490c1eb056bb5ca4f06e6f2ebf6a8cfc913380b5d27e1d07'
