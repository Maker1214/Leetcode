nums = [12,5,9,7,8,10]
target = 11
nums.sort()
print(nums)

def binarySearch(nums,l,r,target):
    if l > r: return -1
    m = (l + r) // 2
    if nums[m] > target:
        idx = binarySearch(nums,l,m-1,target)
    elif nums[m] < target:
        idx = binarySearch(nums,m+1,r,target)
    else:
        idx = m
    return idx 


print(binarySearch(nums,0,len(nums) - 1,target))