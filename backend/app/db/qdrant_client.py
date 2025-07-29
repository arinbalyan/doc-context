from qdrant_client import QdrantClient, models
from app.core.config import settings
from app.services.query_service import embedding_model

def get_qdrant_client() -> QdrantClient:
    client = QdrantClient(url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY)
    collection_name = settings.QDRANT_COLLECTION_NAME
    
    # Check if collection exists, if not, create it
    try:
        client.get_collection(collection_name=collection_name)
    except Exception: # Catch specific exception if possible, e.g., CollectionNotFoundError
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=embedding_model.get_sentence_embedding_dimension(), distance=models.Distance.COSINE),
        )
    return client
