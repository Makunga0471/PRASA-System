class CalculatorError(Exception):
    pass


class DivisionByZeroError(CalculatorError):
    pass


class InvalidInputError(CalculatorError):
    pass


def _validate_inputs(a, b):
    if a is None or b is None:
        raise InvalidInputError("Inputs must not be None.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Inputs must be numeric.")


def add(a, b):
    _validate_inputs(a, b)
    return a + b


def subtract(a, b):
    _validate_inputs(a, b)
    return a - b


def multiply(a, b):
    _validate_inputs(a, b)
    return a * b


def divide(a, b):
    _validate_inputs(a, b)
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b


def modulo(a, b):
    _validate_inputs(a, b)
    if b == 0:
        raise DivisionByZeroError("Cannot perform modulo with zero.")
    return a % b


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Input cannot be empty.")
            continue
        try:
            return float(raw)
        except ValueError:
            print(raw + " is not valid.")


def main():
    print("=== PRASA System Calculator ===")
    operations = {
        "1": ("Add", add, "+"),
        "2": ("Subtract", subtract, "-"),
        "3": ("Multiply", multiply, "*"),
        "4": ("Divide", divide, "/"),
        "5": ("Modulo", modulo, "%"),
    }
    while True:
        print("Choose an operation:")
        for key, (label, _, sym) in operations.items():
            print("  " + key + ". " + label)
        print("  6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "6":
            print("Thank you!")
            break
        if choice not in operations:
            print("Invalid choice.")
            continue
        label, operation, symbol = operations[choice]
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        try:
            result = operation(num1, num2)
            print("Result: " + str(result))
        except DivisionByZeroError as exc:
            print("Error: " + str(exc))
        except CalculatorError as exc:
            print("Error: " + str(exc))


if __name__ == "__main__":
    main()
