class Solution:
    def trap(self, height: List[int]) -> int:
        n, total_water = len(height), 0
        maxL, maxR = [0]*n, [0]*n
        maxL[0], maxR[n-1] = height[0], height[n-1]
        for i in range(1, n): maxL[i] = max(maxL[i-1], height[i])
        for i in range(n-2, -1, -1): maxR[i] = max(maxR[i+1], height[i])
        for i in range(n): total_water += min(maxL[i], maxR[i]) - height[i]
        return total_water