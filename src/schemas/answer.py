from dataclasses import dataclass

@dataclass
class GeneratedAnswer:
    question: str
    answer: str
    model_name: str