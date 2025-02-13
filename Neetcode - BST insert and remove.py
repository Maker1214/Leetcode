class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# worst case為只有左子樹或只有右子樹
# time complexity : O(logn)，但worst case為O(n) ==> sorted array要插入一個值為 O(n)
def insert(root,treeNode):
    if not root:
        return treeNode

    if treeNode.val > root.val:
        root.right = insert(root.right, treeNode)
    elif treeNode.val < root.val:
        root.left = insert(root.left, treeNode)
    
    return root

# time complexity : O(logn)，但worst case為O(n) ==> sorted array要找到最小值為O(1)
def findMinNode(root):
    while root and root.left:
        root = root.left
    
    return root

# recursive to find the min node
def findMinNode(root):
    if not root or not root.left:
        return root
    return findMinNode(root.left)

# time complexity : O(logn)，但worst case為O(n) ==> sorted array要移除一個值為O(n)
def remove(root, val):
    # 沒有找到 val
    if not root: 
        return None


    if root.val > val:
        root.left = remove(root.left, val)
    elif root.val < val:
        root.right = remove(root.right, val)
    else:
        # 0 or 1 child且無右子樹
        if not root.right:
            return root.left
        # 0 or 1 child且無左子樹
        elif not root.left:
            return root.right
        # 2 children
        else:
            target = findMinNode(root.right)
            root.val = target.val
            root.right = remove(root.right, root.val)
    return root
