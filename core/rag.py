from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class KnowledgeArticle:
    id: int
    titulo: str
    conteudo: str
    tags: list[str] = field(default_factory=list)


class RAGKnowledgeBase:
    def __init__(self) -> None:
        self.documents = [
            KnowledgeArticle(
                id=1,
                titulo="Reset de senha e bloqueio de conta",
                conteudo=(
                    "Quando o usuário informa que não consegue acessar o sistema por senha, "
                    "o procedimento seguro é validar identidade, reiniciar a senha e verificar "
                    "se a conta está bloqueada por tentativas ou política de segurança."
                ),
                tags=["senha", "login", "acesso", "bloqueio", "reset"],
            ),
            KnowledgeArticle(
                id=2,
                titulo="Liberação de acesso para novo usuário",
                conteudo=(
                    "Para liberação de acesso, confirmar perfil solicitado, validar necessidade, "
                    "aplicar permissões mínimas e registrar a aprovação do responsável."
                ),
                tags=["acesso", "permissao", "perfil", "usuario"],
            ),
            KnowledgeArticle(
                id=3,
                titulo="Falha de sistema e indisponibilidade",
                conteudo=(
                    "Em casos de falha operacional, confirmar impacto, revisar ocorrências recentes, "
                    "verificar se afeta mais de um usuário e registrar a severidade antes do encaminhamento."
                ),
                tags=["falha", "erro", "indisponibilidade", "sistema"],
            ),
        ]

    def search(self, query: str, limit: int = 3) -> list[dict]:
        if not query or not query.strip():
            return []

        alias_map = {
            "resetar": "reset",
            "senha": "senha",
            "entrar": "acesso",
            "acesso": "acesso",
            "login": "login",
            "autentic": "autenticacao",
            "bloqueio": "bloqueio",
            "falha": "falha",
            "erro": "erro",
            "indispon": "indisponibilidade",
            "permiss": "permissao",
            "perfil": "perfil",
        }

        normalized_query = query.lower().replace("?", " ")
        tokens = [token.strip() for token in normalized_query.split() if token.strip()]
        if not tokens:
            return []

        relevant_words = []
        for token in tokens:
            normalized = token.rstrip("s")
            relevant_words.append(alias_map.get(normalized, normalized))

        scored: list[dict] = []
        for article in self.documents:
            haystack = " ".join([article.titulo, article.conteudo, *article.tags]).lower()
            matched = 0
            for word in relevant_words:
                if word in haystack:
                    matched += 1

            score = matched / max(len(set(relevant_words)), 1)
            if score > 0:
                scored.append(
                    {
                        "id": article.id,
                        "titulo": article.titulo,
                        "score": round(score, 2),
                        "conteudo": article.conteudo,
                    }
                )

        return sorted(scored, key=lambda item: item["score"], reverse=True)[:limit]
