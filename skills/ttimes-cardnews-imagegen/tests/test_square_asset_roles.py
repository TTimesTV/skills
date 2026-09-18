import importlib.util
from pathlib import Path
import pytest

SCRIPT = Path(__file__).parents[1] / 'scripts' / 'validate_square_carousel_roles.py'
spec = importlib.util.spec_from_file_location('roles', SCRIPT)
roles = importlib.util.module_from_spec(spec)
spec.loader.exec_module(roles)


def test_rejects_list_image_as_closing_background(tmp_path: Path):
    source = tmp_path / 'episode_list.jpg'; source.write_bytes(b'same')
    with pytest.raises(ValueError, match='closing background must differ'):
        roles.validate_roles(source, source, [])


def test_accepts_distinct_closing_background(tmp_path: Path):
    source = tmp_path / 'episode_list.jpg'; source.write_bytes(b'cover')
    closing = tmp_path / 'closing_background.png'; closing.write_bytes(b'closing')
    roles.validate_roles(source, closing, [])


def test_rejects_list_hash_in_body(tmp_path: Path):
    source = tmp_path / 'episode_list.jpg'; source.write_bytes(b'same')
    body = tmp_path / 'body.png'; body.write_bytes(b'same')
    with pytest.raises(ValueError, match='cover-only'):
        roles.validate_roles(source, tmp_path / 'closing.png', [body])
