# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000

# O(1)
# 參考 https://www.youtube.com/watch?v=EyPEST8YsTg 
# 例如 :
#  a  b
# -3 -1 => -4
# -3  1 => -2
#  3  1 =>  4
#  3 -1 =>  2
# 答案的正負數由a是否大於0決定，若a < 0，答案一定是負數
# 若 a * b >= 0 ，代表 abs(答案) = abs(a) + abs(b)
# 反之 ，代表 abs(答案) = abs(a) - abs(b)
# 最終答案 = 正數或負數 * abs(答案)

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         x, y = abs(a), abs(b)

#         if x < y:
#             return self.getSum(b, a)
        
#         sign = 1 if a >= 0 else -1

#         if a * b >= 0:
#             while y:
#                 x ,y = x ^ y, (x & y) << 1
#         else:
#             while y:
#                 x, y = x ^ y, ((~x) & y) << 1
        
#         return x * sign


# class Solution:
#     def addTwo(self, a: int, b: int) -> int:
#         print(f"a, b is {a, b}")
#         while b:
#             a, b = a ^ b, (a & b) << 1
#         print(a)
#         return a
        
#     def getSum(self, a: int, b: int) -> int:
#         x, y = abs(a), abs(b)
#         if x < y:
#             return self.getSum(b, a)

#         sign = -1 if a < 0 else 1
#         print(f"sign is {sign}")
#         if a * b >= 0:
#             return sign * self.addTwo(a, b)
#         else:
#             print(~b + 1)
#             return sign * self.addTwo(a, ~b + 1)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        int_max = 0x7fffffff
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a < int_max else ~(a ^ mask)


test = Solution()
print(test.getSum(-5,3))