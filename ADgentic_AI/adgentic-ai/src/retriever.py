import chromadb
from chromadb.utils import embedding_functions

class PromptRetriever:
    """Handles Retrieval Augmented Generation (RAG) by querying ChromaDB."""
    def __init__(self):
        # NOTE: This creates a 'chroma' folder in your project root for persistence
        client = chromadb.PersistentClient(path="./chroma")
        # Using the default Sentence Transformer embedding function
        self.collection = client.get_or_create_collection(
            name="prompts",
            embedding_function=embedding_functions.DefaultEmbeddingFunction(),
        )

    def query(self, text: str) -> list[str]:
        """Queries the collection to find similar, successful prompts."""
        # NOTE: To run this, you need to manually load some successful prompts first!
        result = self.collection.query(query_texts=[text], n_results=3)
        return result.get("documents", [[]])[0]