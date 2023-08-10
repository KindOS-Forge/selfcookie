import re
import subprocess
import tomllib as toml
from pathlib import Path


def get_gh_user(gh_ci_binary: str = "gh") -> str | None:
    """Get the GitHub username of the user using gh auth status"""

    try:
        gh_user: str = subprocess.check_output([gh_ci_binary, "auth", "status"]).decode("utf-8")
        match = re.search(r"Logged in to github.com as (\w*)", gh_user)
        if match:
            gh_user = match.group(1)
            return gh_user
        else:
            print("GitHub username not found in the output.")
            return None
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("GitHub CLI is not installed or you are not authenticated")
        print("Please install it from https://cli.github.com/")
        print()
        print("Then run `gh auth login` to log in to GitHub CLI")
        return None


def is_running_from_source() -> bool:
    """Check if selfcookie is running from source"""
    toml_data = Path("pyproject.toml").read_text()
    pyproject = toml.loads(toml_data)

    return pyproject["project"]["name"] == "selfcookie"
