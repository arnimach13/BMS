def greet_user():
    print("Chatbot: Hello! I'm your Python chatbot.")
    print("Chatbot: Type 'bye' anytime to exit.\n")


def get_response(user):
    user = user.lower()

    if "bye" in user:
        return "exit"

    elif "hello" in user or "hi" in user:
        return "Hello! How can I help you?"

    elif "your name" in user:
        return "I'm a chatbot created using Python functions."

    elif "age" in user:
        return "I don't have an age, but I'm always active!"

    elif "how are you" in user:
        return "I'm doing great! What about you?"

    elif "weather" in user:
        return "I can't check weather, but I hope it's sunny!"

    elif "college" in user:
        return "College life is exciting! What do you want to know?"

    elif "sad" in user:
        return "I'm sorry you're sad. I'm here if you want to talk."

    elif "thank" in user:
        return "You're welcome!"

    else:
        return "Sorry, I didn't understand that."


def chatbot():
    greet_user()

    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        if response == "exit":
            print("Chatbot: Bye! Have a great day!")
            break
        else:
            print("Chatbot:", response)


chatbot()
