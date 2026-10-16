def frequency_sort(items):
    hold = {}
    for num in items:
        if num not in hold:
            hold[num] = 1
        else:
            hold[num] += 1

    sorted_by_key = sorted(hold.items())
    sorted_dict = {}

    for key, value in sorted_by_key:
        sorted_dict[key] = value

    hold = sorted(sorted_dict.items(), key = lambda x: x[1], reverse = True)
    
    res = []
    for num, count in hold:
        holder = [num] * count
        res.extend(holder)

    return res

print(frequency_sort([1, 2, 7, 3, 5, 3, 2, 4, 4, 1, 1, 7]))