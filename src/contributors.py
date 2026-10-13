
import pandas as pd


def contributor_stats(commits):
    columns = ["Contributor", "Commits", "Latest commit"]

    if not commits:
        return pd.DataFrame(columns=columns)

    df = pd.DataFrame(commits)

    # Convert every commit date to a consistent datetime type.
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce",
        utc=True,
    )

    result = (
        df.groupby("author", dropna=False)
        .agg(
            Commits=("hash", "count"),
            Latest=("date", "max"),
        )
        .reset_index()
        .rename(
            columns={
                "author": "Contributor",
                "Latest": "Latest commit",
            }
        )
        .sort_values(
            ["Commits", "Contributor"],
            ascending=[False, True],
        )
    )

    # Format valid dates; show N/A if no valid date exists.
    result["Latest commit"] = result["Latest commit"].apply(
        lambda value: (
            value.strftime("%Y-%m-%d")
            if pd.notna(value)
            else "N/A"
        )
    )

    return result[columns]
