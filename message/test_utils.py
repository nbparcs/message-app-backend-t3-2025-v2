# my_app/test_utils.py
from .utils import add, sub, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(2, 5) == -3

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    # Test edge case: division by zero returns None
    assert divide(10, 0) is None
