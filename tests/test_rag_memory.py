from src.rag.rag_pipeline import RAGPipeline


def test_conversation_memory():

    print("Initializing RAG pipeline...")

    rag = RAGPipeline()

    print("\nQuestion 1:")
    q1 = """
    Explain the purpose of a current mirror
    and how it works in CMOS analog circuits in detail.
    """
    print(q1)
    answer1 = ""

    for output in rag.ask(q1):

        if output["type"] == "token":
            print(output["content"], end="", flush=True)
            answer1 += output["content"]

        elif output["type"] == "final":
            print("\n\nFirst answer completed.")

    print("\n\n--------------------------------\n")

    print("Question 2:")
    q2 = """
    How this is used in differential ampliefier? Explain mathematical equations and some practical examples.
    """
    print(q2)
    answer2 = ""

    for output in rag.ask(q2):

        if output["type"] == "token":
            print(output["content"], end="", flush=True)
            answer2 += output["content"]

        elif output["type"] == "final":
            print("\n\nSecond answer completed.")

    print("\n\n========== Memory Test ==========")

    assert len(answer1) > 0
    assert len(answer2) > 0

    # Check whether second response is related to current mirror
    keywords = [
        "current mirror",
        "mirror",
        "MOS",
        "CMOS",
        "transistor",
        "mismatch",
        "output resistance"
    ]

    matched = [
        word
        for word in keywords
        if word.lower() in answer2.lower()
    ]

    print(
        "Memory related keywords found:",
        matched
    )

    assert len(matched) > 0

    print("\nMemory test passed.")


if __name__ == "__main__":
    test_conversation_memory()