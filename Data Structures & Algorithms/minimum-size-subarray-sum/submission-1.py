class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minLen, i, currSum, subArrayFound = n, 0, 0, False
        for j in range(n):
            currSum += nums[j]
            while currSum >= target:
                subArrayFound = True
                minLen = min(minLen, j-i+1)
                currSum -= nums[i]
                i += 1
        return minLen if subArrayFound else 0