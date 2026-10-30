"""
Drill 02: Constant vs Linear Time Operations
Module: 02-big-o-complexity
"""


def get_extremes_constant(nums: list) -> tuple:
    """
    Returns (first, last) element in O(1) constant time.

    Raises:
        ValueError: If nums is empty.
    """
    # TODO: Implement O(1) index access
    if not nums:
        raise ValueError

    return nums[0], nums[-1]
    
print(get_extremes_constant([10, 20, 30]))

def get_extremes_linear(nums: list) -> tuple:
    """
    Returns (first, last) element in O(n) linear scan time without direct indexing.

    Raises:
        ValueError: If nums is empty.
    """
    # TODO: Implement O(n) sequential extraction
    if not nums:
        raise ValueError

    first = 0
    last = 0

    for i in range(len(nums)):
        if i == 0:
            first = nums[i]

        if nums[i] == nums[-1]:
            last = nums[i]

    return first, last
    
