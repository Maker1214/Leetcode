# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# 方法1 : T : O(n) M : T(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool: 
#         digit = []
#         for i in s.lower():
#             # it's a valid letter
#             if i.isalpha(): digit.append(i)
#             # it's a valid number
#             elif i.isdigit() : digit.append(i)
                    
#         l, r = 0, len(digit) - 1
#         while l < r:
#             if digit[l] != digit[r]: return False
#             l += 1
#             r -= 1
#         return True

# 方法2 : T : O(n) M : T(1)     
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNum(s[l].lower()):
                l += 1
            while l < r and not self.isAlphaNum(s[r].lower()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isAlphaNum(self,c) -> bool: 
            return ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")

test = Solution()
s = ["race a car", "A man, a plan, a canal: Panama", " ", "aa bb", " a b", "a_a, b", "a_b, a,", "a   b___b,,a"]
for i in s:
    print(test.isPalindrome(i))
        

