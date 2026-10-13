from git import Repo

from src.repository import analyze_repository


def test_empty_repository_returns_zero_counts(tmp_path):
    Repo.init(tmp_path)

    result = analyze_repository(tmp_path)

    assert result["commit_count"] == 0
    assert result["contributor_count"] == 0
    assert result["branch_count"] == 0
    assert result["file_count"] == 0
    assert result["commits"] == []
    assert result["first_commit"] == ""
    assert result["latest_commit"] == ""
    assert result["latest_date"] == ""
