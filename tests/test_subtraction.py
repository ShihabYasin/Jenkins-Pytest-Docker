from src.calculator import subtract
import pytest


def test_subtract_positive():
    result = subtract(4, 3)
    assert result == 1


def test_subtract_negative():
    result = subtract(3, 4)
    assert result == -1


def test_subtract_string():
    with pytest.raises(TypeError):
        subtract("string", 4)
