def log_feedback(
    interacao_id: str,
    util: bool,
    editado: bool,
    comentario: str | None = None,
    confianca: float | None = None,
) -> dict:
    return {
        "interacao_id": interacao_id,
        "util": util,
        "editado": editado,
        "comentario": comentario,
        "confianca": confianca,
        "status": "logged",
    }


class FeedbackLogger:
    def __init__(self) -> None:
        self.events: list[dict] = []

    def log(
        self,
        interacao_id: str,
        util: bool,
        editado: bool,
        comentario: str | None = None,
        confianca: float | None = None,
    ) -> dict:
        event = log_feedback(
            interacao_id=interacao_id,
            util=util,
            editado=editado,
            comentario=comentario,
            confianca=confianca,
        )
        self.events.append(event)
        return event
