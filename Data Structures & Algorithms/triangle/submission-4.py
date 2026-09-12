class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = triangle[m-1][:]
        temp = [0]*m
        for i in range(m - 2, -1, -1):
            for j in range(i, -1, -1):
                temp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
            dp = temp[:]
        return dp[0]