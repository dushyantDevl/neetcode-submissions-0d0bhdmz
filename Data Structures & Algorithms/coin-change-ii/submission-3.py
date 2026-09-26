class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]

        for amt in range(amount+1):
            dp[0][amt] = int(amt % coins[0] == 0)

        for idx in range(1,n):
            for amt in range(amount+1):
                notTake = dp[idx-1][amt]
                take = dp[idx][amt-coins[idx]] if amt >= coins[idx] else 0

                dp[idx][amt] = notTake + take

        return dp[n-1][amount]