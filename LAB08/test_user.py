# test_user.py
import pytest
from user import User

@pytest.fixture
def demo_user():
    return User("admin", "1234")

def test_login_success(demo_user):
    assert demo_user.verify_login("admin", "1234") == True

def test_login_wrong_username(demo_user):
    assert demo_user.verify_login("wrong", "1234") == False

def test_login_wrong_password(demo_user):
    assert demo_user.verify_login("admin", "0000") == False



