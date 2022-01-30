from src.calculator import add
import pytest


def test_add():
    result = add(30, 40)
    assert result == 70


def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)
