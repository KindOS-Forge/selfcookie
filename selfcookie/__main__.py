import tempfile

import typer

from .clientchecks import get_gh_user, is_running_from_source
from .package import is_available_on_github, is_available_on_pypi, is_valid_package_name
from .replace import copy_and_replace
from .status import print_success


def main(package_name: str) -> None:
    """Create a cookiecutter template for a python package"""

    if not is_valid_package_name(package_name):
        raise typer.BadParameter(f"{package_name} is not a valid python package name")
    else:
        print_success(f"{package_name} is a valid python package name")

    if not is_available_on_pypi(package_name):
        raise typer.BadParameter(f"{package_name} is already registered on pypi")
    else:
        print_success(f"{package_name} is free on pypi")

    gh_user = get_gh_user()
    print_success(f"Logged in as {gh_user}")
    if not is_available_on_github(package_name, gh_user):
        raise typer.BadParameter(f"{package_name} is already registered on github")
    else:
        print_success(f"github.com {gh_user}/{package_name} repository is available")

    if is_running_from_source():
        print_success(f"Creating {package_name} from our own source")
        # create a tmp directory
        tmp = tempfile.mkdtemp()
        copy_and_replace(".", tmp, "selfcookie", package_name)


if __name__ == "__main__":
    typer.run(main)
