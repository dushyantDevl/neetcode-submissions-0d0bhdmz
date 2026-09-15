class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        NEG = float("-inf")

        # dp[r1][c1][r2] = max cherries for two paths from (r1,c1) and (r2,c2)
        # down to (n-1, n-1). Both paths take the same number of steps, so
        # r1 + c1 == r2 + c2, which lets us derive c2 and drop a dimension.
        dp = [[[NEG] * n for _ in range(n)] for _ in range(n)]

        # Build bottom-up: each cell depends on cells below/right of it.
        for r1 in range(n - 1, -1, -1):
            for c1 in range(n - 1, -1, -1):
                for r2 in range(n - 1, -1, -1):
                    c2 = r1 + c1 - r2

                    # Skip invalid columns or thorn cells.
                    if not (0 <= c2 < n) or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue

                    # Base case: both paths at the bottom-right corner.
                    if r1 == c1 == n - 1:
                        dp[r1][c1][r2] = grid[r1][c1]
                        continue

                    # Try all 4 combinations of next moves (each path goes down or right).
                    best = NEG
                    for nr1, nc1 in ((r1 + 1, c1), (r1, c1 + 1)):
                        for nr2 in (r2 + 1, r2):
                            if nr1 < n and nc1 < n and nr2 < n:
                                best = max(best, dp[nr1][nc1][nr2])

                    if best == NEG:
                        continue

                    # Collect cherries; count the shared cell only once.
                    best += grid[r1][c1] if (r1, c1) == (r2, c2) else grid[r1][c1] + grid[r2][c2]
                    dp[r1][c1][r2] = best

        # If (0,0) is unreachable the corner path is blocked, so clamp to 0.
        return max(0, dp[0][0][0])