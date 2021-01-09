import pytest

from models import User


@pytest.fixture(scope="function")
def user():
    yield User("Paul", "zceeppp@ucl.ac.uk", "UCL", "1234")


class TestUser:
    def test_name(self, user):
        assert user.name == "Paul"

    def test_email(self):
        assert False

    def test_email(self):
        assert False

    def test_university(self):
        assert False

    def test_university(self):
        assert False

    def test_university(self):
        assert False

    def test_password(self):
        assert False

    def test_user_id(self):
        assert False
