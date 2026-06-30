import time

from src.rag.rag_pipeline import RAGPipeline


def test_rag_stream():

    print("Initializing RAG pipeline...")

    rag = RAGPipeline()

    query = (
        """
            Explain the purpose of a current mirror
            and how it works in CMOS analog circuits.
        """
    )

    print("\nStarting stream...\n")

    full_answer = ""

    start = time.time()

    for output in rag.ask(query):

        if output["type"] == "token":

            token = output["content"]

            full_answer += token

            print(
                token,
                end="",
                flush=True
            )

        elif output["type"] == "final":

            print("\n\nGeneration completed.")

            print(
                "\nTime:",
                f"{time.time() - start:.2f}s"
            )

            print(
                "\nSources:"
            )

            for source in output["sources"]:
                print(source)

            assert output["answer"] is not None
            assert len(output["answer"]) > 0

    assert len(full_answer) > 0

    print("\n\nTest passed.")


if __name__ == "__main__":
    test_rag_stream()