# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

##############################################################

############
# method 1 #
############

# Time : O(n)
# Memory : O(n)
# use a set to record if there is a repeated digit or not
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         digit = set()
#         l = res = 0
        
#         for r in range(len(s)):
#             while s[r] in digit:
#                 digit.remove(s[l])
#                 l += 1
#             digit.add(s[r])
#             res = max(res, r - l + 1)
        
#         return res

############
# method 2 #
############
# Time : O(n)
# Memory : O(n)
# use a dict to record the index of the digit. it will be faster than the method 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        digit = {}
        l = res = 0

        for r in range(len(s)):
            # if the digit exists in dict and if the index of the existed digit is bigger than l
            if s[r] in digit and digit[s[r]] >= l:
                # use l to record the first non-repeated digit in current substring
                l = digit[s[r]] + 1
            digit[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
               
test = Solution()
s = "abcabcbb"
print(test.lengthOfLongestSubstring(s))
