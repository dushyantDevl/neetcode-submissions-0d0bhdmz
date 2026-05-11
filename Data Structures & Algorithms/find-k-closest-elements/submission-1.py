class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1

        while r-l+1 > k: # shrink until k elements are left in window
            if abs(arr[l]-x) <= abs(arr[r]-x): # when left end element is closer (already gets the priority in case of equal distance from x)
                r -= 1 # discard the rightmost from the window
            else: # when rightmost from window is closer
                l += 1
        
        return arr[l:r+1]