import typer

from .package import is_available_on_pypi, is_valid_package_name


def main(package_name: str) -> None:
    """Create a cookiecutter template for a python package"""

    if not is_valid_package_name(package_name):
        raise typer.BadParameter(f"{package_name} is not a valid python package name")

    if not is_available_on_pypi(package_name):
        raise typer.BadParameter(f"{package_name} is already registered on pypi")


if __name__ == "__main__":
    typer.run(main)
