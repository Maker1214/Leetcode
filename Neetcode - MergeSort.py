# Definition for a pair.
# Time : O(nlogn)
# Memory : O(n) <- 需要額外的陣列來儲存每次merge後的結果 + O(logn) <- recursive 深度
from typing import Optional, List
def mergeSort(nums: Optional[int], reverse: bool) -> List:

    def mergeSL(left: List, right: List) -> List:
        res = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        res.extend(left[l:])
        res.extend(right[r:])

        return res
    
    def mergeLS(left: List, right: List) -> List:
        res = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        res.extend(left[l:])
        res.extend(right[r:])

        return res



    if len(nums) <= 1: #空陣列或者陣列長度為1
        return nums
    
    m = len(nums) // 2

    left = mergeSort(nums[:m], reverse)
    right = mergeSort(nums[m:], reverse)

    return mergeSL(left, right) if reverse else mergeLS(left, right)

nums = [3,2,4,1,6]
print(mergeSort(nums, False))

    

    

