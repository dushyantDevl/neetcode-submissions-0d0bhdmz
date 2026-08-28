class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [-1] * (n+1)

        def dp(n):
            if n <= 1:
                return n
            if n == 2:
                return 1

            if cache[n] != -1:
                return cache[n]

            cache[n] = dp(n-1) + dp(n-2) + dp(n-3)
            return cache[n]

        return dp(n)