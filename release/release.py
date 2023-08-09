# Desc: Get the latest git tag or commit hash
"""
Get the latest git tag or commit hash
"""
import datetime

from jinja2 import Environment, FileSystemLoader
from setuptools_scm import get_version


def render_template(template_name: str, variables: dict = {}, template_dir: str = "templates") -> str:
    # Load the templates from the template directory
    env = Environment(loader=FileSystemLoader(template_dir))

    # Load the template
    template = env.get_template(template_name)

    # Render the template with the provided variables
    rendered_output = template.render(variables)
    return rendered_output


def update_changelog() -> None:
    version = get_version()
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Generate CHANGELOG.md from CHANGELOG.tpl.md
    change_log = render_template("CHANGELOG.md.j2", locals(), ".")
    with open("CHANGELOG.md", "w") as f:
        f.write(change_log)
