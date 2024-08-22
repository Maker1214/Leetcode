# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: list[Pair]) -> list[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, pairs, l, r):
        if r - l <= 0: return pairs

        pivot = pairs[r].key
        left = l

        for i in range(l,r):
            if pairs[i].key < pivot:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left += 1
        
        pairs[r], pairs[left] = pairs[left], pairs[r]
        self.quickSortHelper(pairs, l, left - 1)
        self.quickSortHelper(pairs, left + 1, r)



pairs = [Pair(3, "cat"), Pair(2, "dog"), Pair(3, "bird")]
# After QuickSort, paris becomes (2, "dog"), (3, "bird"), (3, "cat"). It's unstable.
test = Solution()
test.quickSort(pairs)

for p in pairs:
    print(p.key, p.value)




        