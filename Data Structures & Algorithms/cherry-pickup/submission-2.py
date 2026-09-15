class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Instead of thinking about one person going from the top-left to the bottom-right and
        # then back, we can simulate two people starting from the top-left and moving 
        # simultaneously toward the bottom-right. Since both paths must eventually reach 
        # the destination, we track their positions using four variables (r1, c1) and 
        # (r2, c2). At each step, both move either down or right, giving us 4 combinations 
        # of moves. When they land on the same cell, we only count the cherries once to 
        # avoid double counting.

        # Top-Down (Optimized)
        n = len(grid)
        dp = [[[float("-inf")] * n for _ in range(n)] for _ in range(n)]

        def dfs(r1, c1, r2):
            ## Both person #1 & #2 will going to take the same number of step at any moment
            ## bcoz they are always advancing by one step at a time, e.g. if a person is at (r1,c1)
            ## total step taken will be r1+c1, therefore r1+c1 = r2+c2
            c2 = r1 + c1 - r2
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -1000

            if r1 == r2 == c1 == c2 == n - 1:
                return grid[r1][c1]

            if dp[r1][c1][r2] != float("-inf"):
                return dp[r1][c1][r2]

            # Explore all 4 possible moves
            res = dfs(r1 + 1, c1, r2 + 1)
            res = max(res, dfs(r1 + 1, c1, r2))
            res = max(res, dfs(r1, c1 + 1, r2 + 1))
            res = max(res, dfs(r1, c1 + 1, r2))
            
            # count once in case both person are at same position
            res += grid[r1][c1] if (r1,c1) == (r2,c2) else grid[r1][c1] + grid[r2][c2]

            dp[r1][c1][r2] = res
            return res

        return max(0, dfs(0, 0, 0))
        