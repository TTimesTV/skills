import json
from hashlib import sha256
from pathlib import Path
from PIL import Image

REF=Path(__file__).resolve().parents[1] / 'references'


def test_four_formats_are_user_approved_templates():
    registry=json.loads((REF/'approved-format-registry.json').read_text(encoding='utf-8'))
    assert set(registry['formats'])=={
        'lee-junghak-people-and-technology',
        'park-youngsun-tech-talk',
        'one-person-explainer',
        'general-interview',
    }
    assert all(x['status']=='USER_APPROVED_TEMPLATE' for x in registry['formats'].values())
    assert registry['pending_formats']=={}


def test_approved_one_person_reference_is_locked():
    root=REF/'assets/approved-one-person-laundry'
    manifest=json.loads((root/'approval_manifest.json').read_text(encoding='utf-8'))
    assert len(manifest['files'])==5
    for name,item in manifest['files'].items():
        p=root/name
        assert Image.open(p).size==(1080,1080)
        assert sha256(p.read_bytes()).hexdigest()==item['sha256']


def test_approved_general_interview_reference_is_locked():
    root=REF/'assets/approved-general-interview-linkedin'
    manifest=json.loads((root/'approval_manifest.json').read_text(encoding='utf-8'))
    assert manifest['palette']=={
        'blue':'#0A66C2',
        'pale_blue':'#DCE6F1',
        'slate':'#38434F',
        'offwhite':'#F3F6F8',
    }
    assert len(manifest['files'])==3
    for name,item in manifest['files'].items():
        p=root/name
        assert Image.open(p).size==(1080,1080)
        assert sha256(p.read_bytes()).hexdigest()==item['sha256']
