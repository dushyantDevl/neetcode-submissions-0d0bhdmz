class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n, res = len(nums), 1
        dp = [1]*n # stores the length of LIS upto index i

        for idx in range(n):
            for prevIdx in range(idx):
                # Only increase the length if some previous index element contributes to increasing subsequence
                # e.g. for `nums = [9,1,4,2,3,3,7]` if `idx=4` (i.e. 3) prevIdx will go from index 0 to 2, checking
                # the lengthOfLIS form using element at index 1 & 3
                if nums[prevIdx] < nums[idx]:
                    dp[idx] = max(dp[idx], dp[prevIdx]+1)
            res = max(res, dp[idx])

        return res