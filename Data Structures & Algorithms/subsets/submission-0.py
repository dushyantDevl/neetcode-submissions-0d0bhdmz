class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, temp = [], []
        def backtrack(n, i):
            if i >= n:
                res.append(temp.copy())
                return
            temp.append(nums[i]) # include nums[i]
            backtrack(n, i+1)
            
            temp.pop() # pop the included one to not include nums[i] in next step
            backtrack(n, i+1)
            
        backtrack(len(nums),0)
        return res