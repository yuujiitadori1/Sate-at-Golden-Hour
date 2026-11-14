"""food-picture-01 entry: "Sate at Golden Hour".

Writes the bundled photograph of Indonesian chicken satay -- skewers
with glossy peanut sauce, charred caramelised edges, steam rising --
to the output directory as entry.png. The image was sized to fit
within 1024x1024 (aspect ratio preserved, never cropped) and kept
under 1 MiB during the build, so this program only copies bytes.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
MAX_BYTES = 1048576  # competition cap: 1 MiB
MAX_SIDE = 1024  # competition cap: 1024x1024 pixels
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {len(data)} bytes > {MAX_BYTES}")
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG")
    # PNG header: width and height are big-endian uint32 at bytes 16 and 20.
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(f"entry.png too big: {width}x{height} > {MAX_SIDE}x{MAX_SIDE}")
    with open(dest, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
