
import pandas as pd


def activity_insights(monthly_df):
    """Generate a comparison of the latest two months."""
    if monthly_df is None or monthly_df.empty:
        return {
            "latest_month": None,
            "latest_commits": 0,
            "previous_month": None,
            "previous_commits": 0,
            "change_percent": None,
            "message": "No commit activity is available yet.",
        }

    df = monthly_df[["Month", "Commits"]].copy()
    df["Month"] = pd.to_datetime(
        df["Month"], format="%Y-%m", errors="coerce"
    )
    df["Commits"] = pd.to_numeric(
        df["Commits"], errors="coerce"
    )
    df = df.dropna(subset=["Month", "Commits"])
    df = (
        df.groupby("Month", as_index=False)["Commits"]
        .sum()
        .sort_values("Month")
    )

    if df.empty:
        return {
            "latest_month": None,
            "latest_commits": 0,
            "previous_month": None,
            "previous_commits": 0,
            "change_percent": None,
            "message": "No valid monthly activity data is available.",
        }

    latest = df.iloc[-1]
    latest_month = latest["Month"].strftime("%b %Y")
    latest_count = int(latest["Commits"])

    if len(df) < 2:
        return {
            "latest_month": latest_month,
            "latest_commits": latest_count,
            "previous_month": None,
            "previous_commits": 0,
            "change_percent": None,
            "message": (
                "Only one month of activity is available. "
                "More history is needed for a comparison."
            ),
        }

    previous = df.iloc[-2]
    previous_month = previous["Month"].strftime("%b %Y")
    previous_count = int(previous["Commits"])

    if previous_count == 0:
        change = None
        message = (
            f"{latest_month} has {latest_count} commits. "
            f"{previous_month} had zero commits, so percentage "
            "change cannot be calculated."
        )
    else:
        change = (
            (latest_count - previous_count) / previous_count * 100
        )

        if change > 0:
            direction = "increased"
        elif change < 0:
            direction = "decreased"
        else:
            direction = "remained unchanged"

        message = (
            f"Commit activity {direction} "
            f"{abs(change):.1f}% from {previous_month} "
            f"to {latest_month}."
        )

    return {
        "latest_month": latest_month,
        "latest_commits": latest_count,
        "previous_month": previous_month,
        "previous_commits": previous_count,
        "change_percent": change,
        "message": message,
    }
