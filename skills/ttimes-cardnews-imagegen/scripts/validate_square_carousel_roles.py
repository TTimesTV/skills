#!/usr/bin/env python3
from hashlib import sha256
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def validate_roles(list_image: Path, closing_background: Path, body_visuals: list[Path]) -> None:
    list_image = Path(list_image)
    closing_background = Path(closing_background)
    body_visuals = [Path(p) for p in body_visuals]
    if not list_image.is_file():
        raise ValueError(f'missing list image: {list_image}')
    list_hash = digest(list_image)
    if closing_background.exists() and digest(closing_background) == list_hash:
        raise ValueError('closing background must differ from the cover-only _list_ image')
    for visual in body_visuals:
        if digest(visual) == list_hash:
            raise ValueError(f'_list_ is cover-only, but body reused it: {visual}')
