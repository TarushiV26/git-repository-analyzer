from pathlib import Path
from git import Repo, InvalidGitRepositoryError, NoSuchPathError

def analyze_repository(repo_path):
    path = Path(repo_path).expanduser().resolve()
    if not path.exists() or not path.is_dir():
        raise ValueError("The supplied path does not exist or is not a directory.")
    try:
        repo = Repo(path, search_parent_directories=True)
    except (InvalidGitRepositoryError, NoSuchPathError):
        raise ValueError("No Git repository was found at this path or its parent directories.")
    if repo.bare:
        raise ValueError("Bare repositories are not supported by this dashboard.")

    commits = []
    try:
        for commit in repo.iter_commits(all=True):
            commits.append({
                "hash": commit.hexsha[:8],
                "author": (commit.author.name or "Unknown").strip(),
                "email": (commit.author.email or "").strip(),
                "date": commit.committed_datetime,
                "message": commit.summary,
                "files": list(commit.stats.files.keys()),
            })
    except Exception as exc:
        raise ValueError(f"Unable to read commit history: {exc}")

    # Deduplicate commits reachable from multiple branches.
    unique = {c["hash"]: c for c in commits}
    commits = sorted(unique.values(), key=lambda c: c["date"])
    try:
        branches = [{"Name": b.name, "Commit": b.commit.hexsha[:8]} for b in repo.branches]
        current_branch = repo.active_branch.name
    except TypeError:
        branches, current_branch = [], "Detached HEAD"
    tracked_files = repo.git.ls_files().splitlines()
    authors = {c["author"] for c in commits if c["author"]}
    return {
        "path": str(path),
        "commits": commits,
        "commit_count": len(commits),
        "contributor_count": len(authors),
        "branch_count": len(branches),
        "file_count": len(tracked_files),
        "branches": branches,
        "current_branch": current_branch,
        "first_commit": commits[0]["message"] if commits else "",
        "latest_commit": commits[-1]["message"] if commits else "",
        "latest_date": commits[-1]["date"].strftime("%Y-%m-%d %H:%M") if commits else "",
    }
