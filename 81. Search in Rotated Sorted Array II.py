# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# 
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104
 

# Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
# ==> 會的，當array中的相同數值越多時，時間複雜度越接近為O(n)，worst case為全部的數值都相同，則時間複雜度為 O(n)

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target : return True
            # 例如 [1,0,1,1,1]
            # 首先 [l   m   r]，此時不曉得 m 的哪一邊已經是sorted，先移動l or r，如果array中並非每個數字都相同，如此例題，則一直移動 l 或一直移動 r總會進入下一個判斷式
            if nums[m] == nums[l]:
                l += 1
            # m 的左半邊已經排序
            elif nums[l] < nums[m]:
                #target位於已排序的左半邊
                if nums[l] <= target < nums[m]:
                    r = m - 1
                #target位於未排序的右半邊
                else:
                    l = m + 1
            # m 的右半邊已排序
            else:
                #target位於已排序的右半邊
                if nums[m] < target <= nums[r]:
                    l = m + 1
                #target位於未排序的左半邊
                else:
                    r = m - 1
        return False






test = Solution()
nums = [1,0,1,1,1]
target = 0

print(test.search(nums,target))



