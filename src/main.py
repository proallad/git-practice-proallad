"""Main program for the Git practice assignment."""

from datetime import date

from utils import add, divide, multiply, subtract


STUDENT_NAME = "Proallad"


def main():
    """Run a short calculator demonstration."""
    print(f"Student: {STUDENT_NAME}")
    print(f"Today's date: {date.today().isoformat()}")

    first_number = 10
    second_number = 5

    try:
        print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
        print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}")
        print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}")
        print(f"{first_number} / {second_number} = {divide(first_number, second_number)}")
    except (TypeError, ValueError) as error:
        print(f"Calculation error: {error}")


if __name__ == "__main__":
    main()