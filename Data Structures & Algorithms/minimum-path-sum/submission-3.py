class Solution:

  def minPathSum(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [float("inf")] * n
    dp[0] = 0

    for r in range(m):
      dp[0] += grid[r][0]
      for c in range(1, n):
        dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

    return dp[n-1]