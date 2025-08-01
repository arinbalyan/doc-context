from app.core.config import settings
from openai import OpenAI
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

llm_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENROUTER_API_KEY,
)

qdrant_client = QdrantClient(url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY, timeout=30)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


def get_answer(question: str) -> str:
    query_embedding = embedding_model.encode(question).tolist()

    search_result = qdrant_client.search(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        query_vector=query_embedding,
        limit=3  # Retrieve top 3 relevant chunks
    )

    context = "\n".join([hit.payload['content'] for hit in search_result])

    response = llm_client.chat.completions.create(
        model="google/gemma-3n-e2b-it:free",
        messages=[
            {
                "role": "user",
                "content": f"You are an intelligent query-retrieval system. Answer the user's question based on the provided context. The context is extracted from a document.\n\nContext:\n{context}\n\nQuestion: {question}",
            },
        ],
    )
    return response.choices[0].message.content