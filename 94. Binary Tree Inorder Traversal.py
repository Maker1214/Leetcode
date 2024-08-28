# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 寫法1 : 把res當作參數傳進helper中，即可改變呼叫端的res值
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.inorderTraversalHelper(root, res)
#         return res


#     def inorderTraversalHelper(self, root, res):
#         if not root: return

#         self.inorderTraversalHelper(root.left, res)
#         res.append(root.val)
#         self.inorderTraversalHelper(root.right, res)

#         return

# 寫法2 : 將res宣告成全域變數，即可改變res值
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []

#         def inorderTraversalHelper(root):
#             if not root: return 

#             inorderTraversalHelper(root.left)
#             res.append(root.val)
#             inorderTraversalHelper(root.right)
#             return
          

#         inorderTraversalHelper(root)
#         return res

# 寫法3 : 用迴圈的方式，搭配stack
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         stack, res = [], []

#         curr = root
#         while curr:
#             stack.append(curr)
#             curr = curr.left
#             while not curr and stack:
#                 node = stack.pop()               
#                 res.append(node.val)
#                 curr = node.right

#         return res
    
# 寫法4 : 一樣用迴圈的方式，搭配stack，code的寫法與寫法3稍有不同
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            res.append(curr.val)
            root = curr.right
        
        return res









