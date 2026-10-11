import streamlit as st
from pathlib import Path
from src.repository import analyze_repository
from src.activity import monthly_activity, frequent_files
from src.contributors import contributor_stats
from src.branches import branch_stats

st.set_page_config(page_title="Git Repository Analyzer", page_icon="📊", layout="wide")
st.title("🧑‍💻 Git Repository Analyzer")
st.caption("Explore repository history, contributors, branches, and file activity locally.")

with st.sidebar:
    st.header("Repository")
    repo_path = st.text_input("Local Git repository path", value=".")
    analyze = st.button("Analyze repository", type="primary", use_container_width=True)
    st.caption("Use a local folder containing a .git directory. Do not enter credentials or private tokens.")

if "analysis" not in st.session_state:
    st.session_state.analysis = None
if analyze:
    try:
        st.session_state.analysis = analyze_repository(repo_path)
        st.session_state.repo_path = repo_path
    except Exception as exc:
        st.session_state.analysis = None
        st.error(f"Could not analyze repository: {exc}")

data = st.session_state.analysis
if data is None:
    st.info("Enter a repository path in the sidebar and select **Analyze repository**.")
    st.markdown("""
    ### Features
    - Repository overview: commits, contributors, branches, and tracked files
    - Contributor statistics and commit activity over time
    - Branch listing and most frequently modified files
    - Local-only analysis with clear errors for invalid paths
    """)
    st.stop()

st.caption(f"Repository: `{data['path']}` · Current branch: `{data['current_branch']}`")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Commits", data["commit_count"])
c2.metric("Contributors", data["contributor_count"])
c3.metric("Branches", data["branch_count"])
c4.metric("Tracked files", data["file_count"])

overview, contributors, activity, branches, files_tab = st.tabs(
    ["📊 Overview", "👥 Contributors", "📈 Activity", "🌿 Branches", "📁 File analysis"]
)
with overview:
    left, right = st.columns(2)
    with left:
        st.subheader("Repository details")
        st.write("**First commit:**", data["first_commit"] or "No commits")
        st.write("**Latest commit:**", data["latest_commit"] or "No commits")
        st.write("**Latest commit date:**", data["latest_date"] or "N/A")
    with right:
        st.subheader("Most active month")
        activity_df = monthly_activity(data["commits"])
        if not activity_df.empty:
            top = activity_df.sort_values("Commits", ascending=False).iloc[0]
            st.metric("Peak month", str(top["Month"]), int(top["Commits"]))
        else:
            st.write("No commit activity available.")

with contributors:
    st.subheader("Contributor commit counts")
    df = contributor_stats(data["commits"])
    if df.empty:
        st.warning("No commits were found.")
    else:
        st.download_button(
            label="Download contributor statistics (CSV)",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="contributor_statistics.csv",
            mime="text/csv",
        )
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.bar_chart(df.set_index("Contributor")["Commits"])


with activity:
    st.subheader("Commits over time")
    df = monthly_activity(data["commits"])
    if df.empty:
        st.warning("No commit activity available.")
    else:
        st.download_button(
            label="Download monthly activity (CSV)",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="monthly_activity.csv",
            mime="text/csv",
        )
        st.line_chart(df.set_index("Month")["Commits"])
        st.dataframe(df, use_container_width=True, hide_index=True)

with branches:
    st.subheader("Branches")
    df = branch_stats(data["branches"])
    if df.empty:
        st.info("No branches found.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)

with files_tab:
    st.subheader("Most frequently modified files")
    df = frequent_files(data["commits"])
    if df.empty:
        st.info("No file modification history available.")
    else:
        st.download_button(
            label="Download file analysis (CSV)",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="file_analysis.csv",
            mime="text/csv",
        )
        st.dataframe(df, use_container_width=True, hide_index=True)

