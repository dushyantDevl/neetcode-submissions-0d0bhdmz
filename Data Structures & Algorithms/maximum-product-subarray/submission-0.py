class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), float('-inf')
        for i in range(n):
            prod = nums[i]
            res = max(res, prod)
            for j in range(i+1, n):
                prod *= nums[j]
                res = max(res, prod)
        return res