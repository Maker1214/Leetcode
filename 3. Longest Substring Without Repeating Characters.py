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

# # 使用hashmap來記錄簿重複的字元以及其index，若遇到重複的字元，則更新重複字元的index，並且在要移動 l 到重覆字元的index過程時，會一併清除hashmap中這一路遇到的字元。
# # 例如"pwwkew"，原本的hashmap會存放'p'以及'w'，但當出現第二個'w'時，l 除了需移動到第二個 'w'的位置上之外，也必須從hashmap中清除 'p' 
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res, l, r = 0, 0, 0
#         curr = {}

#         while r < len(s):
#             if s[r] in curr:
#                 res = max(res, r - l)
#                 #print(r, s[r], res, l)
#                 des = curr[s[r]]
#                 while l < des + 1:
#                     curr.pop(s[l])
#                     l += 1                               
#             curr[s[r]] = r
#             r += 1                        
#         return max(res, r - l)


# # 使用 queue 來記錄字元是否有重複。
# from collections import deque

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         q = deque()
#         l = r = res = 0
        
#         while r < len(s):
#             while q.count(s[r]):
#                 q.popleft()
#                 l += 1
#             q.append(s[r])
#             r += 1
#             res = max(res, r - l)
        
#         return res

# 使用set來記錄是否有重複字元
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        digit = set()
        l = res = 0
        
        for r in range(len(s)):
            while s[r] in digit:
                digit.remove(s[l])
                l += 1
            digit.add(s[r])
            res = max(res, r - l + 1)
        
        return res
               
test = Solution()
s = "abcabcbb"
print(test.lengthOfLongestSubstring(s))
