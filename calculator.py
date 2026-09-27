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
            print("Subtraction feature not yet implemented.")
        elif choice == 'm':
            print("Multiplication feature not yet implemented.")
        elif choice == 'd':
            print("Division feature not yet implemented.")
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
