class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalDays = len(prices)
        # Tabulation (Bottom-Up) -> Space Optimization
        curr, after, after1 = [0]*2, [0]*2, [0]*2

        for day in range(totalDays-1, -1, -1):
            curr[True] = max(-prices[day] + after[False], 0 + after[True]) # Buy
            curr[False] = max(prices[day] + after1[True], 0 + after[False]) # Sell

            after1[:] = after[:]
            after[:] = curr[:]

        return curr[True]