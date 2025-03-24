# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container.
# If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = len(nums) - 2, len(nums) - 1

        while l >= 0 and nums[l] >= nums[r]:
            l -= 1
            r -= 1
        # 當遇到從頭一路遞減到尾，如[5,4,3,2,1]時，此時答案應把[5,4,3,2,1]反轉，為[1,2,3,4,5]，但不能直接用nums[::-1]來反轉，因為這樣不會改變原始nums，與題意不符。因此遇到此狀況時(l會等於-1)，直接丟進swap function處理
        # 除了上述狀況外，其餘case的l值皆會大於等於0
        if l >= 0: 
            r = len(nums) - 1
            while nums[l] >= nums[r]:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        self.swap(nums,l + 1)

    # nums[::-1]不會改變原始的nums，會產生一個新的反轉list
    # nums.reverse()會改變原始的nums
    # python 會根據傳入的參數是immutable 或是 mutable 來決定會不會修改原始值，例如此處傳入的nums為list，是mutable，因此採用傳址的方式，會改變原始nums的值，因此符合題意
    def swap(self,nums,l) -> None:
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        


test = Solution()
nums = [1,5,1]
test.nextPermutation(nums)
print(nums,id(nums))
    


            
