class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = triangle[m-1][:]
        for i in range(m - 2, -1, -1): dp = [triangle[i][j] + min(dp[j], dp[j + 1]) for j in range(i + 1)]
        return dp[0]