def basic_chatbot():
    print("🤖 ChatBot: Hello! Type something to talk to me. (Type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("ChatBot: Hi!")
        elif user_input in ["how are you", "how are you doing"]:
            print("ChatBot: I'm fine, thanks! How about you?")
        elif user_input in ["i'm fine", "i am fine", "good", "doing well"]:
            print("ChatBot: That's great to hear!")
        elif user_input in ["what is your name", "who are you"]:
            print("ChatBot: I'm a simple chatbot made in Python!")
        elif user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye! 👋")
            break
        else:
            print("ChatBot: Sorry, I don't understand that.")

# Run the chatbot
basic_chatbot()
