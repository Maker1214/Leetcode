# Design a directed Graph class.

# Your Graph class should support the following operations:

# Graph() will initialize an empty directed graph.
# void addEdge(int src, int dst) will add an edge from src to dst if it does not already exist. If either src or dst do not exist, add them to the graph.
# bool removeEdge(int src, int dst) will remove the edge from src to dst if it exists. Return whether the edge was removed. Either src or dst may not exist in the graph.
# bool hasPath(int src, int dst) will return whether there is a path from src to dst. Assume both src and dst exist in the graph.
# Constraints:

# Each vertex value will be a unique integer.
# Multiple edges from one vertex to another are not allowed.
# A vertex will not have an edge to itself, but the graph may contain a cycle.
# The graph is not necessarily connected (there may be disconnected components).
# Example 1:

# Input:
# ["addEdge", 1, 2, "addEdge", 2, 3, "hasPath", 1, 3, "hasPath", 3, 1, "removeEdge", 1, 2, "hasPath", 1, 3]

# Output:
# [null, null, true, false, true, false]
# Example 2:

# Input:
# ["addEdge", 1, 2, "addEdge", 2, 3, "addEdge", 3, 1, "hasPath", 1, 3, "hasPath", 3, 1]

# Output:
# [null, null, null, true, true]

from collections import deque
class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj: self.adj[src] = []
        if dst not in self.adj: self.adj[dst] = []
        if dst not in self.adj[src]: self.adj[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj or dst not in self.adj[src]: return False

        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set() # avoid to visit the same node again to cause infinite loop
        q = deque()
        q.append(src)
        visit.add(src)

        # BFS
        while q:
            for _ in range(len(q)):
                s = q.popleft()
                # search all neighbors of s. The neighbors of s means the same level of s
                for neighbor in self.adj[s]:
                    if neighbor == dst: return True
                    if neighbor not in visit:
                        visit.add(neighbor)
                        q.append(neighbor)
        
        return False
