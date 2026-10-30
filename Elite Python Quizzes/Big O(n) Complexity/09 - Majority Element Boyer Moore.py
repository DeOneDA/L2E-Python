"""
Drill 09: Boyer-Moore Majority Vote
Module: 02-big-o-complexity
"""


def majority_element(nums: list[int]) -> int:
    """
    Finds the majority element in O(n) time and O(1) space.
    """
    # TODO: Implement Boyer-Moore candidate & count tracking
    res = nums[0]
    count = 1
    for n in range(1, len(nums)):
        if count == 0:
            res = nums[n]

        if nums[n] == res:
            count += 1
            continue

        count -= 1

    return res
