class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ## also store the previous element to check if the the next one is greater or not
        ## `n+1` for prevIdx bcoz its starting from -1 (so that we can always choose 1st element of nums)
        dp = [[-1]*n for _ in range(n+1)] 

        def memoization(idx, prevIdx): 
            # Base Case
            if idx == n:
                return 0

            if dp[idx][prevIdx+1] != -1:
                return dp[idx][prevIdx+1]

            length = 0 + memoization(idx+1, prevIdx) # `prevIdx` stays same since we didn't choose any element
            if prevIdx == -1 or nums[idx] > nums[prevIdx]: # only add in length if the subsequence is increasing
                length = max(length, 1 + memoization(idx+1, idx))

            dp[idx][prevIdx+1] = length
            return length

        return memoization(0, -1)