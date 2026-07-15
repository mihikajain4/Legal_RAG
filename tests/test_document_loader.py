from app.loaders.document_loader import DocumentLoader


def main():

    documents = DocumentLoader.load(
        "data/processed/constitution_metadata.json"
    )

    print(f"Loaded {len(documents)} documents\n")

    print(documents[0])

if __name__ == "__main__":
    main()