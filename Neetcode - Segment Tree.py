class SegmentTree:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total
        self.leftTree = None
        self.rightTree = None
        self.leftIdx = L
        self.rightIdx = R
    
    def build(self, nums: list, L: int, R: int):
        if L == R:
            print(f"leaf node {L, R} is {nums[L]}")
            return SegmentTree(nums[L], L, R)
        
        M = (R - L) // 2
        root = SegmentTree(0, L, R)
        root.leftTree = root.build(nums, L, M)
        root.rightTree = root.build(nums, M + 1, R)

        root.sum = root.leftTree.sum + root.rightTree.sum
        print(f"root node {L, R}, sum is {root.sum}")
        #return root


nums = [9,7,2]
obj = SegmentTree(0, 0, len(nums) - 1)     
obj.build(nums, 0, len(nums) - 1)

