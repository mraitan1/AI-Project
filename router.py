import modules
from llm import ask_llm


def route(user_input):
    text = user_input.lower()

    # Simple routing rules
    if "explain" in text:
        return modules.explain_concept(user_input)
    elif "example" in text:
        return modules.generate_example(user_input)
    elif "def" in text or "error" in text or "doesn't work" in text:
        return modules.debug_code(user_input)
    elif "exercise" in text:
        return modules.create_exercise(user_input)
    elif"feedback" in text:
        return modules.give_feedback(user_input)
    else:
        return ask_llm(user_input)