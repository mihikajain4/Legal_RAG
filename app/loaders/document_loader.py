import json
from pathlib import Path

from langchain_core.documents import Document


class DocumentLoader:
    """
    Loads one or more processed metadata JSON files
    and converts them into LangChain Documents.
    """

    @staticmethod
    def load(file_path: str | Path) -> list[Document]:
        file_path = Path(file_path)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        documents = []

        for item in data:

            text = item.get("text", "").strip()

            if not text:
                continue

            metadata = item.get("metadata", {})

            documents.append(
                Document(
                    page_content=text,
                    metadata=metadata,
                )
            )

        return documents

    @staticmethod
    def load_directory(directory: str | Path) -> list[Document]:

        directory = Path(directory)

        all_documents = []

        for file in sorted(directory.glob("*_metadata.json")):

            docs = DocumentLoader.load(file)

            all_documents.extend(docs)

            print(f"Loaded {len(docs)} documents from {file.name}")

        return all_documents