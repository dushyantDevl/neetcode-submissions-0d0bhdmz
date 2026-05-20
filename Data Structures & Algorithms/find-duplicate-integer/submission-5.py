class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # index pointing to next index pointing to next index (skipping one node in between)
            if slow == fast: break
        # Now slow and fast points to same node

        slow = 0 # at head node again

        while True:
            # Now both slow and fast pointer increment by one node
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast: return slow