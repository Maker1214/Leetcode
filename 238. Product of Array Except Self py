# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# 方法1 : 時間複雜度為O(n)，空間複雜度為O(n)
#nums = [-1,1,0,-3,3]
nums = [1,2,3,4]

# prefix = [0] * len(nums)
# postfix = [0] * len(nums)
# res = [0] * len(nums)
# prefix[0], postfix[-1] = 1, 1

# for i in range(1, len(nums)):
#     prefix[i] = prefix[i-1] * nums[i-1]

# for n in range(len(nums)-2,-1,-1):
#     postfix[n] = postfix[n+1] * nums[n+1]

# for k in range(len(nums)):
#     res[k] = prefix[k] * postfix[k]

# print(res)

# 方法2 : 用一個變數來取代 prefix list 以及 postfix list，直接把結果存在output中，時間複雜度 O(n) ，空間複雜度 O(1)
def productArray():
    res = [0] * len(nums)

    for i in range(len(nums)):
        res[i] = 1 if i == 0 else res[i-1] * nums[i-1]

    postfix = 1
    for n in range(len(nums)-2,-1,-1):
        postfix *= nums[n+1]
        res[n] *= postfix
    
    return res

if __name__ == "__main__":
    output = productArray()
    print(f"output is {output}")

    