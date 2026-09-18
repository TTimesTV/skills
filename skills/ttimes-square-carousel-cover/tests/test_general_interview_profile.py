import json
import importlib.util
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
PROFILE = SKILL_DIR / 'references' / 'general-interview-cover-profile.json'
SCRIPT = SKILL_DIR / 'scripts' / 'build_cover.py'
spec = importlib.util.spec_from_file_location('build_cover', SCRIPT)
build_cover = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_cover)


def test_general_interview_cover_forbids_title_plates():
    profile = json.loads(PROFILE.read_text(encoding='utf-8'))
    assert profile['visual_source'] == 'exact_article_list_image'
    assert profile['title_plate'] is False
    assert profile['rounded_panel'] is False
    assert profile['guest_profile'] is False
    assert profile['source_label'] is False
    assert profile['cover_title_px'] == 80
    assert profile['cover_logo'] == {
        'position': 'upper-right', 'x': 836, 'y': 55, 'width': 176
    }


def test_general_interview_rejects_box_lines():
    try:
        build_cover.validate_profile('general-interview', [2])
    except ValueError as exc:
        assert 'title plates are forbidden' in str(exc)
    else:
        raise AssertionError('expected rejection')


def test_general_interview_accepts_gradient_only():
    build_cover.validate_profile('general-interview', [])


def test_all_ttimes_profiles_force_same_typography_and_logo():
    for profile in (None, 'generic', 'park-tech-talk', 'general-interview'):
        assert build_cover.apply_profile_font_size(profile, None) == 80
        assert build_cover.apply_profile_font_size(profile, 80) == 80
        assert build_cover.profile_logo_geometry(profile) == (836, 55, 176)


def test_all_ttimes_profiles_reject_non_80px_cover_title():
    for profile in (None, 'generic', 'park-tech-talk', 'general-interview'):
        try:
            build_cover.apply_profile_font_size(profile, 79)
        except ValueError as exc:
            assert 'fixed at 80px' in str(exc)
        else:
            raise AssertionError('expected rejection')
