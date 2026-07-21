from pprint import pprint

from app.services.search_service import SearchService


def main():

    service = SearchService()

    results = service.search(
        "What is Article 21?"
    )

    print(f"\nRetrieved {len(results)} results\n")

    for i, result in enumerate(results, start=1):

        print("=" * 80)
        print(f"Result {i}")
        print("-" * 80)

        pprint(result)

        print()


if __name__ == "__main__":
    main()