class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # We just have to found the lower bound of target
        l, r, res = 0, len(nums)-1, len(nums)
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target: # could be a answer
                res = mid
                r = mid-1 # search for even smaller index
            else: l = mid+1
        return res