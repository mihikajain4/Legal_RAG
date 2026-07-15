import json
from pathlib import Path

from langchain_core.documents import Document


class DocumentLoader:
    """
    Loads processed legal JSON files and converts them into
    LangChain Document objects.
    """

    @staticmethod
    def load(file_path: str | Path) -> list[Document]:
        file_path = Path(file_path)

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        documents = []

        for item in data:

            text = item.get("text", "").strip()

            metadata = item.get("metadata", {})

            if not text:
                continue

            documents.append(
                Document(
                    page_content=text,
                    metadata=metadata
                )
            )

        return documents