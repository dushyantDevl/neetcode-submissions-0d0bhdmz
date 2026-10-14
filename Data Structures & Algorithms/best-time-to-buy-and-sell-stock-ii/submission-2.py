class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalDays, profit = len(prices), 0
        ## to make profit only buy and sell if the price is increasing in upcoming days, we can do this bcoz we can see
        ## the future i.e. prices of upcoming days, so just buy when price increases otherwise just hold
        for i in range(totalDays-1): # run until 2nd last day, so that `i+1` don't go out of bound
            net = prices[i+1] - prices[i]
            if net > 0: # profit condition
                profit += net
        return profit