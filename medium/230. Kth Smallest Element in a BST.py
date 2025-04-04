# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. inorder and save it into a list
# 2. find the result from that list
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         res = []

#         def inorder(root):
#             if not root:
#                 return 
#             inorder(root.left)
#             res.append(root.val)
#             inorder(root.right)
#         inorder(root)
#         return res[k - 1]

#寫法2 : 用迴圈來寫    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            root = curr.right






