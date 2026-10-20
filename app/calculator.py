"""Operasi matematika kalkulator."""


def calculate(operation, first, second):
    if operation == "add":
        return first + second

    if operation == "subtract":
        return first - second

    if operation == "multiply":
        return first * second

    if operation == "divide":
        if second == 0:
            raise ValueError("Tidak dapat membagi dengan nol")
        return first / second

    raise ValueError("Operasi tidak dikenal")
