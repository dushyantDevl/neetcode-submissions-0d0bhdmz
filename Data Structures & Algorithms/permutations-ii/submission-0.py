class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, ds = [], []
        vis = {}
        for i in range(len(nums)): vis[i] = False

        def backtrack():
            if len(ds) == len(nums):
                res.append(ds.copy())
                return

            for i in range(len(nums)):
                if vis[i]:
                    continue

                # Skip the element which we've already used to create subset but still include the
                # element which it hasn't visited yet, despite it's duplicate since we've to make
                # permutation of the available elments not just unique elements
                if i > 0 and nums[i] == nums[i-1] and not vis[i-1]:
                    continue

                vis[i] = True
                ds.append(nums[i])

                backtrack()

                ds.pop()
                vis[i] = False

        backtrack()
        return res