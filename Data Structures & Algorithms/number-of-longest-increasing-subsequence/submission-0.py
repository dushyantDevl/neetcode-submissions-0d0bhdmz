class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n      # length of LIS ending at idx
        count = [1] * n   # number of such LIS ending at idx
        longest = 1 # stores length of LIS

        for idx in range(n):
            for prevIdx in range(idx):
                if nums[prevIdx] < nums[idx]:
                    if dp[prevIdx] + 1 > dp[idx]:
                        dp[idx] = dp[prevIdx] + 1
                        count[idx] = count[prevIdx]      # found a longer one → reset
                    elif dp[prevIdx] + 1 == dp[idx]:
                        count[idx] += count[prevIdx]     # another path of same length → add
            longest = max(longest, dp[idx])

        ## A single index can be the endpoint of multiple different LIS, so add all the occurence of length of LIS
        return sum(c for i, c in enumerate(count) if dp[i] == longest)