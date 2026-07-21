from app.config.settings import VECTOR_DB_PATH
from app.loaders.document_loader import DocumentLoader
from app.retrieval.vector_store import VectorStore


def main():

    documents = DocumentLoader.load_directory(
    "data/processed"
    )

    print(f"Loaded {len(documents)} documents")

    store = VectorStore(VECTOR_DB_PATH)

    store.create(documents)

    store.save()

    print("Vector Store Built Successfully")


if __name__ == "__main__":
    main()