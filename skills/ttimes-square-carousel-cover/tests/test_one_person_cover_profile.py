import json
from pathlib import Path

PROFILE=Path(__file__).resolve().parents[1] / 'references' / 'one-person-cover-profile.json'


def test_one_person_profile_inherits_global_contract():
    p=json.loads(PROFILE.read_text(encoding='utf-8'))
    assert p['production_format']=='F1'
    assert p['visual_source']=='exact_article_list_image'
    assert p['cover_title_px']==80
    assert p['cover_logo']=={'position':'upper-right','x':836,'y':55,'width':176}
    assert p['person_required'] is False
    assert p['body_logo'] is False
    assert p['closing_logo']=='bottom-center'
    assert p['page_count']=='variable'
