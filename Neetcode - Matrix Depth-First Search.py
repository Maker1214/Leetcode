class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r: int,c: int,visited: set) -> int:
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited
               or grid[r][c] == 1) :
               return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            count = 0
            visited.add((r,c))
            # 單獨算出每一個(r, c)的valid path數量
            # 例如當藍色(r, c) = (0, 2)時，
            # count += dfs(r + 1, c, visited) ==> 粉紅色，得到1
            # count += dfs(r - 1, c, visited) ==> 超出邊界invalid，得到0
            # count += dfs(r, c + 1, visited) ==> 綠色，得到1
            # count += dfs(r, c - 1, visited) ==> 已走過invaid，得到0
            # 因此藍色(r, c) = (0, 2)的count = 2
            count += dfs(r + 1, c, visited)
            count += dfs(r - 1, c, visited)
            count += dfs(r, c + 1, visited)
            count += dfs(r, c - 1, visited)
            visited.remove((r,c))

            # 把每一個(r, c)的valid path數量加總後回傳，
            return count
        
        return dfs(0, 0, set())