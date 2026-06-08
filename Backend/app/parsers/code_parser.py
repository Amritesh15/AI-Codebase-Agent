import os

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".java",
    ".go",
    ".cs"
}


def get_source_files(repo_path):
    source_files = []

    for root, dirs, files in os.walk(repo_path):

        # Ignore common junk folders
        dirs[:] = [
            d for d in dirs
            if d not in {
                ".git",
                "node_modules",
                "__pycache__",
                "venv",
                ".next",
                "dist",
                "build"
            }
        ]

        for file in files:
            ext = os.path.splitext(file)[1]

            if ext in SUPPORTED_EXTENSIONS:
                source_files.append(
                    os.path.join(root, file)
                )

    return source_files


def read_file(file_path):
    try:
        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:
            return f.read()

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def chunk_text(
    text,
    chunk_size=1000,
    overlap=200
):
    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            text[start:end]
        )

        start += chunk_size - overlap

    return chunks