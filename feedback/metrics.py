from __future__ import annotations


class MetricsCollector:
    def __init__(self) -> None:
        self.events: list[dict] = []

    def record(
        self,
        interacao_id: str,
        confianca: float = 0.0,
        util: bool = False,
        editado: bool = False,
        comentario: str | None = None,
        latency_ms: float | None = None,
    ) -> dict:
        metric = {
            "interacao_id": interacao_id,
            "confianca": confianca,
            "util": util,
            "editado": editado,
            "comentario": comentario,
            "latency_ms": latency_ms,
            "status": "recorded",
        }
        self.events.append(metric)
        return metric

    def snapshot(self) -> dict:
        total_interactions = len(self.events)
        positive_feedback = sum(1 for event in self.events if event["util"])
        edited_feedback = sum(1 for event in self.events if event["editado"])

        confidences = [event["confianca"] for event in self.events if event["confianca"] is not None]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0

        latencies = [event["latency_ms"] for event in self.events if event["latency_ms"] is not None]
        avg_latency_ms = sum(latencies) / len(latencies) if latencies else 0.0

        return {
            "total_interactions": total_interactions,
            "positive_feedback": positive_feedback,
            "edited_feedback": edited_feedback,
            "avg_confidence": avg_confidence,
            "avg_latency_ms": avg_latency_ms,
        }
