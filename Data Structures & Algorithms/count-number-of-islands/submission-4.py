class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # [up, right, down, left]

        def dfs(r,c):
            # return immediately if the island is already visited
            # since we only call dfs for land this will case will trigger only for the visited cells
            if grid[r][c] == "0":
                return

            grid[r][c] = "0" # Mark visited

            for dr,dc in directions:
                rdr, cdc = r+dr, c+dc
                if 0 <= rdr < ROWS and 0 <= cdc < COLS: # run dfs only for valid cells
                    dfs(rdr, cdc)


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                # run dfs only for land
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1

        return res
