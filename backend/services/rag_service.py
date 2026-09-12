from services.retrieval_service import search_documents
from services.llm_service import generate_answer


def answer_question(question):

    # Step 1: Search relevant documents
    results = search_documents(question)

    # Step 2: Extract retrieved chunks
    documents = results["documents"][0]

    # Step 3: Combine chunks into context
    context = "\n\n".join(documents)

    # Step 4: Generate answer using LLM
    answer = generate_answer(
        question,
        context
    )

    return answer