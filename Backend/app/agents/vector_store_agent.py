import chromadb
import uuid
from app.agents.embedding_agent import generate_embedding

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="codebase_chunks"
)


def store_chunks(embedded_chunks):

    for idx, chunk in enumerate(embedded_chunks):

        collection.add(
            ids=[f"chunk_{idx}"],
            embeddings=[chunk["embedding"]],
            documents=[chunk["content"]],
            metadatas=[
                {
                    "file_name": chunk["file_name"],
                    "file_path": chunk["file_path"],
                    "chunk_id": chunk["chunk_id"]
                }
            ]
        )

def get_collection_count():

    return collection.count()

def search_chunks(
    query: str,
    n_results: int = 5
):

    query_embedding = generate_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results