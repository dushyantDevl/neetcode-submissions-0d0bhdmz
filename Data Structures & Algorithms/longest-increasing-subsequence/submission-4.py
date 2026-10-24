class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # Tabulation (Bottom-Up) => Space Optimization
        nxt, curr = [0]*(n+1), [0]*(n+1)

        for idx in range(n-1, -1, -1):
            for prevIdx in range(idx-1, -2, -1):
                length = 0 + nxt[prevIdx+1]
                if prevIdx == -1 or nums[idx] > nums[prevIdx]: # only add in length if the subsequence is increasing
                    length = max(length, 1 + nxt[idx+1])

                curr[prevIdx+1] = length
            
            nxt[:] = curr[:]

        return nxt[-1+1]