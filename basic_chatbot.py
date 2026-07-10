# Function to generate chatbot responses
def chatbot():
    print("===== Welcome to Basic Chatbot =====")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user_input == "i am fine":
            print("Bot: That's great to hear!")

        elif user_input == "what is your name":
            print("Bot: I am a simple Python Chatbot.")

        elif user_input == "who created you":
            print("Bot: I was created using Python.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Call the function
chatbot()