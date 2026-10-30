"""
Drill 07: Two Sum Algorithmic Trade-offs
Module: 02-big-o-complexity
"""


def two_sum_hash(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Finds two indices whose values sum to target in O(n) time and O(n) space.
    """
    # TODO: Implement one-pass hash map complement lookup
    dict_nums = {}
    for i in range(len(nums)):
        dict_nums[nums[i]] = i
    
    for i in range(len(nums)):
        holder = target - nums[i]

        if holder in dict_nums.keys() and dict_nums[holder] != i:
            return (i, dict_nums[holder])

    return None