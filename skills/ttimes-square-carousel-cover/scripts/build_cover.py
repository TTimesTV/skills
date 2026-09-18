#!/usr/bin/env python3
"""Build a variable-layout 1080×1080 TTimes square carousel cover."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont, ImageOps

W = H = 1080


def validate_profile(profile: str | None, box_lines: list[int]) -> None:
    """Apply series/profile invariants before any pixels are rendered."""
    if profile == "general-interview" and box_lines:
        raise ValueError("title plates are forbidden for general-interview covers")


def apply_profile_font_size(profile: str | None, explicit_size: int | None) -> int | None:
    if explicit_size not in (None, 80):
        raise ValueError("all TTimes square cover titles are fixed at 80px")
    return 80


def profile_logo_geometry(profile: str | None) -> tuple[int, int, int] | None:
    return 836, 55, 176


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_font(explicit: str | None) -> Path:
    candidates: Iterable[Path]
    if explicit:
        candidates = [Path(explicit).expanduser()]
    else:
        candidates = [
            Path.home() / "Library/Fonts/NotoSansCJKkr-Black.otf",
            Path.home() / "Library/Fonts/NotoSansKR-Black.otf",
            Path("/Library/Fonts/NotoSansCJKkr-Black.otf"),
            Path("/Library/Fonts/NotoSansKR-Black.otf"),
        ]
    for path in candidates:
        if path.is_file():
            return path
    raise SystemExit(
        "No approved Korean Black font found. Supply --font with a licensed "
        "Sandoll GothicNeo Heavy/Black, Noto Sans CJK KR Black, or Pretendard Black file."
    )


def rgba(value: str) -> tuple[int, int, int, int]:
    rgb = ImageColor.getrgb(value)
    return rgb[0], rgb[1], rgb[2], 255


def render_mask(text: str, font_path: Path, size: int, horizontal_scale: float) -> Image.Image:
    font = ImageFont.truetype(str(font_path), size=size)
    probe = Image.new("L", (2400, 260), 0)
    draw = ImageDraw.Draw(probe)
    draw.text((5, -3), text, font=font, fill=255)
    bbox = probe.getbbox()
    if not bbox:
        raise ValueError(f"Title line rendered empty: {text!r}")
    mask = probe.crop(bbox)
    return mask.resize(
        (max(1, round(mask.width * horizontal_scale)), mask.height),
        Image.Resampling.LANCZOS,
    )


def choose_layout(
    lines: list[str],
    font_path: Path,
    max_width: int,
    max_height: int,
    explicit_size: int | None,
    explicit_scale: float | None,
    explicit_gap: int | None,
) -> tuple[int, float, int, list[Image.Image]]:
    scales = [explicit_scale] if explicit_scale is not None else [1.00, 0.97, 0.94, 0.91, 0.88]
    sizes = [explicit_size] if explicit_size is not None else list(range(132, 53, -1))
    candidates = []
    for scale in scales:
        if scale is None or not 0.75 <= scale <= 1.10:
            continue
        for size in sizes:
            if size is None:
                continue
            masks = [render_mask(line, font_path, size, scale) for line in lines]
            gap = explicit_gap if explicit_gap is not None else max(14, round(size * 0.26))
            width = max(mask.width for mask in masks)
            height = sum(mask.height for mask in masks) + gap * (len(masks) - 1)
            if width <= max_width and height <= max_height:
                # Prefer larger glyphs but penalize unnecessary horizontal crushing.
                score = size - 40 * (1.0 - scale)
                candidates.append((score, size, scale, gap, masks))
                break
    if not candidates:
        raise SystemExit(
            "No title layout fits. Improve semantic line breaks, add a line, reduce --font-size, "
            "or expand the title rectangle; do not silently crush the title."
        )
    _, size, scale, gap, masks = max(candidates, key=lambda item: item[0])
    return size, scale, gap, masks


def add_gradient(base: Image.Image, start_y: int, max_opacity: int, color: str) -> Image.Image:
    if max_opacity <= 0:
        return base
    cr, cg, cb = ImageColor.getrgb(color)
    gradient = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pixels = gradient.load()
    span = max(1, H - start_y)
    for y in range(H):
        t = max(0.0, min(1.0, (y - start_y) / span))
        alpha = int((t**1.55) * max_opacity)
        for x in range(W):
            pixels[x, y] = (cr, cg, cb, alpha)
    return Image.alpha_composite(base, gradient)


def paste_shadowed(
    canvas: Image.Image,
    mask: Image.Image,
    color: tuple[int, int, int, int],
    x: int,
    y: int,
    shadow_blur: int,
) -> None:
    layer = Image.new("RGBA", mask.size, color)
    layer.putalpha(mask)
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    alpha = Image.new("L", canvas.size, 0)
    alpha.paste(mask, (x + 6, y + 7))
    alpha = alpha.filter(ImageFilter.GaussianBlur(shadow_blur))
    shadow.putalpha(alpha.point(lambda value: int(value * 0.88)))
    canvas.alpha_composite(shadow)
    canvas.alpha_composite(layer, (x, y))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=["general-interview", "one-person", "park-tech-talk", "generic"])
    parser.add_argument("--list-image", required=True)
    parser.add_argument("--logo", required=True)
    parser.add_argument("--font")
    parser.add_argument("--line", action="append", required=True, help="Repeat once per displayed title line")
    parser.add_argument("--color", action="append", required=True, help="Repeat per line, or pass once for all lines")
    parser.add_argument("--output", required=True)
    parser.add_argument("--font-size", type=int, help="Omit for automatic fit")
    parser.add_argument("--horizontal-scale", type=float, help="Omit for automatic 100–88% fit search")
    parser.add_argument("--line-gap", type=int)
    parser.add_argument("--x", type=int, default=62)
    parser.add_argument("--title-y", type=int, help="Top of title block; omit to bottom-anchor")
    parser.add_argument("--bottom-margin", type=int, default=82)
    parser.add_argument("--max-width", type=int, default=952)
    parser.add_argument("--max-height", type=int, default=360)
    parser.add_argument("--logo-x", type=int, default=64)
    parser.add_argument("--logo-y", type=int, default=56)
    parser.add_argument("--logo-width", type=int, default=190)
    parser.add_argument("--gradient-start", type=int, default=600)
    parser.add_argument("--gradient-opacity", type=int, default=160)
    parser.add_argument("--gradient-color", default="#0A0816")
    parser.add_argument("--shadow-blur", type=int, default=6)
    parser.add_argument("--box-line", type=int, action="append", default=[], help="1-based line number to place on a box")
    parser.add_argument("--box-color", default="#F5222D")
    parser.add_argument("--box-padding-x", type=int, default=14)
    parser.add_argument("--box-padding-y", type=int, default=8)
    args = parser.parse_args()
    validate_profile(args.profile, args.box_line)
    args.font_size = apply_profile_font_size(args.profile, args.font_size)
    logo_geometry = profile_logo_geometry(args.profile)
    if logo_geometry is not None:
        args.logo_x, args.logo_y, args.logo_width = logo_geometry

    source = Path(args.list_image).expanduser().resolve()
    logo_path = Path(args.logo).expanduser().resolve()
    font_path = resolve_font(args.font).resolve()
    output = Path(args.output).expanduser().resolve()
    for required in (source, logo_path, font_path):
        if not required.is_file():
            raise SystemExit(f"Missing required file: {required}")

    lines = args.line
    colors = args.color
    if len(colors) == 1:
        colors = colors * len(lines)
    if len(colors) != len(lines):
        raise SystemExit("Pass one --color for all lines or exactly one --color per --line")
    if any(index < 1 or index > len(lines) for index in args.box_line):
        raise SystemExit("--box-line must identify an existing 1-based title line")

    output.parent.mkdir(parents=True, exist_ok=True)
    source_image = Image.open(source).convert("RGB")
    base = ImageOps.fit(
        source_image,
        (W, H),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    ).convert("RGBA")
    base = add_gradient(base, args.gradient_start, args.gradient_opacity, args.gradient_color)

    logo = Image.open(logo_path).convert("RGBA")
    logo_h = round(logo.height * args.logo_width / logo.width)
    logo = logo.resize((args.logo_width, logo_h), Image.Resampling.LANCZOS)
    base.alpha_composite(logo, (args.logo_x, args.logo_y))

    size, scale, gap, masks = choose_layout(
        lines,
        font_path,
        args.max_width,
        args.max_height,
        args.font_size,
        args.horizontal_scale,
        args.line_gap,
    )
    block_height = sum(mask.height for mask in masks) + gap * (len(masks) - 1)
    title_y = args.title_y if args.title_y is not None else H - args.bottom_margin - block_height
    if title_y < 0:
        raise SystemExit("Title block starts outside canvas")

    positions = []
    y = title_y
    for index, (mask, color_value) in enumerate(zip(masks, colors), start=1):
        if args.x + mask.width > W - 20 or y + mask.height > H - 20:
            raise SystemExit(f"Line {index} violates the output safe area")
        if index in args.box_line:
            box = (
                args.x - args.box_padding_x,
                y - args.box_padding_y,
                args.x + mask.width + args.box_padding_x,
                y + mask.height + args.box_padding_y,
            )
            ImageDraw.Draw(base).rectangle(box, fill=rgba(args.box_color))
        paste_shadowed(base, mask, rgba(color_value), args.x, y, args.shadow_blur)
        positions.append({"line": index, "x": args.x, "y": y, "width": mask.width, "height": mask.height})
        y += mask.height + gap

    final = base.convert("RGB")
    final.save(output, optimize=True)
    if Image.open(output).size != (W, H):
        raise SystemExit("Output dimension verification failed")

    manifest = {
        "contract": "exact _list_ image + official logo + classified variable title",
        "profile": args.profile,
        "title_plate": bool(args.box_line),
        "source": str(source),
        "source_size": list(source_image.size),
        "source_sha256": sha256(source),
        "logo": str(logo_path),
        "logo_sha256": sha256(logo_path),
        "font": str(font_path),
        "font_sha256": sha256(font_path),
        "lines": lines,
        "colors": colors,
        "selected_font_size_px": size,
        "selected_horizontal_scale": scale,
        "selected_line_gap_px": gap,
        "positions": positions,
        "box_lines": args.box_line,
        "box_color": args.box_color if args.box_line else None,
        "gradient": {
            "start_y": args.gradient_start,
            "max_opacity": args.gradient_opacity,
            "color": args.gradient_color,
        },
        "output": str(output),
        "output_size": [W, H],
        "output_sha256": sha256(output),
    }
    output.with_suffix(".manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
