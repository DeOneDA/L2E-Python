"""
Drill 05: Load Factor & Distribution Metrics
Module: 03-hashing-and-hashmaps
"""

class MeasurableHashMap:
    """Hash map with real-time load factor and distribution telemetry."""

    def __init__(self, capacity: int = 7):
        # TODO: Initialize map
        self.result = [[] for _ in range(capacity)]
        self.capacity = capacity

    def _hash(self, key: str) -> int:
        # TODO: Compute bucket index
        return sum(ord(c) for c in key) % self.capacity
    
    def put(self, key: str, value: any) -> None:
        slot = self._hash(key)
        for j, (keys, _) in enumerate(self.result[slot]):
            if keys == key:
                self.result[slot][j] = (key, value)
                return None
        self.result[slot].append((key, value))
        return None
    
    def load_factor(self) -> float:
        """Returns n / capacity."""
        # TODO: Calculate load factor
        return round(sum(len(value) for value in self.result)/self.capacity, 4)

    def bucket_stats(self) -> dict:
        """Calculates distribution metrics."""
        # TODO: Calculate empty_buckets, max_bucket_length, collision_rate
        empty_buckets = sum(1 for slot in self.result if len(slot) == 0)
        max_bucket_length = max(len(slot) for slot in self.result)
        total_items = sum(len(values) for values in self.result)
        non_empty_buckets = sum(1 for slot in self.result if len(slot) > 0)
        collision_rate = round(((total_items - non_empty_buckets)/total_items), 2) if total_items > 0 else 0
        return {
            "empty_buckets": empty_buckets,
            "max_bucket_length": max_bucket_length,
            "collision_rate": collision_rate
        }
        
