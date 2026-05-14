class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        currentMax = max(nums[:k])
        res = [currentMax]
        l = 1
        for r in range(k, n):
            currentMax = max(currentMax, nums[r])
            res.append(currentMax)
        return res