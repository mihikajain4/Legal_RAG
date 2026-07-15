from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from app.embeddings.embedding_model import EmbeddingModel


class VectorStore:

    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)
        self.embeddings = EmbeddingModel.get_model()
        self.vectorstore = None

    def create(self, documents: list[Document]) -> None:
        """
        Create a FAISS vector store from a list of Documents.
        """
        self.vectorstore = FAISS.from_documents(
            documents,
            self.embeddings,
        )

    def save(self) -> None:
        """
        Save the FAISS index locally.
        """
        if self.vectorstore is None:
            raise ValueError("Vector store has not been created.")

        self.db_path.mkdir(parents=True, exist_ok=True)

        self.vectorstore.save_local(
            folder_path=str(self.db_path)
        )

    def load(self) -> None:
        """
        Load an existing FAISS index.
        """
        self.vectorstore = FAISS.load_local(
            folder_path=str(self.db_path),
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True,
        )

    def get_store(self):
        return self.vectorstore