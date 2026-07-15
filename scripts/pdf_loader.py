import fitz  # PyMuPDF
import json
import os
from pathlib import Path



def load_pdf(pdf_path):
    """
    Reads a PDF and extracts text page by page.
    Returns a list of dictionaries.
    """

    document = fitz.open(pdf_path)

    pages = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()

        pages.append({
            "page": page_num + 1,
            "text": text
        })

    document.close()

    return pages


def save_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


from pathlib import Path

def main():

    project_root = Path(__file__).resolve().parent.parent

    raw_folder = project_root / "data" / "raw"
    processed_folder = project_root / "data" / "processed"

    processed_folder.mkdir(exist_ok=True)

    pdf_files = list(raw_folder.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return

    print(f"Found {len(pdf_files)} PDF(s).\n")

    for pdf in pdf_files:

        print(f"Processing: {pdf.name}")

        pages = load_pdf(str(pdf))

        output_file = processed_folder / f"{pdf.stem}_raw.json"

        save_json(pages, str(output_file))

        print(f"Pages: {len(pages)}")
        print(f"Saved: {output_file.name}\n")

    print("All PDFs processed successfully!")

if __name__ == "__main__":
    main()