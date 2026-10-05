"""Rule-Based AI Chatbot.

This project uses only predefined rules and responses. It does not use
machine learning, APIs, databases, or external libraries.
"""


# Each intent groups phrases that have the same meaning.
INTENT_PHRASES = {
    "greeting": {
        "hello",
        "hi",
        "hey",
        "good morning",
        "good evening",
    },
    "farewell": {
        "bye",
        "exit",
        "quit",
        "goodbye",
    },
    "name": {
        "what is your name",
        "who are you",
        "tell me your name",
    },
    "help": {
        "help",
        "what can i ask",
        "how can you help me",
    },
    "thanks": {
        "thank you",
        "thanks",
        "thankyou",
    },
    "capabilities": {
        "what can you do",
        "what are your capabilities",
        "what do you do",
    },
    "about": {
        "what is rule based ai",
        "what is a rule based chatbot",
        "about chatbot",
    },
}


# This dictionary is the chatbot's predefined knowledge base.
RESPONSES = {
    "greeting": "Hello! How can I help you?",
    "farewell": "Goodbye! Have a great day!",
    "name": "I am a simple rule-based AI chatbot.",
    "help": (
        "You can ask me about my name, capabilities, or rule-based AI. "
        "You can also say hello or type goodbye to exit."
    ),
    "thanks": "You're welcome!",
    "capabilities": "I can respond to predefined questions and commands.",
    "about": (
        "A rule-based chatbot follows predefined rules to choose a response. "
        "It does not learn from data."
    ),
}

FALLBACK_RESPONSE = "Sorry, I don't understand that yet. Please try another question."


def sanitize_input(user_input):
    """Return input in a consistent form for comparing with predefined rules."""
    return user_input.lower().strip().rstrip("?.!")


def get_response(cleaned_input):
    """Find and return the predefined response that matches the user's input."""
    for intent, phrases in INTENT_PHRASES.items():
        if cleaned_input in phrases:
            return RESPONSES.get(intent, FALLBACK_RESPONSE)

    return FALLBACK_RESPONSE


def chatbot():
    """Run the chatbot until the user enters a farewell command."""
    print("=" * 60)
    print("                 RULE-BASED AI CHATBOT")
    print("=" * 60)
    print("Bot: Hello! I respond using predefined rules.")
    print("Bot: Type 'help' to see supported topics.")
    print("Bot: Type 'bye', 'exit', 'quit', or 'goodbye' to end the chat.\n")

    # The while loop keeps the conversation running continuously.
    while True:
        user_input = input("You: ")
        cleaned_input = sanitize_input(user_input)

        # Check exit commands before continuing the conversation.
        if cleaned_input in INTENT_PHRASES["farewell"]:
            print(f"Bot: {RESPONSES.get('farewell')}\n")
            break

        response = get_response(cleaned_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    chatbot()
