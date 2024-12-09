from collections import deque

def BFS(root):
    queue = deque()

    if root:
        queue.append(root)
    
    while len(queue) > 0:
        curr = queue.popleft()

        print(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        