class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def lowerBound():
            l, r, res = 0, n-1, n
            while l <= r:
                m = l + (r-l)//2
                if nums[m] >= target:
                    res = m
                    r = m-1
                else:
                    l = m+1
            return res
        
        def upperBound():
            l, r, res = 0, n-1, n
            while l <= r:
                m = l + (r-l)//2
                if nums[m] > target:
                    res = m
                    r = m-1
                else:
                    l = m+1
            return res
        
        lb = lowerBound()
        ## here writing lb == n first is important for empty array edge case since if that condition
        ## is true. it means it won't check for nums[lb] != target, to avoid all this we can also just
        ## write a condition in start `if not nums: return [-1,-1]`
        if lb == n or nums[lb] != target: return [-1,-1]
        return [lb, upperBound()-1]