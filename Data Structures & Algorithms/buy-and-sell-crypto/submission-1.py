class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, buyDay, sellDay, maxProfit = len(prices), 0, 1, 0
        while sellDay < n:
            if prices[sellDay] > prices[buyDay]:
                profit = prices[sellDay] - prices[buyDay]
                maxProfit = max(maxProfit, profit)
            else:
                buyDay += 1
            sellDay += 1
        return maxProfit