import os 
from app.parsers.code_parser import (
    get_source_files,
    read_file,
    chunk_text
)


def parse_repository(repo_path):

    all_chunks = []

    files = get_source_files(repo_path)

    for file_path in files:

        content = read_file(file_path)

        chunks = chunk_text(content)

        for idx, chunk in enumerate(chunks):

            all_chunks.append(
                    {
                        "file_path": file_path,
                        "file_name": os.path.basename(file_path),
                        "extension": os.path.splitext(file_path)[1],
                        "chunk_id": idx,
                        "content": chunk
                    }
            )

    return all_chunks