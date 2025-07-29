from fastapi import APIRouter, Depends
from app.models.schemas import Document, Answer
from app.core.security import verify_token
from app.services.document_service import process_document
from app.services.query_service import get_answer, embedding_model
from app.db.qdrant_client import get_qdrant_client
from qdrant_client import QdrantClient, models
from app.core.config import settings

router = APIRouter()

@router.post("/hackrx/run", response_model=Answer, dependencies=[Depends(verify_token)])
def hackrx_run(document: Document, qdrant_client: QdrantClient = Depends(get_qdrant_client)):
    text = process_document(document.documents)

    # Embed and store the document chunks
    collection_name = settings.QDRANT_COLLECTION_NAME
    

    # A simple chunking strategy
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

    embeddings = embedding_model.encode(chunks).tolist()

    qdrant_client.upsert(
        collection_name=collection_name,
        points=[
            models.PointStruct(id=i, vector=embedding, payload={"content": chunk})
            for i, (embedding, chunk) in enumerate(zip(embeddings, chunks))
        ],
        wait=True,
    )

    answers = []
    for question in document.questions:
        answer = get_answer(question)
        answers.append(answer)

    return Answer(answers=answers)
