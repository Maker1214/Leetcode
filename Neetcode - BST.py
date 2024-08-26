class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Search(root, target):
    if not root:
        return False
    if target < root.value:
        return Search(root.left, target)
    elif target > root.value:
        return Search(root.right, target)
    else:
        return True
