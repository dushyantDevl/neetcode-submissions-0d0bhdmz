class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minLen, i, currSum = n+1, 0, 0
        for j in range(n):
            currSum += nums[j]
            while currSum >= target: # shrink window to find min length subarray
                minLen = min(minLen, j-i+1) # store the current min. window length
                currSum -= nums[i] # decrement sum by element at left pointer of window
                i += 1
        return 0 if minLen == n+1 else minLen