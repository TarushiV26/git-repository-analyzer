# Contributing

Thanks for considering a contribution to Git Repository Analyzer.

## Workflow
1. Open or select a GitHub Issue describing a reproducible problem or enhancement.
2. Create a focused branch, such as `fix/invalid-repository-path`.
3. Make a small, clearly scoped change.
4. Add or update tests.
5. Run `pytest -q` and manually check the Streamlit UI.
6. Open a Pull Request describing the problem, implementation, tests, and limitations.
7. Request review and address feedback before merging.

## Code expectations
- Keep repository parsing separate from presentation.
- Validate user inputs and provide useful error messages.
- Avoid uploading repository contents or credentials.
- Add tests for new helper behavior.
- Describe actual test results; do not claim tests passed unless run.
