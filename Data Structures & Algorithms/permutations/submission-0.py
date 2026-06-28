class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, ds = [], []
        vis = {}
        for i in range(len(nums)): vis[i] = False

        def backtrack():
            if len(ds) == len(nums):
                res.append(ds.copy())
                return

            for i in range(len(nums)):
                if not vis[i]:
                    ds.append(nums[i])
                    vis[i] = True
                    backtrack()
                    vis[i] = False
                    ds.pop()

        backtrack()
        return res