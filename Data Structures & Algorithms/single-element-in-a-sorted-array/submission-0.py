class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i-1 >= 0 and i+1 < len(nums):
                if nums[i-1] == nums[i] or nums[i] == nums[i+1]: continue
                else: return nums[i]