"""
Drill 05: Count Target Occurrences
Module: 01-recursion
"""


def count_occurrences(items: list, target, index: int = 0) -> int:
    """
    Recursively counts how many times target appears in items.

    Args:
        items (list): The list to search.
        target: The item to count.
        index (int): Current position.

    Returns:
        int: Frequency of target in items.

    Raises:
        TypeError: If items is not a list.
    """
    # TODO: Implement validation, base case, and recursive accumulation
    if type(items) != list: raise TypeError
    return 0 if index == len(items) else 1 + count_occurrences(items, target, index + 1) if items[index] == target else count_occurrences(items, target, index + 1)