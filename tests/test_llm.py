from core.llm import LLMAdapter


def test_llm_generates_structured_response_for_password_reset() -> None:
    adapter = LLMAdapter()
    result = adapter.generate(
        pergunta="Preciso resetar minha senha e não consigo entrar no sistema.",
        artigos=[
            {
                "titulo": "Reset de senha e bloqueio de conta",
                "conteudo": "Para reset de senha, valide identidade e confirme bloqueio de conta.",
                "score": 0.94,
            }
        ],
    )

    assert result["resposta"]
    assert result["categoria"] in {"acesso", "senha", "suporte"}
    assert 0.0 <= result["confianca"] <= 1.0
    assert result["urgencia"] >= 1
    assert result["impacto"] >= 1
