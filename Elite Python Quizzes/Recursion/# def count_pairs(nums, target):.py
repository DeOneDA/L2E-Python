# def count_pairs(nums, target):
#     targets = {}
#     count = 0
#     for i in nums:
#         if target - i in targets:
#             continue
#         targets[i] = target - i
#         count += 1

#     return count

# count_pairs([1, 5, 7, -1, 5], 6)

def count_pairs(nums, target):
    seen = {}
    count = 0
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            count += 1
        seen[n] = i

    return count

count_pairs([1, 5, 7, -1, 5], 6)
