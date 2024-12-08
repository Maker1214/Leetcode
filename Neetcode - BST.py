class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def Search(self, root, target):
        if not root:
            return False
        
        if root.val < target:
            return self.Search(root.right, target)
        elif root.val > target:
            return self.Search(root.left, target)
        else:
            return True