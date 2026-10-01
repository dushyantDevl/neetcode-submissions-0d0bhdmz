class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Logic:
        ## A simpler 1D approach: let dp[i] be the length of the longest increasing subsequence 
        ## starting at index i. Working from right to left, for each i, we check all j > i. 
        ## If nums[i] < nums[j], we can extend the subsequence starting at j. We take the maximum 
        ## extension and add 1 for the current element.


        n = len(nums)
        dp = [1] * n

        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if nums[i] < nums[j]: dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)