# Rule-Based AI Chatbot

## Objective

Create a simple Python chatbot that replies to predefined user inputs with
deterministic rules. This is a rule-based project, not a machine-learning or
generative-AI chatbot.

## Features

- Runs continuously in the terminal until the user enters an exit command.
- Cleans input using `lower()` and `strip()` before matching it with a rule.
- Handles greetings, farewells, name questions, help, thanks, capabilities,
  and rule-based AI information.
- Stores phrases and predefined responses in dictionaries.
- Uses `.get()` to retrieve a response safely.
- Provides a fallback response for unsupported questions.
- Uses only built-in Python concepts and no external packages.

## Technologies Used

- Python 3
- Basic Python strings, sets, dictionaries, functions, `if` statements, and a
  `while` loop

## How to Run

1. Open a terminal in the project folder.
2. Run:

   ```powershell
   python chatbot.py
   ```

3. Type a supported message, such as `hello`, `help`, or `what can you do`.
4. Type `bye`, `exit`, `quit`, or `goodbye` to finish the conversation.

## Sample Interaction

```text
Bot: Hello! I respond using predefined rules.
You: what is your name?
Bot: I am a simple rule-based AI chatbot.

You: thank you
Bot: You're welcome!

You: bye
Bot: Goodbye! Have a great day!
```

## Future Improvements

1. Add more predefined topics such as the date, time, or basic Python facts.
2. Display a conversation counter to show the number of user messages.
3. Add a simple, safe calculator for basic arithmetic.
