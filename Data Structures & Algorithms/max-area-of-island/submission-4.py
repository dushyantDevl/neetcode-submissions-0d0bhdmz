class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COlS = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # [up, right, down, left]

        def dfs(r,c):
            grid[r][c] = 0 # mark visited

            area = 1 # for current land cell

            for dr,dc in directions:
                rdr, cdc = r+dr, c+dc
                if 0 <= rdr < ROWS and 0 <= cdc < COlS and grid[rdr][cdc] == 1:
                    area += dfs(rdr,cdc) # add area of valid land cells
            
            return area
        
        maxArea = 0

        for r in range(ROWS):
            for c in range(COlS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea