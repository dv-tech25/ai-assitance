import chromadb

from services.embedding_service import model


def search_documents(query):

    # Connect to existing ChromaDB
    client = chromadb.PersistentClient(
        path="vector_db"
    )

    # Get existing collection
    collection = client.get_collection(
        name="placement_documents"
    )

    # Convert question into embedding
    query_embedding = model.encode(query)

    # Search database
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    return results