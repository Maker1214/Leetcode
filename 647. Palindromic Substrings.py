def helper(l,r,s):
    res = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
        res += 1
    return res

def palindromic(s):
    output = 0
    for cur in range(len(s)):       
        output += helper(cur, cur, s)
    
    for cur in range(len(s)):
        output += helper(cur, cur + 1, s)
    
    return output


test = ["aaa", "abc", "aba", "aabbaa", "aaaa"]

for i in test:
    print(f"string : {i}, output = {palindromic(i)}")
