import unittest
from unittest import mock
from unittest.mock import Mock


class LoginChecker:

    def is_valid_username(self, username):
        return True


class MyService:
    def __init__(self, loginchecker: LoginChecker=None):
        self.__login_checker = loginchecker

    def do_login(self, username=None):
        if self.__login_checker.is_valid_username(username):
            return f"Hello, {username}"
        return "Please login"


class TestMyService(unittest.TestCase):

    def test_do_login(self):
        login_checker = Mock(LoginChecker)
        service = MyService(login_checker)
        ret_val = service.do_login(username="Jaydeep")
        print(ret_val)
        self.assertEqual(ret_val, "Hello, Jaydeep")

    def test_do_login_without_username(self):
        login_checker = Mock(LoginChecker)
        service = MyService(login_checker)
        ret_val = service.do_login()
        print(ret_val)
        self.assertEqual(ret_val, "Hello, None")

    def test_is_username_validate(self):
        login_checker = Mock(LoginChecker)
        service = MyService(login_checker)
        username = "Jaydeep"
        service.do_login(username=username)
        login_checker.is_valid_username.assert_called_with(username)


if __name__ == "__main__":
    unittest.main()