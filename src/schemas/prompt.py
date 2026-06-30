from dataclasses import dataclass

@dataclass
class PromptPackage:
    system_prompt: str
    user_prompt: str
    full_prompt: str