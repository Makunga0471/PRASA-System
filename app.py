# PRASA-System - Open Source Collaboration Calculator

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b. Returns error message if dividing by zero."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def main():
    print("=== PRASA System Calculator ===")
    print("Welcome to the collaborative calculator project!\n")
    
    while True:
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using PRASA Calculator!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please try again.\n")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers!\n")
            continue
        
        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}\n")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}\n")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}\n")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}\n")


if __name__ == "__main__":
    main()