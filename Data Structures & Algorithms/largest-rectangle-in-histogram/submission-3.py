class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, stk, maxArea = len(heights), [], 0
        for i in range(n):
            while stk and heights[i] <= heights[stk[-1]]:
                element = heights[stk[-1]]
                stk.pop()
                pse = stk[-1] if stk else -1
                nse = i
                maxArea = max(maxArea, element*(nse-pse-1))
            stk.append(i)
        while stk:
            element = heights[stk[-1]]
            stk.pop()
            nse = n
            pse = stk[-1] if stk else -1
            maxArea = max(maxArea, element*(nse-pse-1))
        return maxArea
