class Solution:
    def findMin(self, nums: List[int]) -> int:
        minN, l, r = nums[0], 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                minN = min(minN, nums[l])
                break
            
            m = (l+r)//2
            minN = min(minN, nums[m])
            if nums[l] <= nums[m]: # search in right sorted part
                l = m+1
            else:
                r = m-1
        return minN