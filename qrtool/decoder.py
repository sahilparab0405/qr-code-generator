"""
decoder.py
----------
The "reverse" direction: reads an existing QR code image and extracts
the text/URL encoded inside it, using OpenCV's built-in QR detector.

Deliberately using OpenCV instead of a zbar-based library here --
OpenCV installs as a plain pip wheel with no extra system dependencies,
which keeps this project a simple 'pip install, then run' experience
on any machine.
"""

from pathlib import Path
import cv2


def decode_qr(image_path: Path) -> str | None:
    """
    Read a QR code from an image file and return the decoded text.
    Returns None if the file can't be read or no QR code is found.
    """
    image = cv2.imread(str(image_path))
    if image is None:
        return None

    detector = cv2.QRCodeDetector()
    data, _points, _ = detector.detectAndDecode(image)

    return data if data else None
