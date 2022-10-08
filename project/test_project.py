from io import StringIO
from project import choice, new_user, exist_user
from method_signup import Project_New_User
from method_login import Project_Login


# Testing the code
def test_choice(monkeypatch):

    number_inputs = StringIO("1")
    monkeypatch.setattr("sys.stdin", number_inputs)
    assert choice() == "1"


# Testing the code
def test_new_user(monkeypatch):

    create = Project_New_User()
    number_inputs = StringIO("1")
    monkeypatch.setattr("sys.stdin", number_inputs)
    assert choice() == "1"


# Testing the code
def test_exist_user(monkeypatch):
    create = Project_Login()
    number_inputs = StringIO("2")
    monkeypatch.setattr("sys.stdin", number_inputs)
    assert choice() == "2"