# Implement Insertion Sort and return intermediate states.

# Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right. It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

# Objective:

# Given a list of key-value pairs, sort the list by key using Insertion Sort. Return a list of lists showing the state of the array after each insertion. If two key-value pairs have the same key, maintain their relative order in the sorted list.

# Input:

# pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).
# Example 1:

# Input:
# pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

# Output:
# [[(5, "apple"), (2, "banana"), (9, "cherry")], 
#  [(2, "banana"), (5, "apple"), (9, "cherry")], 
#  [(2, "banana"), (5, "apple"), (9, "cherry")]]
# Notice that the output shows the state of the array after each insertion. The last state is the final sorted array. There should be pairs.length states in total.

# Example 2:

# Input:
# pairs = [(3, "cat"), (3, "bird"), (2, "dog")]

# Output:
# [[(3, "cat"), (3, "bird"), (2, "dog")], 
#  [(3, "cat"), (3, "bird"), (2, "dog")],
#  [(2, "dog"), (3, "cat"), (3, "bird")]]
# In this example, you can observe that the pairs with key=3 ("cat" and "bird") maintain their relative order, illustrating the stability of the Insertion Sort algorithm.
from typing import Optional
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
# # Time: O(n ** 2), Memory : O(n)
# class Solution:
#     def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:

#         for i in range(len(pairs)):
#             while i > 0 and pairs[i].key < pairs[i - 1].key:
#                 pairs[i], pairs[i - 1] = pairs[i - 1], pairs[i]
#                 i -= 1
        
#         return pairs

# test = Solution()
# pairs = [Pair(5, "Apple"), Pair(1, "Orange"), Pair(3, "Guava")]

# output = test.insertionSort(pairs)
# for o in output:
#     print(o.key, o.value)

def insertionSort(nums: Optional[int]):
    for i in range(1, len(nums)):
        # 若當前元素小於左邊元素，則進行swap，直到當前元素不小於左邊元素
        while i > 0 and nums[i] < nums[i - 1]: 
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1
    
    return nums

print(insertionSort([2,3,1,4,6]))


