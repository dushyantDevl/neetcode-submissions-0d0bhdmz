class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res, l, r = 0, 0, len(heights)-1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] > heights[r]: r -= 1
            else: l += 1 # in case of equal heights we can increment/decrement either one
        return res