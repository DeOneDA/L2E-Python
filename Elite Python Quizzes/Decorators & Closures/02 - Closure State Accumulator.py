"""
Drill 02: Closure State Accumulator
Module: 04-decorators-and-closures
"""


def make_accumulator(initial_value: int = 0) -> callable:
    """
    Returns an accumulate function retaining state across calls via nonlocal.
    """
    # TODO: Implement closure with nonlocal accumulator
    total = initial_value
    def accumulate(delta):
        nonlocal total
        total += delta
        return total
    return accumulate
