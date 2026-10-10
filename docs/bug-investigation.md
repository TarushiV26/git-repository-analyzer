# Bug Investigation — Suggested test case

## Candidate scenario
Entering a directory that is not a Git repository should produce a clear error instead of crashing the dashboard.

## Environment
Record your actual OS, Python version, Git version, and installed dependency versions.

## Reproduction steps
1. Start the application with `streamlit run app.py`.
2. Enter the path to an existing ordinary folder that is not inside a Git repository.
3. Select **Analyze repository**.

## Expected result
The application shows a readable validation message and remains usable.

## Actual result
Fill this in only after running the test. Capture a screenshot or terminal evidence.

## Fix / verification
Record the actual code change and test result. Do not claim reproduction or resolution until verified.
