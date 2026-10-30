"""
Drill 01: Duplicate Detection & The 3 Classical Trade-offs
Module: 02-big-o-complexity
"""


def has_duplicate_quadratic(items: list) -> bool:
    """
    Checks for duplicates in O(n^2) time and O(1) space.
    """
    # TODO: Implement brute-force nested loop check
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j] == items[i]:
                return True

    return False

print(has_duplicate_quadratic([1, 2, 3, 2]))

def has_duplicate_hash(items: list) -> bool:
    """
    Checks for duplicates in expected O(n) time and O(n) space.
    """
    # TODO: Implement set-based early return check
    holder = set(items)
    if len(holder) == len(items):
        return False

    return True

print(has_duplicate_quadratic([1, 2, 3, 2]))

def has_duplicate_sorted(items: list) -> bool:
    """
    Checks for duplicates in O(n log n) time using sorting and adjacent comparison.
    """
    # TODO: Implement sorted adjacent comparison check
    new = sorted(items)

    for i in range(len(new)-1):
        if new[i+1] == new[i]:
            return True

    return False

print(has_duplicate_quadratic([1, 2, 3, 2]))