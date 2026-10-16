def intersection(a, b):
    result = []

    for i in a:
        if i in b and i not in result:
            result.append(i)

    return result