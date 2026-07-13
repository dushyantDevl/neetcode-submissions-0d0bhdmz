class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        vis = set()
        def dfs(r, c):
            # Invalid move also means at edge of the island i.e. outer boundary i.e. perimeter candidate
            if (r<0 or c<0 or # area edge
                r>=ROW or c>= COL or # are edge
                grid[r][c] == 0 # edge near water
            ): 
                return 1

            if (r, c) in vis: # perimeter already counted for this cell so don't add 
                return 0

            vis.add((r,c))
            
            return dfs(r,c+1) + dfs(r+1,c) + dfs(r,c-1) + dfs(r-1,c)

        perimeter = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    perimeter += dfs(r,c)

        return perimeter