"""Antarmuka command-line SimpleCalc."""
import argparse

from app.calculator import calculate
from app.formatter import format_result
from app.validator import validate_number, validate_operation


def main():
    parser = argparse.ArgumentParser(
        description="Kalkulator matematika sederhana"
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
    )
    parser.add_argument("first", help="Angka pertama")
    parser.add_argument("second", help="Angka kedua")
    args = parser.parse_args()

    try:
        operation = validate_operation(args.operation)
        first = validate_number(args.first)
        second = validate_number(args.second)
        result = calculate(operation, first, second)
        print(format_result(operation, first, second, result))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
