class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        vis = set()

        def dfs(r, c):
            if ((r,c) in vis or
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == '0'
            ):
                return

            vis.add((r,c))
            
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        noOfIsland = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in vis and grid[r][c] == '1':
                    noOfIsland += 1
                    dfs(r, c)

        return noOfIsland