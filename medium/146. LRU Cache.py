# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# time complexity: the worst case is O(n). Becasue deque.remove() is O(n) in the worst case and "in" is O(n) in the worst case.
# space complexity: O(n) where n is the capacity of the cache
# from collections import deque

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.order = deque()
#         self.size = capacity

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1

#         self.order.remove(key)    
#         self.order.append(key)
#         return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.order.remove(key)
#         elif len(self.cache) >= self.size:
#             del self.cache[self.order.popleft()]
        
#         self.cache[key] = value
#         self.order.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# time complexity: O(1) for both get and put operations
# space complexity: O(n) where n is the capacity of the cache
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.size: # key is not in the cache but the size is larger than capacity
            self.cache.popitem(last=False) # remove the oldest key from the OrderedDict
        
        self.cache[key] = value