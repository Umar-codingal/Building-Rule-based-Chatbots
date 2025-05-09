# Enhanced Rule-based Chatbot

def chatbot_response(user_input):
    # Predefined responses based on user input
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a program, but I'm here to help you!",
        "what is your name": "I am a rule-based chatbot. What's your name?",
        "what can you do": "I can answer basic questions and have simple conversations with you.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! Let me know if you need anything else.",
        "help": "Sure! You can ask me things like 'What is your name?', 'Tell me a joke', or just say 'hello'.",
    }

    # Normalize user input
    user_input = user_input.lower()

    # Check if input matches a predefined response
    return responses.get(user_input, "I'm sorry, I don't understand that. Could you rephrase?")

def main():
    print("Chatbot: Hello! I am an enhanced rule-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()