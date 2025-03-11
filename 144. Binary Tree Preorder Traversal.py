# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,2,3]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [1,2,4,5,6,7,3,8,9]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right        

# recursive : time O(n) space O(n)    
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def helper(root):
#             if root:
#                 res.append(root.val) # because no res is defined inside the helper, it will try to find the res outside the helper
#                 helper(root.left)
#                 helper(root.right)

#         helper(root)
#         return res

# iterative 寫法1 : time O(n) space O(n)
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
#         res = []
#         nodeStack = [] # without this stack, we can't got back to the right sub tree

#         while root or nodeStack:
#             if root:
#                 res.append(root.val)
#                 nodeStack.append(root.right)
#                 nodeStack.append(root.left)
#             if nodeStack:
#                 root = nodeStack.pop()
#             else:
#                 root = None
        
#         return res

#iterative 寫法2 : time O(n) space O(n)
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
#         res = []
#         nodeStack = [] # without this stack, we can't got back to the right sub tree

#         while root or nodeStack:
#             if root:
#                 res.append(root.val)
#                 nodeStack.append(root.right)
#                 root = root.left
#             else: # when no root and root.left, we pop the right sub tree
#                 root = nodeStack.pop()
        
#         return res

