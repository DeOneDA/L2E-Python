def most_frequent(items):
    result = {}
    count = 0
    highest = None

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    for i, value in result.items():
        if value > count:
            highest, count = i, value
            

    return highest