from app.config.settings import TOP_K, VECTOR_DB_PATH
from app.retrieval.vector_store import VectorStore


class Retriever:
    """
    Loads the FAISS vector store and performs similarity search.
    """

    def __init__(self):
        self.store = VectorStore(VECTOR_DB_PATH)
        self.store.load()

    def search(self, query: str, k: int = TOP_K):
        vectorstore = self.store.get_store()

        results = vectorstore.similarity_search(
            query=query,
            k=k
        )

        return results