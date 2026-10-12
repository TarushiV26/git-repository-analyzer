
import pandas as pd

from src.insights import activity_insights


def test_activity_increases():
    data = pd.DataFrame({
        "Month": ["2026-08", "2026-09"],
        "Commits": [10, 15],
    })
    result = activity_insights(data)
    assert result["change_percent"] == 50.0
    assert "increased" in result["message"]


def test_activity_decreases():
    data = pd.DataFrame({
        "Month": ["2026-08", "2026-09"],
        "Commits": [20, 10],
    })
    result = activity_insights(data)
    assert result["change_percent"] == -50.0
    assert "decreased" in result["message"]


def test_empty_activity():
    result = activity_insights(
        pd.DataFrame(columns=["Month", "Commits"])
    )
    assert result["change_percent"] is None


def test_single_month():
    data = pd.DataFrame({
        "Month": ["2026-09"],
        "Commits": [5],
    })
    result = activity_insights(data)
    assert result["change_percent"] is None
    assert "Only one month" in result["message"]
