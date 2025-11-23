from llm import ask_llm

def explain_concept(user_request):
    prompt = f"""
    You are an AI Python tutor.

    The user asked: "{user_request}"

    Explain the concept clearly, with:
    - a simple explanation
    - at least one analogy
    - an example
    """
    return ask_llm(prompt)

def generate_example(user_request):
    prompt = f"""
    Generate a Python example for: "{user_request}"

    Include:
    - Code with comments
    - A short explanation after
    """
    return ask_llm(prompt)

def debug_code(user_request):
    prompt = f"""
    The user has a bug in their code.

    Request:
    {user_request}

    Explain:
    - The error
    - Why it happens
    - How to fix it
    - A corrected version of the code
    """
    return ask_llm(prompt)

def create_exercise(user_request):
    prompt = f"""
    Create a short Python exercise based on: "{user_request}"

    Include:
    - A problem statement
    - Hints (but not the answer)
    - Difficulty level (Beginner / Intermediate / Advanced)
    """
    return ask_llm(prompt)


def give_feedback(user_request):
    prompt = f"""
    Give constructive feedback.

    User answer or code:
    {user_request}

    Provide:
    - Identify correct aspects
    - A correction (if needed)
    - Encouragement and potential steps
    """
    return ask_llm(prompt)