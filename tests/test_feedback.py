from feedback.logger import log_feedback
from feedback.metrics import MetricsCollector


def test_log_feedback_records_interaction() -> None:
    result = log_feedback(
        interacao_id="int-100",
        util=True,
        editado=False,
        comentario="Resposta útil e clara.",
    )

    assert result["interacao_id"] == "int-100"
    assert result["util"] is True
    assert result["status"] == "logged"


def test_metrics_collector_tracks_feedback_summary() -> None:
    collector = MetricsCollector()
    collector.record("int-100", 0.92, True, False)
    collector.record("int-101", 0.74, False, True)

    summary = collector.snapshot()

    assert summary["total_interactions"] == 2
    assert summary["positive_feedback"] == 1
    assert summary["edited_feedback"] == 1
    assert summary["avg_confidence"] >= 0.0
