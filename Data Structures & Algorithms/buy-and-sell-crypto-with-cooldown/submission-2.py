class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalDays = len(prices)
        # Tabulation (Bottom-Up)
        dp = [[0]*2 for _ in range(totalDays+2)]

        for day in range(totalDays-1, -1, -1):
            for canBuy in [True, False]:
                if canBuy:
                    profit = max(
                        ## buying will decrease the money we've that's why `-`
                        ## can't buy more than once (before sell) after buying on current day
                        -prices[day] + dp[day+1][False], # take
                        ## didn't buy bcoz maybe price is more
                        ## can buy next since we did't at current day/index
                        0 + dp[day+1][True] # not take
                    )
                else:
                    profit = max(
                        ## selling will increase the money that's why prices[day] is added
                        ## to profit and since there's a cooldown of one day i.e. we aren't allowed to buy next day
                        ## that's why day+2 (skip the next day)
                        prices[day] + dp[day+2][True], # sell the stocks
                        0 + dp[day+1][False] # hold the stocks
                    )

                dp[day][canBuy] = profit


        return dp[0][True]