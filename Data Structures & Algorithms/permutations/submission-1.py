class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, n):
            if idx >= n:
                res.append(nums.copy())
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx+1, n)
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0, len(nums))
        return res