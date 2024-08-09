# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# 當open數量小於n時(n為總共幾對括號)，可以加入open或者closed
# 當open數量大於等於closed數量時，才能加入closed
# 所有open跟closed都用完後把結果加入res中

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def createParenthesis(openN : int, closedN : int, currStr : str) -> None:
            # base case
            if openN == closedN == n:
                res.append(currStr)

            else:
                if openN < n:
                    createParenthesis(openN + 1, closedN, currStr + "(")
                if closedN < openN:
                    createParenthesis(openN, closedN + 1, currStr + ")")
                
        createParenthesis(0,0,"")
        return res

test = Solution()

for i in range(1,6):
    print(f"{i}對括號的結果為{test.generateParenthesis(i)}")
