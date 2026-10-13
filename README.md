# RepoPulse — Git Repository Analyzer

RepoPulse is a Python-based application that analyzes local Git repositories and presents repository statistics through an interactive Streamlit dashboard. It helps users explore commit activity, contributor statistics, branch information, and tracked-file analysis, with CSV exports for further analysis.

## Features

- **Repository Overview:** View key statistics about a Git repository.
- **Commit Activity:** Inspect commit history and monthly commit activity.
- **Contributor Analysis:** View contributor statistics.
- **Branch Information:** Explore repository branches.
- **File Analysis:** View information about tracked files.
- **CSV Export:** Download contributor statistics, monthly commit activity, and file-analysis results as CSV files.
- **Empty Repository Handling:** Analyze repositories with no commits without an unhandled commit-reference error.
- **Automated Testing:** Run tests using pytest to verify expected behavior.

## Technology Stack

- **Python:** Core programming language.
- **Streamlit:** Interactive dashboard and user interface.
- **GitPython:** Access to Git repository information.
- **pytest:** Automated testing.
- **Git and GitHub:** Version control, issue tracking, pull requests, and collaboration.

## Requirements

Before running RepoPulse, ensure that the following are installed:

- Python
- Git
- Project dependencies

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/TarushiV26/git-repository-analyzer.git
cd git-repository-analyzer
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

If a `requirements.txt` file is available, install the dependencies using:

```bash
pip install -r requirements.txt
```

Otherwise, follow the dependency instructions provided in the project repository.

## Running the Application

From the project root directory, execute:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL in the terminal. Open the URL in a web browser to access the dashboard.

## How to Use RepoPulse

1. Launch the Streamlit application.
2. Enter or select the path to a local Git repository.
3. Run the repository analysis.
4. Explore repository statistics, commit activity, contributors, branches, and file information.
5. Use the available CSV download controls to export supported analysis results.
6. Open the downloaded CSV files in spreadsheet software for further analysis.

## CSV Export Enhancement

The CSV export enhancement allows users to save analysis results locally instead of viewing them only in the dashboard.

The supported export categories include:

- Contributor statistics
- Monthly commit activity
- File-analysis results

The downloaded files can be opened in spreadsheet applications for reporting, comparison, and further analysis.

CSV download controls should be available when the corresponding data is present.

## Handling Repositories with No Commit History

A newly initialized Git repository may contain no commits. In this situation, the repository's `HEAD` reference may not point to an existing commit.

Attempting to access commit history without checking this condition can result in a missing-reference error.

RepoPulse handles this scenario by checking whether `HEAD` is valid before reading commit history. If the repository contains no commits, the analyzer returns appropriate empty results rather than failing.

A regression test in `tests/test_repository.py` verifies the empty-repository scenario, including zero counts and empty commit details.

## Running Automated Tests

To execute the test suite, run the following command from the project root:

```bash
python -m pytest -q
```

The latest recorded test run during development reported **9 passed**. Run the command on your current checkout to verify the test result for that version.

## Project Structure

The main project files include:

```text
git-repository-analyzer/
├── app.py
├── src/
│   └── repository.py
├── tests/
│   └── test_repository.py
├── screenshots/
└── README.md
```

Additional files and directories may be present in the repository.

- `app.py` — application entry point.
- `src/repository.py` — repository-analysis logic.
- `tests/test_repository.py` — repository-analysis regression tests.
- `screenshots/` — screenshots used to demonstrate application features.

## GitHub Collaboration Workflow

GitHub Issues and Pull Requests help organize development and track changes.

The workflow followed in the project is:

1. Identify and document a bug or enhancement in a GitHub Issue.
2. Create a separate branch for the change.
3. Implement the required code changes.
4. Run relevant tests.
5. Commit and push the changes.
6. Create a Pull Request describing the implementation.
7. Review and merge the changes when approved.

This workflow supports traceability, code review, and collaborative development.

## Screenshots

The `screenshots/` directory contains screenshots of the dashboard and CSV export workflow. These images can be used to demonstrate repository analysis, data visualization, and downloaded results.

## Contributing

Improvements and bug fixes can be proposed through GitHub Issues and Pull Requests.

Contributors should clearly describe the issue or enhancement, implement the required changes, run relevant tests, and provide screenshots or test results when appropriate.

## License

Add the applicable project license here if one has been selected. Refer to the repository's license file or metadata before specifying a license.
