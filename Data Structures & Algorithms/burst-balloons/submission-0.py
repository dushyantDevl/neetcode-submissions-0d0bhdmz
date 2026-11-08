class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]
        
        def memoization(l, r):
            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
                
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += memoization(l, i - 1) + memoization(i + 1, r)
                dp[l][r] = max(dp[l][r], coins)
            return dp[l][r]

        return memoization(1, len(nums) - 2)