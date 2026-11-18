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
    if type(n) != int: raise TypeError
    if n < 0: raise ValueError
    return 1 if n == 0 else n * factorial(n-1)