class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        largest = 0

        def dfs(r,c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0
            ):
                return 0
            grid[r][c] = 0
            area = 1

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                area += dfs(r + dr, c + dc)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    largest = max(largest, dfs(r,c))
        return largest