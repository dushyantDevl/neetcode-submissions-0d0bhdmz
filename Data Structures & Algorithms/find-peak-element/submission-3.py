class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        if n == 2: return 0 if nums[0] > nums[1] else 1
        l, r = 1, n-2
        while l <= r:
            m = l + (r-l)//2
            if nums[m-1] < nums[m] > nums[m+1]: return m
            if nums[m-1] <= nums[m] <= nums[m+1]: l = m+1
            elif nums[m-1] >= nums[m] >= nums[m+1]: r = m-1