class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# time complexity : O(logn) ==> 比 sorted array還快，array要插入一個值得time complexity為 O(n)
def insert(root,treeNode):
    if not root:
        return treeNode

    if treeNode.val > root.val:
        root.right = insert(root.right, treeNode)
    elif treeNode.val < root.val:
        root.left = insert(root.left, treeNode)
    
    return root

# time complexity : O(logn)
def findMinNode(root):
    while root and root.left:
        root = root.left
    
    return root

# recursive to find the min node
def findMinNode(root):
    if not root or not root.left:
        return root
    return findMinNode(root.left)


# time complexity : O(logn) ==> 比 sorted array還快，array要插入一個值得time complexity為 O(n)
def remove(root, val):
    # 沒有找到 val
    if not root: 
        return None


    if root.val > val:
        root.left = remove(root.left, val)
    elif root.val < val:
        root.right = remove(root.right, val)
    else:
        # 0 or 1 child且右邊無child
        if not root.right:
            return root.left
        # 0 or 1 child且左邊無child
        elif not root.left:
            return root.right
        # 2 children
        else:
            target = findMinNode(root.right)
            root.val = target.val
            root.right = remove(root.right, root.val)
    return root
