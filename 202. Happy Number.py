# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# Example 2:

# Input: n = 2
# Output: false
 

# Constraints:

# 1 <= n <= 231 - 1

# #方法1 : 時間複雜度 O(n)， 空間複雜度 O(n)
# def helper(n) -> int:
#     s = 0
#     while n:
#         s += (n % 10) ** 2
#         n //= 10
#     #print(s)
#     return s
    
# def isHappyNumber(n) -> int:
#     count = set()
#     while n:
#         n = helper(n)
#         if n == 1: return True
#         if n in count:
#             return False
#         count.add(n)

# 方法2 : 時間複雜度 O(n)， 空間複雜度 O(1)，不happy number代表計算過程中某個數字會重複出現，因此造成計算過程為無窮迴圈，因此運用Floyd's algorithm來判斷是否有重複數字
def helper(n:int) -> int:
    s = 0
    while n:
        s += (n % 10) ** 2
        n //= 10
    return s

def isHappyNumber(n:int) -> bool :
    slow = fast = n
    while True:
        slow = helper(slow)
        fast = helper(helper(fast))        
        if slow == 1 or fast == 1: return True
        elif slow == fast: return False

    

if __name__ == "__main__":
    for i in range(101):
        res = isHappyNumber(i)
        if res: print(f"{i} is happy number : {res}")

