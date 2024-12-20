# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?
# time : O(ROWS * COLS * 4 ** wordLen)
# memory : O(worldLen)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS, wordLen = len(board), len(board[0]), len(word)
        pathSet = set()

        def dfs(col, row, idx):
            if idx == wordLen:
                return True
            if col < 0 or col == COLS or row < 0 or row == ROWS or (row, col) in pathSet or board[row][col] != word[idx]:
                return False
            pathSet.add((row, col))
            if dfs(col + 1, row, idx + 1) or dfs(col - 1, row, idx + 1) or dfs(col, row + 1, idx + 1) or dfs(col, row - 1, idx + 1):
                return True
            pathSet.remove((row, col))
            return False


        for col in range(COLS):
            for row in range(ROWS):
                if dfs(col, row, 0):
                    return True
        
        return False
        
        




        


                    
                        
                    
                    


