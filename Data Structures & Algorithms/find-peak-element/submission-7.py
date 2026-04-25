class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            # Left neighbor is greater
            if m > 0 and nums[m] < nums[m-1]:
                r = m-1 # search in left part
            # Right neighbor is greater
            elif m < n-1 and nums[m] < nums[m+1]:
                l = m+1 # search in right part
            else:
                return m
        return -1