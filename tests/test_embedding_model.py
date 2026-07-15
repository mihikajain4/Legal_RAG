from app.embeddings.embedding_model import EmbeddingModel


def main():
    model = EmbeddingModel.get_model()

    embeddings = model.embed_query(
        "What is Article 21 of the Indian Constitution?"
    )

    print(f"Embedding Dimension: {len(embeddings)}")
    print(embeddings[:10])


if __name__ == "__main__":
    main()