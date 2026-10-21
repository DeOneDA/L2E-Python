# Time Complexity of O(n ^ 2)
def majority_element(numbers):
    if len(numbers) == 0:
        return None
    
    result = None

    for i in range(len(numbers)//2 + 1):
        count = 1
        for j in range(i+1, len(numbers)):
            if numbers[j] == numbers[i]:
                count += 1
        if count > len(numbers)//2:
            result = numbers[i]
            break


    return result

# Time Complexity of O(n)
def majority_element(numbers):
    if len(numbers) == 0:
        return None

    half = len(numbers)//2

    candidate = 0
    votes = 0

    for i in numbers:
        if votes == 0:
            candidate = i

        if i == candidate:
            votes += 1
        else:
            votes -= 1


    count = 0

    for j in numbers:
        if j == candidate:
            count += 1

    if count > half:
        return candidate
    return None