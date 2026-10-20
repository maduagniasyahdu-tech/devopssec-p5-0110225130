"""Pemformatan hasil kalkulasi."""


def format_result(operation, first, second, result):
    symbols = {
        "add": "+",
        "subtract": "-",
        "multiply": "*",
        "divide": "/",
    }

    if operation not in symbols:
        raise ValueError("Operasi tidak dikenal")

    return f"{first:g} {symbols[operation]} {second:g} = {result:g}"
