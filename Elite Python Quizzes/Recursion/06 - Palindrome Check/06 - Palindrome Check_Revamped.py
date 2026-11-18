"""
Drill 06: Recursive Palindrome Check
Module: 01-recursion
"""


def is_palindrome(text: str, left: int = 0, right: int | None = None) -> bool:
    """
    Recursively determines if a string is a palindrome using two pointers.

    Args:
        text (str): String to check.
        left (int): Left index pointer.
        right (int | None): Right index pointer.

    Returns:
        bool: True if text is a palindrome, False otherwise.

    Raises:
        TypeError: If text is not a string.
    """
    # TODO: Implement validation, base cases, and two-pointer recursive convergence
    if type(text) != str: raise TypeError
    if len(text) == 0: return True
    right = len(text)-1-left
    text = text.lower()
    if left >= right: return True
    if text[left] != text[right]: return False
    return is_palindrome(text, left + 1, right - 1)