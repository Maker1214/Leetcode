#top-down(memo)
"""
method = {1:1,
          2:2}

def climb(n,method):
    if n in method: return method[n]
    method[n] = climb(n-1,method) + climb(n-2,method)
    print(f"第{n}層:{method[n]}")

    return method[n]


stairs = 9
print(climb(stairs,method))
"""

#tabulation

def climb(n,dp):
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"第{i}層:{dp[i]}")
    return dp[n]



stairs = 9
dp = [0] * (stairs + 1)
dp[1], dp[2] = 1, 2

print(climb(stairs,dp))

