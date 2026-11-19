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
    if type(arr) != list:
        raise TypeError

    if type(target) != int:
        raise TypeError

    if arr == []:
        return -1

    if arr[low] == target:
        return low

    low += 1

    if low == len(arr):
        return -1
    
    return binary_search(arr, target, low)

# Alternative Solutions:
# lst = [1, 3, 5, 7, 9, 11]
# target = int(input("Enter your target number: "))
# result = [ls for ls in range(len(lst)) if lst[ls] == target]
# if not result:
#     print(-1)
# else:
#     print(result)


# def binary_search(items, target):
#     test = [x for x in items if x == target]
#     return test[0] if test else -1

# print(binary_search([1, 3, 5, 7, 9, 11], 4))
# print(binary_search([1, 3, 5, 7, 9, 11], 7))