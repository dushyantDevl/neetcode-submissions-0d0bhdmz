class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Bottom-Up
        n = len(grid)
        dp = [[[float("-inf")] * n for _ in range(n)] for _ in range(n)]

        # Will go from last to first position now (move only left or up)
        for r1 in range(n-1,-1,-1):
            for c1 in range(n-1,-1,-1):
                for r2 in range(n-1,-1,-1):
                    c2 = r1 + c1 - r2
                    
                    if c2 < 0 or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue
                    
                    # Base case
                    if r1 == c1 == n-1:
                        dp[r1][c1][r2] = grid[r1][c1]

                    else:
                        res = max(
                            dp[r1 + 1][c1][r2 + 1] if r1 + 1 < n and r2 + 1 < n else -1000,
                            dp[r1 + 1][c1][r2] if r1 + 1 < n else -1000,
                            dp[r1][c1 + 1][r2 + 1] if c1 + 1 < n and r2 + 1 < n else -1000,
                            dp[r1][c1 + 1][r2] if c1 + 1 < n else -1000
                        )
                        if res == -1000:
                            continue
                        
                        res += grid[r1][c1] if (r1,c1) == (r2,c2) else grid[r1][c1] + grid[r2][c2]

                        dp[r1][c1][r2] = res

        return max(0, dp[0][0][0])
        