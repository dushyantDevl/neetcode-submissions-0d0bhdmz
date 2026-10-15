class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}

        def memoization(currTarget):
            if currTarget == 0:
                return 0

            if currTarget in dp:
                return dp[currTarget]

            res = currTarget
            for i in range(1,currTarget):
                if i*i > currTarget:
                    break
                res = min(res, 1+memoization(currTarget-i*i))

            dp[currTarget] = res
            return dp[currTarget]

        return memoization(n)