class Solution:
    def rob(self, nums: List[int]) -> int:
        # Tabulation (Bottom-up)
        n = len(nums)
        cache = [-1] * (n)
        cache[0] = nums[0]

        for i in range(1, n):
            choose = nums[i]
            if i > 1:
                choose = nums[i] + cache[i-2]
            skip = 0 + cache[i-1]

            cache[i] = max(choose, skip)

        return cache[n-1]