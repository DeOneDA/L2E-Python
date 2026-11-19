"""
Drill 09: Flatten Arbitrarily Nested List
Module: 01-recursion
"""


def flatten(nested: list, index: int = 0) -> list:
    """
    Recursively flattens an arbitrarily nested list of items.

    Args:
        nested (list): The nested list.
        index (int): Pointer index in the current list level.

    Returns:
        list: A 1D flattened list.

    Raises:
        TypeError: If nested is not a list.
    """
    # TODO: Implement structural recursion across nested elements
    if type(nested) != list: raise TypeError
    if index == len(nested): return []
    if type(nested[index]) != list: return [nested[index]] + flatten(nested, index + 1)
    return sorted(flatten(nested, index + 1) + flatten(nested=nested[index], index=0))