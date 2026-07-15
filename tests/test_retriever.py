from app.retrieval.retriever import Retriever


def main():

    retriever = Retriever()

    results = retriever.search(
        "What is Article 21?"
    )

    print(f"\nRetrieved {len(results)} documents\n")

    for i, doc in enumerate(results, start=1):

        print("=" * 80)
        print(f"Result {i}")
        print("-" * 80)

        print("Metadata:")
        print(doc.metadata)

        print("\nContent:")
        print(doc.page_content[:400])
        print()


if __name__ == "__main__":
    main()