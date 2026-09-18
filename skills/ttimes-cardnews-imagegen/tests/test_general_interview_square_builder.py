import importlib.util
from pathlib import Path

SCRIPT=Path(__file__).parents[1]/'scripts'/'build_general_interview_square.py'
spec=importlib.util.spec_from_file_location('builder',SCRIPT);builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)


def test_contract_constants():
    assert builder.BODY_TOP_H in range(480,521)
    assert builder.NUMBER_BADGE=={'shape':'square','size':92,'radius':0}
    assert builder.BODY_LOGO_ENABLED is False
    assert builder.CLOSING_LOGO_POSITION=='bottom-center'
    assert builder.CLOSING_USES_LIST_IMAGE is False
    assert builder.GENERAL_COVER_TITLE_PX == 80
    assert builder.GENERAL_BODY_TITLE_PX == 80
    assert builder.GENERAL_BODY_PX == 40
    assert builder.GENERAL_CLOSING_QUOTE_PX == 50
    assert builder.GENERAL_PROFILE_PX == 30


def test_closing_rejects_list_hash(tmp_path: Path):
    from PIL import Image
    same=tmp_path/'same.png';Image.new('RGB',(10,10)).save(same)
    try:
        builder.render_closing_card(background=same,list_image=same,quote_white='a',quote_highlight='b',profile='c',output=tmp_path/'out.png',black_font=Path('/missing'),logo_path=Path('/missing'))
    except ValueError as exc:
        assert 'must differ' in str(exc)
    else:raise AssertionError('expected rejection')
