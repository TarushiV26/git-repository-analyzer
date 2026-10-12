
import streamlit as st
import pandas as pd
import plotly.express as px

from src.repository import analyze_repository
from src.activity import monthly_activity, frequent_files
from src.contributors import contributor_stats
from src.branches import branch_stats
from src.insights import activity_insights

def dark_table(df):
    return (
        df.style
        .set_properties(**{
            "background-color": "#151a2e",
            "color": "#e5e7f5",
            "border-color": "#303653",
        })
        .set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", "#222747"),
                    ("color", "#c4b5fd"),
                    ("border-color", "#343b60"),
                    ("font-weight", "600"),
                ],
            },
            {
                "selector": "td",
                "props": [
                    ("background-color", "#151a2e"),
                    ("color", "#e5e7f5"),
                    ("border-color", "#303653"),
                ],
            },
        ])
    )


st.set_page_config(
    page_title="RepoPulse | Repository Intelligence",
    page_icon="📊",
    layout="wide",
)

# ---------- Theme ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

.stApp {
    background: #0b1020;
    color: #edf1ff;
    font-family: 'DM Sans', sans-serif;
}
.block-container {
    max-width: 1500px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}
h1, h2, h3, h4 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #f4f6ff !important;
}
p, label, .stMarkdown {
    color: #c4cce2;
}
.hero {
    background: linear-gradient(115deg, #171d3b 0%, #29245b 55%, #402a76 100%);
    border: 1px solid #464078;
    border-radius: 22px;
    padding: 28px 30px;
    margin-bottom: 20px;
    box-shadow: 0 12px 38px rgba(35, 25, 90, .25);
}
.eyebrow {
    color: #b7a8ff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.hero h1 {
    font-size: 36px;
    line-height: 1.15;
    margin: 8px 0;
}
.hero p {
    color: #c7cbed;
    margin: 0;
    font-size: 15px;
}
.repo-strip {
    background: #121a30;
    border: 1px solid #273452;
    padding: 14px 18px;
    border-radius: 12px;
    margin-bottom: 18px;
    color: #c8d3ed;
    overflow-wrap: anywhere;
}
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #151e35, #11182b);
    border: 1px solid #2b3857;
    padding: 17px 18px;
    border-radius: 16px;
    box-shadow: 0 8px 22px rgba(0, 0, 0, .12);
}
div[data-testid="stMetricLabel"] {
    color: #aebcda !important;
    font-weight: 600;
}
div[data-testid="stMetricValue"] {
    color: #f3f5ff !important;
    font-family: 'Space Grotesk', sans-serif;
}
div[data-testid="stMetricDelta"] {
    font-size: 12px;
}
div[data-testid="stTabs"] {
    margin-top: 12px;
}
div[data-testid="stTabs"] button {
    color: #bac6e0;
    font-weight: 600;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #c6b7ff;
}
div[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    background-color: #9a83ff;
}
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #11192c;
    border: 1px solid #293653;
    border-radius: 16px;
    padding: 14px;
}
div[data-testid="stDataFrame"] {
    border: 1px solid #293653;
    border-radius: 10px;
}
.stButton button[kind="primary"] {
    background: linear-gradient(100deg, #6553df, #9271ff);
    border: 0;
    border-radius: 10px;
    font-weight: 700;
}
.stDownloadButton button {
    background: #202b46;
    color: #e3eaff;
    border: 1px solid #3b4a6c;
    border-radius: 9px;
    font-weight: 600;
}
.stDownloadButton button:hover {
    border-color: #a08cff;
    color: #ffffff;
}
div[data-testid="stAlert"] {
    border-radius: 12px;
}
hr {
    border-color: #293653;
}
[data-testid="stSidebar"] {
    background: #0e1527;
    border-right: 1px solid #273452;
}
[data-testid="stSidebar"] h2 {
    font-size: 20px;
}
.small-note {
    color: #92a2c2;
    font-size: 13px;
    margin-top: -8px;
}


/* Dark theme for chart and dataframe surfaces */
[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"],
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background: #151a2e !important;
    border: 1px solid #29314d !important;
    border-radius: 12px !important;
    padding: 8px !important;
}

/* Keep section cards consistent */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #29314d !important;
    border-radius: 14px !important;
}

