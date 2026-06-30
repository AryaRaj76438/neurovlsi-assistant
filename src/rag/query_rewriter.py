from src.schemas.rewrite import RewrittenQuery


class QueryRewriter:
    """
    Converts conversational queries
    into standalone retrieval queries.
    """

    def rewrite(
        self,
        query: str,
        conversation_history=None
    ) -> RewrittenQuery:

        # No conversation
        if not conversation_history:
            return RewrittenQuery(
                original_query=query,
                rewritten_query=query,
                rewritten=False
            )

        previous_history = conversation_history[:-1]


        if not previous_history:
            return RewrittenQuery(
                original_query=query,
                rewritten_query=query,
                rewritten=False
            )


        last_context = previous_history[-1]


        rewritten_query = (
            f"{query}. "
            f"Related previous context: {last_context}"
        )


        return RewrittenQuery(
            original_query=query,
            rewritten_query=rewritten_query,
            rewritten=True
        )