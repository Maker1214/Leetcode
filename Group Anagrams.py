# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


# strs = ["act","pots","tops","cat","stop","hat"]
strs = [""]
record = {}
v = 0
res = [[],[],[]]
for s in strs:
    appearence = [0] * 26
    for c in s:
        appearence[ord(c) - ord('a')] += 1
    
    if tuple(appearence) not in record:
        record[tuple(appearence)] = v
        v += 1        
    res[record[tuple(appearence)]].append(s)

print(res)


    



