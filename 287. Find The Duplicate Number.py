# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

# Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

# Example 1:

# Input: nums = [1,2,3,2,2]

# Output: 2
# Example 2:

# Input: nums = [1,2,3,4,4]

# Output: 4
# Follow-up: Can you solve the problem without modifying the array nums and using 𝑂(1) extra space?

# Constraints:
# 1 <= n <= 10000
# nums.length == n + 1
# 1 <= nums[i] <= n

# https://www.youtube.com/watch?v=wjYnzkAhcNk 說明如何證明Floyd's algorithm
# idx         :  0 1 2 3 4
# nums        : [1,2,3,4,4]
# linked list :  inedx 0 -> 值為1，找index 1 -> 值為2，找index 2 -> 值為3，找index 3 -> 值為4，找index 4 -> 值為4，找index 4 (把 nums 的值當成下一個 linked list 的 node)

nums = [1,2,3,2,2]

#方法1 : 時間複雜度為O(n)，空間複雜度為O(n)
def findDuplicateNum():
    c = set()
    for i in nums:
        if i in c: return i
        c.add(i)


#方法2 : 時間複雜度為O(n)，空間複雜度為O(1)
# def findDuplicateNum():
#     slow, fast = 0, 0
#     while True:
#         # 這次 slow 的值會變成下次 slow 的 index
#         slow = nums[slow]
#         # 這次 fast 的值會變成下次 fast 的 index
#         fast = nums[nums[fast]]
#         # slow 跟 fast 第一次碰面
#         if slow == fast: 
#             break
    
#     slow2 = 0

#     while True:
#         # slow 為 fast/slow 第一次碰面的點
#         slow = nums[slow]
#         # slow2 為 起始點
#         slow2 = nums[slow2]
#         # 根據Floyd's algorithm, slow跟slow2碰面的點即為開始循環的點
#         if slow == slow2:
#             return slow

if __name__ == "__main__":
    res = findDuplicateNum()
    print(f"res is {res}")
