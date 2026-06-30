from dataclasses import dataclass


@dataclass
class GenerationConfig:
    temperature: float = 0.2
    top_p: float = 0.9
    max_new_tokens: int = 256
    do_sample: bool = True