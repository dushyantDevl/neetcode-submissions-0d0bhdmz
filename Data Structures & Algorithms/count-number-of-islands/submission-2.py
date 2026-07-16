class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == '0'
            ):
                return

            # mark visited in grid itself (since we not gonna visit the same cell anyway)
            grid[r][c] = '0'
            
            for dr, dc in direction:
                dfs(r+dr, c+dc)

        noOfIsland = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    noOfIsland += 1

        return noOfIsland