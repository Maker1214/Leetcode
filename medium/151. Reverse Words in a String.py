# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
# 迴圈
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         l = len(s) - 1
#         res = ""
#         while l >= 0:
#             while l >= 0 and s[l] == " ":
#                 l -= 1
#             if l < 0: break
#             r = l
#             while l >= 0 and s[l] != " ":
#                 l -= 1
#             res += s[l+1:r+1] + " "
        
#         return res[:-1:]

# 尚待完成
# class Solution:
#     def reverseWords(self, s: str) -> str:

#         r = len(s) - 1
#         while r >= 0 and s[r] == " ":
#             r -= 1
#         l = r
#         while l >= 0 and s[l] != " ":
#             l -= 1
#         # 只有l == -1 ==> 不是空白的頭 ==> 本身
#         # 若r == l == -1 ==> 空白的頭 ==> 回"" 
#         # 其他 ==> 不是頭 ==> 本身 + " " + 遞迴
#         if r == -1: 
#             return ""
#         elif l == -1:
#             return s[l+1:r+1]
#         else:
#             return s[l+1:r+1] + " " + self.reverseWords(s[:l])

# 遞迴
class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()
        l = len(s) - 1
        while l >= 0 and s[l] != " ":
            l -= 1
        # l == -1 ==> 不是空白的頭 ==> 本身
        # 其他 ==> 不是頭 ==> 本身 + " " + 遞迴
        if l == -1:
            return s[l+1:]
        else:
            return s[l+1:] + " " + self.reverseWords(s[:l])

test = Solution()
s = "the sky is blue"
print(test.reverseWords(s), len(test.reverseWords(s)))


                

