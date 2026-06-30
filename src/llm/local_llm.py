from threading import Thread
import time
import torch

from transformers import GenerationConfig as HFGenerationConfig, TextIteratorStreamer

from src.llm.model_loader import ModelLoader
from src.llm.response_parser import ResponseParser
from src.llm.generation_config import GenerationConfig
from src.core.config import load_settings


class LocalLLM:
    def __init__(self):
        print("Loading settings...")
        settings = load_settings()
        self.model_name = settings["models"]["llm"]["name"]

        print(f"Loading model: {self.model_name}")
        start = time.time()

        self.model, self.tokenizer = ModelLoader.load(self.model_name)

        print(f"Model loaded in {time.time() - start:.2f}s")

        self.parser = ResponseParser()

    def generate(self, prompt, config=None):
        print("Generate() called")

        if config is None:
            config = GenerationConfig()

        print("Building chat template...")

        messages = [{"role": "user", "content": prompt}]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        print("Tokenizing prompt...")

        inputs = self.tokenizer(text, return_tensors="pt")

        device = next(self.model.parameters()).device

        inputs = {
            key: value.to(device)
            for key, value in inputs.items()
        }

        print("Model Device:", device)
        print("Input Tokens:", inputs["input_ids"].shape)

        generation_config = HFGenerationConfig(
            temperature=config.temperature,
            top_p=config.top_p,
            max_new_tokens=config.max_new_tokens,
            do_sample=config.do_sample,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.eos_token_id
        )

        print("Starting generation...")

        start = time.time()

        with torch.inference_mode():
            outputs = self.model.generate(
                **inputs,
                generation_config=generation_config
            )

        print(f"Generation finished in {time.time() - start:.2f}s")

        print("Decoding output...")

        generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

        response = self.tokenizer.decode(
            generated_tokens,
            skip_special_tokens=True
        )

        print("Decoding finished")

        return self.parser.parse(response)
    

    def generate_stream(self, prompt, config=None):
        if config is None:
            config = GenerationConfig()

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        )

        device = next(self.model.parameters()).device

        inputs = {
            key: value.to(device)
            for key, value in inputs.items()
        }

        streamer = TextIteratorStreamer(
            self.tokenizer,
            skip_prompt=True,
            skip_special_tokens=True
        )

        generation_config = HFGenerationConfig(
            temperature=config.temperature,
            top_p=config.top_p,
            max_new_tokens=config.max_new_tokens,
            do_sample=config.do_sample,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.eos_token_id
        )

        generation_kwargs = dict(
            **inputs,
            generation_config=generation_config,
            streamer=streamer
        )

        thread = Thread(
            target=self.model.generate,
            kwargs=generation_kwargs
        )

        thread.start()

        for token in streamer:
            yield token