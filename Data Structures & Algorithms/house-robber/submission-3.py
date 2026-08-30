class Solution:
    def rob(self, nums: List[int]) -> int:
        # Tabulation (Space Optimization)
        n = len(nums)
        last, last2nd = nums[0], 0


        for i in range(1, n):
            choose = nums[i]
            if i > 1:
                choose += last2nd
            skip = 0 + last

            curr = max(choose, skip)
            last2nd = last
            last = curr

        return last