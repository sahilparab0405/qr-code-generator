# QR Code Tool

A small interactive Python tool that does both directions of QR codes:
generates them from text/URLs, and decodes existing QR images back into text.
Also supports batch-generating a whole list of links at once from a file.

## Features

1. **Generate** — turn any text or URL into a QR code PNG
2. **Batch generate** — read a list of links from a text file and generate
   a QR code for each one in a single run
3. **Decode** — read an existing QR code image and extract the text/URL
   encoded inside it

## Project structure

```
qr-code-generator/
├── main.py              # interactive menu, entry point
├── requirements.txt
├── qrtool/
│   ├── generator.py      # text -> QR image
│   ├── batch.py           # list of lines -> multiple QR images
│   └── decoder.py         # QR image -> text (via OpenCV)
├── samples/
│   └── links.txt          # example input for batch mode
└── output/                # generated QR images are saved here
```

## Running it locally

```bash
git clone https://github.com/<your-username>/qr-code-generator.git
cd qr-code-generator
pip install -r requirements.txt
python main.py
```

Then pick an option from the menu:
- `1` to generate a single QR code
- `2` to batch-generate from `samples/links.txt` (or your own file)
- `3` to decode an existing QR image (try pointing it at one you just generated)
- `4` to exit

## Why OpenCV for decoding instead of a zbar-based library?

Most QR-decoding tutorials use `pyzbar`, which depends on a system-level
`zbar` library that has to be installed separately outside of pip -- an
extra setup step that varies by OS. `opencv-python-headless` installs as
a plain pip wheel with no extra system dependencies, so this project stays
a simple "pip install, then run" experience on any machine.
