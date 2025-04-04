class SegmentTree():
    def __init__(self, nums: list, n: int):
        self.arr = nums
        self.tree = [0] * 3 * n # n is the len(nums)
        
    def buildTree(self, rootNode: int, L: int, R: int):
        if L == R:
            self.tree[rootNode] = self.arr[L]
        else:
            leftNode = rootNode * 2 + 1
            rightNode = rootNode * 2 + 2
            M = (L + R) // 2
            self.buildTree(leftNode, L, M)
            self.buildTree(rightNode, M + 1, R)
            self.tree[rootNode] = self.tree[leftNode] + self.tree[rightNode]
    
    def update(self, rootNode: int, L: int, R: int, idx: int, val: int):
        if L == R:
            self.tree[rootNode] = val
            return
        leftNode = rootNode * 2 + 1
        rightNode = rootNode * 2 + 2
        M = (L + R) // 2
        if idx <= M: # this node belongs to left tree
            self.update(leftNode, L, M, idx, val)
        else: # this node belongs to right tree
            self.update(rightNode, M + 1, R, idx, val)
        self.tree[rootNode] = self.tree[leftNode] + self.tree[rightNode]
    
    def query(self, rootNode: int, L: int, R: int, start: int, end: int) -> int:
        print(f"rootNode is {rootNode}, [L, R] is {L, R}")
        if start == L and end == R:
            return self.tree[rootNode]

        leftNode = rootNode * 2 + 1
        rightNode = rootNode * 2 + 2
        M = (L + R) // 2
        if end <= M: # the entire query range locates in left tree
            return self.query(leftNode, L, M, start, end)
        elif start > M: # the entire query range locates in right tree
            return self.query(rightNode, M + 1, R, start, end)
        else:
            # query [2 ,5] 只送符合左樹range[0(L) ,2(M)]的範圍到左樹，也就是[2(start), 2(M)]
            # query [2 ,5] 只送符合右樹range[3(M+1) ,5(R)]的範圍到右樹，也就是[3(M+1), 5(end)]
            return self.query(leftNode, L, M, start, M) + self.query(rightNode, M + 1, R, M + 1, end)

nums = [1,3,5,7,9,11]
obj = SegmentTree(nums, len(nums))
obj.buildTree(0, 0, len(nums) - 1)

for v in range(len(obj.tree)):
    print(f"tree node {v} is {obj.tree[v]}")

print("=======")

obj.update(0, 0, len(nums) - 1, 4, 6)
for v in range(len(obj.tree)):
    print(f"tree node {v} is {obj.tree[v]}")

val = obj.query(0, 0, len(nums) - 1, 1 ,5)
print(val)


# class SegmentTree:
#     def __init__(self, n:int):
#         self.tree = [0] * 4 * n
    
#     def build(self, rootNode:int, start:int, end:int, arr):
#         if start == end:
#             self.tree[rootNode] = arr[start]
#         else:
#             m = (start + end) // 2
#             leftNode = rootNode * 2 + 1
#             rightNode = rootNode * 2 + 2
#             self.build(leftNode, start, m, arr)
#             self.build(rightNode, m+1, end, arr)
#             self.tree[rootNode] = self.tree[leftNode] + self.tree[rightNode]
    
#     def update(self, rootNode:int, start:int, end:int, arr, idx:int, val:int):
#         if start == end:
#             self.tree[rootNode] = val
        
#         else:
#             m = (start + end) // 2
#             leftNode = rootNode * 2 + 1
#             rightNode = rootNode * 2 + 2
#             if idx <= m: # idx is in the left tree
#                 self.update(leftNode, start, m, arr, idx, val)
#             else: # idx is in the right tree
#                 self.update(rightNode, m+1, end, arr, idx, val)
#             self.tree[rootNode] = self.tree[leftNode] + self.tree[rightNode]
    
#     def query(self, rootNode: int, start:int, end:int, s:int, e:int) -> int:
#         if start == s and end == e:
#             return self.tree[rootNode]
        

#         m = (start + end) // 2
#         leftNode = rootNode * 2 + 1
#         rightNode = rootNode * 2 + 2

#         if e <= m: # the range is all in the left tree
#             return self.query(leftNode, start, m, s, e)
#         elif s > m: # the range is all in the right tree
#             return self.query(rightNode, m + 1, end, s, e)
#         else: # the range cover left and right tree
#             return self.query(leftNode, start, m, s, m) + self.query(rightNode, m + 1, end, m+1, e)
                    


# nums = [1,3,5,7,9,11]
# obj = SegmentTree(len(nums))
# obj.build(0, 0, len(nums) - 1, nums)

# for v in range(len(obj.tree)):
#     print(f"tree node {v} is {obj.tree[v]}")

# print("=======")

# obj.update(0, 0, len(nums) - 1, nums, 4, 6)
# for v in range(len(obj.tree)):
#     print(f"tree node {v} is {obj.tree[v]}")

# val = obj.query(0, 0, len(nums) - 1, 1 ,5)
# print(val)
        
