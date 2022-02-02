from src.compute import add, divide, subtract, multiply
import pytest


def test_add():
    result = add (30, 40)
    assert result == 70


def test_add_string():
    with pytest.raises (TypeError):
        add ("MyString", 98)


def test_divide():
    result = divide (33, 5)
    assert result == 6.6


def test_divide_by_zero():
    with pytest.raises (ZeroDivisionError) as e:
        divide (9, 0)


def test_divide_string():
    with pytest.raises (TypeError):
        divide ("MyString", 2)


def test_multiply():
    result = multiply (8, 4)
    assert result == 32


def test_multiply_string():
    with pytest.raises (TypeError):
        multiply ("MyString", 4)


def test_subtract_positive():
    result = subtract (7, 6)
    assert result == 1


def test_subtract_negative():
    result = subtract (4, 9)
    assert result == -5


def test_subtract_string():
    with pytest.raises (TypeError):
        subtract ("MyString", 6)
