class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, inAscending, inDescending = len(prices), True, True
        for i in range(1, n):
            if prices[i-1] > prices[i]: inAscending = False
            if prices[i-1] < prices[i]: inDescending = False
        if inAscending: return prices[n-1] - prices[0]
        if inDescending: return 0

        profit = 0
        for i in range(n):
            for j in range(i+1, n):
                profit = max(profit, prices[j]-prices[i])
        
        return profit