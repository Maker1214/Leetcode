# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -10 ** 4 <= nums[i] <= 10 ** 4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10 ** 4 <= target <= 10 ** 4

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:  return m
            #左半邊已排序
            if nums[l] <= nums[m]:
                #target坐落在已排序的左半邊
                if nums[l] <= target < nums[m]:
                    #也可直接用原本的while loop繼續做binary search
                    #return self.binarySearch(l,m,target,nums)
                    r = m - 1
                #target坐落在右半邊
                else:
                    l = m + 1
            #右半邊已排序
            else:
                #target坐落在已排序的右半邊
                if nums[m] < target <= nums[r]:
                    #也可直接用原本的while loop繼續做binary search
                    #return self.binarySearch(m,r,target,nums)
                    l = m + 1
                else:
                    r = m - 1
        return -1
    
    # def binarySearch(self, l:int, r:int, t:int, nums:list) -> int:
    #     while l <= r:
    #         m = (l + r) // 2
    #         if nums[m] == t: return m
    #         #target坐落在已排序的右半邊
    #         elif nums[m] < t:
    #             l = m + 1
    #         else:
    #             r = m - 1
    #     return -1

test = Solution()
nums = [1]
target = 5
print(test.search(nums,target))





            