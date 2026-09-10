class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = [[-1]*n for _ in range(m)]

        # Top-Down Approach: go from bottom-right to top left instead
        def dp(r, c): # returns minPathSum from (0,0) to (r,c)
            if r < 0 or c < 0:
                return int(1e9)

            if r == c == 0:
                return grid[r][c]

            if cache[r][c] != -1:
                return cache[r][c]

            # take the number from the current cell and move either left or up
            left = grid[r][c] + dp(r, c-1) 
            up = grid[r][c] + dp(r-1, c)

            cache[r][c] = min(left, up) # store the path with minimum sum
            return cache[r][c]

        return dp(m-1,n-1)