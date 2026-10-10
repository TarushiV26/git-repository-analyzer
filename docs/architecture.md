# Architecture

## Components
- `app.py`: Streamlit UI and tab layout.
- `src/repository.py`: reads local Git metadata and prepares repository summary data.
- `src/contributors.py`: aggregates commit counts by author.
- `src/activity.py`: aggregates monthly activity and file-touch frequency.
- `src/branches.py`: formats branch information.
- `tests/`: unit tests for analysis helpers.

## Data flow
User enters local path -> repository validation -> Git metadata extraction -> analysis helpers -> dashboard tables/charts.

## Privacy
The application analyzes local Git metadata. It does not send repository data to a remote service.
