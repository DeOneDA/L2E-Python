def fizzbuzz(n):
    result = []
    if n == 0:
        return result
    
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(i))
    return result
