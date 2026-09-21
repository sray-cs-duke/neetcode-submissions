from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                
        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc

                if (
                    r < 0 or r >= rows or
                    c < 0 or c >= cols or 
                    grid[r][c] != 2147483647
                ):
                    continue
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr,nc))