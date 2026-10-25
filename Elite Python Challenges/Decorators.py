def announce(func):
    print("Decorator is running")

    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result

    return wrapper

@announce
def multiply(a, b):
    print("Multiplying")
    return a * b

print("Program started")
answer = multiply(3, 4)
print("Answer:", answer)

# Predict Output:
# Decorator is running
# Program Started
# Before Function
# Multiplying
# After Function
# Answer:
# The reason why 'Decorator is running' is printed before
# 'Program Started' is because of the shorthand @announce which
# initializes the decorator on the multiply function, so the moment
# we call the multiply function, we automatically initiate the decorator
# function first.

# Explain The Parts:
# @announce is the distinct chateristic of decorators
# that separate them from closures, this simple line performs 
# the initializing line of code of a closure, for instance, writing
# test = announce(multiply) is a closure method of calling the higher
# order function on the multiply function, but for decorators
# @announce does this automatically.
# The wrapper is the inner function that applies the parameters into
# the multiply function, it works hand in hand with the *args and **kwargs
# where *args means that it doesn't matter the number of single arguments 
# passed in the parameter (5, 6, 7) while **kwargs means that it doesn't matter 
# the number of keyword arguments passed into the parameter (count = 5, name = "Drake").
# The purpose of the wrapper is to apply the function passed into the announce function
# on the parameters given to it.
# Return result matters in the wrapper because after perfoming the task the function
# needs to return the output back to the terminal/user.

# Repair a bug:
def announce(func):
    print("Decorator is running")

    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        # return result # Uncomment this to correct the code

    return wrapper

@announce
def multiply(a, b):
    print("Multiplying")
    return a * b

print("Program started")
answer = multiply(3, 4)
print("Answer:", answer)

# The reason why the answer returns None is because in our wrapper
# function we are performing the calculation, however we are not 
# telling python to give the answer to that calculation back as it's
# output hence why you get a None result.

# Implement:
def count_calls(func):
    count = 0
    def wrapper(*args):
        nonlocal count
        count += 1
        result = func(*args)
        if count == 3:
            print(f"Count = {count}")
        return result
    return wrapper

@count_calls
def add(x, y):
    res = x + y
    return res

print(add(5, 7))
print(add(4, 6))
print(add(3, 5))