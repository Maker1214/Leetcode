# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.

# Example 1:

# Input:
# n=3
# edges=[[0,1], [0,2]]

# Output:
# 1
# Example 2:

# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]

# Output:
# 2
# Constraints:

# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2
from typing import List

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [-1] * n
        self.rank = [0] * n
    
    def findRoot(self, x: int) -> int:
        curr = self.parent

        if curr[x] == -1:
            return x
        curr[x] = self.findRoot(curr[x])
        return curr[x]
    
    def unionVertices(self, x: int, y: int) -> int:
        xRoot, yRoot = self.findRoot(x), self.findRoot(y)

        if xRoot == yRoot: # x and y have the same parent
            return 0

        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1
        
        return 1


# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         uf = UnionFind(n)

#         for x, y in edges:
#             uf.unionVertices(x, y)
        
#         return uf.parent.count(-1)     

# a smart coding
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n

        for x, y in edges:
            res -= uf.unionVertices(x, y)
        
        return res