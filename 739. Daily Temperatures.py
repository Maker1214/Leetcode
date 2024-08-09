# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

# T : O(n) // M : O(n)
# 解法1 : 用一個stack來記錄溫度跟idx，其實可以只記錄idx，詳見下一個解法
# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         res = [0] * len(temperatures)
#         stack = [] # [temp, idx]

#         for i, t in enumerate(temperatures):
#             while len(stack) and t > stack[-1][0]:
#                 res[stack[-1][1]] = i - stack[-1][1]
#                 stack.pop()
#             stack.append([t, i])
        
#         return res

# 解法2 : 用一個stack來記錄idx

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] # [idx]

        for i, t in enumerate(temperatures):
            while len(stack) and t > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res


test = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(test.dailyTemperatures(temperatures))
                
            
            

