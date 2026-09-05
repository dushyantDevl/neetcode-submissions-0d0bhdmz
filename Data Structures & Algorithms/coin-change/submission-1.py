class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dp(curr):
            if curr == 0:
                return 0

            if curr in cache:
                return cache[curr]

            res = float('inf')

            for coin in coins:
                if curr - coin >= 0:
                    res = min(res, 1 + dp(curr-coin))
            
            cache[curr] = res
            
            return res

        res = dp(amount)

        return -1 if res == float('inf') else res
            