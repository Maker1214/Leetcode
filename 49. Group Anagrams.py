# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

strs = ["ddddddddddg","dgggggggggg"]
record = {}
res = []

for s in strs:
    seed = [0] * 26
    for c in s:
        seed[ord(c) - ord('a')] += 1

    record[tuple(seed)] = record.get(tuple(seed), []) + [s]

for i in record:
    res.append(record[i])

print(res)






    



