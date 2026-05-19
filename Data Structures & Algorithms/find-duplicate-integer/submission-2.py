class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        slow = fast = 0
        while True:
            if slow != fast and nums[slow % n] == nums[fast % n]:
                return nums[slow % n]
            slow += 1
            fast += 2