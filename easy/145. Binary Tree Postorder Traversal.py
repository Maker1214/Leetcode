# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [3,2,1]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,6,7,5,2,9,8,3,1]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

# iterative : time O(n), space O(n)
# two stacks : stack1 :[中，左，右](TreeNode處理順序，先處理的TreeNode先放進stack1，
#                                  遍歷順序越後面需要越被先處理，stack1的順序為右子樹 -> 左子樹) 
#              stack2:[中，右，左](最後將stack2反序拿出來，即為結果)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        stack1 = [root]
        stack2 = []

        while stack1:
            curr = stack1.pop()
            stack2.append(curr.val)
            if curr.left: #先等右子樹處理完後再來處理左子樹，因為左子樹在stack2的順序是比較後面的，因此需要比較晚被加入stack2
                stack1.append(curr.left)
            if curr.right: #下一輪優先處理右子樹，因為右子樹需要比左子樹更早被加入stack2中
                stack1.append(curr.right)
        
        return stack2[::-1]
            

# recursive : time O(n), space O(n * function)            
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []

#         def helper(root: Optional[TreeNode]):
#             if not root: return
            
#             helper(root.left)
#             helper(root.right)
#             res.append(root.val)
        
#         helper(root)

#         return res


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack1 = [root]
        stack2 = []
        
        while stack1:
            cur = stack1.pop()
            stack2.append(cur.val)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
        
        return stack2[::-1]


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(None)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

test = Solution()
print(test.postorderTraversal(tree))
