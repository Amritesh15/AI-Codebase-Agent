from app.agents.vector_store_agent import (
    search_chunks
)

results = search_chunks(
    "authentication"
)

for idx, metadata in enumerate(
    results["metadatas"][0]
):

    print(
        f"\nResult {idx+1}"
    )

    print(
        metadata["file_name"]
    )

    print(
        metadata["file_path"]
    )

    print(
        "-" * 50
    )

    print(
        results["documents"][0][idx][:500]
    )