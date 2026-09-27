def get_number(prompt):
    """Repeatedly prompt until the user enters a valid number."""
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def main():
    while True:
        print("\n=== Calculator Master ===")
        print("[a] Addition")
        print("[s] Subtraction")
        print("[m] Multiplication")
        print("[d] Division")
        print("[x] Exit")
        choice = input("Select an operation: ").strip().lower()

        if choice == 'x':
            print("Goodbye!")
            break
        elif choice == 'a':
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")
            result = add(x, y)
            print(f"Result: {result:.2f}")
        elif choice == 's':
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")
            result = subtract(x, y)
            if result < 0:
                print(f"Result: {result:.2f} (negative)")
            else:
                print(f"Result: {result:.2f}")
        elif choice == 'm':
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")
            result = multiply(x, y)
            print(f"Result: {result:.2f}")
        elif choice == 'd':
            print("Division feature not yet implemented.")
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
