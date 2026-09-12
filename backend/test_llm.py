from services.llm_service import generate_answer


question = "What happens if a student cheats during an online test?"


context = """
If any student is caught in any cheating activities during the online test,
he/she will be debarred from the complete campus since it affects the name
and reputation of the institute.
"""


answer = generate_answer(
    question,
    context
)


print(answer)