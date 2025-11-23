from llm import ask_llm
import modules

def main():
    print("AI Python Tutor — type 'quit' to exit")

    while True:
        user = input("\nYou: ")

        if user.lower() == "quit":
            break

        # Simple routing rules
        if "explain" in user.lower():
            print(modules.explain_concept(user))
        elif "example" in user.lower():
            print(modules.generate_example(user))
        elif "def" in user.lower() or "error" in user.lower() or "doesn't work" in user.lower():
            print(modules.debug_code(user))
        elif "exercise" in user.lower():
            print(modules.create_exercise(user))
        else:
            print(modules.give_feedback(user))


if __name__ == "__main__":
    main()