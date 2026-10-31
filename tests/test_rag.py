from core.rag import RAGKnowledgeBase


def test_rag_returns_relevant_articles_for_password_reset() -> None:
    kb = RAGKnowledgeBase()
    results = kb.search("preciso resetar minha senha e não consigo entrar")

    assert len(results) >= 1
    assert any(result["titulo"] == "Reset de senha e bloqueio de conta" for result in results)
    assert results[0]["score"] >= 0.5
