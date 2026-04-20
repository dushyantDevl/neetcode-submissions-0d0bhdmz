class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, mini = 0, len(nums)-1, nums[0]
        while l <= r:
            m = l + (r - l) // 2
            if nums[l] <= nums[m]:
                mini = min(mini, nums[l])
                l = m+1
            else:
                mini = min(mini, nums[m])
                r = m-1
        return mini