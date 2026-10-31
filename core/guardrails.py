from __future__ import annotations


class Guardrails:
    def validate(self, resposta: str, requires_approval: bool = False) -> dict:
        text = (resposta or "").lower()

        sensitive_markers = [
            "liberar acesso administrativo",
            "acesso total",
            "remover bloqueio",
            "desativar segurança",
            "conta privilegiada",
            "senha permanente",
            "resetar senha sem validação",
        ]

        if any(marker in text for marker in sensitive_markers):
            return {
                "seguro": False,
                "aprovacao_humana": True,
                "motivo": "Resposta contém ação sensível ou fora do escopo de segurança operacional.",
            }

        if requires_approval:
            return {
                "seguro": True,
                "aprovacao_humana": True,
                "motivo": "Ação crítica exige revisão humana antes da execução.",
            }

        return {
            "seguro": True,
            "aprovacao_humana": False,
            "motivo": "Resposta adequada ao contexto e segura para uso do assistente.",
        }
