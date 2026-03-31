class Solution:
    def trap(self, height: List[int]) -> int:
        ## Since we want the min of maxR and maxL we can just solve 
        ## it using two pointers at extreme end and shift the pointer which has
        ## smaller element 
        n, total_water = len(height), 0
        l, r = 0, n-1
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                total_water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total_water += maxR - height[r]
        return total_water