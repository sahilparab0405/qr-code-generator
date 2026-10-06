"""
generator.py
------------
Turns a piece of text (a URL, a message, whatever) into a QR code image.
"""

from pathlib import Path
import qrcode


def generate_qr(data: str, filename: str, output_dir: Path) -> Path:
    """
    Generate a QR code PNG for `data` and save it as `filename`
    inside `output_dir`. Returns the path it was saved to.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=None,          # let the library pick the smallest size that fits
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    save_path = output_dir / filename
    img.save(save_path)
    return save_path
