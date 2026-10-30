"""
Drill 04: Logarithmic Growth
Module: 02-big-o-complexity
"""


def count_divisions(n: int) -> int:
    """
    Returns the number of times n can be divided by 2 until it reaches 1.

    Raises:
        ValueError: If n <= 0.
    """
    # TODO: Implement step-halving loop
    if n <= 0:
        raise ValueError("n must be positive")

    if n == 1:
        return 0

    return 1 + count_divisions(n//2)

    # Alternative Solution

    # count = 0
    # while n > 1:
    #     n  = n//2
    #     count += 1

    # return count