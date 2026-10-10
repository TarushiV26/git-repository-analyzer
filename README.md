# Git Repository Analyzer

A small open-source Python dashboard for exploring a local Git repository's commit history, contributors, branches, tracked files, and file activity.

## Features
- Repository overview metrics
- Contributor commit counts
- Monthly commit activity
- Branch list
- Most frequently modified files (based on commit-level file statistics)
- Input validation for invalid paths
- Automated helper-function tests

## Requirements
Python 3.10+ and Git installed locally.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

In the sidebar, enter the path to a local Git repository and choose **Analyze repository**. For the project repository itself, `.` is sufficient when the app is launched from this directory.

## Test
```bash
pytest -q
```

## Work package mapping
- **A — Project & Repository:** `app.py`, `src/repository.py`
- **B — Issue & Bug Investigation:** `src/activity.py`, `tests/`, `docs/bug-investigation.md`
- **C — Contribution & Pull Request:** `src/contributors.py`, `src/branches.py`, `CONTRIBUTING.md`, `docs/pull-request-investigation.md`

This mapping categorizes project responsibilities; it does not imply that three people made commits. Record actual authorship, review, and testing honestly.

## Limitations
- Analysis is local and does not call the GitHub API.
- Contributor identity is grouped by Git author name, which may vary across commits.
- Branch metrics list local branches; remote-only branches are not listed.
- File frequency is derived from Git commit statistics and is not a measure of lines changed.
- A reproducible bug or Pull Request must be investigated using actual repository evidence; templates in `docs/` are not evidence by themselves.

## References
- GitPython documentation: https://gitpython.readthedocs.io/
- Streamlit documentation: https://docs.streamlit.io/
- Git documentation: https://git-scm.com/docs
