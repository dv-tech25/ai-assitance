from services.rag_service import answer_question


question = "What happens if a student cheats during an online test?"


answer = answer_question(question)


print("\nQUESTION:")

print(question)


print("\nANSWER:")

print(answer)