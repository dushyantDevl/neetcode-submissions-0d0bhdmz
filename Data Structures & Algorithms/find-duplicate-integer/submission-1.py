class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        slow = fast = 0
        while slow < n:
            if slow != fast and nums[slow] == nums[fast % n]:
                return nums[slow]
            slow += 1
            fast += 2