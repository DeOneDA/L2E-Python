"""
Drill 10: In-Place Sorted Array Merge
Module: 02-big-o-complexity
"""


def merge_inplace(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merges nums2 into nums1 in-place in O(m + n) time and O(1) space.
    """
    # TODO: Implement backwards three-pointer placement
    j = 0
    for i in range(m, len(nums1)):
        nums1[i] = nums2[j]
        j += 1

    for i in range(1, len(nums1)-1):
        if nums1[i-1] < nums1[i] and nums1[i] > nums1[i+1]:
            nums1[i], nums1[i+1] = nums1[i+1], nums1[i]
    
    return None