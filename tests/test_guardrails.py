from core.guardrails import Guardrails


def test_guardrails_block_unsafe_action_without_human_approval() -> None:
    guardrails = Guardrails()
    result = guardrails.validate(
        resposta="Vou liberar acesso administrativo imediato sem revisão.",
        requires_approval=True,
    )

    assert result["aprovacao_humana"] is True
    assert result["seguro"] is False
    assert result["motivo"]


def test_guardrails_allow_safe_password_guidance() -> None:
    guardrails = Guardrails()
    result = guardrails.validate(
        resposta="Valide a identidade do usuário e siga o fluxo de reset de senha.",
        requires_approval=False,
    )

    assert result["aprovacao_humana"] is False
    assert result["seguro"] is True
