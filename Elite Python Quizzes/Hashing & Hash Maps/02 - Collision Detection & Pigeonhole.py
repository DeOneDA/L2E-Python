"""
Drill 02: Collision Detection & Pigeonhole Principle
Module: 03-hashing-and-hashmaps
"""

def analyze_collisions(keys: list[str], capacity: int = 7) -> dict:
    """
    Distributes keys across slots and reports collision metrics.

    Args:
        keys (list[str]): List of string keys to analyze.
        capacity (int): Number of slots in the hash table.

    Returns:
        dict: Summary containing 'slots', 'collision_count', and 'max_bucket_depth'.

    Raises:
        TypeError: If keys is not a list or contains non-strings, or capacity is invalid.
        ValueError: If capacity <= 0.
    """
    # TODO: Implement distribution and collision metrics
    if type(keys) != list: raise TypeError
    if type(capacity) != int: raise TypeError
    if capacity <= 0: raise ValueError
    res = {"slots": {slot: [] for slot in range(capacity)},
           "collision_count": 0,
           "max_bucket_depth": 0}
    for key in keys:
        slot = sum(ord(c) for c in key) % capacity
        res["slots"][slot].append(key)
        if len(res["slots"][slot]) > 1:
            res["collision_count"] += 1
    
    if res["slots"]:
        res["max_bucket_depth"] = max((len(values) for values in res["slots"].values()))

    return res