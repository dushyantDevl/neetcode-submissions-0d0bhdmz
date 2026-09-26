class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]

        def memo(idx, amt):
            if idx == 0:
                return 1 if amt % coins[idx] == 0 else 0

            if dp[idx][amt] != -1:
                return dp[idx][amt]

            notTake = memo(idx-1, amt)
            take = memo(idx, amt-coins[idx]) if amt >= coins[idx] else 0

            dp[idx][amt] = notTake + take
            return dp[idx][amt]

        return memo(len(coins)-1, amount)