/* Improve dataframe readability */
[data-testid="stDataFrame"] iframe {
    background: #151a2e !important;
}


/* Blend Streamlit's top toolbar into the app */
[data-testid="stHeader"] {
    background: rgba(13, 17, 32, 0.96) !important;
}

[data-testid="stToolbar"] {
    right: 1rem;
}

/* Remove excess top gap above the hero */
.block-container {
    padding-top: 1.5rem !important;
}


/* Dark, readable tables */
[data-testid="stDataFrame"] {
    background: #11192c !important;
    border: 1px solid #293653 !important;
    border-radius: 12px !important;
    overflow: hidden;
}

/* Dark table fallback */
[data-testid="stTable"] {
    background: #11192c !important;
    color: #dce4ff !important;
    border-color: #293653 !important;
}

/* Keep Streamlit's top bar consistent */
[data-testid="stHeader"] {
    background: #0b1020 !important;
}



# ---------- Dark table styling ----------



</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="hero">
    <div class="eyebrow">DEVELOPER ANALYTICS / LOCAL REPOSITORY</div>
    <h1>RepoPulse</h1>
    <p>Repository intelligence beyond commit counts. Explore activity,
    contributors, branches and file-change patterns.</p>
</div>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## Repository")
    repo_path = st.text_input(
        "Local repository path",
        value=".",
        help="Path to a local folder containing a .git directory.",
    )
    analyze = st.button(
        "Analyze repository",
        type="primary",
        use_container_width=True,
    )
    st.caption(
        "Runs locally against the selected Git repository. "
        "Do not enter passwords, tokens or credentials."
    )
    st.divider()
    st.caption("REPOPULSE · Repository intelligence")

if "analysis" not in st.session_state:
    st.session_state.analysis = None


if analyze:
    try:
        with st.spinner("Scanning repository and reading commit history..."):
            st.session_state.analysis = analyze_repository(repo_path)
    except Exception as exc:
        st.session_state.analysis = None
        st.error(f"Could not analyze repository: {exc}")


data = st.session_state.analysis

if data is None:
    st.markdown("### Start with a repository")
    st.write(
        "Enter a local Git repository path in the sidebar and select "
        "**Analyze repository** to explore its history."
    )
    a, b, c = st.columns(3)
    with a:
        with st.container(border=True):
            st.markdown("#### Activity")
            st.write("Explore monthly commit patterns.")
    with b:
        with st.container(border=True):
            st.markdown("#### Contributors")
            st.write("Compare commit counts by author.")
    with c:
        with st.container(border=True):
            st.markdown("#### File intelligence")
            st.write("Find frequently modified files.")
    st.stop()

# ---------- Repository identity ----------
st.markdown(
    f"""<div class="repo-strip">
    <b>REPOSITORY</b> &nbsp; {data['path']}<br>
    <b>ACTIVE BRANCH</b> &nbsp; {data['current_branch']}
    </div>""",
    unsafe_allow_html=True,
)

# ---------- KPI cards ----------
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.metric("Total commits", data["commit_count"])
with k2:
    st.metric("Contributors", data["contributor_count"])
with k3:
    st.metric("Branches", data["branch_count"])
with k4:
    st.metric("Tracked files", data["file_count"])

overview, contributors, activity, branches, files_tab = st.tabs([
    "Overview",
    "Contributors",
    "Activity & Insights",
    "Branches",
    "File Intelligence",
])

