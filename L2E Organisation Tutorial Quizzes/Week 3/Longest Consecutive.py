# Personal Solution
def longest_consecutive(numbers):
    if len(numbers) == 0:
        return 0

    count = 1
    i = 0
    
    j = numbers[i] + 1
    storage = []

    while i < len(numbers):
        if j in numbers:
            count += 1
            j += 1
            continue
        elif j not in numbers:
            storage.append(count)
            count = 1
            i += 1
            if i == len(numbers):
                break
            else:
                j = numbers[i] + 1
            continue

    res = storage[0]

    for num in storage:
        if num > res:
            res = num
    
    return res

# Alternative Solution
def longest_consecutive(numbers):
    if len(numbers) == 0:
        return 0

    numbers = set(numbers)
    count = 1
    storage = 0
    for i in numbers:
        if i - 1 in numbers:
            continue
        while i + 1 in numbers:
            count += 1
            i += 1
        storage = max(count, storage)
        count = 1

    return storage