import json
from pathlib import Path
from PIL import Image


def make_contract_fixture(root):
    assets = root / 'assets'
    carousel = root / 'carousel_final'
    assets.mkdir(parents=True)
    carousel.mkdir()
    visuals = {}
    for index in range(1, 4):
        name = f'body-{index}.png'
        Image.new('RGB', (1254, 1254), 'white').save(assets / name)
        visuals[name] = {
            'source_type': 'generated_square_natural_editorial_illustration',
            'video_capture': False,
            'photoreal_cgi': False,
            'single_scene': True,
            'color_grade': 'none',
            'source_size': [1254, 1254],
        }
    manifest = {
        'body_visuals': visuals,
        'body_split': {'visual_px': 540, 'text_px': 540, 'ratio': '1:1'},
        'typography': {'body_title': 74, 'body': 35, 'highlight': 35},
        'palette': {
            'ttimes_red': '#E30613',
            'inline_highlight': '#FEF601',
            'inline_highlight_text': '#070707',
            'visual_color_grade': 'none',
        },
    }
    (carousel / 'manifest.json').write_text(json.dumps(manifest), encoding='utf-8')


def test_body_visuals_are_square_generated_assets_not_video_captures(tmp_path):
    root = tmp_path / 'synthetic_one_person'
    make_contract_fixture(root)
    manifest=json.loads((root/'carousel_final/manifest.json').read_text(encoding='utf-8'))
    visuals=manifest['body_visuals']
    assert len(visuals)==3
    for name,item in visuals.items():
        assert item['source_type']=='generated_square_natural_editorial_illustration'
        assert item['video_capture'] is False
        assert item['photoreal_cgi'] is False
        assert item['single_scene'] is True
        assert item['color_grade']=='none'
        assert item['source_size'][0]==item['source_size'][1]
        assert Image.open(root/'assets'/name).size==(1254,1254)
    assert manifest['body_split']=={'visual_px':540,'text_px':540,'ratio':'1:1'}
    assert manifest['typography']['body_title']==74
    assert manifest['typography']['body']==35
    assert manifest['typography']['highlight']==35
    assert manifest['palette']['ttimes_red']=='#E30613'
    assert manifest['palette']['inline_highlight']=='#FEF601'
    assert manifest['palette']['inline_highlight_text']=='#070707'
    assert manifest['palette']['visual_color_grade']=='none'
