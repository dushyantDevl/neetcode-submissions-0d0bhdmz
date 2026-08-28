class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n!= 0 else 0

        # Bottom-Up approach
        cache = [0] * (n+1)
        cache[1] = cache[2] = 1

        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2] + cache[i-3]

        return cache[n]