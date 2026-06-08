from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def generate_embedding(text: str):
    return model.encode(text).tolist()


def embed_chunks(chunks):

    embedded_chunks = []

    for chunk in chunks:

        vector = generate_embedding(
            chunk["content"]
        )

        embedded_chunks.append(
            {
                **chunk,
                "embedding": vector
            }
        )

    return embedded_chunks