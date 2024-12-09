class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# sort(small -> big)
# time complexity : O(n)
def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# time complexity : O(n)
# sort(big -> small)
def inorder(root):
    if not root:
        return
    inorder(root.right)
    print(root.val)
    inorder(root.left)

# time complexity : O(n)
def preorder(root):
    if not root:
        return
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# time complexity : O(n)
def postorder(root):
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)