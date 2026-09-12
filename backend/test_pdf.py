# from services.document_service import read_pdf
# from services.chunk_service import create_chunks
# from services.embedding_service import create_embeddings
# from services.vector_service import store_chunks


# file_path = "data/pdfs/placement_policy.pdf"


# STEP 1: Read PDF
# text = read_pdf(file_path)


# STEP 2: Create chunks
# chunks = create_chunks(text)


# STEP 3: Create embeddings
# embeddings = create_embeddings(chunks)


# STEP 4: Store in ChromaDB
# collection = store_chunks(chunks, embeddings)


# print("Data successfully stored in ChromaDB")


# print("Total chunks stored:", collection.count())



# searching_query 

from services.retrieval_service import search_documents


question = "What happens if a student cheats during an online test?"


results = search_documents(question)


print("\nQUESTION:")

print(question)


print("\nRELEVANT DOCUMENTS:\n")


for document in results["documents"][0]:

    print("=" * 50)

    print(document)

    print("=" * 50)