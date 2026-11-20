"""
Drill 01: Manual Hash Function
Module: 03-hashing-and-hashmaps
"""

def hash_key(key: str, capacity: int = 7) -> int:
    """
    Deterministically maps a string key to a slot index in the range [0, capacity - 1].

    Args:
        key (str): The string key to hash.
        capacity (int): The number of slots in the table. Defaults to 7.

    Returns:
        int: The bucket index.

    Raises:
        TypeError: If key is not a str or capacity is not an int.
        ValueError: If capacity <= 0.
    """
    # TODO: Implement type validation and modulo ASCII hash
    if type(key) != str: raise TypeError
    if type(capacity) != int: raise TypeError
    if capacity <= 0: raise ValueError
    return sum(ord(c) for c in key) % capacity
