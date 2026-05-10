class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minLen, i, currSum, subArrayFound = n, 0, 0, False
        for j in range(n):
            currSum += nums[j]
            while currSum >= target: # shrink window to find min length subarray
                subArrayFound = True # flagging for finding out that atleast the required subarray exist
                minLen = min(minLen, j-i+1) # store the current min. window length
                currSum -= nums[i] # decrement sum by element at left pointer of window
                i += 1
        return minLen if subArrayFound else 0