# ---------- Overview ----------
with overview:
    st.subheader("Repository overview")
    st.markdown(
        '<p class="small-note">A snapshot of the available local Git history.</p>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 1], gap="large")
    with left:
        with st.container(border=True):
            st.markdown("#### Commit timeline")
            st.write("**First commit:**", data["first_commit"] or "No commits")
            st.write("**Latest commit:**", data["latest_commit"] or "No commits")
            st.write("**Latest commit date:**", data["latest_date"] or "N/A")

    with right:
        with st.container(border=True):
            st.markdown("#### Activity highlight")
            overview_df = monthly_activity(data["commits"])
            if overview_df.empty:
                st.info("No commit activity is available.")
            else:
                peak = overview_df.sort_values(
                    "Commits", ascending=False
                ).iloc[0]
                st.metric(
                    "Busiest recorded month",
                    int(peak["Commits"]),
                    help=str(peak["Month"]),
                )
                st.caption(
                    f"{peak['Month']} has the highest commit count "
                    "among the months present in this repository history."
                )

    with st.container(border=True):
        st.markdown("#### What this analysis covers")
        st.write(
            "Commit history, contributor counts, branch information and "
            "frequently modified files. Results reflect the history available "
            "in the selected local clone."
        )

# ---------- Contributors ----------
with contributors:
    st.subheader("Contributor intelligence")
    st.markdown(
        '<p class="small-note">Compare commit counts and inspect author-level data.</p>',
        unsafe_allow_html=True,
    )
    df = contributor_stats(data["commits"])

    if df.empty:
        st.info("No contributor data is available.")
    else:
        
        st.download_button(
             label="📥 Download CSV",
             data=df.to_csv(index=False).encode("utf-8"),
             file_name="contributor_statistics.csv",
             mime="text/csv",
             key="contributor_statistics_csv",
             use_container_width=True,
            )


        chart_col, table_col = st.columns([1, 1.2], gap="large")
        with chart_col:
            with st.container(border=True):
                st.markdown("#### Commit distribution")
                
                chart_df = df.nlargest(10, "Commits").sort_values("Commits")
                fig = px.bar(
                    chart_df,
                    x="Commits",
                    y="Contributor",
                    orientation="h",
                    text="Commits",
                    title="Top 10 contributors",
                    color="Commits",
                    color_continuous_scale=["#5145cd", "#a78bfa"],
                )
                fig.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#dce4ff", family="Arial"),
                    margin=dict(l=10, r=15, t=50, b=10),
                    height=420,
                    coloraxis_showscale=False,
                    xaxis_title="Commits",
                    yaxis_title="",
                )
                fig.update_traces(textposition="outside", cliponaxis=False)
                st.plotly_chart(fig, use_container_width=True)

                st.caption("Commit counts grouped by recorded author.")
        with table_col:
            with st.container(border=True):
                st.markdown("#### Contributor details")
                st.dataframe(
    dark_table(df),
    use_container_width=True,
    hide_index=True,
)

        if len(df) == 1:
            st.info(
                "Only one contributor appears in this analyzed history. "
                "This does not establish the size of the wider project team."
            )

