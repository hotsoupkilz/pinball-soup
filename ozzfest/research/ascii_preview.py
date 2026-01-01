#!/usr/bin/env python3
from pathlib import Path

from PIL import Image, ImageFilter

DEFAULT_CHARS = "@%#*+=-:. "


def to_ascii(image, width=80, charset=DEFAULT_CHARS):
    # maintain aspect ratio by adjusting height with 0.55 factor
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width * 0.55)
    resized = image.resize((width, max(1, new_height)))
    grayscale = resized.convert("L")
    pixels = grayscale.getdata()
    ascii_pixels = [charset[int(pixel * (len(charset) - 1) / 255)] for pixel in pixels]
    lines = ["".join(ascii_pixels[i : i + width]) for i in range(0, len(ascii_pixels), width)]
    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--width", type=int, default=80)
    parser.add_argument("--invert", action="store_true")
    parser.add_argument("--edges", action="store_true")
    parser.add_argument("--chars", type=str, default=DEFAULT_CHARS)
    args = parser.parse_args()

    image = Image.open(args.path)
    if args.invert:
        image = Image.eval(image, lambda p: 255 - p)
    if args.edges:
        image = image.convert("L").filter(ImageFilter.FIND_EDGES)
    print(to_ascii(image, width=args.width, charset=args.chars))


if __name__ == "__main__":
    main()
