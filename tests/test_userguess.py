from selfcookie.clientchecks import get_gh_user


def test_get_gh_user():
    get_gh_user()
    get_gh_user("missing-gh-cli")  # Force a failed login if running on an authenticated system
