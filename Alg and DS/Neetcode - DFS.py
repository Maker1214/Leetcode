class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    # 對BST而言，inorder可依序由小到大印出
    def inorder(self, root: "TreeNode") -> None: # 由小到大
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
    
    def inorder(self, root: "TreeNode") -> None: # 由大到小
        if root:
            self.inorder(root.right)
            print(root.val)
            self.inorder(root.left)
    
    def preorder(self, root: "TreeNode") -> None:
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self, root: "TreeNode") -> None:
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)