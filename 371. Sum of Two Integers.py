# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000

class Solution:
    def getSum(self, a: int, b: int) -> int:
        res, carry, cnt, temp = 0, 0, 0, 0
        while a or b:
            #print(f"a , b, carry, res = {a, b, carry, res}")
            if carry == 1:
                temp = carry ^ ((a & 1) ^ (b & 1))                      
                if a & 1 == 0 and b & 1 == 0: # it means the last bit of a and b are both 0
                    carry = 0      

            else:
                temp = (a & 1) ^ (b & 1)
                if a & 1 == 1 and b & 1 == 1: # it means the last bit of a and b are both 1
                    carry = 1
            res |= temp << cnt
            cnt += 1
            a >>= 1
            b >>= 1
        
        if carry:
            res |= carry << cnt
        return res

test = Solution()
print(test.getSum(0,0))