from src.schemas.prompt import PromptPackage


class PromptBuilder:
    """
    Builds the final prompt sent to the LLM.

    Input
    -----
    grounded_context : GroundedContext

    history : List[dict]
        [
            {
                "role": "user",
                "content": "..."
            },
            {
                "role": "assistant",
                "content": "..."
            }
        ]

    Returns
    -------
    PromptPackage
    """

    def __init__(self):
        pass

    def build(
        self,
        grounded_context,
        history=None
    ):
        system_prompt = """
You are NeuroVLSI.

You are an expert semiconductor engineering assistant.

Rules:

1. Use ONLY the provided evidence.
2. Never invent facts.
3. If evidence is insufficient, explicitly say:
   "The provided evidence does not contain enough information."
4. Always explain technical concepts clearly.
5. Always cite supporting evidence using:
   [Source X]
6. Do not reference knowledge outside the evidence.
7. Prefer detailed engineering explanations.
8. When possible explain:
   - theory
   - operation
   - design implications
   - practical usage
""".strip()

        history_text = ""

        if history:

            history_lines = []

            for item in history:
                history_lines.append(
                    f"{item['role'].upper()}: "
                    f"{item['content']}"
                )

            history_text = (
                "Conversation History\n"
                "====================\n\n"
                + "\n\n".join(history_lines)
            )

        evidence_blocks = []

        for idx, source in enumerate(
            grounded_context.sources,
            start=1
        ):
            evidence_blocks.append(
                f"""
[Source {idx}]

Document: {source.source}
Page: {source.page}

{source.evidence}
""".strip()
            )

        evidence_text = "\n\n".join(
            evidence_blocks
        )

        user_prompt = f"""
Question
========

{grounded_context.query}

Evidence
========

{evidence_text}

Instructions
============

Answer the question using ONLY the evidence.

Required format:

1. Direct answer
2. Technical explanation
3. Important engineering observations
4. Citations

Example citation:

[Source 1]

If evidence is insufficient, say so.
""".strip()

        full_prompt_parts = [
            system_prompt
        ]

        if history_text:
            full_prompt_parts.append(
                history_text
            )

        full_prompt_parts.append(
            user_prompt
        )

        full_prompt = "\n\n".join(
            full_prompt_parts
        )

        return PromptPackage(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            full_prompt=full_prompt
        )