class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # Top-Down Approach (optimized)
        prev, prev2 = 2, 1

        for _ in range(3, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        
        return prev