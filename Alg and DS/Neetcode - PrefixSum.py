class PrefixSum:
    def __init__(self,arr):
        self.currSum = []
        prefix = 0
        for i in arr:
            prefix += i
            self.currSum.append(prefix)

    def rangeSum(self, l, r):
        return self.currSum[r] if l == 0 else self.currSum[r] - self.currSum[l - 1]



