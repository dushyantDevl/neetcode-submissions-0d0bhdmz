class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 1, n-2 # ignore corner elements since they can't be at peak
        
        ## Run Binary Search to find the peak, so that we can apply Binary Search again
        ## in left (ascending) and right (descending) sorted parts
        while l <= r:
            m = (l+r)//2
            # saving these before since no. of times `get` can be called is limited (100)
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

            if left < mid < right: 
                l = m+1 # Search for peak in right half since mid is part of left sorted
            elif left > mid > right: 
                r = m-1 # Search for peak in left half since mid is part of right sorted
            else: break
        
        peak = m
        
        # Now that a peak is found we can run binary search in both left and right sorted parts
        ## Search in Left portion (ascending)
        l, r = 0, peak
        while l <= r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val > target: r = m-1
            elif val < target: l = m+1
            else: return m

        ## Search in Rigt portion (descending)
        l, r = peak, n-1
        while l <= r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val < target: r = m-1
            elif val > target: l = m+1
            else: return m

        return -1