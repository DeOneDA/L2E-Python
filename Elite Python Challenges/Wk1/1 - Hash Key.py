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
class SevenSlotHashMap:
    def __init__(self, capacity = 7):
        self.capacity = capacity
        self.slots = [[] for _ in range(self.capacity)]

    def hash(self, key):
        total_hash = 0
        primer = 29

        for ch in key:
            total_hash = (total_hash * primer) + ord(ch)

        slot_index = total_hash % self.capacity
        return slot_index

    def put(self, key, value):
        key_index = self.hash(key)
        slot = self.slots[key_index]

        for index, item in enumerate(slot):
            if item[0] == key:
                slot[index] = [key, value]
                return f"Successfully updated {key} to {value}"

        slot.append([key, value])
        return f"Successfully Added {key} and {value} to the Map"

    def get(self, key):
        key_index = self.hash(key)
        slot = self.slots[key_index]

        for items in slot:
            if items[0] == key:
                return items[1]

        return None

    def delete(self, key):
        key_index = self.hash(key)
        slot = self.slots[key_index]

        for index, items in enumerate(slot):
            if items[0] == key:
                slot.pop(index)
                return f"Successfully removed {key}"

        return f"This {key} doesn't exist in the map"

seven_hash = SevenSlotHashMap()
print(seven_hash.put("Drake", 25))
print(seven_hash.get("Drake"))
print(seven_hash.delete("Drake"))

# Analyze:
# Based on the SevenSlotHashMap built above the average time
# complexity for .get and .delete methods is O(n) while its the
# same for .put when updating an existing key with a new value,
# however, if you are inputing a new key, value pair into the hash
# map then you get an implementation speed of O(1). The reason for 
# this is because when updating, getting or deleting from the hash 
# map we are essentially looping through the entire hashmap in order
# to get to the right pair we wish to work on. The issue with this hash
# map can be really felt when we have over 100 key, value pairs in each
# slot of the map because in order to perform any update, get any value
# or delete any pair we need to first loop through each and every single
# item in the list to find the right key we are looking for. A worse case
# scenario can be envisioned when we have a situation where we have over 500
# pairs in each slot and we wish to get the value of pair 499 in slot 5,
# regardless of how fast it's able to identify which slot the pair can be 
# located in, we have to first loop through 498 individual pairs while comparing
# the keys of each of these pairs with the one we are looking for just to arrive
# at pair 499 before displaying the value of that key. Assuming your laptop
# performance is a factor in this case then what about 100,000,000 pairs?
# As long as we are limited to the constraint of 7 slots in this map we will
# constantly have an issue of increasing time complexity as the map gets bigger.
# A larger table size of the map would greatly improve the borderline limit of
# the map that comes with the constraint of O(n) but it doesn't solve the issue
# because at the end of the day, the larger the map the more time it takes, hence 
# the best solution comes with implementing an automatic table checker that doubles
# the size of our table as soon as it gets to a certain capacity. This makes our
# hash map dynamic while also making the speed at which it checks the contents of 
# each slot minimal which would end up making our average time complexity of the
# program to be O(1).