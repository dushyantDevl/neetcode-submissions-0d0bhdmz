class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, minPrice, maxProfit = len(prices), prices[0], 0
        for i in range(1, n):
            maxProfit = max(maxProfit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return maxProfit