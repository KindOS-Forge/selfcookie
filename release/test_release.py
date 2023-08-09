import version

from release import update_changelog


def test_release():
    update_changelog()
    assert version.get_version()
