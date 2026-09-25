class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Tabulation (Bottom-up, opposite of recursive i.e. top-down approach)
        n = len(coins)
        prev, curr = [0]*(amount+1), [0]*(amount+1)

        ## Base case
        for amt in range(amount+1):
            prev[amt] = amt // coins[0] if amt % coins[0] == 0 else float('inf')

        ## fill the rest of dp list (starting from index=1)
        for idx in range(1, n):
            for amt in range(amount+1):
                notTake = 0 + prev[amt] # didn't choose the coin at index=idx
                take = 1 + curr[amt-coins[idx]] if amt >= coins[idx] else float('inf')

                curr[amt] = min(notTake, take)
            prev = curr[:]

        return prev[amount] if prev[amount] != float('inf') else -1