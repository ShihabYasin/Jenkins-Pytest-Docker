from src.calculator import divide
import pytest


def test_divide():
    result = divide(3, 2)
    assert result == 1.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        divide(3, 0)


def test_divide_string():
    with pytest.raises(TypeError):
        divide("string", 2)
