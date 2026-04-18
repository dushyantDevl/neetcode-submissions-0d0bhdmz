class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(leftSearch):
            l, r, res = 0, len(nums)-1, -1
            while l <= r:
                m = l + (r-l)//2
                if nums[m] < target: l = m+1
                elif nums[m] > target: r = m-1
                else:
                    res = m
                    if leftSearch: r = m-1
                    else: l = m+1
            return res
        
        return [binarySearch(True), binarySearch(False)]