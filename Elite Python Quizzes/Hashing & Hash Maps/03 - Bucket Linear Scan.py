"""
Drill 03: Bucket Linear Scan
Module: 03-hashing-and-hashmaps
"""

def bucket_get(bucket: list, key: str) -> tuple[bool, any]:
    """Searches a bucket for a key."""
    # TODO: Implement linear scan
    for pair in bucket:
        keys, value = pair
        if keys == key:
            return (True, value)

    return (False, None) 

def bucket_put(bucket: list, key: str, value: any) -> bool:
    """Updates existing key or appends new key-value pair."""
    # TODO: Implement update-or-insert
    for i, (keys, _) in enumerate(bucket):
        if keys == key:
            bucket[i] = (key, value)
            return False
    bucket.append((key, value))
    return True



def bucket_delete(bucket: list, key: str) -> bool:
    """Deletes a key from the bucket if present."""
    # TODO: Implement deletion
    for i, (keys, _) in enumerate(bucket):
        if key == keys:
            bucket.pop(i)
            return True

    return False