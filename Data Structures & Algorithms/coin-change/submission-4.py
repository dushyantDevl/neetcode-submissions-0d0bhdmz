class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Why does greedy fail?
        ## e.g. coins = [9,6,5,1], amount = 11
        ## going greedy, pick the elements in decreasing order:
        ## 11//9 = 1 => 2//6 (not possible) => 2//5 (not possible) => 2//1 = 1 => 1//1 = 1
        ## so according to greedy, we need total of 3 coins: [9,1,1]
        ## but better solution is to just use 2 coins: [5,6] 
        ## therfore, greey fails here, bcoz there's no uniformity here
        dp = [[-1]*(amount+1) for _ in range(len(coins))]

        def dfs(idx, currAmt):
            if idx == 0:
                # only possible if the remaining coin is fully divisible by amount left
                return currAmt // coins[idx] if currAmt % coins[idx] == 0 else float('inf')

            if dp[idx][currAmt] != -1:
                return dp[idx][currAmt]

            notTake = 0 + dfs(idx-1, currAmt) # didn't choose the coin at index=idx
            take = 1 + dfs(idx, currAmt-coins[idx]) if currAmt>=coins[idx] else float('inf')

            dp[idx][currAmt] = min(notTake, take)
            return dp[idx][currAmt]

        res = dfs(len(coins)-1, amount)
        return res if res != float('inf') else -1