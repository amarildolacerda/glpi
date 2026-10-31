def log_feedback(interacao_id: str, util: bool, editado: bool, comentario: str | None = None) -> dict:
    return {
        "interacao_id": interacao_id,
        "util": util,
        "editado": editado,
        "comentario": comentario,
        "status": "logged",
    }
