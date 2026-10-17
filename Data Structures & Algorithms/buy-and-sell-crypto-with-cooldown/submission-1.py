class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalDays = len(prices)
        dp = [[-1]*2 for _ in range(totalDays)]

        def memoization(day, canBuy):
            # Base Case
            if day >= totalDays:
                ## even if you've a stocks, you can't sell, now that the window to 
                ## buy or sell is over and there's no negative profit either in just
                ## holding the stocks at this point
                return 0

            if dp[day][canBuy] != -1:
                return dp[day][canBuy]

            profit = 0

            if canBuy:
                profit = max(
                    ## buying will decrease the money we've that's why `-`
                    ## can't buy more than once (before sell) after buying on current day
                    -prices[day] + memoization(day+1, False), # take
                    ## didn't buy bcoz maybe price is more
                    ## can buy next since we did't at current day/index
                    0 + memoization(day+1, True) # not take
                )
            else:
                profit = max(
                    ## selling will increase the money that's why prices[day] is added
                    ## to profit and since there's a cooldown of one day i.e. we aren't allowed to buy next day
                    ## that's why day+2 (skip the next day)
                    prices[day] + memoization(day+2, True), # sell the stocks
                    0 + memoization(day+1, False) # hold the stocks
                )

            dp[day][canBuy] = profit
            return dp[day][canBuy]

        return memoization(0, True)