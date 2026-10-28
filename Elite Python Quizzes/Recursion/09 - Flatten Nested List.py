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
    if type(nested) != list:
        raise TypeError("Input must be a list")

    if nested == []:
        return []

    if type(nested[0]) != list:
        return [nested[index]] + flatten(nested[1:], index)

    return flatten(nested[0], index) + flatten(nested[1:], index)