# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10 ** 4 <= root.val <= 10 ** 4
# -10 ** 4 <= subRoot.val <= 10 ** 4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#寫法1
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
#         def isSameTree(root, subRoot):
#             if not root and not subRoot:
#                 return True
#             if not root or not subRoot or root.val != subRoot.val:
#                 return False
            
#             return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
#         res = False

#         # 空的subRoot必定是root的subtree，無論root有沒有值
#         if not subRoot:
#             return True
#         # 因為上面判斷式的關係，此時subRoot必定為非空，因此此時非空的subRoot必定不是空的root的subtree
#         if not root:
#             return False
        
#         if root.val == subRoot.val:
#             res |= isSameTree(root, subRoot)
        
#         res |= self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#         return res

#寫法2 : 去掉res
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False            
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

        if not subRoot:
            return True
        
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)