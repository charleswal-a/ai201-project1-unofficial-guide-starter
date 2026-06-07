import os
from config import DOCS_PATH


def load_documents():
    """
    Load all .txt source documents from the docs folder.
    """

    documents = []

    for filename in sorted(os.listdir(DOCS_PATH)):

        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(DOCS_PATH, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        source_name = (
            filename.replace(".txt", "")
            .replace("_", " ")
            .title()
        )

        documents.append({
            "source": source_name,
            "filename": filename,
            "text": text
        })

    print(
        f"Loaded {len(documents)} document(s): "
        f"{[d['source'] for d in documents]}"
    )

    return documents

def chunk_document(text, source_name):
    """
    Split a source document into chunks ready for embedding.
    """

    chunk_size = 300
    overlap = 50
    min_length = 50

    chunks = []

    prefix = source_name.lower().replace(" ", "_")
    counter = 0

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk_text = text[start:end].strip()

        if len(chunk_text) >= min_length:

            chunks.append({
                "text": chunk_text,
                "source": source_name,
                "chunk_id": f"{prefix}_{counter}"
            })

            counter += 1

        start += chunk_size - overlap

    return chunks