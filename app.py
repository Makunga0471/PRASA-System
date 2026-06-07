# PRASA-System - Open Source Collaboration Calculator


class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when input values are invalid (e.g. None, non-numeric types)."""
    pass


def _validate_inputs(a, b):
    """Validate that both inputs are numeric (int or float) and not None."""
    if a is None or b is None:
        raise InvalidInputError("Inputs must not be None.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError(
            f"Inputs must be numeric, got: {type(a).__name__} and {type(b).__name__}."
        )


def add(a, b):
    """Return the sum of a and b.

    Raises:
        InvalidInputError: If either input is not a valid number.
    """
    _validate_inputs(a, b)
    return a + b


def subtract(a, b):
    """Return the difference of a and b.

    Raises:
        InvalidInputError: If either input is not a valid number.
    """
    _validate_inputs(a, b)
    return a - b


def multiply(a, b):
    """Return the product of a and b.

    Raises:
        InvalidInputError: If either input is not a valid number.
    """
    _validate_inputs(a, b)
    return a * b


def divide(a, b):
    """Return the result of dividing a by b.

    Raises:
        InvalidInputError: If either input is not a valid number.
        DivisionByZeroError: If b is zero.
    """
    _validate_inputs(a, b)
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """Prompt the user for a numeric value, re-asking on invalid input."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("  Input cannot be empty. Please enter a number.")
            continue
        try:
            return float(raw)
        except ValueError:
            print(f"  '{raw}' is not a valid number. Please try again.")


def main():
    print("=== PRASA System Calculator ===")
    print("Welcome to the collaborative calculator project!\n")

    operations = {
        "1": ("Add",      add,      "+"),
        "2": ("Subtract", subtract, "-"),
        "3": ("Multiply", multiply, "*"),
        "4": ("Divide",   divide,   "/"),
    }

    while True:
        print("Choose an operation:")
        for key, (label, _, _sym) in operations.items():
            print(f"  {key}. {label}")
        print("  5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("Thank you for using PRASA Calculator!")
            break

        if choice not in operations:
            print("Invalid choice! Please enter a number between 1 and 5.\n")
            continue

        label, operation, symbol = operations[choice]

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = operation(num1, num2)
            print(f"Result: {num1} {symbol} {num2} = {result}\n")
        except DivisionByZeroError as exc:
            print(f"Error: {exc}\n")
        except CalculatorError as exc:
            print(f"Calculation error: {exc}\n")


if __name__ == "__main__":
    main()