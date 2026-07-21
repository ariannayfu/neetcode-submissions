class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs (r: int, c: int):
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    numIslands += 1
                    dfs(r, c)

        return numIslands