# ---------- Activity + insights ----------
with activity:
    st.subheader("Activity & repository insights")
    st.markdown(
        '<p class="small-note">See the trend, then read what the available data supports.</p>',
        unsafe_allow_html=True,
    )

    df = monthly_activity(data["commits"])
    insight = activity_insights(df)

    chart_col, insight_col = st.columns([1.55, 1], gap="large")

    with chart_col:
        with st.container(border=True):
            st.markdown("#### Monthly commit activity")
            if df.empty:
                st.info("No commit activity is available.")
            else:
                
                st.download_button(
                    label="📥 Download CSV",
                    data=df.to_csv(index=False).encode("utf-8"),
                    file_name="monthly_activity.csv",
                    mime="text/csv",
                    key="monthly_activity_csv",
                    use_container_width=True,
                    )

                chart_df = df.copy()
                chart_df["Month"] = chart_df["Month"].astype(str)
                
                fig = px.bar(
                    chart_df,
                    x="Month",
                    y="Commits",
                    title="Monthly commit activity",
                    color="Commits",
                    color_continuous_scale=["#5145cd", "#a78bfa"],
                    hover_data={"Month": True, "Commits": True},
                )
                fig.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#dce4ff"),
                    margin=dict(l=10, r=10, t=50, b=10),
                    height=420,
                    coloraxis_showscale=False,
                    xaxis_title="Month",
                    yaxis_title="Commits",
                )
                fig.update_xaxes(tickangle=-45, showgrid=False)
                fig.update_yaxes(gridcolor="#293653")
                st.plotly_chart(fig, use_container_width=True)

                st.dataframe(
    dark_table(df),
    use_container_width=True,
    hide_index=True,
)

    with insight_col:
        with st.container(border=True):
            st.markdown("#### Generated insight")
            st.info(insight["message"])
            st.metric(
                "Latest month commits",
                insight["latest_commits"],
                help=insight["latest_month"] or "No month available",
            )
            st.metric(
                "Previous month commits",
                insight["previous_commits"],
                delta=(
                    f'{insight["change_percent"]:+.1f}%'
                    if insight["change_percent"] is not None
                    else None
                ),
                help=insight["previous_month"] or "No previous month available",
            )
            st.caption(
                "A percentage comparison is only meaningful when a prior "
                "month with a non-zero commit count is available."
            )

    if len(df) == 1:
        st.warning(
            "Limited history: only one month is represented. "
            "A month-to-month trend cannot be inferred yet."
        )

# ---------- Branches ----------
with branches:
    st.subheader("Branch explorer")
    st.markdown(
        '<p class="small-note">Inspect branches discovered in the local repository.</p>',
        unsafe_allow_html=True,
    )
    df = branch_stats(data["branches"])

    if df.empty:
        st.info("No branch information is available.")
    else:
        with st.container(border=True):
            st.dataframe(
    dark_table(df),
    use_container_width=True,
    hide_index=True,
)

# ---------- File intelligence ----------
with files_tab:
    st.subheader("File-change intelligence")
    st.markdown(
        '<p class="small-note">Identify files most often changed in the recorded commit history.</p>',
        unsafe_allow_html=True,
    )
    df = frequent_files(data["commits"])

    if df.empty:
        st.info("No file modification history is available.")
    else:
        st.download_button(
            label="📥 Download CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="file_analysis.csv",
            mime="text/csv",
            key="file_analysis_csv",
            use_container_width=True,
)


        chart_col, table_col = st.columns([1, 1.2], gap="large")
        with chart_col:
            with st.container(border=True):
                st.markdown("#### Most frequently modified files")
                chart_files = df.head(10).sort_values(
                    "Changes across commits", ascending=True
                )
                
                fig = px.bar(
                    chart_files,
                    x="Changes across commits",
                    y="File",
                    orientation="h",
                    text="Changes across commits",
                    title="Most frequently modified files",
                    color="Changes across commits",
                    color_continuous_scale=["#5145cd", "#a78bfa"],
                )
                fig.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#dce4ff"),
                    margin=dict(l=10, r=15, t=50, b=10),
                    height=450,
                    coloraxis_showscale=False,
                    xaxis_title="Changes across commits",
                    yaxis_title="",
                )
                fig.update_traces(textposition="outside", cliponaxis=False)
                st.plotly_chart(fig, use_container_width=True)

        with table_col:
            with st.container(border=True):
                st.markdown("#### File details")
                st.dataframe(
    dark_table(df),
    use_container_width=True,
    hide_index=True,
)

        top_file = df.iloc[0]
        st.info(
            f"Most frequently modified file in the analyzed history: "
            f"`{top_file['File']}` "
            f"({top_file['Changes across commits']} recorded commits)."
        )
