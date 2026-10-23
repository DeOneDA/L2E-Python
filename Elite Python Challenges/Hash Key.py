def hash_key(key):
    return sum(ord(char) for char in key) % 7

print(hash_key("dog"))

# Calculate:
# The slot index for cat would be (99 + 97 + 116) % 7 == 4
# The slot index for act would be (97 + 99 + 116) % 7 == 4
# The slot index for dog would be (100 + 111 + 103) % 7 == 6
# The slot index for god would be (103 + 111 + 100) % 7 == 6

# Reason About Collisions:
# Based on the slot indexes above there would be a collision in slot
# index 4 and 6 because two different keys ("cat" & "act") and ("dog" 
# & "god") are being stored in the same index slots, however this doesn't
# mean that those two keys are equal in the respective index slots, instead
# python handles them with strategies like chaining in a list or checking
# nearby slots to see of they are free so they can allocate the extra value
# into the empty slot.

# Implement:
