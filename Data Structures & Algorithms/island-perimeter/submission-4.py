class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        vis = set()
        def dfs(r, c):
            ## Return 1 for every invalid move, going from certain cell to 
            ## out of boundary or in a cell with water means that certain cell represents the 
            ## corner element or it contains boundary that means this boundary will be counted
            ## in perimeter
            if r<0 or c<0 or r>=ROW or c>= COL or grid[r][c] == 0:
                return 1

            ## If perimeter of certain cell is already counted
            if (r, c) in vis:
                return 0

            vis.add((r,c))

            ## check for all the valid neighboring lands (vertical and horizontal)    
            return dfs(r,c+1) + dfs(r+1,c) + dfs(r,c-1) + dfs(r-1,c)

        res = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    return dfs(r,c)

        return res