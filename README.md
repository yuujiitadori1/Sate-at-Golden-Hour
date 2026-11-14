# Sate at Golden Hour — food-picture-01

A photorealistic plate of Indonesian chicken satay at golden hour:
skewers with glossy peanut sauce, charred caramelised edges, fried
shallots and a lime wedge, steam rising in warm evening light.

The program copies the bundled photograph to the output directory
as `entry.png` (832x832 PNG, under 1 MiB), refusing to emit it if
the file is not a PNG, exceeds 1 MiB, or is larger than 1024x1024.

Run it:

    python3 main.py

It writes to `$MAKEFUN_OUTPUT_DIR`, or to `/output` when that
variable is not set.
