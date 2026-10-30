"""
Drill 06: Prefix Sum Optimization
Module: 02-big-o-complexity
"""


class RangeSumQuery:
    """
    Precomputes running prefix sums to answer range queries in O(1) time.
    """

    def __init__(self, nums: list[int]):
        # TODO: Precompute prefix sums in O(n)
        self.nums = nums
        self.totals = [0]
        for i in self.nums:
            self.totals.append(self.totals[-1] + i)

    def query(self, left: int, right: int) -> int:
        """
        Returns sum of nums[left:right+1] in strictly O(1) time.
        """
        # TODO: Calculate range sum using prefix lookup in O(1)
        self.right = self.totals[right + 1]
        self.left = self.totals[left]
        return self.right - self.left