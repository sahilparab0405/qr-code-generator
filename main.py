"""
main.py
-------
Interactive entry point for the QR Code tool.
Run with: python main.py

Supports three things:
  1. Generate a QR code from text/a URL you type in
  2. Batch-generate QR codes from a list in a text file
  3. Decode an existing QR code image back into text (the "scan" direction)
"""

from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from qrtool.generator import generate_qr
from qrtool.batch import batch_generate
from qrtool.decoder import decode_qr

console = Console()
OUTPUT_DIR = Path(__file__).parent / "output"


def print_header() -> None:
    console.rule("[bold cyan]QR Code Tool[/bold cyan]")
    console.print(
        "[dim]1[/dim] Generate a QR code   "
        "[dim]2[/dim] Batch generate from a file   "
        "[dim]3[/dim] Decode a QR image   "
        "[dim]4[/dim] Exit"
    )


def handle_generate() -> None:
    text = Prompt.ask("Enter the text or URL to encode")
    filename = Prompt.ask("Save as (filename)", default="qr_code.png")
    path = generate_qr(text, filename, OUTPUT_DIR)
    console.print(Panel(f"Saved to [bold]{path}[/bold]", title="Done", border_style="green"))


def handle_batch() -> None:
    file_path = Prompt.ask(
        "Path to your input file", default="samples/links.txt"
    )
    input_file = Path(file_path)

    if not input_file.exists():
        console.print(Panel(f"File not found: {input_file}", border_style="red"))
        return

    results = batch_generate(input_file, OUTPUT_DIR)

    table = Table(title="Batch Generation Results")
    table.add_column("Input")
    table.add_column("Saved As")
    for original_text, saved_path in results:
        table.add_row(original_text, str(saved_path))

    console.print(table)


def handle_decode() -> None:
    file_path = Prompt.ask("Path to the QR image to decode")
    image_path = Path(file_path)

    if not image_path.exists():
        console.print(Panel(f"File not found: {image_path}", border_style="red"))
        return

    result = decode_qr(image_path)

    if result:
        console.print(Panel(result, title="Decoded Text", border_style="green"))
    else:
        console.print(
            Panel("Couldn't read a QR code from that image.", border_style="red")
        )


def main() -> None:
    while True:
        print_header()
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"])

        if choice == "1":
            handle_generate()
        elif choice == "2":
            handle_batch()
        elif choice == "3":
            handle_decode()
        elif choice == "4":
            console.print("[bold]Goodbye![/bold]")
            break

        console.print()  # spacing before next loop


if __name__ == "__main__":
    main()
