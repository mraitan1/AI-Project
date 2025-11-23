from router import route

def main():
    print("AI Python Tutor — type 'quit' to exit")

    while True:
        user = input("\nYou: ")

        if user.lower() == "quit":
            break

        print(route(user))

if __name__ == "__main__":
    main()