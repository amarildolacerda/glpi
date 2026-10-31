from __future__ import annotations


class LLMAdapter:
    def generate(self, pergunta: str, artigos: list[dict] | None = None) -> dict:
        cleaned = (pergunta or "").lower()
        artigos = artigos or []

        if any(token in cleaned for token in ["senha", "login", "acesso", "autentic", "reset"]):
            categoria = "senha"
            urgencia = 4
            impacto = 3
            confianca = 0.93
            resposta = (
                "Recomendo validar a identidade do usuário, confirmar se a conta está bloqueada "
                "ou se a senha precisa ser redefinida, e revisar se o problema afeta outros acessos."
            )
        elif any(token in cleaned for token in ["erro", "falha", "indispon", "quebra"]):
            categoria = "suporte"
            urgencia = 3
            impacto = 4
            confianca = 0.88
            resposta = (
                "Sugiro confirmar a falha relatada, verificar impactos recentes e revisar se o problema "
                "afeta mais de um usuário ou serviço antes de qualquer ação definitiva."
            )
        else:
            categoria = "suporte"
            urgencia = 3
            impacto = 3
            confianca = 0.84
            resposta = (
                "Sugestão inicial: revisar o contexto do ticket, confirmar a exigência do usuário e "
                "aplicar a categoria correta antes da aprovação final."
            )

        if artigos:
            top_article = artigos[0]
            article_title = top_article.get("titulo", "artigo de suporte")
            resposta = (
                f"{resposta} Baseado em '{article_title}', valide o contexto do artigo mais relevante antes "
                "de concluir o atendimento."
            )

        return {
            "resposta": resposta,
            "categoria": categoria,
            "urgencia": urgencia,
            "impacto": impacto,
            "confianca": confianca,
        }
