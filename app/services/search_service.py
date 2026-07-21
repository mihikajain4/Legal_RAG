from app.retrieval.retriever import Retriever


class SearchService:

    def __init__(self):
        self.retriever = Retriever()

    def search(self, query: str, k: int = 5):

        docs = self.retriever.search(query, k)

        results = []

        for doc in docs:

            results.append(
                {
                    "document": doc.metadata.get("document"),
                    "source": doc.metadata.get("source"),
                    "page": doc.metadata.get("page"),
                    "part": doc.metadata.get("part"),
                    "article": doc.metadata.get("article"),
                    "section": doc.metadata.get("section"),
                    "chapter": doc.metadata.get("chapter"),
                    "content": doc.page_content,
                }
            )

        return results