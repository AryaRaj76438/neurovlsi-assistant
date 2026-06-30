class ConversationMemory:
    """
    Stores recent conversation turns.

    Parameters
    ----------
    max_turns : int
        Number of user/assistant exchanges
        to keep in memory.
    """

    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = []

    def add_user_message(self, message):
        self.history.append(
            {
                "role": "user",
                "content": message
            }
        )

        self._trim()

    def add_assistant_message(self, message):
        self.history.append(
            {
                "role": "assistant",
                "content": message
            }
        )

        self._trim()

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []

    def _trim(self):
        max_messages = self.max_turns * 2

        if len(self.history) > max_messages:
            self.history = self.history[-max_messages:]