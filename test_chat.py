from agents.chat_agent import chat_with_pharmacy

print("Welcome to Agentic Pharmacy! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chat_with_pharmacy(user_input)
    print("Pharmacy Agent:", response)
