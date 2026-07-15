import json
import re
from pathlib import Path


def clean_text(text):
    """
    Cleans extracted PDF text while preserving legal meaning.
    """

    # Remove tabs
    text = text.replace("\t", " ")

    # Remove multiple spaces
    text = re.sub(r" +", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text


def clean_json(input_file, output_file):

    with open(input_file, "r", encoding="utf-8") as f:
        pages = json.load(f)

    cleaned_pages = []

    for page in pages:

        cleaned_pages.append({
            "page": page["page"],
            "text": clean_text(page["text"])
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(cleaned_pages, f, indent=4, ensure_ascii=False)

    print(f"Saved cleaned file to:\n{output_file}")


def main():

    project_root = Path(__file__).resolve().parent.parent

    processed_folder = project_root / "data" / "processed"

    raw_files = list(processed_folder.glob("*_raw.json"))

    if not raw_files:
        print("No raw JSON files found.")
        return

    print(f"Found {len(raw_files)} raw JSON file(s).\n")

    for raw_file in raw_files:

        output_file = processed_folder / raw_file.name.replace("_raw.json", "_clean.json")

        print(f"Cleaning: {raw_file.name}")

        clean_json(raw_file, output_file)

        print(f"Saved: {output_file.name}\n")

    print("All files cleaned successfully!")


if __name__ == "__main__":
    main()