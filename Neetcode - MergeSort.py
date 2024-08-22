# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: list[Pair]) -> list[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs: list[Pair], l: int, r: int) -> list[Pair]:
        # 這種寫法如果pairs是[]，那麼l > r，不會進入base case，所以要改成r - l <= 0
        # if l == r: return pairs
        if r - l <= 0: return pairs
        
        m = (l + r) // 2
        self.mergeSortHelper(pairs, l, m)
        self.mergeSortHelper(pairs, m+1, r)

        self.merge(pairs,l,m,r)

        return pairs

    # def merge(self, pairs: list[Pair], start: int, m: int, end: int) -> None:
    #     L = pairs[start:m+1]
    #     R = pairs[m+1:end+1]
    #     l, c, r = 0, start, 0
        
    #     while l < len(L) and r < len(R):
    #         if L[l].key <= R[r].key:
    #             pairs[c] = L[l]
    #             l += 1
    #         else:
    #             pairs[c] = R[r]
    #             r += 1
    #         c += 1
        
    #     while l < len(L):
    #         pairs[c] = L[l]
    #         l += 1
    #         c += 1
        
    #     while r < len(R):
    #         pairs[c] = R[r]
    #         r += 1
    #         c += 1

    # 這種寫法雖然把L 跟 R 用一個unsroted來代替，但後續的邊界處理不直覺，使用上面的方式比較容易處理
    def merge(self, pairs: list[Pair], start: int, m: int, end: int) -> None:
        unsorted = pairs[start:end+1]
        l, r, c = 0, m - start + 1, start

        while l <= m - start and r <= end - start:
            if unsorted[l].key <= unsorted[r].key:
                pairs[c] = unsorted[l]
                l += 1
            else:
                pairs[c] = unsorted[r]
                r += 1
            c += 1
        
        while l <= m - start:
            pairs[c] = unsorted[l]
            l += 1
            c += 1
        
        while r <= end - start:
            pairs[c] = unsorted[r]
            r += 1
            c += 1
        

test = Solution()
pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry"), Pair(1, "date"), Pair(9, "elderbarry")]
test.mergeSort(pairs)

for p in pairs:
    print(p.key, p.value)

