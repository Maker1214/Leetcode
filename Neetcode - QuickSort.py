# Definition for a pair.
from typing import Optional, List
# Time : O(nlogn)，但當原本的陣列已經是排序好的陣列時，時間複雜度會變成O(n ** 2)
# Memory : O(logn) <- recursive深度，但當遇上worst case時，會變成O(n)
def quickSort(nums: Optional[int], s: int, e: int) -> List:
    #[1 ,2]
    #[s, e] => pivot = 2, 跑完後，left = 1
    #recursive時會變成quickSort(nums, 0, 0)與quickSort(nums, 2, 1)

    #[2, 1]
    #[s, e] => pivot = 1, 跑完後，left = 0
    #recursive時會變成quickSort(nums, 0, -1)與quickSort(nums, 1, 1)

    #由以上兩種例子可知，e最後都跟s相同或比s小1
    if e <= s:
        return nums
    pivot = nums[e]
    left = s

    for i in range(s, e):
        if nums[i] < pivot:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
    
    nums[e], nums[left] = nums[left], nums[e]
    quickSort(nums, s, left - 1)
    quickSort(nums, left + 1, e)

    return nums

nums = [6,2,4,1,3]

print(quickSort(nums, 0, len(nums) - 1))


def quick_Sort(nums: Optional[int]) -> List:
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [l for l in nums if l < pivot]
    middle = [m for m in nums if m == pivot]
    right = [r for r in nums if r > pivot]

    return quick_Sort(left) + middle + quick_Sort(right)

nums = [6,2,4,1,3]

print(quick_Sort(nums))   