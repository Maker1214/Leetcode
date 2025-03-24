# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

##############################################################

# Time : O(m * n) ==> need to traverse entire grid
# Memory : O(m * n) ==> len of queue
# use BFS

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh, minutes = 0, 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2: queue.append([row, col]) # add current rotten oranges into the queue
                elif grid[row][col] == 1: fresh += 1 # calculate the number of all fresh ornages

        # 4 directions
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c+ dc
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLS or grid[newR][newC] != 1:
                        continue
                    fresh -= 1
                    grid[newR][newC] = 2
                    queue.append([newR, newC]) # add the new rotten oranges for the next run
            minutes += 1

        return -1 if fresh else minutes # if fresh != 0 means that there is still fresh orange

