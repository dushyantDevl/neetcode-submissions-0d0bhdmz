class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[[float("-inf")] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]

        def dfs(r1, c1, r2, c2):
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -1000

            if r1 == n - 1 and r2 == n - 1 and c1 == n - 1 and c2 == n - 1:
                return grid[r1][c1]

            if dp[r1][c1][r2][c2] != float("-inf"):
                return dp[r1][c1][r2][c2]

            res = dfs(r1 + 1, c1, r2 + 1, c2)
            res = max(res, dfs(r1 + 1, c1, r2, c2 + 1))
            res = max(res, dfs(r1, c1 + 1, r2 + 1, c2))
            res = max(res, dfs(r1, c1 + 1, r2, c2 + 1))
            res += grid[r1][c1] + grid[r2][c2]
            if r1 == r2 and c1 == c2:
                res -= grid[r1][c1]

            dp[r1][c1][r2][c2] = res
            return res

        return max(0, dfs(0, 0, 0, 0))