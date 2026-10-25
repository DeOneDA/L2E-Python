"""
Drill 04: Pure Recursive List Sum
Module: 01-recursion
"""


def sum_list(numbers: list[int | float], index: int = 0) -> int | float:
    """
    Recursively sums a list of numbers using an index pointer.

    Args:
        numbers (list): List of integers or floats.
        index (int): Current position in the list.

    Returns:
        int | float: The sum of elements.

    Raises:
        TypeError: If numbers is not a list.
    """
    # TODO: Implement validation, base case, and index-based recursive step
    if type(numbers) != list:
        raise TypeError("Input must be a list")

    if len(numbers) == 0 or index == len(numbers):
        return 0
    
    if index < len(numbers):
        num = index
        index += 1
        return numbers[num] + sum_list(numbers, index)
    

print(sum_list([10, -5, 2]))