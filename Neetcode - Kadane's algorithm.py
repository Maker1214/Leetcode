nums = [4,-1,2,-7,3,4]

# bruteForce : O(n ** 2)
def bruteForce(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        currSum = 0

        for j in range(i, len(nums)):
            currSum += nums[j]
            maxSum = max(maxSum, currSum)
    
    return maxSum

print(bruteForce(nums))

# Kadane : O(n)
def Kadane(nums):
    maxSum = nums[0]
    currSum = 0

    for i in nums:
        currSum = max(0, currSum) + i
        maxSum = max(maxSum, currSum)
    
    return maxSum

print(Kadane(nums))

# return the index of maxSum
def slidingWindow(nums):
    maxSum = nums[0]
    currSum = 0
    L = 0

    for R in range(len(nums)):
        if currSum < 0:
            L = R
            currSum = 0
        currSum += nums[R]
        
        if currSum >= maxSum:
            maxSum = currSum
            maxL, maxR = L, R
            print([maxL, maxR])

    return [maxL, maxR]

print(slidingWindow(nums))
        

        