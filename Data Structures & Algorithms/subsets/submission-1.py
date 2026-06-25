class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, temp = [], []
        def backtrack(n, i):
            if i >= n:
                ## We've to store `temp.copy()` otherwise (if we just store `temp`) since res is only 
                ## storing reference to temp, so whenever we make changes in temp it'll get affected 
                ## in the stored version of res, and that will eventually just leads to res storing
                ## empty list 2^n times since we're appending and poping from temp at each function call
                res.append(temp.copy())
                return
            temp.append(nums[i]) # include nums[i]
            backtrack(n, i+1)
            
            temp.pop() # pop the included one to not include nums[i] in next step
            backtrack(n, i+1)
            
        backtrack(len(nums),0)
        return res