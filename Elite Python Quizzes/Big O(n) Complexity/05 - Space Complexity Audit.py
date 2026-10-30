"""
Drill 05: Space Complexity Audit
Module: 02-big-o-complexity
"""


def reverse_with_allocation(nums: list) -> list:
    """
    Returns a new reversed list in O(n) time and O(n) auxiliary space.
    """
    # TODO: Implement non-mutating copy reversal
    res = []
    for i in range(len(nums)-1, -1, -1):
        res.append(nums[i])

    return res


def reverse_in_place(nums: list) -> None:
    """
    Reverses nums in-place in O(n) time and O(1) auxiliary space using two pointers.
    """
    # TODO: Implement in-place two-pointer swap
    if not nums:
        return None
    
    end = -1
    for i in range(0, len(nums)//2):
        nums[i], nums[end] = nums[end], nums[i]
        end -= 1

    return None