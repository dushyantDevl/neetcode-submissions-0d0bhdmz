class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0
            ):
                return 0

            # mark visited in grid itself (since we not gonna visit the same cell anyway)
            grid[r][c] = 0

            return (1 + dfs(r+1, c) + # down cell
                        dfs(r, c+1) + # right cell
                        dfs(r-1, c) + # upper cell
                        dfs(r, c-1)) # left cell

        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea