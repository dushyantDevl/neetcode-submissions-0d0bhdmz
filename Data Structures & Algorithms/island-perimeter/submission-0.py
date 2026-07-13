class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        vis = set()
        def dfs(r, c):
            if r<0 or c<0 or \
                r>=ROW or c>= COL or \
                grid[r][c] == 0:
                return 1

            if (r, c) in vis:
                return 0

            vis.add((r,c))
            
            return dfs(r,c+1) + dfs(r+1,c) + dfs(r,c-1) + dfs(r-1,c)

        res = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    return dfs(r,c)

        return res