# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107


# https://www.youtube.com/watch?v=ph0v80-rRtQ 
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        PrefixSumCnt = {0:1}
        res = 0
        PrefixSum = 0

        for i in nums:
            PrefixSum += i
            #       [1,2,1,3,4,2,3] , k = 8 
            # index  0 1 2 3 4 5 6, , 假設目前迴圈跑到 index 4
            # index 0 <-> 4 : 稱為S1，prefixSum = 11
            # index 0 <-> 1 : 稱為S2，prefixSum = 3
            # index 2 <-> 4 : 稱為required，也就是符合 k = 8 的subarray
            # 因此只要知道 hashMap 中到目前為止總共有幾個 prefixSum為 3 (目前為止的prefixSum - k)，就可以知道 index 4時，有幾組 subarray符合條件
            target = PrefixSum - k
            res += PrefixSumCnt.get(target, 0)
            # 如果先把 index 4的prefixSum存進 hashMap中，當碰到k = 0時，那麼target會等於index 4的prefixSum，進入 hashMap(target)會得到值。但不應該得到值，因為 k = 0，明顯此題沒有任何subarray的和為0
            PrefixSumCnt[PrefixSum] = PrefixSumCnt.get(PrefixSum, 0) + 1
            
        
        return res