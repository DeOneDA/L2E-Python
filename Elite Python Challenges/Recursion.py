def total(n):
    if n == 1:
        return 1
    return n + total(n - 1)

# Trace It:
# total(4) would give an output of 4 + total(3)
# total(3) would then be called which would give 3 + total(2)
# total(2) would then be called which would give 2 + total(1)
# and since total(1) was taken care of in the if statement that
# declared if n == 1 return 1, then python would take 1 and stack
# upwards meaning 1 + 2 + 3 + 4 which would output a total of 10.

# Find The Problem:
# The current code would lead to an infinite loop for any case when
# n < 1, e.g, 0, -1, -10, etc. Below is the fix of the code:

def total(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError

    if n < 0:
        raise ValueError
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    # elif n in [0, 1]:
    #   return n

    return n + total(n-1)

# I used try and except to catch non-integer values so that the
# program doesn't crash while I took care of negative, 0 and 1 values
# with if conditions before returning the recursive call.

# Explain The Termination:
# The base case is defined in the if condition that checks if n is
# either 0 or 1 while the recursive call is found in the return 
# statement at the bottom of the function that calls the function again
# with n - 1, this is what ensures that eventually the value of n reaches
# the base case stated in the if condition. In the first code a situation
# where the base case is never reached could potentially occur which would
# lead to an infinite loop.

# Code It:
def countdown_sum(n):
    # if n <= 0:
    #     return n

    # if n % 2 != 0:
    #     return n + countdown_sum(n-1)
    
    # return countdown_sum(n-1)

    return n if n <= 1 else countdown_sum(n-1) if n%2 == 0 else n + countdown_sum(n-1)

print(countdown_sum(10))
print(countdown_sum(4))
print(countdown_sum(1))
print(countdown_sum(0))