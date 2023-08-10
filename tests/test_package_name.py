import uuid

from selfcookie.package import is_available_on_pypi, is_valid_package_name


def test_is_valid_package_name():
    assert is_valid_package_name("selfcookie") is True
    # reserved keyword
    assert is_valid_package_name("if") is False
    # starts with number
    assert is_valid_package_name("1selfcookie") is False
    # contains special character
    assert is_valid_package_name("selfcookie!") is False
    # check if it contains an unicode char
    assert is_valid_package_name("selfcookie😀") is False


def test_is_available_on_pypi():
    assert is_available_on_pypi("fastapi") is False
    # generate a random puuid
    random_package = str(uuid.uuid4())[:8]
    assert is_available_on_pypi(random_package) is True
