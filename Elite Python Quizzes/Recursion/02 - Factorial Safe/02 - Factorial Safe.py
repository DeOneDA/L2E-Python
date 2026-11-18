"""
Drill 02: Safe Factorial
Module: 01-recursion
"""


def factorial(n: int) -> int:
    """
    Recursively calculates n! with strict validation.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: The factorial value.

    Raises:
        ValueError: If n < 0.
        TypeError: If n is not an integer.
    """
    # TODO: Implement validation, base case, and recursive step
    if type(n) != int:
        raise TypeError("Input must be an integer")
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)