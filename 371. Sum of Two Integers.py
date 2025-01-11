# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000
# O(32)
# 參考 https://www.youtube.com/watch?v=mXB9jbJzXwU
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFF # becase -1000 <= a, b <= 1000, we could use 11 bits to represent a and b(Assume a = 1000 and b = 1000, a + b = 2000 < 2 ** 11)
        maxInt = 1 << 15 # 1 << 15 means 16th bit. If the value is bigger than maxInt, it means this value should be considered as a negative number

        while b:
            a , b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(f"(a, b) id {a, b}")
        
        # Why Flip the Bits and Take Two's Complement?
        # In Python, numbers are treated as UNSIGNED by default, meaning Python will interpret all binary representations as POSITUVE integers. 
        # To simulate signed 16-bit integers (e.g., negative numbers), we need to handle cases where the result of our operation exceeds the maximum positive value of a 16-bit integer (1 & (1 << 15) == 1).

        # Here’s the process:

        # 1. If the result of the computation exceeds the 16-bit signed integer max (1 & (1 << 15) == 1), we know it’s a negative number in the context of 16-bit integers.

        # 2. To convert this value into its correct signed representation, we invert its bits using a bitwise XOR with the mask 0xFFFF:
        # # this example assumes an int is 4 bits instead of 32 for easier reading
        # mask = 1111
        # a =    1100 # python treats this as 12 in unsigned format
        # flipped_bits = a ^ mask = 0011

        # 3. Next, we re-flip back the bits using python's two complement operator to force python to treat the number as a signed, negative value
        # # ~ is the 2s complement operator in python. ~x = -x-1 
        # flipped_bits = a ^ mask = 0011
        # ~flipped_bits = ~(a ^ mask) = 1100 # python now treats this as -4

        # 4. Therefore, if our final sum is less than 1 << 15, we return back the answer, else we return back ~(a ^ mask)

        # 10進位若是負值或者小於maxInt，則用原本的10進位表示
        # 10進位若是大於等於maxInt，Python認為是正值，但我們希望認定為負值，利用~(a ^ mask)來告訴Python用負10進位來表示
        return a if a < maxInt else ~(a ^ mask)
        
test = Solution()
print(test.getSum(-100,0))




