class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # Tabulation (Bottom-Up)
        ## also store the previous element to check if the the next one is greater or not
        ## `n+1` for prevIdx bcoz its starting from -1 (so that we can always choose 1st element of nums)
        dp = [[0]*(n+1) for _ in range(n+1)] 

        for idx in range(n-1, -1, -1):
            for prevIdx in range(idx-1, -2, -1):
                ## `prevIdx+1` for accessing correct element from dp (as it's shifted by 1 for prevIdx to start 
                ## from -1 instead of 0)
                length = 0 + dp[idx+1][prevIdx+1]
                if prevIdx == -1 or nums[idx] > nums[prevIdx]: # only add in length if the subsequence is increasing
                    length = max(length, 1 + dp[idx+1][idx+1])

                dp[idx][prevIdx+1] = length

        return dp[0][-1+1]