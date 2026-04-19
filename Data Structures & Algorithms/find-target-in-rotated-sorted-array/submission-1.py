class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target: return m
            elif nums[l] <= nums[m]: # left half is sorted
                if target >= nums[l] and target <= nums[m]: # search in sorted half
                    r = m-1
                else:
                    l = m+1
            else: # right half is sorted
                if target >= nums[l] and target <= nums[r]: # search in sorted half
                    r = m-1
                else:
                    l = m+1
        return -1