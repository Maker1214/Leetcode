# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1] * len(edges)
        rank = [0] * len(edges)

        def findRoot(x: int) -> int:
            if parent[x] == -1:
                return x
            parent[x] = findRoot(parent[x])
            return parent[x]

        def unionVertices(x: int, y: int) -> bool:
            # x and y have the same root
            if findRoot(x) == findRoot(y):
                return False
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[y] < rank[x]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x] += 1
            return True

        for x, y in edges:
            if unionVertices(x - 1, y - 1) == False:
                return [x, y]
        
        for x, y in edges:
            print(f"for {[x, y]}, root is {[findRoot(x - 1), findRoot(y - 1)]}")
