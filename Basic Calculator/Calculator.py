import sys
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nPlease enter a number\n")


def get_operation():
    operations = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "exit"}
    while True:
        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice [1-5]: ")

        if choice in operations:
            return operations[choice]
        print("\nPlease enter a valid choice for 1 to 5\n")


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("\nCan't divide by zero\n")
            return None
        return num1 / num2


def main():
    clear_screen()

    while True:
        try:
            num1 = get_number("Enter 1st number: ")
            num2 = get_number("Enter 2nd number: ")

            operation = get_operation()

            if operation == "exit":
                sys.exit("\nThank you for using my calculator. Exiting...")

            result = calculate(num1, num2, operation)

            if result is not None:
                print(f"\n{num1} {operation} {num2} = {result}\n")

            if (
                input("\nIf you want to continue, type 'yes', else type 'no': ")
                .strip()
                .lower()
                == "no"
            ):
                print("\nThank you for using my calculator.")
                break

            clear_screen()

        except Exception:
            print("\nAn error occurred")
            if (
                input("\nIf you want to continue, type 'yes', else type 'no': ")
                .strip()
                .lower()
                == "no"
            ):
                print("\nThank you for using my calculator.")
                break



if __name__ == "__main__":
    main()