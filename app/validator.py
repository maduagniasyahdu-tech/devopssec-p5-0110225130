"""Validasi input kalkulator."""

SUPPORTED_OPERATIONS = ("add", "subtract", "multiply", "divide")


def validate_operation(operation):
    if operation not in SUPPORTED_OPERATIONS:
        raise ValueError("Operasi tidak dikenal")
    return operation


def validate_number(value):
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("Input harus berupa angka") from exc
