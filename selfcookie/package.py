import json
import keyword
import re
import urllib.error
import urllib.request


def is_available_on_pypi(package_name: str) -> bool:
    url = f"https://pypi.org/pypi/{package_name}/json"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            if data["info"]["name"] == package_name:
                return False
    except urllib.error.HTTPError as e:
        if e.code == 404:
            pass

    return True


def is_valid_package_name(name: str) -> bool:
    # Check if the name is a valid identifier
    if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):
        return False

    # Check if the name is not a reserved keyword
    if keyword.iskeyword(name):
        return False

    return True


def is_available_on_github(name: str, username: str) -> bool:
    """Check if the repository name is available on GitHub for username"""
    url = f"https://api.github.com/repos/{username}/{name}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            if data["name"] == name:
                return False
    except urllib.error.HTTPError as e:
        if e.code == 404:
            pass

    return True
