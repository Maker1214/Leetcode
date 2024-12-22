# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10 ** 4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# Time Limited Exceeded
# Time : O(len(words) * ROWS * COLS * 4 ** wordlen)
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         ROWS, COLS = len(board), len(board[0])
#         res = []
        
        
#         def dfs(col, row, word, idx, wordLen, v):
#             if idx == wordLen:
#                 return True
#             if col < 0 or row < 0 or col == COLS or row == ROWS or board[row][col] != word[idx] or (col, row) in v:
#                 return False
#             v.add((col, row))
#             if (dfs(col + 1, row, word, idx + 1, wordLen, v) or dfs(col - 1, row, word, idx + 1, wordLen, v) 
#                 or dfs(col, row + 1, word, idx + 1, wordLen, v) or dfs(col, row - 1, word, idx + 1, wordLen, v)):
#                 return True
#             v.remove((col, row))
#             return False

#         for word in words:
#             visited = set()
#             wordLen = len(word)
#             skip = False
#             for col in range(COLS):
#                 if skip:
#                     break
#                 for row in range(ROWS):                    
#                     if dfs(col, row, word, 0, wordLen, visited):
#                         res.append(word)
#                         skip = True
#                         break
        
#         return res

class TrieNode:
    def __init__(self):
        self.links = {}
        self.isEnd = False
    
    def TrieAdd(self, word):
        curr = self

        for c in word:
            if c not in curr.links:
                curr.links[c] = TrieNode()
            curr = curr.links[c]
        
        curr.isEnd = True

# Time : O(m * n * 4 ** l), Memory : O(l), l is the longest length of word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.TrieAdd(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visited, dup = set(), set(), set()

        def dfs(c, r, curr, word):
            if c < 0 or r < 0 or c == COLS or r == ROWS or board[r][c] not in curr.links or (r, c) in visited:
                return
            visited.add((r,c))
            curr = curr.links[board[r][c]]
            word += board[r][c]
            if curr.isEnd:
                res.add(word)
            dfs(c + 1, r, curr, word)
            dfs(c - 1, r, curr, word)
            dfs(c, r + 1, curr, word)
            dfs(c, r - 1, curr, word)
            visited.remove((r,c))

        for c in range(COLS):
            for r in range(ROWS):
                if board[r][c]  not in dup:
                    dfs(c, r, root, "")
                            
        return list(res)

