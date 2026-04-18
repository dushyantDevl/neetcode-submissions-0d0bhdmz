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
        if nums[lb] != target or lb == n: return [-1,-1]
        return [lb, upperBound()-1]