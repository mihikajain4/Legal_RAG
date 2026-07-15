import json
import re
from pathlib import Path
from constitution_parser import ConstitutionParser

# Information that is constant for each document
DOCUMENT_INFO = {
    "constitution": {
        "document": "Constitution of India",
        "year": 1950
    },
    "ipc": {
        "document": "Indian Penal Code",
        "year": 1860
    },
    "crpc": {
        "document": "Code of Criminal Procedure",
        "year": 1973
    },
    "bns": {
        "document": "Bharatiya Nyaya Sanhita",
        "year": 2023
    },
    "bnss": {
        "document": "Bharatiya Nagarik Suraksha Sanhita",
        "year": 2023
    },
    "bsa": {
        "document": "Bharatiya Sakshya Adhiniyam",
        "year": 2023
    }
}


def extract_part(text):
    """
    Extracts PART I, PART II, etc.
    """
    match = re.search(r"PART\s+[IVXLC]+", text, re.IGNORECASE)
    return match.group(0) if match else None


def extract_article(text):
    """
    Extracts Article numbers like:
    19
    21A
    Article 32
    """

    match = re.search(r"Article\s+(\d+[A-Z]?)", text, re.IGNORECASE)

    if match:
        return match.group(1)

    match = re.search(r"\b(\d+[A-Z]?)\.\s", text)

    if match:
        return match.group(1)

    return None


def extract_section(text):
    """
    Extract sections (mostly useful for IPC/BNS)
    """

    match = re.search(r"Section\s+(\d+[A-Z]?)", text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None


def build_metadata(document_key, page):

    info = DOCUMENT_INFO.get(document_key, {})

    metadata = {

        "document": info.get("document", document_key),

        "source": f"{document_key}.pdf",

        "page": page["page"],

        "year": info.get("year"),

        "jurisdiction": "India",

        "language": "English",

        "part": extract_part(page["text"]),

        "article": extract_article(page["text"]),

        "section": extract_section(page["text"]),

        "chapter": None
    }

    return metadata


def process_file(input_file, output_file):

    document_key = input_file.stem.replace("_clean", "")

    with open(input_file, "r", encoding="utf-8") as f:
        pages = json.load(f)

    parser = ConstitutionParser()

    processed = []

    for page in pages:

        parser_metadata = parser.parse_page(page)

        processed.append({

            "page": page["page"],

            "text": page["text"],

            "metadata": {

                "document": "Constitution of India",

                "source": "constitution.pdf",

                "page": page["page"],

                "year": 1950,

                "jurisdiction": "India",

                "language": "English",

                **parser_metadata
            }

        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=4, ensure_ascii=False)


def main():

    project_root = Path(__file__).resolve().parent.parent

    processed_folder = project_root / "data" / "processed"

    clean_files = list(processed_folder.glob("*_clean.json"))

    if not clean_files:
        print("No cleaned JSON files found.")
        return

    print(f"Found {len(clean_files)} cleaned file(s).\n")

    for clean_file in clean_files:

        output_file = processed_folder / clean_file.name.replace(
            "_clean.json",
            "_metadata.json"
        )

        print(f"Building metadata for {clean_file.name}")

        process_file(clean_file, output_file)

        print(f"Saved {output_file.name}\n")

    print("Metadata generation completed.")


if __name__ == "__main__":
    main()