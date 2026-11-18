"""
Drill 03: Recursive String Reversal
Module: 01-recursion
"""


def reverse_string(text: str) -> str:
    """
    Recursively reverses a string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    # TODO: Implement validation, base cases, and head/tail recursive step
    if type(text) != str: raise TypeError
    return "" if len(text) == 0 else text[-1] + reverse_string(text[:-1])