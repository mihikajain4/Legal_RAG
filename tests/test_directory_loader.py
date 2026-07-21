from app.loaders.document_loader import DocumentLoader


def main():

    documents = DocumentLoader.load_directory(
        "data/processed"
    )

    print()

    print("=" * 60)

    print(f"TOTAL DOCUMENTS : {len(documents)}")

    print("=" * 60)

    print()

    print(documents[0].metadata)

    print()

    print(documents[-1].metadata)


if __name__ == "__main__":
    main()