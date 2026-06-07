from ingest import load_documents, chunk_document

documents = load_documents()

# Use the first document for testing
doc = documents[0]

chunks = chunk_document(doc["text"], doc["source"])

print(f"Total chunks: {len(chunks)}\n")

for chunk in chunks[:10]:
    print("=" * 80)
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Source: {chunk['source']}")
    print()
    print(chunk["text"])
    print()