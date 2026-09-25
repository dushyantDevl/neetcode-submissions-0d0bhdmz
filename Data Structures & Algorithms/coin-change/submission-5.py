class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Tabulation (Bottom-up, opposite of recursive i.e. top-down approach)
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]

        ## Base case
        for amt in range(amount+1):
            dp[0][amt] = amt // coins[0] if amt % coins[0] == 0 else float('inf')

        ## fill the rest of dp list (starting from index=1)
        for idx in range(1, n):
            for amt in range(amount+1):
                notTake = 0 + dp[idx-1][amt] # didn't choose the coin at index=idx
                take = 1 + dp[idx][amt-coins[idx]] if amt >= coins[idx] else float('inf')

                dp[idx][amt] = min(notTake, take)

        return dp[n-1][amount] if dp[n-1][amount] != float('inf') else -1