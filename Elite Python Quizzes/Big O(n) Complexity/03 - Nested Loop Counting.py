"""
Drill 03: Dependent Nested Loop Counting
Module: 02-big-o-complexity
"""


def count_unique_pairs(items: list) -> tuple[list[tuple], int]:
    """
    Generates all unique index-ordered pairs and returns (pairs, comparisons_count).
    """
    # TODO: Implement dependent nested loop pair generation
    pairs = []
    count = 0

    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[j] > items[i] and (items[i], items[j]) not in pairs:
                pairs.append((items[i], items[j]))
            count += 1

    return pairs, count