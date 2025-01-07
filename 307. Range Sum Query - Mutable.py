# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]

# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 104 calls will be made to update and sumRange.
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] * len(nums) * 4
        self.arr = nums
        self.buildTree(0, 0, len(self.arr) - 1)

    def buildTree(self, rootNode: int, L: int, R: int) -> None:
        if L == R:
            self.tree[rootNode] = self.arr[L]
            return

        leftNode = rootNode * 2 + 1
        rightNode = rootNode * 2 + 2
        M = (L + R) // 2
        self.buildTree(leftNode, L, M)
        self.buildTree(rightNode, M + 1, R)
        self.tree[rootNode] = self.tree[leftNode] + self.tree[rightNode]

    def update(self, index: int, val: int) -> None:
        def update_helper(index: int, val: int, rootNode: int, L: int, R: int) -> None:
            if L == R: # L equals to R equals to index
                self.tree[rootNode] = val
                return

            leftNode = rootNode * 2 + 1
            rightNode = rootNode * 2 + 2
            M = (L + R) // 2
            if index <= M: # this index is in the leftTree
                update_helper(index, val, leftNode, L , M)
            else: # this index is in the rightTree
                update_helper(index, val, rightNode, M + 1 , R)
            self.tree[rootNode] = self.tree[leftNode] + self.tree[rightNode]
        update_helper(index, val, 0, 0, len(self.arr) - 1)

    def sumRange(self, left: int, right: int) -> int:
        def query(rootNode: int, L: int, R: int, start: int, end: int) -> int:
            print(f"rootNode is {rootNode}, L, r is {L, R}")
            if L == start and R == end: # [start, end] equals the range of the node[L, R]
                return self.tree[rootNode]

            leftNode = rootNode * 2 + 1
            rightNode = rootNode * 2 + 2
            M = (L + R) // 2
            if start > M: # [start, end] is in the rightTree
                return query(rightNode, M + 1, R, start, end)
            elif end <= M: # [start, end] is in the leftTree
                return query(leftNode, L, M, start, end)
            else: # [start, end] is in both the leftTree and rightTree
                return query(rightNode, M + 1, R, M + 1, end) + query(leftNode, L, M, start, M)
        
        return query(0, 0, len(self.arr) - 1, left, right)

# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
for i in range(len(obj.tree)):
    print(f"obj.tree[{i}] is {obj.tree[i]}")

print("===========")
obj.update(1,2)
for i in range(len(obj.tree)):
    print(f"obj.tree[{i}] is {obj.tree[i]}")
param_2 = obj.sumRange(0,2)
print(f"param_2 is {param_2}")