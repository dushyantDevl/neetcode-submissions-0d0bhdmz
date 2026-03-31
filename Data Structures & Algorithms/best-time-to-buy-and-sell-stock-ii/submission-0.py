class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, total_days = 0, len(prices)
        for i in range(1,total_days):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit