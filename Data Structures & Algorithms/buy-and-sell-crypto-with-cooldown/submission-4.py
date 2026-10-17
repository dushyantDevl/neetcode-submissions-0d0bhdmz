class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalDays = len(prices)
        # Tabulation (Bottom-Up)
        ## bcoz of [day+2] case it's better to not do any space optimization, tho we can do it via 3 different lists
        dp = [[0]*2 for _ in range(totalDays+2)]

        for day in range(totalDays-1, -1, -1):
            dp[day][True] = max(-prices[day] + dp[day+1][False], 0 + dp[day+1][True]) # Buy
            dp[day][False] = max(prices[day] + dp[day+2][True], 0 + dp[day+1][False]) # Sell

        return dp[0][True]