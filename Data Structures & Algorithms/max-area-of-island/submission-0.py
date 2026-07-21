class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        maxSize = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int, c: int) -> int:
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            return (1 + 
                    dfs(r + 1, c) + # Down
                    dfs(r - 1, c) + # Up
                    dfs(r, c + 1) + # Right
                    dfs(r, c - 1))  # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = dfs(r, c)
                    maxSize = max(maxSize, size)
        return maxSize
        