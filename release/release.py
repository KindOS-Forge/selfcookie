# Desc: Get the latest git tag or commit hash
"""
Get the latest git tag or commit hash
"""
import datetime
import subprocess

from jinja2 import Environment, FileSystemLoader


def render_template(template_name, variables={}, template_dir="templates"):
    # Load the templates from the template directory
    env = Environment(loader=FileSystemLoader(template_dir))

    # Load the template
    template = env.get_template(template_name)

    # Render the template with the provided variables
    rendered_output = template.render(variables)
    return rendered_output


def update_changelog():
    latest_commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()

    try:
        latest_tag = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0", latest_commit],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except subprocess.CalledProcessError:
        latest_tag = None

    version = latest_commit or latest_tag
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Generate CHANGELOG.md from CHANGELOG.tpl.md
    change_log = render_template("CHANGELOG.md.j2", locals(), ".")
    with open("CHANGELOG.md", "w") as f:
        f.write(change_log)
