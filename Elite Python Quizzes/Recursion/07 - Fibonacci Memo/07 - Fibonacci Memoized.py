"""
Drill 07: Fibonacci with Memoization
Module: 01-recursion
"""


def fibonacci(n: int, memo: dict | None = None) -> int:
    """
    Recursively computes the n-th Fibonacci number using memoization.

    Args:
        n (int): Non-negative integer.
        memo (dict | None): Optional dictionary caching previous results.

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n < 0.
        TypeError: If n is not an integer.
    """
    # TODO: Implement validation, base cases, memo lookup, and recursive caching
    if n < 0:
        raise ValueError("n must be non-negative")

    if type(n) != int:
        raise TypeError("n must be an integer")
    
    if memo == None:
        memo = {0: 0, 1: 1}

    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]