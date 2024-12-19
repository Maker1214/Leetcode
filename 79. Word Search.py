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

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        charCnt = [0] * 26
        hashMap = {}
        length, width = len(board), len(board[0])


        for i in range(length):
            for j in range(width):
                
                hashMap[board[i][j]] = hashMap.get(board[i][j], charCnt)
                hashMap[board[i][j]][ord(board[i][j]) - ord('A')] += 1
                # except for the 1st row
                if i < length - 1:
                    # down char
                    hashMap[board[i][j]][ord(board[i + 1][j]) - ord('A')] += 1
                    if j < width - 1:                        
                        # right char
                        hashMap[board[i][j]][ord(board[i][j + 1]) - ord('A')] += 1
                    elif j > 0:
                        # left char
                        hashMap[board[i][j]][ord(board[i][j - 1]) - ord('A')] += 1
                # except for the last row
                elif i > 0:
                    # up char
                    hashMap[board[i][j]][ord(board[i - 1][j]) - ord('A')] += 1
        

        for c in range(len(word)):
            if word[c] not in hashMap:
                return False
            if c == 0 and word[c + 1] not in hashMap[word[c]]:
                return False




        


                    
                        
                    
                    


