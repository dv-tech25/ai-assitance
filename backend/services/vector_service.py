import chromadb


def store_chunks(chunks, embeddings):

    client = chromadb.PersistentClient(
        path="vector_db"
    )

    collection = client.get_or_create_collection(
        name="placement_documents"
    )

    ids = []

    for index in range(len(chunks)):
        ids.append(f"chunk_{index}")

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )

    return collection