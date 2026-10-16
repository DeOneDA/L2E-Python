def remove_duplicates(nums):
    result = []
    for i in nums:
        if i in result:
            continue
        else:
            result.append(i)

    return result