# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.

class NumArray:

    def __init__(self, nums: list[int]):
        self.PrefixSum = [0]
        total = 0

        for i in nums:
            total += i
            self.PrefixSum.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        #PrefixSum[目前index] 代表從頭加到目前index的總和，因此 left <-> right 間的和為 PrefixSum[right] - PrefixSum[left - 1]
        return self.PrefixSum[right + 1] -self.PrefixSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# C code

#include<stdlib.h>

# typedef struct {
#     int* PrefixSum;
# } NumArray;


# NumArray* numArrayCreate(int* nums, int numsSize) {
#     NumArray* obj = (NumArray *)malloc(sizeof(NumArray));
#     obj -> PrefixSum = (int *)malloc((numsSize + 1) * sizeof(int));
#     obj -> PrefixSum[0] = 0;

#     for (int i = 1 ; i <= numsSize; i++){
#         obj -> PrefixSum[i] = obj -> PrefixSum[i - 1] + nums[i - 1];
#     }

#     return obj;
    
# }

# int numArraySumRange(NumArray* obj, int left, int right) {
#     return obj -> PrefixSum[right + 1] - obj -> PrefixSum[left];
# }

# void numArrayFree(NumArray* obj) {
#     free(obj -> PrefixSum);
#     free(obj);
    
# }

# /**
#  * Your NumArray struct will be instantiated and called as such:
#  * NumArray* obj = numArrayCreate(nums, numsSize);
#  * int param_1 = numArraySumRange(obj, left, right);
 
#  * numArrayFree(obj);
# */