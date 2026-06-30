from src.rag.conversation_memory import ConversationMemory

memory = ConversationMemory(
    max_turns=2
)

memory.add_user_message(
    "What is a current mirror?"
)

memory.add_assistant_message(
    "Current mirrors copy current."
)

memory.add_user_message(
    "Why are they used?"
)

memory.add_assistant_message(
    "Bias generation."
)

memory.add_user_message(
    "What is cascode mirror?"
)

print(
    memory.get_history()
)