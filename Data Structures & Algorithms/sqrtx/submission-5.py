class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        l, r = 0, x//2
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid == x: return mid
            elif mid*mid > x: r = mid-1
            else: l = mid+1
        return r