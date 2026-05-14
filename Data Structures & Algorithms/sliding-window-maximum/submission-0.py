class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [max(nums[:k])]
        l = 1
        for r in range(k, n):
            res.append(max(nums[l:r+1]))
            l += 1
        return res