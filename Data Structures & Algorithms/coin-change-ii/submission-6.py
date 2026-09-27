class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)

        # Base cases
        for amt in range(amount+1): dp[amt] = int(amt % coins[0] == 0)

        for idx in range(1, n):
            for amt in range(1, amount+1):
                notTake = dp[amt]
                take = dp[amt-coins[idx]] if amt >= coins[idx] else 0

                dp[amt] = notTake + take

        return dp[amount]