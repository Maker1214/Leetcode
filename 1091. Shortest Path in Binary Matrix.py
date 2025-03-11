# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1
        directions = [[0,1], [0,-1], [-1,0], [1,0], [-1,-1], [-1,1], [1,-1], [1,1]]
        queue = deque()
        length = 0
        queue.append([0,0])
        grid[0][0] = 1 # 標記訪問過，避免重複行走
        while len(queue):
            # 檢查這一層的所有valid節點
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return length + 1 # 已經到終點，length需多1
                # 對每一個節點檢查8個方向
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if min(newR,newC) < 0 or max(newR, newC) >= n or grid[newR][newC] == 1:
                        continue
                    queue.append([newR,newC])
                    grid[newR][newC] = 1
            length += 1 #每過一層就加1
        return -1
            


