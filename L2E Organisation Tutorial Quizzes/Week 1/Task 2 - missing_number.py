def find_missing(nums):
    missing = 0
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 1:
            continue
        else:
            missing = nums[i] + 1
            break
    return missing