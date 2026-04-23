class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[n-1] != nums[n-2]: return nums[n-1]

        l, r = 1, n-2

        while l <= r:
            m = l + (r-l)//2
            
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]: return nums[m]

            # mid is part of left half of singleNonDuplicate
            if (
                (m % 2 == 0 and nums[m] == nums[m+1]) or
                (m % 2 == 1 and nums[m] == nums[m-1])
            ):
                l = m+1 # eliminate left part to search in right part
            
            # mid is part of right half of singleNonDuplicate
            else:
                r = m-1 # eliminate right part to search in left part
        
        return -1 # never reach here, just there to show its returning a integer