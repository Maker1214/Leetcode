# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:          
          if r >= ROWS or c >= COLS or min(r,c) < 0 or grid[r][c] == '0':
              return
          grid[r][c] = '0'
          # 判斷4個方向是否能走，把所有相連並且能走的路都走過
          dfs(r + 1, c)
          dfs(r - 1, c)
          dfs(r, c + 1)
          dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
              if grid[r][c] == '1':
                islands += 1            
                dfs(r,c)                           
        return islands
