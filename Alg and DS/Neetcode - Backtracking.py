from collections import deque
from typing import Optional

class TreeNode():
    def __init__(self, v: int):
        self.val = v
        self.left = None
        self.right = None
    
    def insert(self, root: "TreeNode", n: int):
        queue = deque()
        queue.append(root)

        while len(queue):
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            else:
                cur.left = TreeNode(n)
                break
            if cur.right:
                queue.append(cur.right)
            else:
                cur.right = TreeNode(n)
                break

    def BFS(self, root: "TreeNode"):
        queue = deque()
        if root:
            queue.append(root)
        
        while len(queue):
            cur = queue.popleft()
            print(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    
    def findNoneZeroPath(self, root: "TreeNode") -> bool:
        if not root or root.val == 0: # 單一 child 時 root == None
            return False
        
        if not root.left and not root.right: # root為 leaf node
            return True
        
        if self.findNoneZeroPath(root.left):
            return True
        if self.findNoneZeroPath(root.right):
            return True
        return False # root 只有一個 child 且 child值為0時進到這一行
    
    def printNoneZeroPath(self, root: "TreeNode", path: Optional[int]) -> bool:
        if not root or root.val == 0:
            return False
        
        path.append(root.val)
        
        if not root.left and not root.right:
            return True
        
        if self.printNoneZeroPath(root.left, path):
            return True
        if self.printNoneZeroPath(root.right, path):
            return True
        
        path.pop()
        return False
        

root = TreeNode(4)
nums = [0,1,5,7,3,2,1,2,3,4,0]
for i in nums:
    root.insert(root, i)

print("==========")
root.BFS(root)

print(f"reach leaf node: {root.findNoneZeroPath(root)}")

print("==========")

res = []
root.printNoneZeroPath(root, res)
print(f"None zero path: {res}")