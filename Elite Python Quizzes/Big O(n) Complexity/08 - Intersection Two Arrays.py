"""
Drill 08: Intersection of Two Arrays
Module: 02-big-o-complexity
"""


def intersection(a: list, b: list) -> list:
    """
    Returns unique elements present in both a and b in O(len(a) + len(b)) time.
    """
    # TODO: Implement O(m + n) set-based intersection
    set_a = set(a)
    set_b = set(b)

    return list(set_a & set_b)
