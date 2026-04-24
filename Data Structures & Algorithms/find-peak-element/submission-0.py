class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        for i in range(n):
            if i-1 >= 0 and i+1 < n and nums[i-1] < nums[i] > nums[i+1]:
                return i

