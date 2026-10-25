"""
Drill 01: Functions as First-Class Citizens
Module: 04-decorators-and-closures
"""


def make_multiplier(factor: int) -> callable:
    """
    Returns a function that multiplies its argument by factor.
    """
    # TODO: Implement closure returning inner multiplier function
    def wrapper(num):
        return num * factor
    return wrapper


def apply_pipeline(data: list[int], operations: list[callable]) -> list[int]:
    """
    Applies a sequence of functional operations to each element in data.
    """
    # TODO: Pipe each element through operations list
    result = []
    for i in data:
        start = operations[0](i)
        end = operations[1](start)
        result.append(end)
    return result
