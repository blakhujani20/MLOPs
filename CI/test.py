import pytest
from CI.app import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5, "Addition failed"
    assert add(-1, 1) == 0, "Addition with negative number failed"
    assert add(0, 0) == 0, "Addition with zeros failed"

def test_subtract():
    assert subtract(5, 3) == 2, "Subtraction failed"
    assert subtract(0, 1) == -1, "Subtraction resulting in negative failed"
    assert subtract(-1, -1) == 0, "Subtraction with negatives failed"

def test_multiply():
    assert multiply(2, 3) == 6, "Multiplication failed"
    assert multiply(-1, 5) == -5, "Multiplication with negative number failed"
    assert multiply(0, 100) == 0, "Multiplication with zero failed"

def test_divide():
    assert divide(6, 3) == 2, "Division failed"
    assert divide(-6, 3) == -2, "Division with negative number failed"
    assert divide(0, 1) == 0, "Division of zero failed"
    assert divide(5, 0) == "Error! Division by zero."



