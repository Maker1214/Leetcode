# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# open == closed == n
# 當open數量大於等於closed數量時，才能加入closed
# 所有open跟closed都用完後結束

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pass
