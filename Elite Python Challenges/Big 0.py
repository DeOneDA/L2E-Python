def has_duplicate_a(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

def has_duplicate_b(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

def has_duplicate_c(items):
    items = sorted(items)
    for i in range(1, len(items)):
        if items[i] == items[i - 1]:
            return True
    return False


# Analyze:
# for the has_duplicate_a, the time complexity is O(n^2) because
# of the nested loop in it while for has_duplicate_b, the time
# complexity is O(n) while the third function is O(nlog(n)).

# Predict Before Running:
# If you have a list of 2 items then the third function would be the
# fastest because of log n, however if we have a list of over 10k items
# then the slowest would be the first function because the longer the list
# the slower it gets because of how much time it takes to loop twice while
# the fastest would be the second loop, the reason for this is once again
# the log n, log n of any length less than 10 would yield 0.something which
# in turn makes the code faster as compared to the second function, but the
# moment it goes beyond 10 in length then it becomes minutely slower than O(n).

# Correct The Misconception:
# The misconception arises from the understanding of set as a function
# in the implementation of the second function, the set is being used to
# create a new list that is being used to validate if the number we are
# checking already exists in that list. In reality, the time complexity
# of the second function is O(n) because the longer the list, the more
# time it takes to go through all the items in that list.

# Make An Engineering Choice:
# In a situation where we have millions of records I would go for the second
# implementation because of how large the list is, to put it in practical sense
# O(n) compared to O(nlog(n)), if we have a list of 5 items where n = 5:
# O(n) == O(5), whereas
# O(nlog(n)) == O(5 * log(5)) == O(3.5)
# In this case we can see that the third implementation is faster than the second
# implementation, however if we have a list of length 1000, the reality becomes:
# O(n) == O(1000)
# O(nlog(n)) == O(1000 * log(1000)) == O(3000)
# As you can see the when we go beyond log(10) which is equals to 1, then the third
# implementation becomes a lot slower than the second implementation, as for the first
# implementation, the reality of that implementation is:
# O(n^2) == O(5 * 5) == O(25), and
# O(n^2) == O(1000 * 1000) == O(1,000,000)
# As you can see the first implementation, no matter the situation is just slow.
# So for millions of records I would definitely go for the second implementation in terms
# of time complexity.
# In terms of Space Complexity, the first implementation is O(1) while the second and third
# is O(n), now because of my choice of implementing the second function, I'm trading off the
# auxillary space complexity of O(n) for O(1) which is worth it when you consider the amount of
# items the list has as well as how fast the function is supposed to run for.