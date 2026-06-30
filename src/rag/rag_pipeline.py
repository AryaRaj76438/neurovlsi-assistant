from src.retrieval.retrieval_pipeline import RetrievalPipeline
from src.rag.context_builder import ContextBuilder
from src.rag.answer_grounder import AnswerGrounder
from src.rag.prompt_builder import PromptBuilder
from src.llm.local_llm import LocalLLM
from src.rag.citation_injector import CitationInjector
from src.rag.conversation_memory import ConversationMemory
from src.rag.query_rewriter import QueryRewriter

class RAGPipeline:
    """
    Main NeuroVLSI QA pipeline.

    Input
    -----
    query : str

    Output
    ------
    {
        "answer": str,
        "sources": List[GroundedSource]
    }
    """

    def __init__(self):
        self.retrieval = RetrievalPipeline()
        self.context_builder = ContextBuilder()
        self.grounder = AnswerGrounder()
        self.prompt_builder = PromptBuilder()
        self.llm = LocalLLM()
        self.citation_injector = CitationInjector()
        self.memory = ConversationMemory()
        self.query_rewriter = QueryRewriter()

    def ask(
        self,
        query,
        retrieve_k=20,
        rerank_k=5
    ):
        self.memory.add_user_message(query)

        rewritten = self.query_rewriter.rewrite(
            query=query,
            conversation_history=self.memory.get_history()
        )

        retrieval_query = rewritten.rewritten_query

        ranked_chunks = self.retrieval.retrieve(
            query=retrieval_query,
            retrieve_k=retrieve_k,
            rerank_k=rerank_k
        )

        # ranked_chunks = self.retrieval.retrieve(
        #     query=query,
        #     retrieve_k=retrieve_k,
        #     rerank_k=rerank_k
        # )

        context = self.context_builder.build(
            query=query,
            ranked_chunks=ranked_chunks
        )

        grounded_sources = self.grounder.ground(
            query=query,
            chunks=context.documents
        )

        prompt = self.prompt_builder.build(
            grounded_context=grounded_sources,
            history=self.memory.get_history()
        )

        
        # answer = self.llm.generate(
        #     prompt.full_prompt
        # )

        answer = ""
        for token in self.llm.generate_stream(prompt.full_prompt):
            answer += token
            yield {
                "type": "token",
                "content": token
            }


        self.memory.add_assistant_message(answer)

        final_answer = (
            self.citation_injector.inject(
                answer=answer,
                sources=grounded_sources.sources
            )
        )

        return {
            "answer": final_answer,
            "sources": grounded_sources.sources,
            "rewritten_query": retrieval_query
        }