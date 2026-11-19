"""
Drill 08: Pure Recursive Binary Search
Module: 01-recursion
"""


def binary_search(arr: list[int], target: int, low: int = 0, high: int | None = None) -> int:
    """
    Recursively searches for target in sorted arr using binary search pointers.

    Args:
        arr (list[int]): Sorted list of integers.
        target (int): Integer to find.
        low (int): Lower bound index.
        high (int | None): Upper bound index.

    Returns:
        int: Index of target if found, else -1.

    Raises:
        TypeError: If inputs are invalid types.
    """
    # TODO: Implement validation, base cases, midpoint calculation, and recursive step
    if type(arr) != list: raise TypeError
    if type(target) != int: raise TypeError
    if not high: high = len(arr) - 1
    return -1 if low > high else low if arr[low] == target else high if arr[high] == target else binary_search(arr, target, low+1, high-1)