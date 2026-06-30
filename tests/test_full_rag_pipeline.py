from src.rag.rag_pipeline import RAGPipeline



def print_result(title, result):

    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)


    print("\nRewritten Query:")
    print(result["rewritten_query"])


    print("\nAnswer:")
    print(result["answer"])


    print("\nSources:")

    for source in result["sources"]:
        print(source)




def main():

    rag = RAGPipeline()



    # -------------------------------
    # Query 1
    # -------------------------------

    query1 = """
    Explain the working principle of Current Mirror.
    Describe the current mirror architecture.
    """


    result1 = rag.ask(
        query=query1,
        retrieve_k=20,
        rerank_k=5
    )


    print_result(
        "QUERY 1 RESULT",
        result1
    )



    # -------------------------------
    # Query 2 (depends on Query 1)
    # -------------------------------

    query2 = """
    What some mathematical equation related to that?
    """


    result2 = rag.ask(
        query=query2,
        retrieve_k=20,
        rerank_k=5
    )


    print_result(
        "QUERY 2 RESULT",
        result2
    )




if __name__ == "__main__":
    main()