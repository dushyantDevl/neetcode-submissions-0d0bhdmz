class Solution:
    def previousSmallerElement(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res, stk = [-1]*n, []
        for i in range(n):
            height = heights[i]
            while stk and height <= stk[-1][0]: stk.pop()
            if stk:
                res[i] = stk[-1][1]
            else:
                res[i] = 1
            stk.append((height, i))
        return res
    
    def nextSmallerElement(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res, stk = [-1]*n, []
        for i in range(n-1,-1,-1):
            height = heights[i]
            while stk and height <= stk[-1][0]: stk.pop()
            if stk:
                res[i] = stk[-1][1]
            else:
                res[i] = n
            stk.append((height, i))
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        pse = self.previousSmallerElement(heights)
        nse = self.nextSmallerElement(heights)
        maxArea, n = 0, len(heights)
        for i in range(n):
            height = heights[i]
            maxArea = max(maxArea, height * (nse[i]-pse[i]-1))
        return maxArea