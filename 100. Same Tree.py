# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -10 ** 4 <= Node.val <= 10 ** 4


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 寫法1
# from collections import deque
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         stackP, stackQ = [], []
#         def bfs(root, stack):
#             q = deque()            
#             q.append(root)
#             while q:
#                 for i in range(len(q)):
#                     node = q.popleft()
#                     stack.append(node.val) if node else stack.append(None)
#                     if node:
#                         q.append(node.left)                
#                         q.append(node.right)
        
#         bfs(p, stackP)
#         bfs(q, stackQ)

#         return stackP == stackQ

# 寫法2  
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)