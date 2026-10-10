from collections import Counter
import pandas as pd

def monthly_activity(commits):
    if not commits:
        return pd.DataFrame(columns=["Month", "Commits"])
    counts = Counter(c["date"].strftime("%Y-%m") for c in commits)
    return pd.DataFrame(sorted(counts.items()), columns=["Month", "Commits"])

def frequent_files(commits):
    counts = Counter()
    for commit in commits:
        counts.update(set(commit.get("files", [])))
    return pd.DataFrame(
        sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:20],
        columns=["File", "Changes across commits"]
    )
