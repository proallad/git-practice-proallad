"""Utility functions for the calculator project."""


def _validate_number(value, name):
    """Raise TypeError when a value is not an int or float."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")


def add(a, b):
    """Return the sum of two numbers."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b
def divide(a, b):
    """Return the result of dividing a by b."""
    _validate_number(a, "a")
    _validate_number(b, "b")

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b