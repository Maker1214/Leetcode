

# C code
#include <stdio.h>
#include <stdlib.h>

# // time : O(n)
# void initParent(int *parent){
#     for (int i=0; i<6; i++){
#         *parent++ = -1;
#     }
# }

# // time : O(n)
# // int findRoot(int x, int *parent){
# //     while (parent[x] != -1){
# //         x = parent[x];
# //     }
# //     return x;
# // }
# int findRoot(int x, int *parent){
#     if (parent[x] == -1){
#         return x;
#     }
#     // time : O(n)
#     //return findRoot(parent[x], parent);
#     // time : O(rank) < O(n)
#     return (parent[x] = findRoot(parent[x], parent));
# }

# // return 1 : union successfully. return 0 : union unsuccessfully and it means it's a cycle
# // time : O(n)
# int unionVertices(int x, int y, int *parent, int *rank){
#     int xRoot = findRoot(x, parent);
#     int yRoot = findRoot(y, parent);
    
#     // x and y have the same root
#     if (xRoot == yRoot){
#         return 0;
#     }
#     if (rank[xRoot] > rank[yRoot]){
#         parent[yRoot] = xRoot;
#     }
#     else if (rank[xRoot] < rank[yRoot]){
#         parent[xRoot] = yRoot;
#     }
#     else{
#         rank[yRoot]++;
#         // union x and y, x's root is y
#         parent[xRoot] = yRoot;
#     }
#     return 1;
# }

# int main()
# {
#     int parent[6] = {0};
#     int rank[6] = {0};
#     initParent(parent);
    
#     int edges[5][2] = {
#       {0,1}, {1,2}, {1,3},
# 	    {3,4}, {2,5}  
#     };
    
#     for (int i=0; i<5; i++){
#         int x = edges[i][0];
#         int y = edges[i][1];
#         if (unionVertices(x, y, parent, rank) == 0){
#             printf("There is a cycle\n");
#             exit(0);
#         }
#     }
#     for (int j=0; j<5; j++){
#         printf("rank[%d] is %d\n", j, rank[j]);
#     }
#     printf("No cycle\n");
    
#     return 0;
# }

class UnionFind:
    # n is the number of the nodes
    def __init__(self,n):
        self.parent = [-1] * n
        self.rank = [0] * n
    
    def findRoot(self, x: int) -> int:
        if self.parent[x] == -1:
            return x    

        # path compression
        self.parent[x] = self.findRoot(self.parent[x])
        return self.parent[x]

    def unionVertices(self, x: int, y: int) -> bool:
        xRoot, yRoot = self.findRoot(x), self.findRoot(y)

        if xRoot == yRoot: # x and y have the same root
            return False # there is a cycle if union x and y
        # union by rank
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1
        return True


edges = [[0,1],[1,2],[1,3],[3,4],[2,5],[0,2]]
obj = UnionFind(6)

for x, y in edges:
    if obj.unionVertices(x, y) == False:
        print(f"There is a cycle after add {[x, y]}!")
        break
