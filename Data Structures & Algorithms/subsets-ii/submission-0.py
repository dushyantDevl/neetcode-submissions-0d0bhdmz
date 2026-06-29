class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, temp = [], []

        def backtrack(idx, n):
            if idx == n:
                res.append(temp[::])
                return

            # All Subsets that include nums[idx]
            temp.append(nums[idx])
            backtrack(idx+1, n)

            temp.pop() # remove the element just added to consider the not include case

            # After taking the first unique element ignore the duplicates (if any) on upcoming
            # indexes, since nums is sorted all duplicates are together and we're just picking
            # the first one
            while idx+1 < n and nums[idx] == nums[idx+1]:
                idx += 1
            
            # All Subsets that doesn't include nums[idx]
            backtrack(idx+1, n)

        backtrack(0, len(nums))

        return res