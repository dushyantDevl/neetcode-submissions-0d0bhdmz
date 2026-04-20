class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target: return True
            elif nums[l] < nums[m]: # search in left sorted half
                if nums[l] <= target < nums[m]: r = m-1
                else: l = m+1
            elif nums[l] > nums[m]: # search in right sorted half
                if nums[m] < target <= nums[r]: l = m+1
                else: r = m-1
            else: # when we couldn't identify the sorted half (i.e. nums[l]==nums[m])
                l += 1
        return False