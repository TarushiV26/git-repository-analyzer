import pandas as pd

def contributor_stats(commits):
    if not commits:
        return pd.DataFrame(columns=["Contributor", "Commits", "Latest commit"])
    df = pd.DataFrame(commits)
    result = (df.groupby("author")
                .agg(Commits=("hash", "count"), Latest=("date", "max"))
                .reset_index()
                .rename(columns={"author": "Contributor", "Latest": "Latest commit"})
                .sort_values(["Commits", "Contributor"], ascending=[False, True]))
    result["Latest commit"] = result["Latest commit"].dt.strftime("%Y-%m-%d")
    return result
