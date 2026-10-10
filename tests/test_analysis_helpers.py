from datetime import datetime
from src.activity import monthly_activity, frequent_files
from src.contributors import contributor_stats
from src.branches import branch_stats

def sample_commits():
    return [
        {"hash":"a1","author":"Asha","date":datetime(2026,1,2),"files":["app.py","README.md"]},
        {"hash":"b2","author":"Ravi","date":datetime(2026,1,3),"files":["app.py"]},
        {"hash":"c3","author":"Asha","date":datetime(2026,2,1),"files":["tests/test_app.py"]},
    ]

def test_monthly_activity_counts_commits():
    df = monthly_activity(sample_commits())
    assert dict(zip(df["Month"], df["Commits"])) == {"2026-01": 2, "2026-02": 1}

def test_frequent_files_counts_commits_touching_file():
    df = frequent_files(sample_commits())
    assert dict(zip(df["File"], df["Changes across commits"]))["app.py"] == 2

def test_contributor_counts():
    df = contributor_stats(sample_commits())
    assert dict(zip(df["Contributor"], df["Commits"])) == {"Asha": 2, "Ravi": 1}

def test_empty_inputs():
    assert monthly_activity([]).empty
    assert frequent_files([]).empty
    assert contributor_stats([]).empty
    assert branch_stats([]).empty
