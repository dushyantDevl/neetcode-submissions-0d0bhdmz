class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        preFix, postFix = 1, 1
        for i in range(n):
            res[i] = preFix
            preFix *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= postFix
            postFix *= nums[i]
        return res