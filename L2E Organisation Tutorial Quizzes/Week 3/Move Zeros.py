def move_zeros(numbers):
    if len(numbers) == 0 or len(numbers) == 1:
        return numbers

    i = 0
    length = 0

    for num in numbers:
        if num != 0:
            length += 1

    for j in range(len(numbers)):
        if numbers[j] != 0:
            numbers[i] = numbers[j]
            i += 1
            continue
            
    for k in range(length, len(numbers)):
        numbers[k] = 0

    return numbers

# Alternative Solution:
# def move_zeros(numbers):
#     i = 0
#     for j in range(len(numbers)):
#         if numbers[j] != 0:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#             i += 1

#     return numbers