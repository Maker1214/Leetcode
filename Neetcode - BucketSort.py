# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

# Assume that the value of Pair.key is less than 100
class Solution:
    def bucketSort(self, pairs: list[Pair]) -> None:
        bucket = [[] for i in range(100)]

        for pair in pairs:
            bucket[pair.key].append(pair)
        
        i = 0
        for k in range(len(bucket)):
            while bucket[k]:
                pairs[i] = bucket[k].pop()
                i += 1


pairs = [Pair(5, "Apple"), Pair(1, "Orange"), Pair(3, "Guava"), Pair(9, "cherry"), Pair(1, "date"), Pair(9, "elderbarry")]

test = Solution()
test.bucketSort(pairs)

for pair in pairs:
    print(pair.key, pair.value)








