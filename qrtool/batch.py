"""
batch.py
--------
Reads a text file (one entry per line) and generates a QR code for
each line in a single run -- useful when you have a list of links,
contacts, or codes to turn into QR images at once.
"""

from pathlib import Path
from .generator import generate_qr


def batch_generate(input_file: Path, output_dir: Path) -> list[tuple[str, Path]]:
    """
    Generate one QR code per non-empty line in `input_file`.
    Returns a list of (original_text, saved_path) pairs.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    results = []
    for index, text in enumerate(lines, start=1):
        filename = f"batch_{index}.png"
        saved_path = generate_qr(text, filename, output_dir)
        results.append((text, saved_path))

    return results
