from langchain_huggingface import HuggingFaceEmbeddings

from app.config.settings import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Singleton wrapper around the HuggingFace embedding model.
    Ensures the model is loaded only once.
    """

    _instance = None

    @classmethod
    def get_model(cls):
        if cls._instance is None:
            cls._instance = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={"device": "cpu"},
                encode_kwargs={"normalize_embeddings": True},
            )
        return cls._instance