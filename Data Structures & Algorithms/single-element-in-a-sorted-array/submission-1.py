class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        for i in range(n):
            if i-1 >= 0 and i+1 < n:
                if nums[i-1] == nums[i] or nums[i] == nums[i+1]: continue
                else: return nums[i]