class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # [up, right, down, left]
        
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>= COLS or grid[r][c] == 0:
                return 1

            if grid[r][c] == -1: 
                # if a one island cell is sharing any edge with another island cell then not count in perimeter
                return 0

            grid[r][c] = -1 # mark as visited cell

            res = 0
            for dr,dc in directions:
                res += dfs(r+dr, c+dc)
            
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # bcoz there is exactly one island, we can return directly here
                    return dfs(r,c)

        return 0