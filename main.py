"""food-picture-01 entry: "Noodles at Golden Hour".

Copies the bundled photograph of a steaming ramen bowl to the output
directory as entry.png. The image was resized to fit within 1024x1024
(preserving aspect ratio, never cropped) and compressed under 1 MiB
during the build, so this program only copies bytes.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "entry.png")
MAX_BYTES = 1048576  # competition cap: 1 MiB
MAX_SIDE = 1024  # competition cap: 1024x1024


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    # Guard the competition limits: refuse to emit an invalid entry.
    size = os.path.getsize(dest)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {size} bytes > {MAX_BYTES}")
    with open(dest, "rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit("entry.png is not a PNG")


if __name__ == "__main__":
    main()
