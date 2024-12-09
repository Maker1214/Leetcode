class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    # time complexity : O(logn) ， 最糟的狀況為只有單邊 node ，也就像 single linkded list，此時 time complexity 為 O(n)
    def Search(self, root, target):
        if not root:
            return False
        
        if root.val < target:
            return self.Search(root.right, target)
        elif root.val > target:
            return self.Search(root.left, target)
        else:
            return True