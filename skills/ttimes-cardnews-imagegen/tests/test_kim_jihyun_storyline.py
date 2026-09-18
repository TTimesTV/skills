import json
from pathlib import Path

FIXTURE = Path(__file__).resolve().parent / 'fixtures' / 'synthetic_kim_jihyun_general_interview_pages.json'


def test_storyline_has_one_thesis_and_five_pages():
    data = json.loads(FIXTURE.read_text(encoding='utf-8'))
    assert data['thesis_id'] == 'spare-capacity-to-jevons-to-memory'
    assert len(data['pages']) == 5
    assert [p['function'] for p in data['pages']] == [
        'cover', 'problem_and_reframe', 'efficiency_mechanism', 'jevons_implication', 'guest_quote'
    ]


def test_omits_full_video_summary_topics():
    data = json.loads(FIXTURE.read_text(encoding='utf-8'))
    joined = json.dumps(data['pages'], ensure_ascii=False)
    for forbidden in ['3대 메가 프로젝트', '피지컬 AI', '중국 추격', '주가 전망']:
        assert forbidden not in joined
