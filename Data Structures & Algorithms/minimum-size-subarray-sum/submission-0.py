class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n, subArrayFound = len(nums), False
        minLen = n
        for i in range(n):
            currSum = 0
            for j in range(i, n):
                currSum += nums[j]
                if currSum >= target:
                    subArrayFound = True
                    minLen = min(minLen, j-i+1)
                    break
        return minLen if subArrayFound else 0