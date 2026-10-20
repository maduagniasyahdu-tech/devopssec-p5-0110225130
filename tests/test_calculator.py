import pytest

from app.calculator import calculate


def test_addition():
    assert calculate("add", 5, 3) == 8


def test_subtraction():
    assert calculate("subtract", 5, 3) == 2


def test_multiplication():
    assert calculate("multiply", 5, 3) == 15


def test_division():
    assert calculate("divide", 6, 3) == 2


def test_division_by_zero():
    with pytest.raises(ValueError):
        calculate("divide", 5, 0)


def test_unknown_operation():
    with pytest.raises(ValueError):
        calculate("power", 2, 3)
