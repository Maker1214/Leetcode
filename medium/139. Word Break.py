
"""
#DP top-down
test = "leetcode"
dict = ["l", "ee", "t", "coda"]
wordDict = set(dict)
memo = {len(test) : True}


def wordBreak(start):
    if start in memo: return memo[start]

    for i in range(start, len(test)):
        if test[start:i+1] in wordDict and wordBreak(i+1):
            memo[start] = True
            return True
    memo[start] = False
    return False

wordBreak(0)
print(memo[0])
"""

test = "leetcode"
dict = ["l", "ee", "t"]
wordDict = set(dict)
dp = [False] * (len(test) + 1)
dp[-1] = True

for i in range(len(test)-1, -1, -1):
    for j in range(i, len(test)):
        dp[i] |= test[i:j+1] in wordDict and dp[j+1]
    #print(dp[i])

print(f"result : {dp[0]}")





