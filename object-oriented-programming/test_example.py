# pytest는 파일명에 test를 prefix로 달아줘야 한다.

# Unit Test
import pytest


def add(a: int, b: int) -> int:
    return a + b


def test_add():
    a, b = 1, 2
    assert add(a, b) == 3


def test_add_fail():
    assert not add(1, 2) == 4


# Integration Test
class User:
    def __init__(self, user_id, user_password):
        self.user_id = user_id
        self.user_password = user_password

    def check_password(self, user_password):
        if self.user_password != user_password:
            raise Exception("not authorization")


class UserRepository:
    def __init__(self):
        self.users = [User("wogns0108", "12345")]

    def find_by_id(self, user_id) -> User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise Exception("No User")


def login(user_id, user_password) -> str:
    user_repository = UserRepository()
    user = user_repository.find_by_id(user_id)
    user.check_password(user_password)
    return "login succeed"


def test_login():
    assert login("wogns0108", "12345") == "login succeed"


def test_login_failed():
    with pytest.raises(Exception):
        login("wogns0108", "1")


def test_login_no_user():
    with pytest.raises(Exception):
        login("wogns0107", "12345")