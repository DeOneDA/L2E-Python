def rotate_list(nums, k):
    if len(nums) == 0:
        return []
    
    slicer = k * -1
    if k > len(nums):
        new = k % len(nums)
        slicer = new * -1
    
    start = nums[slicer:]
    end = nums[:slicer]

    return start + end
