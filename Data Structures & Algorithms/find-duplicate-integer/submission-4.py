class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            ConnectedIndex = abs(num) - 1 
            if nums[ConnectedIndex] < 0:
                return abs(num)
            nums[ConnectedIndex] *= -1
        return -1