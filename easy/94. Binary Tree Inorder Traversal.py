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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

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
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorderTraversalHelper(root):
            if not root: return []

            inorderTraversalHelper(root.left) # 一直尋找左子樹，直到最後一個左子樹為止
            res.append(root.val) # 將目前最深的左子樹的值記錄下來
            inorderTraversalHelper(root.right) # 開始尋找右子樹         

        inorderTraversalHelper(root)
        print(res)
        return res

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

#寫法4 : 一樣用迴圈的方式，搭配stack，code的寫法與寫法3稍有不同
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root: return []
#         stack = [] # space O(h) h為樹的高度
#         res = []

#         while root or stack:
#             while root: # 一直往左子樹尋找，直到最後一個左子樹
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             res.append(root.val)
#             root = root.right # 尋找右子樹，把右子樹的root作為目前的root

#         print(res)
#         return res


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

test = Solution()
test.inorderTraversal(tree)










