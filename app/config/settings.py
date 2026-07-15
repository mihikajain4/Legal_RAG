from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Paths
VECTOR_DB_PATH = BASE_DIR / "vectorstore"
SAMPLE_DATA_PATH = BASE_DIR / "sample_data"

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Retrieval
TOP_K = 5