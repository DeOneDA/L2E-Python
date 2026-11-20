"""
Drill 04: Separate Chaining Hash Map
Module: 03-hashing-and-hashmaps
"""

class ChainingHashMap:
    """A 7-slot hash map using separate chaining for collision resolution."""

    def __init__(self, capacity: int = 7):
        # TODO: Initialize buckets and size counter
        self.result = [[] for _ in range(capacity)]
        self.capacity = capacity

    def _hash(self, key: str) -> int:
        # TODO: Compute bucket index
        return sum(ord(c) for c in key) % self.capacity

    def put(self, key: str, value: any) -> None:
        # TODO: Insert or update key-value pair
        slot = self._hash(key)
        for j, (keys, _) in enumerate(self.result[slot]):
            if keys == key:
                self.result[slot][j] = (key, value)
                return None
        self.result[slot].append((key, value))
        return None

    def get(self, key: str) -> any:
        # TODO: Retrieve value or return None        
        slot = self._hash(key)
        bucket = self.result[slot]
        for pair in bucket:
            keys, value = pair
            if keys == key:
                return value
        return None 

    def delete(self, key: str) -> bool:
        # TODO: Delete key if present
        slot = self._hash(key)
        for j, (keys, _) in enumerate(self.result[slot]):
            if key == keys:
                self.result[slot].pop(j)
                return True
        return False

    def __len__(self) -> int:
        return sum((len(value) for value in self.result))

    def __contains__(self, key: str) -> bool:
        slot = self._hash(key)
        for keys, _ in self.result[slot]:
            if key == keys:
                return True
        return False