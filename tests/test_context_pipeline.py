from src.rag.rag_pipeline import RAGPipeline



def main():


    rag = RAGPipeline()


    query = """
    Explain how a current mirror works in CMOS
    and why it is used in analog circuits.
    """



    result = rag.ask(
        query=query,
        retrieve_k=20,
        rerank_k=5
    )



    print("\n")
    print("="*80)
    print("ANSWER")
    print("="*80)


    print(result["answer"])



    print("\n")
    print("="*80)
    print("SOURCES")
    print("="*80)



    for source in result["sources"]:

        print(
            source.source,
            source.page
        )



if __name__=="__main__":
    main()