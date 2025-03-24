# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

nums = [3,2,3,1,2,4,5,5,6]
k = 5

# 這個作法會 Time Limit Exceeded
# new = nums[:k]
# for i in range(k,len(nums)):
#     if nums[i] > min(new): 
#         new.append(nums[i])
#         new.remove(min(new))

# print(min(new))

# 這個作法會 Time Limit Exceeded
# frequency = {}
# for i in nums:
#     if i not in frequency:
#         frequency[i] = nums.count(i)

# # sorted可對可迭代的物件做排序，回傳一個排序好的列表，sort()則是列表的其中一個方法，會in-place排序，因此會改變原列表
# sorted_freq = sorted(frequency.keys(),reverse = True)
# for i in sorted_freq:
#     k -= frequency[i]
#     if k <= 0: 
#         print(f"{i} is the answer")
#         break

# quicksort
# k = len(nums) - k
# def quickSelect(l,r):
#     pivot, p = nums[r], l
#     for i in range(l,r):
#         if nums[i] <= pivot:
#             nums[i], nums[p] = nums[p], nums[i]
#             p += 1
#     nums[p], nums[r] = nums[r], nums[p]

#     if p < k: return quickSelect(p+1, r)
#     elif p > k: return quickSelect(l,p-1)
#     else: return nums[p]

# print(quickSelect(0,len(nums)-1))

# heap : 先heapify整個array. Time Complexity : O(n)
import heapq

# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         heapq.heapify(nums)

#         while len(nums) > k:
#             heapq.heappop(nums)
        
#         return heapq.heappop(nums)

# heap : 直接maintain一個比較小的heap array. Time Complexity : O(nlogk)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minHeap = []
        for i in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, i)
            elif i > minHeap[0]:
                heapq.heappushpop(minHeap, i)        
        return heapq.heappop(minHeap)


test = Solution()
print(test.findKthLargest(nums, k))