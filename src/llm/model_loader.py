import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)

class ModelLoader:
    _model = None
    _tokenizer = None

    @classmethod
    def load(
        cls,
        model_name
    ):
        if cls._model is not None:
            return (
                cls._model,
                cls._tokenizer
            )

        print("Loading tokenizer...")

        cls._tokenizer = (
            AutoTokenizer.from_pretrained(
                model_name
            )
        )

        device = (
            "mps"
            if torch.backends.mps.is_available()
            else "cpu"
        )

        print(
            f"Using device: {device}"
        )

        print("Loading model weights...")

        cls._model = (
            AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16
                if device == "mps"
                else torch.float32
            )
        )

        print(
            "Moving model to device..."
        )

        cls._model.to(device)

        print(
            "LLM ready"
        )

        return (
            cls._model,
            cls._tokenizer
        )