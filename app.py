def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


if __name__ == "__main__":

    print("===== PRASA Python Calculator =====")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nResults:")
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))