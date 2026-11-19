"""
Drill 10: Deep Nested Dictionary Lookup
Module: 01-recursion
"""


def deep_get(data: dict, keys: list[str], index: int = 0):
    """
    Recursively retrieves a value from a nested dictionary following a list of keys.

    Args:
        data (dict): The root or current dictionary.
        keys (list[str]): Path of keys to follow.
        index (int): Current position in keys.

    Returns:
        The retrieved value, or None if not found.
    """
    # TODO: Implement base cases and recursive dictionary descent
    if not keys:
        return None

    if type(data) != dict and index == 0:
        raise TypeError

    if index == len(keys):
        return data
    
    holder = keys[index]
    index += 1

    if type(data) == dict:
        if holder in data:
            data = data[holder]
            return deep_get(data, keys, index)

    return None