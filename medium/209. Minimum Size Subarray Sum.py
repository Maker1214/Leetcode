# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        currSum, L = 0, 0
        minLen = float("inf")
        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                minLen = min(minLen, R - L + 1)
                currSum -= nums[L]
                L += 1
        
        return 0 if minLen == float("inf") else minLen

test = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(test.minSubArrayLen(target, nums))

# C code:
#include <limits.h>
#define MIN(i, j) ((i < j) ? i : j)

# int minSubArrayLen(int target, int* nums, int numsSize) {
#     int minLen = INT_MAX;
#     int curSum = 0;
#     int l = 0;

#     for (int r = 0; r < numsSize; r++){
#         curSum += nums[r];
#         while (curSum >= target){
#             minLen = MIN(minLen, r - l + 1);
#             curSum -= nums[l];
#             l++;
#         }
#     }
#     return (minLen == INT_MAX) ? 0 : minLen;
# }
