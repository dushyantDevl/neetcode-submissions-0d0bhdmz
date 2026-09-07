class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, pre, suf = len(nums), 1, 1
        res = -10e9
        for i in range(n):
            if pre == 0: pre = 1
            if suf == 0: suf = 1

            pre *= nums[i]
            suf *= nums[n-i-1]
            res = max(res, pre, suf)

        return res