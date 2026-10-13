class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]

        def memoization(idx, canBuy):
            # Base Case
            if idx == n:
                ## even if you've a stocks, you can't sell now that the window to 
                ## buy or sell is over and there's no negative profit either in just
                ## holding the stocks at this point
                return 0

            if dp[idx][canBuy] != -1:
                return dp[idx][canBuy]

            profit = 0

            if canBuy:
                profit = max(
                    ## buying will decrease the money we've that's why `-`
                    ## can't buy more than once (before sell) after buying on current day
                    -prices[idx] + memoization(idx+1, False), # take
                    ## didn't buy bcoz maybe price is more
                    ## can buy next since we did't at current day/index
                    0 + memoization(idx+1, True) # not take
                )
            else:
                profit = max(
                    ## selling will increase the money that's why prices[idx] is added
                    ## to profit
                    prices[idx] + memoization(idx+1, True), # sell the stocks
                    0 + memoization(idx+1, False) # hold the stocks
                )

            dp[idx][canBuy] = profit
            return dp[idx][canBuy]

        return memoization(0,True)