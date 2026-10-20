import pytest

from app.validator import validate_number, validate_operation


def test_validate_number():
    assert validate_number("12.5") == 12.5


def test_invalid_number():
    with pytest.raises(ValueError):
        validate_number("abc")


def test_valid_operation():
    assert validate_operation("add") == "add"


def test_invalid_operation():
    with pytest.raises(ValueError):
        validate_operation("power")
